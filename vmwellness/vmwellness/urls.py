"""vmwellness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include, url
from vmwellnessapp import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^dashboard/?$', v.dashboard),
    url(r'^water/?$', v.water_tracker),
    url(r'^stream/?$', v.activity_stream),
    url(r'^goals/?$', v.goals),
    url(r'^resources/?$', v.resources),
    url(r'^about/?$', v.about)
]
