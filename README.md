# MoocOnline
django项目--慕课在线学习平台


使用的插件
++django-simple-captcha==0.4.6
++django-pure-pagination-0.3.0



配置网易邮箱(163)如下：
    # 一开始配置的QQ邮箱竟然被禁了,还是网易邮箱好哇
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = "smtp.163.com"
    EMAIL_PORT = 25
    EMAIL_HOST_USER = "邮箱"
    EMAIL_HOST_PASSWORD = "客户端授权码"
    EMAIL_USE_TLS = False
    EMAIL_FROM = "邮箱"

    ++++此处email_password为客户端授权码,网易邮箱比较特殊,此处配置时应该用客户端授权码代替登录密码进行配置




mysql安装信息：

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'djangodemo',
            'USER': '用户名',
            'PASSWORD': '密码',
            'HSOT': '127.0.0.1',
        }
    }

mkvirtualenv virtualenvironment_name(建立虚拟环境)-->

大量内置应用
++后台管理系统admin
++用户认证系统auth
++回话系统sessions
安全性
++表单验证
++SQL注入
++跨站点攻击

    设置databases,templates下的dirs,新建的staticfiles_dirs
    migration生成数据表-->编写views.py(后台的业务逻辑:编写负责相应url请求的函数/功能模块)-->配置urls.py(将用户的请求url映射到某一个函数/模块)-->{1、HTML与css文件分离 2、css文件分离与地址修改}
    STATICFILES_DIRS=[
        os.path.join(BASE_DIR,'static')
    ]设置静态文件的默认目录

ORM  (Object Relation Mapping对象关系映射)

     models.py和数据库相关，定义数据库中的表 django1.8后migrations 数据移植、数据迁移(新出现的)也是和数据库相关的
     使用了ORM模型,
     models:django提供了大量的field类型，这些类型不仅对应着数据库中的类型，也对应着很多更加高级的类型
     models.ForeignKey
     models.DateTimeField
     models.IntegerField
     models.IPAddressField
     models.FileField
     models.ImageField

admin.py给admin应用做配置使用
test.py用于测试（用于放置测试脚本）
项目目录文件
++manage.py管理项目，例如runserver启动服务器

++settins.py整个网站的配置情况 settings中的templates用于配置处理模板文件的类

    settings中ALLOWED_HOSTS表示允许访问本程序的用户，若设置为'localhost'，则只允许外界用localhost访问本网站
    ROOT_URLCONF指向url配置文件

url

    urls.py映射配置文件:决定一个url访问被哪个程序(函数)相应  urlpatterns即映射表
    为了避免在同一个url配置文件中存在url冲突，可以用include包含其他url配置文件，但是其他url配置文件中的url被“拉长”了。例如：
    在根目录的url文件中进行配置:   url(r'^index/',include('blog.urls')),
    在blog目录中的url文件中进行配置: url(r'^index/',views.index),
    那么实际访问index的url应该是******index/index/
    通常将blog中的url配置成空字符串,即用正则表达式“r'^$'”约束为空字符串
    	****注意配置url的时候一定注意在url的末尾加上'/'这样配置，用户访问该url时，末尾无论加不加'/'都可以成功访问。

templates

    HTML文件，使用了Django模板语言(DTL)
    DTL初步
    	render()函数中支持一个dict类型的参数
    	该字典是后台传递到模板的参数，键为参数名
    	在模板中使用{{参数名}}来直接使用
    django会按照INSTALLED_APPS中的添加顺序查找Templates，因此不同app下templates目录中同名.html文件会造成冲突
    	解决办法:在各app的templates目录下建立一个与该app同名的文件夹，然后将各自具有冲突的页面放进去即可

init.py声明模块的文件

++wsgi.py :python应用程序和web服务器之间的接口

migrate makemigrations和同步数据库有关

将新添加的应用

子目录project-name中是一些关于项目的配置文件:

++总的urls配置文件 urls.py 以及部署服务器时用到的 wsgi.py 文件

++init.py 是python包的目录结构必须的，与调用有关。

django-admin startproject project-name

django-admin startapp app-name

django-admin start 

mysql配置:

    user:MrRobot
    password:Mr.Robot
    dbadmin

workon查看当前有哪些虚拟环境

workon 虚拟环境名 :即进入想要进入的虚拟环境



使用url别名（避免后期改动url的时候改动大量语句）

    html中:
    <form action="{% url 'go_form' %}" method="post" class="smart-green">
    url.py中：
      urlpatterns = [
      url(r'^admin/', admin.site.urls),
      url(r'^form_go/$', getform,name='go_form'),
    ]



解决model循环引用的问题:分层设计

    为方便管理一个大平台下的各app,我们通常将所有app统一存放在项目根目录的apps(Programmer所建)下,此时必须在在项目settings的文件中，进行如下配置:
    import sys
    sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
    即将apps目录作为第一搜索目录(下标为0)

PEP8 (Python编码规范)

  赋值"="两遍加空格

  给出多参数时,逗号后面空格再写下一项

    class Course(models.Model):
    # Course即数据库表名,django中均继承自models.Model
      name = models.CharField(max_length=50, verbose_name=u"课程名")
      # CharField指该列为char类型,verbose_name指该列对应名称,前缀u指进行unicode编码
      detail = models.TextField(verbose_name=u"课程详情")
      # detail为文本域
      learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟)")
      image = models.ImageField(upload_to="courses/%Y/%m",verbose_name=u"封面图片", max_length=100)
      # upload_to指该图片的url地址
      add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
      # default=datetime.now指默认为当前时间
    
      class Meta:
      # Meta前面空一行
          verbose_name = u"课程"
          # verbose_name即对该model的名字进行设置
          verbose_name_plural = verbose_name
          # verbose_name_plural是对model的复述,如果注释以上语句,则系统进行解析时会自动在verbose_name后加上's'

重载model中class的unicode(def)方法可以自定义该model的"缩写"显示格式



踩过的坑

一、

    继承自AbstractUser的UserProfile类，在用admin添加用户时出现错误：1452, 'Cannot add or update a child row: a foreign key constraint fails是因为在第一次做数据库修改时，必须在做任何数据迁移之前做makemigrations命令。
    解决办法:删库-->重新创建superuser-->makemigrations-->migrate即可

二、
模板引擎

    for循环中有存在内置的循环记数变量{{ forloop.counter }}可调出(从1开始)
