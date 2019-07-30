from django.urls import path
from. import views

app_name = "players"
urlpatterns=[
    path('create0/', views.create0, name="create0"),
    path('create1/', views.create1, name="create1"),
    path('create2/', views.create2, name="create2"),
    path('create3/', views.create3, name="create3"),
    path('show/<int:id>/', views.show, name="show"), 
    path('show2/<int:id>/', views.show2, name="show2"), 
    path('edit/<int:id>/', views.edit, name="edit"),
    path('udpate/<int:id>/', views.update, name="update"), 
    path('delete/<int:id>/', views.delete, name="delete"),
]