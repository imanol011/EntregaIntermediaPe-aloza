from django.contrib import admin
from django.urls import path, include

from final_project.views import index



urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),

    path('products/', include('products.urls')), 
    path('orders/', include('orders.urls')),
]
