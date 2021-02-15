"""ticket_office URL Configuration

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
from django.urls import path, include, re_path

from ticket_office.event_catalog import views as event_catalog_views
from ticket_office.ordering import views as ordering_views
from ticket_office.shopping_basket import views as shopping_basket_views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    # events catalog
    path('events/', event_catalog_views.EventList.as_view()),
    path('events/<int:pk>/', event_catalog_views.EventDetail.as_view()),
    path('venues/', event_catalog_views.VenueList.as_view()),
    path('venues/<int:pk>/', event_catalog_views.VenueDetail.as_view()),
    path('categories/', event_catalog_views.CategoryList.as_view()),
    path('categories/<int:pk>/', event_catalog_views.CategoryDetail.as_view()),

    # shopping basket
    path('baskets/<int:pk>/', shopping_basket_views.BasketDetail.as_view()),
    path('baskets/<int:pk>/basketlines/', shopping_basket_views.BasketLineList.as_view()),
    path('baskets/<int:basket_id>/basketlines/<int:pk>/', shopping_basket_views.BasketLineDetail.as_view()),
    path('baskets/<int:basket_id>/checkout/', shopping_basket_views.checkout),
    path('baskets/<int:basket_id>/clear/', shopping_basket_views.clear),

    # ordering
    path('user/<int:pk>', ordering_views.OrderList.as_view()),
    path('orders/<int:pk>/', ordering_views.OrderDetail.as_view()),
]
