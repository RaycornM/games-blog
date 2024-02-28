from django.conf.urls import url
from . import views
urlpatterns = [
    #显示主页
    url('^index/$',views.index,name="index"),
    #显示注册页面
    url('^register/$',views.register,name="register"),
    #执行注册操作
    url('^peoregister/$',views.peoregister,name="peoregister"),
    #注册页面验证
    url('^userContrast/([^/]+)/$',views.userContrast,name="userContrast"),
    #显示登录页面
    url('^login01/$',views.login01,name="login01"),
    #执行登录操作
    url(r'^do_login/$', views.do_login, name='do_login'),

    #显示文章
    url('^wz/$',views.wz,name="wz"),
    url('^wz01/$',views.wz01,name="wz01"),
    url('^wz02/$',views.wz02,name="wz02"),
    url('^wz03/$',views.wz03,name="wz03"),
    url('^wz04/$',views.wz04,name="wz04"),

    #显示资讯
    url('^zx/$',views.zx,name="zx"),
    url('^zx01/$',views.zx01,name="zx01"),
    url('^zx02/$',views.zx02,name="zx02"),
    url('^zx03/$',views.zx03,name="zx03"),
    url('^zx04/$',views.zx04,name="zx04"),

    #显示团队介绍页面
    url('^aboutUs/$',views.aboutUs,name="aboutUs"),
]