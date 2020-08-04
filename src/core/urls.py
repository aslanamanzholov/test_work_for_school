from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

# from core.settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from rest_framework.routers import DefaultRouter

from .topics.views import TopicViewSet

router = DefaultRouter()

router.register(r'topic', TopicViewSet,
                basename='topic_view_list')

urlpatterns = i18n_patterns(
    path(route='admin/', view=admin.site.urls),
    path(route='api/v1/', view=include(router.urls))
)

# if DEBUG:
#     from debug_toolbar import urls
#     from django.conf.urls.static import static
#
#     urlpatterns += (
#         path(route='__debug__/', view=include(urls)),
#         path(route='silk/', view=include('silk.urls')),
#     )
#     urlpatterns += tuple(
#         static(MEDIA_URL, document_root=MEDIA_ROOT)
#     )
