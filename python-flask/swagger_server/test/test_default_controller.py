# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.customer_type import CustomerType  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_new_person_post(self):
        """Test case for new_person_post

        Create new person
        """
        response = self.client.open(
            '/sirJames/Person/1.0.0/newPerson',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_person_put(self):
        """Test case for update_person_put

        Create new person
        """
        query_string = [('Name', 'Name_example'),
                        ('employer', 'employer_example')]
        response = self.client.open(
            '/sirJames/Person/1.0.0/updatePerson',
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
