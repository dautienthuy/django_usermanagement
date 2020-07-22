from django.conf.urls import url, include
from users import views

import django.contrib.auth.urls

urlpatterns = [
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]