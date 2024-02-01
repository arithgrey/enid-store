from django.test import TestCase
from unittest.mock import patch, Mock, call
from functools import reduce
from order.stripe_payment import StripePayment
from stripe.error import CardError, StripeError


class TestsStripePayment(TestCase):
    def setUp(self):
        self.stripePayment = StripePayment()
        self.data = {'products': [{'price': 10.0, 'quantity': 2}], 'stripe_token': 'valid_token', 'email': 'test@example.com', 'phone_number': '123456789'}

    def success_charge(self):
        with patch('order.stripe_payment.stripeCharge') as mock_stripe_charge_create:

            expected = {'status': 'success','message': f'Cargo exitoso. ID: 123'}
            mock_stripe_charge_create.return_value = Mock(status='success', id=123)
            order = Mock(id=1)
            self.stripePayment.stripeCharge(data=self.data, order=order)
            self.assertEqual(mock_stripe_charge_create, expected)

    def test_calculate_total(self):

        products = [{'price': 10.0, 'quantity': 2}, {'price': 15.0, 'quantity': 1}]
        total = self.stripePayment._calculate_total(products=products) 
        self.assertEqual(total, 35)
    
    def test_handle_charge_response_success(self):
        
        charge = Mock(status='succeeded', id=123)
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


    def test_stripe_charge_handle_exception_cardError(self):
        with patch('order.stripe_payment.stripe.Charge.create') as mock_charge_create:
            
            mock_charge_create.side_effect =  CardError('error_type', 'message', 'param', 'code', 'http_status')
            order = Mock(id=1)
            response = self.stripePayment.stripeCharge(data=self.data, order=order)
            expected = {'status': 'failed','stripe_error': 'error_type'}
            self.assertEqual(expected, response)
            

    def test_stripe_charge_handle_exception_stripe_error(self):
        with patch('order.stripe_payment.stripe.Charge.create') as mock_charge_create:
            mock_charge_create.side_effect = StripeError('error stripe')
            order = Mock(id=1)
            response = self.stripePayment.stripeCharge(data=self.data, order=order)
            expected = {'status': 'failed','stripe_error': 'error stripe'}
            self.assertEqual(expected, response)
            
            

            