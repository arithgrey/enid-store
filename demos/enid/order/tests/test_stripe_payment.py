from django.test import TestCase
from unittest.mock import patch, Mock, call
from functools import reduce
from rest_framework.test import APIClient
from order.stripe_payment import StripePayment
import stripe
import re

class TestsStripePayment(TestCase):
    def setUp(self):
        self.stripePayment = StripePayment()
        self.data = {'products': [{'price': 10.0, 'quantity': 2}], 'stripe_token': 'valid_token', 'email': 'test@example.com', 'phone_number': '123456789'}

    def success_charge(self):
        with patch('order.stripe_payment.stripeCharge') as mock_stripe_charge_create:

            expected = {'status': 'success','message': f'Cargo exitoso. ID: 123'}
            response = mock_stripe_charge_create.return_value = Mock(status='success', id=123)
            order = Mock(id=1)
            self.stripePayment.stripeCharge(data=self.data, order=order)
            self.assertEqual(response, expected)

    def test_stripe_charge_card_error(self):
        
        order = Mock(id=1)
        data = {'products': [{'price': 10.0, 'quantity': 2}], 'stripe_token': 'invalid_token', 'email': 'test@example.com', 'phone_number': '123456789'}
        with patch('order.stripe_payment.stripeCharge') as mock_stripe_charge_create:
            mock_stripe_charge_create.side_effect = stripe.error.CardError("Error en la tarjeta ...", param='', code=500)
            response = self.stripeCharge(data, order)            
            self.assertEqual(response.status_code, 500)
            self.assertIn('error', response.data)

    def test_calculate_total(self):

        products = [{'price': 10.0, 'quantity': 2}, {'price': 15.0, 'quantity': 1}]
        total = self.stripePayment._calculate_total(products=products) 
        self.assertEqual(total, 35)
    
    def test_handle_charge_response_success(self):
        
        charge = Mock(status='success', id=123)
        response = self.stripePayment._handle_charge_response(charge=charge)
        expected = {'status': 'success','message': f'Cargo exitoso. ID: 123'}
        self.assertEqual(expected, response)


    def test_handle_charge_response_failed(self):
        
        charge = Mock(status='failed', failure_message='Error en el pago')
        response = self.stripePayment._handle_charge_response(charge=charge)
        expected = {
                'status': 'failed',
                'message': f'Cargo fallido. Estado: failed, Razón: Error en el pago'}
        self.assertEqual(expected, response)


