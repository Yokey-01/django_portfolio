from . import views
from django.urls import path

urlpatterns=[
    path("",views.index,name="index"),
    path("717821i261/portfolio/",views.html,name='html'),
    path('index2/',views.index2,name='index2'),
    path("table1/",views.table1,name='table1'),
    path("table1/add/",views.add,name='add'),
    path("table1/add/addrecord/",views.addrecord,name="addrecord"),
]