from django.urls import path
from . import views
urlpatterns = [
    path('webpage/',views.webpage,name='webpage'),
    path('register/',views.register,name='register'),
    path('topic/',views.topic,name='topic'),
    path('detail/<int:maso>',views.detail,name='detail'),
]
