from django.conf.urls import url, include

from rest_framework import routers

from .views import ReservationViewSet, ReservationFilter

router = routers.DefaultRouter()
router.register(r'reservations', ReservationViewSet)


urlpatterns = [
    url(r'', include(router.urls)),
    url('^reservation-filter/(?P<start_date>.+)/(?P<end_date>.+)/$', ReservationFilter.as_view(),
        name='reservation-filter'),
]
