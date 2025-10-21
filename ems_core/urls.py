from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/users/', include('users.urls')),
    #path('api/employees/', include('employees.urls')),
    #path('api/attendance/', include('attendance.urls')),
    #path('api/payroll/', include('payroll.urls')),
    #path('api/reports/', include('reports.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
