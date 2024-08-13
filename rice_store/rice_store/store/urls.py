from django.urls import path
from . import views
from .views import manage_rice_items, save_rice_item, delete_rice_item
urlpatterns = [
    path('', views.home, name='home'),
    path('add_to_cart/<int:rice_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('update_delivery_status/', views.update_delivery_status, name='update_delivery_status'),
    path('manage_rice_items/', manage_rice_items, name='manage_rice_items'),
    path('save_rice_item/', save_rice_item, name='save_rice_item'),
    path('delete_rice_item/<int:id>/', delete_rice_item, name='delete_rice_item'),
    # Add other URL patterns as needed
]
