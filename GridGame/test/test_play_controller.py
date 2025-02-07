# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from GridGame.models.id_move_body import IdMoveBody  # noqa: E501
from GridGame.models.move_result import MoveResult  # noqa: E501
from GridGame.test import BaseTestCase


class TestPlayController(BaseTestCase):
    """PlayController integration test stubs"""

    def test_world_id_move_delete(self):
        """Test case for world_id_move_delete

        Delete the most recent move made in the world.
        """
        response = self.client.open(
            '/api/world/{id}/move'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_world_id_move_post(self):
        """Test case for world_id_move_post

        Create a new move for the current player in the world.
        """
        body = IdMoveBody()
        response = self.client.open(
            '/api/world/{id}/move'.format(id='id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
