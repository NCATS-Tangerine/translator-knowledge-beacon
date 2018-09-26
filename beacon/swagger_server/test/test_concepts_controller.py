# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.beacon_concept import BeaconConcept  # noqa: E501
from swagger_server.models.beacon_concept_with_details import BeaconConceptWithDetails  # noqa: E501
from swagger_server.models.exact_match_response import ExactMatchResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestConceptsController(BaseTestCase):
    """ConceptsController integration test stubs"""

    def test_get_concept_details(self):
        """Test case for get_concept_details

        
        """
        response = self.client.open(
            '/concepts/{concept_id}'.format(concept_id='concept_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_concepts(self):
        """Test case for get_concepts

        
        """
        query_string = [('keywords', 'keywords_example'),
                        ('categories', 'categories_example'),
                        ('offset', 56),
                        ('size', 56)]
        response = self.client.open(
            '/concepts',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_exact_matches_to_concept_list(self):
        """Test case for get_exact_matches_to_concept_list

        
        """
        query_string = [('c', 'c_example')]
        response = self.client.open(
            '/exactmatches',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
