"""django_project URL Configuration

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
from products import views
from accounts.views import (
    register_view,
    login_view,
    logout_view
)
from django.views.generic import TemplateView
from orders.views import order_checkout_view, download_order,my_order_view

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.featured_product_view),
    path('admin/', admin.site.urls),
    path('search/', views.search_view),
    path('login/', login_view),
    path('success/', my_order_view),
    path('orders/', my_order_view),
    path('checkout/', order_checkout_view),
    path('orders/<int:order_id>/download/', download_order),
    path('register/', register_view),
    path('logout/', logout_view),
    #path('bad_view/', views.bad_view),
    path('product/create/', views.product_create_view),
    path('product/', views.product_list_view),
    path('product/<int:id>/', views.detail_home_view),

]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
