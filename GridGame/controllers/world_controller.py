import connexion
import six

from GridGame.models.world import World  # noqa: E501
from GridGame.models.world_body import WorldBody  # noqa: E501
from GridGame.models.world_save import WorldSave  # noqa: E501
from GridGame import util


def world_get():  # noqa: E501
    """Fetch a list of worlds.

    Fetches a list of different worlds/maps. Ideally used by a UI to make a selection interface from. # noqa: E501


    :rtype: List[World]
    """
    return 'do some magic!'


def world_id_get(id):  # noqa: E501
    """Get a particular world.

    Gets world information for a particular id. # noqa: E501

    :param id: The ID of the world to retrieve info for
    :type id: 

    :rtype: WorldSave
    """
    return 'do some magic!'


def world_post(body=None):  # noqa: E501
    """Create a new world.

    Creates a new world according to the given properties. # noqa: E501

    :param body: Properties about how the world should be generated.
    :type body: dict | bytes

    :rtype: World
    """
    if connexion.request.is_json:
        body = WorldBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def world_random_get():  # noqa: E501
    """Get a world at random.

    Gets a saved world at random. # noqa: E501


    :rtype: World
    """
    return 'do some magic!'
