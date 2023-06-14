from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap
sitemaps = {'static': StaticViewSitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('community.urls')),
    path('',include('account.urls')),
    path('',include('services.urls')),
    path('',include('core.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
