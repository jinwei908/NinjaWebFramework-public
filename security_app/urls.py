"""security_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView

import sys 
sys.path.append(settings.PROJECT_ROOT)

from rest_framework import routers
from restapi import views
from restapi import views_get

# this is DRF router for REST API viewsets
router = routers.DefaultRouter()

# register REST API endpoints with DRF router
router.register(r'tool', views.DataInsert, r'tool')
#router.register(r'tool_put', views.ToolViewSet.put_query, r'tool_put')

#router.register(r'tool_insert', views.ToolViewInsert, r'tool_insert')
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    # Django Admin
    url(r'^admin/', include(admin.site.urls)),
    # Tiny MCE Urls
    #url(r'^tinymce/', include('tinymce.urls')),
    # Other App
    #url(r'^other/', include('projectname.other.urls', namespace='other')),
    # Blog App
    url(r'^$',  TemplateView.as_view(template_name='index.html'), name="index"),
   url(r'^api-auth/get/getdashboard/', views_get.GetHomeDashboardData.as_view({'get':'list'})),
   #url(r'^api-auth/post/data/', views.DataInsert.as_view({'post':'create', 'get':'list'})),
    url(r'^api-auth/post/data/', views.DataInsert.as_view({'post':'create'})),
    url(r'^api-auth/post/hostlog/', views.HostLogInsert.as_view({'post':'create'})),
    url(r'^api-auth/post/imageupload/', views.PhotoInsert.as_view({'post':'create'})),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)