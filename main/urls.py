from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

urlpatterns = [
    path('set_language/', set_language, name='set_language'),
]

urlpatterns += i18n_patterns(
    path('', include('website.urls')),  # пути из твоего приложения
    path('admin/', admin.site.urls),
    path('services/', include('services.urls', namespace='services')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls', namespace='about')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
