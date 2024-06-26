from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from invoice import views

urlpatterns = ([
    path('admin/', admin.site.urls),

    # -- INVOICE URLS --
    path('', views.index, name='index'),
    path('', include('invoice.urls')),
])

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
