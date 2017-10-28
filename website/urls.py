"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from cooktopper.views import StoveViewSet, BurnerStateViewSet, TemperatureViewSet, BurnerViewSet
from cooktopper.views import RequestBurnerViewSet, PanStateViewSet, PanViewSet
from cooktopper.views import ProgrammingDetailsViewSet, ProgrammingViewSet, ShortcutViewSet

router = DefaultRouter()
router.register(r'stove', StoveViewSet, base_name='stove')
router.register(r'burner_state', BurnerStateViewSet, base_name='burner_state')
router.register(r'temperature', TemperatureViewSet, base_name='temperature')
router.register(r'burner', BurnerViewSet, base_name='burner')
router.register(r'request_burner', RequestBurnerViewSet, base_name='request_burner')
router.register(r'pan_state', PanStateViewSet, base_name='pan_state')
router.register(r'pan', PanViewSet, base_name='pan')
router.register(r'programming_details', ProgrammingDetailsViewSet, base_name='programming_details')
router.register(r'programming', ProgrammingViewSet, base_name='programming')
router.register(r'shortcut', ShortcutViewSet, base_name='shortcut')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
