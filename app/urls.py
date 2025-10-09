"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarListView, NewCarsCreateView, CarDetailView, CarUpdateView, CarDeleteView, NewBrandCreateView
from accounts.views import change_view, logout_view, profile_view, edit_profile_view, auth_page_view #login_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', CarListView.as_view(), name='cars_list'),
    path('newcars/', NewCarsCreateView.as_view(), name='car_form'),
    path('register/', auth_page_view, name="register"),
    path('change/', change_view, name='change'),
    path('brand/', NewBrandCreateView.as_view(), name='brand'),
    path('login/', auth_page_view, name="login"),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('editprofile/', edit_profile_view, name='edit_profile'),
    path('analytics/', include('analytics.urls')),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete', CarDeleteView.as_view(), name='car_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
