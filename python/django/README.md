# Django Beginner

[TOC]

* MacOS / Linux (CentOS/Ubuntu)
* Python 2.7.x
* Django 1.11
* Django Rest Framework
* PyCharm

## Reference

* [Python风格规范 - Google 开源项目风格指南](http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/)
* [Python v2.7.8 文档](http://python.usyiyi.cn/translate/python_278/index.html)
* [Django 1.11.6 文档](http://python.usyiyi.cn/translate/Django_111/index.html)
* [Django REST Framework](http://www.django-rest-framework.org/tutorial/quickstart/)
* [Django Web 框架(python)](https://developer.mozilla.org/zh-CN/docs/Learn/Server-side/Django)
* [django-rest-framework](https://darkcooking.gitbooks.io/django-rest-framework-cn/content/chapter0.html)

## Target & Plan

### Target 

* API: Get everything in json format.
* Cli: Get everything in command line.
* UI:  Get everything in web UI.

### Function

* Notifition
    * Aliyun Emai Push
* Device Management
* Host Management
    * Host 
        * Region
        * Zone
        * Type
        * Network
        * Pay 
* User Management
* Permission Management
* Thirdpart Management
    * Email
    * Shimo
    * Teambition

### Plan

* Project & APP
* Model
* View
    * API 
    * Cli
    * Web UI
* Code Review
* Deploy
    * Docker AutoBuild
    * Document & Example
    * Distribution

## Installing

### Install virtualenv

```bash
pip install --upgrade pip

pip install virtualenv

pip install virtualenvwrapper

source $(which virtualenvwrapper.sh)
[[ -f ~/.profile ]] || touch ~/.profile && chmod +x ~/.profile
grep 'virtualenvwrapper.sh' ~/.profile || echo 'source $(which virtualenvwrapper.sh)' >> ~/.profile

mkvirtualenv cmdb

workon devops
```

### Install Django-1.11

```bash
pip install django==1.11
```

## Setting PyCharm

* 新建`django`项目
    * 设置: `File` -> `New Project` -> 
        * 选择`Django` 
        * `Location` => `djangotest` 
        * `Interpreter` => `djangootest/bin/python`
    * 检查 `File` -> `Default Setting` -> `Search "Interpreter"`
    * 运行 `PyCharm` 点击 `Run`, 或者命令行执行 `./manage.py runserver`
    * 测试 通过浏览器访问 `http://127.0.0.1:8000`

* ~~设置keymap ???未找到???~~
    * ~~`File` -> `Setting` -> `Search "keymap"`~~

* 配置Server
    * 配置监听地址及端口 

        ```bash
        # PyCharm
        Run -> Edit Configurations： Host -> 0.0.0.0
        
        # Shell
        python manage.py runserver 0.0.0.0:80
        ```
         
    * 设置允许访问IP地址:

        ```bash
        # 修改 djangotest/settings.py，列表`ALLOWED_HOSTS` 中增加允许访问的IP地址
        ALLOWED_HOSTS = ['localhost','127.0.0.1','192.168.1.253']
        ```
        
* 标记目录：右击目录 -> Mark Directory As ->
    * `Template Folder` 模板目录，默认为：`templates/`
    * `Sources Root`    包文件的导入目录

## Django

### Start a Django Project

```bash
# Create a Django project
django-admin startproject cmdb  

# Create a app for Django project
cd cmdb
python manage.py startapp userAdmin
python manage.py showmigrations     # 查看数据变更
python manage.py makemigrations     # 生成migrations临时文件
python manage.py migrate            # 将migrations的内容入库

# Create Admin User
python manage.py createsuperuser
    Username (leave blank to use 'cmdb'): cmdb
    Email address: cmdb@mail.teachmyself.cn
    Password:
    Password (again):
    Superuser created successfully.

# Start icmdb
python manage.py runserver
# Start icmdb, and specify ip:port，default is 127.0.0.1:8000 
python manage.py runserver 0.0.0.0:8080
```

> http://localhost:8000/
> http://localhost:8000/admin/


> Pay attentation of Django directory tree.

```bash
./icmdb
    ├── cmdb
    │   ├── __init__.py
    │   ├── __init__.pyc
    │   ├── settings.py         # Global Setting
    │   ├── urls.py             # Global Entry
    │   └── wsgi.py
    ├── db.sqlite3
    ├── manage.py               # Management File
    └── userAdmin               # APP - userAdmin
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── migrations
        │   └── __init__.py
        ├── models.py
        ├── tests.py
        └── views.py
```

### Create `static` and `templates` directory

```bash
cd cmdb
mkdir -p static/{css,js,images} templates/{common,useradmin}
```

### Change Database Setting

> Sqlite -> MySQL

1. **Start MySQL Instance**

    ```bash
    docker run -d \
        --name mysql \
        --hostname mysql \
        -p 3306:3306 \
        --restart always \
        mysql
    ```

2. **Create Database `cmdb`**

    ```SQL
    CREATE DATABASE IF NOT EXISTS `cmdb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    ```
    
3. **Change Default Engine**

    * settings.py

    ```python
    # Change 
    DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
       }
    }
        
    # To
    DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'cmdb',
           'USER': 'root',
           'PASSWORD': '',
           'HOST': '127.0.0.1',
       }
    }
    ```

4. **Install `MySQL-python`**

    ```bash
    pip install MySQL-python
    ```

5. **Make makemigrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
    
6. **Create super user**

    ```bash
    python manage.py createsuperuser
        Username (leave blank to use 'your_local_user'): cmdb
        Email address: cmdb@mail.teachmyself.cn
        Password:
        Password (again):
        Superuser created successfully.
    ```

### Create APP by PyCharm

* 通过`PyCharm`创建：Tools -> Run Manage.py Task -> startapp message
* 通过命令创建：`./manage.py startapp message`
    * @TODO: 移动新app到`apps`目录

* PyCharm配置

    ```python
    # 导入 apps/message/views
    from apps.message import views
    ```
    
    > `PyCharm`中 右击 -`apps` - `Mark Directory As` - `Sources Root`
    
    ```python
    # 可以直接导入 message.views
    import message.views
    # 或
    from message import views
    ```

### Create APP userAdmin

#### Data Design

* BaseModel
    * id
    * name
    * createtime
    * updatetime
* UserAdmin
    * gender
    * mobile
    * email
    * exmail

#### Create Model

* Create Models in `userAdmin/models.py`
    
    ```python
    class BaseModel(models.Model):
        name = models.CharField(max_length=50)
        comment = models.TextField(max_length=100, null=True, blank=True)
        createtime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
        updatetime = models.DateTimeField(auto_now=True, null=True, blank=True)
    
        # use __str__ replace __unicode__ in python3
        def __unicode__(self):
            return self.name
    
        class Meta:
            ordering = ['-id']
            abstract = True
    
    
    class UserAdmin(BaseModel):
        gender = models.IntegerField(default=1)
        mobile = models.CharField(max_length=11, null=True, blank=True)
        email  = models.CharField(max_length=30, null=False, blank=False)
        exmail = models.CharField(max_length=50, null=True, blank=True)
    ```

* Create sql to import test data:

    ```bash
    counts=20
    dbname="cmdb"
    tbname="cmdb_user_cmdb_user"
    
    domain=("gmail" "hotmail" "yahoo" "qq" "163" "126")
    > ${dbname}.${tbname}.sql
    echo -n "truncate ${dbname}.${tbname}; INSERT INTO ${dbname}.${tbname} (name,comment,gender,mobile,email,exmail,createtime,updatetime) VALUES" | tee -a ${dbname}.${tbname}.sql
    for i in $(seq ${counts})
    do
        echo -n "(
            \"user_${i}\",
            \"comment_${i}\",
            $(expr ${i} % 2),
            \"13$(expr $i % 9)$(date +%s|sed "s#[0-9]\{2\}##")\",
            \"name_${i}@${domain[$(expr $i % ${#domain})]}.com\",
            \"name_${i}@cmdb.com\",
            unix_timestamp(),
            unix_timestamp()
        )" | tee -a ${dbname}.${tbname}.sql
        (if [[ ${i} -eq ${counts} ]] ; then echo -n ";"; else echo -n ","; fi) | tee -a ${dbname}.${tbname}.sql
        #sleep 0.5
    done
    echo -e "\n\tsource $(pwd)/${dbname}.${tbname}.sql;\n"
    ```

> ????

    ```???
    randnum=$(seq 1 9)
    echo ${#randnum}
    17
    
    for i in $(seq 0 19); do  echo $(expr $i % 9); done # 为毛没有9
    ???
    ```

#### Register APP in `setting.py`

```py
INSTALLED_APPS = [
    'userAdmin',
]
```

#### Register Admin in `admin.py`

```py
from .models import UserAdmin

admin.site.register(UserAdmin)
```

> http://127.0.0.1:8000/admin 登录后可以管理 `UserAdmin` 表数据

#### Create View

Create `templates/index.html`

```py
{{ title }}
```

Create view `userAdmin/view.py`

```py
def 
```


## Setting Navicat/Sequel

* 新建链接: 连接数据库
* 新建数据: `djangotest`
* 新建表: 
    * 表名
    * 列名 
* 修改表：右键 - 设计表 - 增加列
* 添加数据 - F5刷新确认
* 执行SQL: 查询 - 新建查询 - 输入SQL - 运行 - 结果/信息/概况/状态
* 复制表
* 数据传输：来源数据库 - 右键-数据传输 - 目标库
* 数据库导出/导入
* 删除表/清空表


## 创建项目相关目录及文档

```bash
cd cmdb

mkdir -p ./apps                     # apps目录作为模块存放目录
touch ./apps/__init__.py            # apps可以作为一个包导入

mkdir -p ./static/{images,js,css}   # 静态资源文件
mkdir -p ./log                      # 日志目录
mkdir -p ./upload                   # 附件目录

touch README.md                     # 项目说明        
touch setup.sh                      # 部署脚本
touch package.sh                    # 打包脚本
touch requirements.txt              # 依赖列表，用pip freeze > requirements.txt生成
```

## Django REST Framework



--------------

### 命令行运行配置

1. 函数增加
    
    ```python
    # 修改 `settings.py` 在 `BASE_DIR` 下添加：
    import sys
    APPS_DIR = '/'.join([BASE_DIR, 'apps'])
    sys.path.append(APPS_DIR)
    ```

2. 用户设置环境变量`PYTHONPATH`
3. 增加`.pth`文件，如：

    ```bash
    # 在虚拟环境创建.ph文件
    echo '/path/to/project/apps' > ${HOME}/.virtualenvs/django/lib/python2.7/site-packages/project.ph
    
    # Ubuntu全局路径
    /usr/local/lib/python2.7/dist-packages
    
    # CentOS全局路径
    /usr/lib/python2.7/site-packages
    ```

命令行运行，需要配置 `setting.py` 将 `apps` 目录作为根搜索路径 `BASE_DIR`

```bash
.
├── apps
│   ├── __init__.py
│   └── message
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── migrations
│       │   └── __init__.py
│       ├── models.py
│       ├── tests.py
│       └── views.py
├── db.sqlite3
├── djangotest
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── settings.py
│   ├── settings.pyc
│   ├── urls.py
│   └── wsgi.py
├── log
├── manage.py
├── static
│   ├── css
│   ├── images
│   └── js
├── templates
├── upload
└── uploads
```

* 文件说明
    * `models.py`    # 数据库设计
    * `urls.py`      # url,view编写
    * `views.py`
    * `templates`    # 展示数据库数据
* 相关配置 (`settings.py`)
    * `ALLOWED_HOSTS`
    * `INSTALLED_APPS`
    * `STATIC_URL`
    * `STATICFILES_DIRS` 

# setting.py for admin
MIDDLEWARE -> MIDDLEWARE_CLASSES


## Remove a APP in Django

1.删除models.py
无论是删除一个单独的model还是删除整个App,都需要首先删除models.py文件中的模型。

确认没有其他文件引用models.py中的类。
迁移或者删除你的数据库，Django提供了简便的方法方便用户删除某App下的所有数据(Django 1.7)。

./manage.py migrate your_app_name zero
删除models.py中的数据模型。
2.删除App
再次确认其他App中没有引用此App的文件
删除整个App文件夹
在settings.py的Installed Apps中移除该app。
3.REFRENCE

http://www.marinamele.com/how-to-correctly-remove-a-model-or-app-in-django 
http://stackoverflow.com/questions/3329773/django-how-to-completely-uninstall-a-django-app



为Django的TextInput添加文字注释
    http://cheng.logdown.com/posts/2015/05/04/add-placeholder-comments-to-textinput-in-django

