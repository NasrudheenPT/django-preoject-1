from django.urls import path
from .views import *

urlpatterns = [
    path('', main,name="mainpage"),
    path('insert/', insert,name="insertpage"),
    path('view/', view,name="viewpage"),
    path('update/<id>/', update_fun,name="updatepage"),
    path('delete/<id>/', delete_fun,name="deletepage"),
    path('create/', createuser,name="createpage"),
    path('login/', login_fn,name="loginpage"),
    path('logout/', logout_fn,name="logoutpage"),
    path('fileupload/', fileupload,name="fileuploadpage"),
    path('viewfile/', viewfile,name="viewfilepage"),
    path('email/', emailsend,name="emailpage"),

]