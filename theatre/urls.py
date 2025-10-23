from django.urls import path, include
from rest_framework import routers

from theatre.views import (
    GenreViewSet,
    ActorViewSet,
    TheatreHallViewSet,
    PLayViewSet,
    PerformanceViewSet,
    ReservationViewSet,
    TicketViewSet,
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("theatre_halls", TheatreHallViewSet)
router.register("plays", PLayViewSet)
router.register("performance", PerformanceViewSet)
router.register("tickets", TicketViewSet, basename="ticket")
router.register("reservation", ReservationViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "theatre"
