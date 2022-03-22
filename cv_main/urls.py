from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='cv'),
    path('about', views.works, name='works'),
]