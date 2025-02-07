import connexion
import six

from GridGame.models.id_move_body import IdMoveBody  # noqa: E501
from GridGame.models.move_result import MoveResult  # noqa: E501
from GridGame import util


def world_id_move_delete(id):  # noqa: E501
    """Delete the most recent move made in the world.

    Undoes the last move taken by the player. # noqa: E501

    :param id: The ID of the world in which we wish to undo the last operation.
    :type id: 

    :rtype: MoveResult
    """
    return 'do some magic!'


def world_id_move_post(id, body=None):  # noqa: E501
    """Create a new move for the current player in the world.

    Perform a given action for the player in the given world. # noqa: E501

    :param id: The ID of the world to perform the move against.
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: MoveResult
    """
    if connexion.request.is_json:
        body = IdMoveBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
