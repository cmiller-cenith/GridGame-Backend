# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from GridGame.models.base_model_ import Model
from GridGame.models.coord import Coord  # noqa: F401,E501
from GridGame.models.world_weights import WorldWeights  # noqa: F401,E501
from GridGame import util


class WorldBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, start: Coord=None, end: Coord=None, weights: WorldWeights=None):  # noqa: E501
        """WorldBody - a model defined in Swagger

        :param start: The start of this WorldBody.  # noqa: E501
        :type start: Coord
        :param end: The end of this WorldBody.  # noqa: E501
        :type end: Coord
        :param weights: The weights of this WorldBody.  # noqa: E501
        :type weights: WorldWeights
        """
        self.swagger_types = {
            'start': Coord,
            'end': Coord,
            'weights': WorldWeights
        }

        self.attribute_map = {
            'start': 'start',
            'end': 'end',
            'weights': 'weights'
        }
        self._start = start
        self._end = end
        self._weights = weights

    @classmethod
    def from_dict(cls, dikt) -> 'WorldBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The world_body of this WorldBody.  # noqa: E501
        :rtype: WorldBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def start(self) -> Coord:
        """Gets the start of this WorldBody.


        :return: The start of this WorldBody.
        :rtype: Coord
        """
        return self._start

    @start.setter
    def start(self, start: Coord):
        """Sets the start of this WorldBody.


        :param start: The start of this WorldBody.
        :type start: Coord
        """

        self._start = start

    @property
    def end(self) -> Coord:
        """Gets the end of this WorldBody.


        :return: The end of this WorldBody.
        :rtype: Coord
        """
        return self._end

    @end.setter
    def end(self, end: Coord):
        """Sets the end of this WorldBody.


        :param end: The end of this WorldBody.
        :type end: Coord
        """

        self._end = end

    @property
    def weights(self) -> WorldWeights:
        """Gets the weights of this WorldBody.


        :return: The weights of this WorldBody.
        :rtype: WorldWeights
        """
        return self._weights

    @weights.setter
    def weights(self, weights: WorldWeights):
        """Sets the weights of this WorldBody.


        :param weights: The weights of this WorldBody.
        :type weights: WorldWeights
        """

        self._weights = weights
