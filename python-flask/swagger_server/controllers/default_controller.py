import connexion
import six

from swagger_server.models.customer_type import CustomerType  # noqa: E501
from swagger_server import util


def new_person_post():  # noqa: E501
    """Create new person

    Create new person # noqa: E501


    :rtype: List[CustomerType]
    """
    return 'do some magic!'


def update_person_put(Name=None, employer=None):  # noqa: E501
    """Create new person

    Create new person # noqa: E501

    :param Name: person name
    :type Name: str
    :param employer: person employer
    :type employer: str

    :rtype: None
    """
    return 'do some magic!'
