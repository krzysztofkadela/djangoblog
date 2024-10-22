from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Zbyszko',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_form_required_name_is_not_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form is valid name not filledin.")

    def test_form_required_email_is_not_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Zbyszko',
            'email': 'testtest.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form is valid name not filledin.")

    def test_form_required_massage_required(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Zbyszko',
            'email': 'testtest.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Form is valid name not filledin.")
    
   
