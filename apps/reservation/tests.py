from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from .models import Reservation


class AnimalTestCase(TestCase):
    def setUp(self):
        Reservation.objects.create(first_name='John', last_name='Dou', room='401a',
                                   start_date='2017-08-19T19:07:39Z', end_date='2017-08-19T19:07:41Z')
        Reservation.objects.create(first_name='Peter', last_name='Schulz', room='12',
                                   start_date='2017-09-17T10:00:00Z', end_date='2017-12-17T12:00:00Z')
        Reservation.objects.create(first_name='Lola', last_name='Scwarz', room='212',
                                   start_date='2017-10-10T10:00:00Z', end_date='2017-10-14T10:10:00Z')

    def test_booked_rooms(self):
        """Animals that can speak are correctly identified"""
        john = Reservation.objects.get(first_name='John', last_name='Dou')
        peter = Reservation.objects.get(first_name='Peter', last_name='Schulz')
        self.assertEqual(john.room, '401a')
        self.assertEqual(peter.start_date, '2017-09-17T10:00:00Z')


class ApiRequestFactoryTests(APIRequestFactory):
    # Using the standard RequestFactory API to create a form POST request
    factory = APIRequestFactory()
    request = factory.post('/reservations/', {'title': 'new idea'}, format='json')


class ReservationTests(APITestCase):
    def test_create_reservation(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('reservations')
        data = {'first_name': 'Peter', 'last_name': 'Pen', 'room': '12',
                'start_date': '2017-10-10T10:00:00Z', 'end_date': '2017-10-12T10:00:00Z'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reservation.objects.count(), 1)
        self.assertEqual(Reservation.objects.get().first_name, 'Peter')
        self.assertEqual(Reservation.objects.get().room, '12')
