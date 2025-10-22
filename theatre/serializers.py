from django.db import transaction
from rest_framework import serializers

from theatre.models import (
    Genre,
    Actor,
    Performance,
    Play,
    TheatreHall,
    Ticket,
    Reservation,
)