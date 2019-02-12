# itdb

环境说明

windows下，安装python-3.4
python-3.4.4.amd64.msi
链接：https://pan.baidu.com/s/11HiR5YzYVllkdSVQYiVkeg 
提取码：8ec4 

python虚拟环境
pip install virtualenvwrapper-win -i https://pypi.doubanio.com/simple/
-------------------------------------------------------------------
创建数据库：itdb_v2
itdb_v2.settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'itasv2',
        'HOST': '192.168.168.12',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD':'root',
    }
}
-------------------------------------------------------------------
C:\Windows\system32>cd /d C:\Python34\Scripts
C:\Python34\Scripts>pip -V
pip 7.1.2 from c:\python34\lib\site-packages (python 3.4)
C:\Python34\Scripts>pip install virtualenvwrapper-win -i https://pypi.doubanio.com/simple/
Collecting virtualenvwrapper-win
  Downloading https://pypi.doubanio.com/packages/f5/23/4cba98733b9122219ce67177d745e4984b524b867cf3728eaa807ea21919/virtualenvwrapper-win-1.2.5.tar.gz
Collecting virtualenv (from virtualenvwrapper-win)
  Downloading https://pypi.doubanio.com/packages/7e/1b/6c00d57127608793e16e8b7f813e64d58a1938505c42fe190d1386ab41e1/virtualenv-16.4.0-py2.py3-none-any.whl (2.0MB)
    100% |████████████████████████████████| 2.0MB 9.4MB/s
Installing collected packages: virtualenv, virtualenvwrapper-win
  Running setup.py install for virtualenvwrapper-win
Successfully installed virtualenv-16.4.0 virtualenvwrapper-win-1.2.5
You are using pip version 7.1.2, however version 19.0.2 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
-------------------------------------------------------------------
mkvirtualenv -p C:\Python34\python.exe itdb
workon itdb

(itdb) C:\Users\JJX-Lin>python -V
Python 3.4.4
(itdb) C:\Users\JJX-Lin>pip -V
pip 19.0.2 from c:\python27\evns\itdb\lib\site-packages\pip (python 3.4)

pip install -i https://pypi.doubanio.com/simple/ django==1.9.13
xlwt==1.3.0
pymysql==0.9.3
xlrd==1.2.0
certifi==2018.11.29 
chardet==3.0.4 
idna==2.8 
requests==2.21.0 
urllib3==1.24.1
-------------------------------------------------------------------
python manage.py makemigrations

Migrations for 'assets':
  0001_initial.py:
    - Create model UserProfile
    - Create model AssetAttr
    - Create model AssetInfo
    - Create model AssetModel
    - Create model AssetName
    - Create model AssetProvider
    - Create model AssetStatus
    - Create model CheckInfo
    - Create model DeviceModel
    - Create model InOutReasons
    - Create model InReasons
    - Create model InStock
    - Create model Level
    - Create model NonStock
    - Create model OfficePlace
    - Create model OperationLogs
    - Create model OutReasons
    - Create model ProductConf
    - Create model StorePlace
    - Create model Supplier
    - Create model UseType
    - Add field product_conf to devicemodel
    - Add field provider to devicemodel
    - Add field level to assetprovider
    - Add field model_name to assetname
    - Add field level to assetmodel
    - Add field asset_model to assetinfo
    - Add field asset_name to assetinfo
    - Add field asset_provider to assetinfo
    - Add field asset_status to assetinfo
    - Add field device_model to assetinfo
    - Add field in_out_reason to assetinfo
    - Add field last_check_time to assetinfo
    - Add field level to assetinfo
    - Add field office_place to assetinfo
    - Add field operator to assetinfo
    - Add field owner to assetinfo
    - Add field product_conf to assetinfo
    - Add field store_place to assetinfo
    - Add field supplier to assetinfo
    - Add field use_type to assetinfo
    - Add field user_name to assetinfo
    - Add field level to assetattr
    - Add field office_place to userprofile
    - Add field store_place to userprofile
    - Add field user_permissions to userprofile

Process finished with exit code 0
-------------------------------------------------------------------
python manage.py migrate

Operations to perform:
  Apply all migrations: assets, admin, contenttypes, auth, sessions
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying assets.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying sessions.0001_initial... OK
  
Process finished with exit code 0
-------------------------------------------------------------------
因assets_userprofile表有外键关联，需要先在assets_officeplace插入一行数据：
INSERT INTO `itasv2`.`assets_officeplace`(`id`, `office_place`) VALUES (1, '中国总部');
否则报错：
django.db.utils.IntegrityError: (1452, 'Cannot add or update a child row: a foreign key constraint fails (`itasv2`.`assets_userprofile`, CONSTRAINT `assets_userpro_office_place_id_238ad
ae8_fk_assets_officeplace_id` FOREIGN KEY (`office_place_id`) REFERENCES `assets_officeplace` (`id`))')
-------------------------------------------------------------------
(itdb) E:\1workplace\itdb>python manage.py createsuperuser
用户名: admin
Email: 123@qq.com
Password:admin123
Password (again):admin123
Superuser created successfully.
-------------------------------------------------------------------
python manage.py runserver 0:8000

Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.
February 11, 2019 - 17:06:13
Django version 1.9, using settings 'itdb_v2.settings'
Starting development server at http://0:8000/
Quit the server with CTRL-BREAK.
-------------------------------------------------------------------
后台：http://127.0.0.1:8000/admin/
前台：http://127.0.0.1:8000/
admin / admin123
