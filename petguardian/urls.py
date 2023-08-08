from django.contrib import admin
from django.urls import path

from petlostandfound import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SinglePageView.as_view(), name='single_page'),
]
