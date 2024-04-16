from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('films/', include('films.urls'), name='films'),
    path("auth/", include("users.urls"), name="auth"),
    path("auth/", include("django.contrib.auth.urls"), name="auth"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
