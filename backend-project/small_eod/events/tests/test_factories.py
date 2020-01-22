from django.test import TestCase

from ..factories import EventFactory
from ..models import Event
from ...generic.tests.mixins import FactoryTestCaseMixin


class EventFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = EventFactory
    MODEL = Event
