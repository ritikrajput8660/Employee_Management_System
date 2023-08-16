from django.urls import path
from app.views import *
appname = 'app'
urlpatterns = [
    # path('',homePage,name='homePage'),
    path('home/',homePage,name='homePage'),
    path('add_Emp/',add_Emp,name='add_Emp'),
    path('update_Emp/<id>',update_Emp,name='update_emp'),
    path('delete_emp/<int:id>',delete_Emp,name='delete_emp'),
    # path('do_update_Emp/<int:EmpId>',do_update_Emp,name='do_update_Emp'),
]