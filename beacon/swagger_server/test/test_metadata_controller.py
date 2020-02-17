# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.beacon_concept_category import BeaconConceptCategory  # noqa: E501
from swagger_server.models.beacon_knowledge_map_statement import BeaconKnowledgeMapStatement  # noqa: E501
from swagger_server.models.beacon_predicate import BeaconPredicate  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMetadataController(BaseTestCase):
    """MetadataController integration test stubs"""

    def test_get_concept_categories(self):
        """Test case for get_concept_categories

        
        """
        response = self.client.open(
            '/categories',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_knowledge_map(self):
        """Test case for get_knowledge_map

        
        """
        response = self.client.open(
            '/kmap',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_predicates(self):
        """Test case for get_predicates

        
        """
        response = self.client.open(
            '/predicates',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
