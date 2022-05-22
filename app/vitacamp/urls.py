from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_user', views.add_user, name='add_user'),
    path('add_event', views.add_event, name='add_event'),
    path('add_squad', views.add_squad, name='add_squad'),
    path('add_camp', views.add_camp, name='add_camp'),
    path('api/children', views.SelectChildren.as_view(), name='select_children')
]
