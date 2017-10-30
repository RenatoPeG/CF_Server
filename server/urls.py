from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from cholofighter import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^personajes/', views.PersonajeList.as_view()),
    url(r'^stocks/(?P<pk>[0-9]+)/', views.StockDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)