"""koodausblogi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blogi import views as blogi_views

# This was for activating sentry.io (error & user tracking)
# def trigger_error(request):      activates an error for sentry-
#     division_by_zero = 1 / 0      -to identify

urlpatterns = [
    path('django-admin-hallinto/', admin.site.urls),
    path('', blogi_views.postaukset, name="postauslista"),
    path('postaus/<int:id>', blogi_views.nayta_postaus, name="nayta_postaus"),
    # path('uusi/', blogi_views.uusi_postaus, name="uusi_postaus"),
    # path('sentry-debug/', trigger_error),
    path('search-post', blogi_views.search_post, name="search_post"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)