from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',include("dashboard.urls")),
    path('accounts/',include("accounts.urls")),
    path('',include("app.urls")),
]

