# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from GridGame.models.world import World  # noqa: E501
from GridGame.models.world_body import WorldBody  # noqa: E501
from GridGame.models.world_save import WorldSave  # noqa: E501
from GridGame.test import BaseTestCase


class TestWorldController(BaseTestCase):
    """WorldController integration test stubs"""

    def test_world_get(self):
        """Test case for world_get

        Fetch a list of worlds.
        """
        response = self.client.open(
            '/api/world',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_world_id_get(self):
        """Test case for world_id_get

        Get a particular world.
        """
        response = self.client.open(
            '/api/world/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_world_post(self):
        """Test case for world_post

        Create a new world.
        """
        body = WorldBody()
        response = self.client.open(
            '/api/world',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_world_random_get(self):
        """Test case for world_random_get

        Get a world at random.
        """
        response = self.client.open(
            '/api/world/random',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
