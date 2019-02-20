from django.shortcuts import render,HttpResponse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required,permission_required

from django.views.generic.base import View
from .forms import AssetQuery
import json
from datetime import datetime,date
from  .models import AssetInfo
from config import assets_config
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
class BaseResponse(object):
    def __init__(self):
        self.status = True
        self.data = None
        self.message = None

class CJsonEncoder(json.JSONEncoder):
    '''Queryset 对象中datetime对象无法json序列化， 重写json序列化方法'''
    def default(self, o):
        if isinstance(o,datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o,date):
            return o.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self,o)

@login_required
def index(request):
    return render(request,'assets/index.html')

# def asset_query(request):
#     if request.method == 'GET':
#         search_form = AssetQuery()
#         return render(request, 'assets/asset_query/asset_query.html', {'form':search_form,"stitle":"资产查询"})
class Asset_query(View):
    @method_decorator(login_required)
    def get(self,request,*args,**kwargs):
        search_form = AssetQuery()

        response = BaseResponse()
        try:
            query_table_config = assets_config.query_table_config
            # 需要从数据库中取得字段
            field_list = []
            for item in query_table_config:
                if item['display']:
                    field_list.append(item['field'])
            # 查询数据
            query_data = list(AssetInfo.objects.all().values(*field_list))

        except Exception as e:
            response.status = False
            response.message = str(e)
        # return HttpResponse(json.dumps(response.__dict__))
        return render(request, 'assets/asset_query/asset_query.html', {'form':search_form,"stitle":"资产查询",'query_data':query_data,})

class Asset_query_all_json(View):
    @method_decorator(login_required)
    def post(self,request,*args,**kwargs):
        print("all-1")
        search_form = AssetQuery()
        response = BaseResponse()
        try:
            query_table_config = assets_config.query_table_config
            # 需要从数据库中取得字段
            field_list = []
            for item in query_table_config:
                if item['display']:
                    field_list.append(item['field'])
            # 查询数据
            query_data = list(AssetInfo.objects.all().values(*field_list))
            #将数据json序列化
            query_data_json = json.dumps(query_data,cls=CJsonEncoder)
            #返回个前端的数据
            data_back = {
                "config":query_table_config,
                'query_data':query_data_json
            }
            data_back_json = json.dumps(data_back)
            response.data = data_back_json
        except Exception as e:
            response.status = False
            response.message = str(e)
        return HttpResponse(json.dumps(response.__dict__))

class Asset_query_json(View):
    @method_decorator(login_required)
    def post(self, request,field_value, *args, **kwargs):
        response = BaseResponse()
        query_content = request.body.decode("utf-8")
        print("field-2")
        try:
            query_table_config = assets_config.query_table_config
            # 需要从数据库中取得字段
            field_list = []
            for item in query_table_config:
                if item['display']:
                    field_list.append(item['field'])

            #查询数据
            for field_name in field_list:
                query_data = list(AssetInfo.objects.filter(**{field_name+"__icontains":field_value}).values(*field_list))
                if query_data :
                    break
            #将数据json序列化
            query_data_json = json.dumps(query_data,cls=CJsonEncoder)
            #返回个前端的数据
            data_back = {
                "config":query_table_config,
                'query_data':query_data_json
            }

            data_back_json = json.dumps(data_back)
            response.data = data_back_json

        except Exception as e:
            response.status = False
            response.message = str(e)
        return HttpResponse(json.dumps(response.__dict__))

