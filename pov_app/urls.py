from django.urls import path
from . import views


urlpatterns = [
    path('',views.index_view,name='index_view'),
    # path('visitors',views.visitors_view,name='visitors_view')
    



    
]