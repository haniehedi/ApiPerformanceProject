from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Property, Agent

class PropertyTests(APITestCase):
    def setUp(self):
        self.agent = Agent.objects.create(name='Test Agent', email='agent@example.com')
        self.property = Property.objects.create(
            title='Test Property',
            description='Description of test property',
            address='123 Main St',
            price=100000.00,
            agent=self.agent
        )

    def test_property_list_view(self):
        url = reverse('listing:properties-list')  # Use the namespace here
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_property_detail_view(self):
        url = reverse('listing:properties-detail', kwargs={'pk': self.property.pk})  # Use the namespace here
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.property.title)

    def test_property_cache(self):
        url = reverse('listing:properties-list')  # Use the namespace here
        response = self.client.get(url)
        response_2 = self.client.get(url)
        # Optionally check for cache headers or similar

    def test_property_throttling(self):
        url = reverse('listing:properties-list')  # Use the namespace here
        for _ in range(2):  # Assuming throttle limit
            response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

    def test_agent_creation(self):
        url = reverse('listing:agents-list')  # Assuming you want to test agent creation
        response = self.client.post(url, {
            'name': 'New Agent',
            'email': 'newagent@example.com'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_property_image_creation(self):
        # Assuming you have a PropertyImage model and want to test its creation
        url = reverse('listing:properties-detail', kwargs={'pk': self.property.pk})  # Get property detail URL
        # You would create an image related to this property here
        # e.g., PropertyImage.objects.create(property=self.property, image_url='http://image.url/2')
        self.assertEqual(self.property.title, 'Test Property')  # Example assertion


