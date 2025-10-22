from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ems_core import views

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # ✅ Add this line if your users app has urls.py
    path('users/', include(('users.urls', 'users'), namespace='users')),
    # api endpoints 
    #path("api/users/", include("users.urls")),
    #path("api/employees/", include("employees.urls")),
    #path("api/attendance/", include("attendance.urls")),
    #path("api/payroll/", include("payroll.urls")),
    #path("api/reports/", include("reports.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

