"""config URL Configuration

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
# from django.contrib import admin 
# from django.urls import path, include
# from  config.views import logout_view
# from page.views import home_view, page_view

# from  django.conf.urls.static import static
# from django.conf import settings
# from page.views import home_view


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# My Views:
from config.views import logout_view
from page.views import home_view


urlpatterns = [
    path('', home_view, name="home"),

    # Pages:
    path('page/', include('page.urls', namespace='page')),

    # Todo App:
    path('todo/', include('todo.urls', namespace='todo')),

    # Blog App:
    path('blog/', include('blog.urls', namespace='blog')),

    # Auth:
    path('account/logout/', logout_view, name="logout_view"),

    # TinyMCE
    path('tinymce/', include('tinymce.urls')),

    # ADMIN:
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# urlpatterns = [


#     path("todo/", include("todo.urls", namespace='todo')),

#     path("page/", include("page.urls", namespace='page')),

#     path('admin/', admin.site.urls),

#     path("blog/", include("blog.urls", namespace='blog')),

#     path('', home_view, name='home'),
#     path('account/logout/', logout_view, name='logout_view'),

    
#     # tinyMCE
#     path('tinymce/', include('tinymce.urls')),


# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
