from django.conf.urls import url
from apps.tables import views

app_name = 'tables'
urlpatterns = [
    url(r'^$', views.tables, name='tables'),
]
