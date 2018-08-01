# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PersonObj(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, ssn: float=None, dob: date=None):  # noqa: E501
        """PersonObj - a model defined in Swagger

        :param name: The name of this PersonObj.  # noqa: E501
        :type name: str
        :param ssn: The ssn of this PersonObj.  # noqa: E501
        :type ssn: float
        :param dob: The dob of this PersonObj.  # noqa: E501
        :type dob: date
        """
        self.swagger_types = {
            'name': str,
            'ssn': float,
            'dob': date
        }

        self.attribute_map = {
            'name': 'name',
            'ssn': 'ssn',
            'dob': 'dob'
        }

        self._name = name
        self._ssn = ssn
        self._dob = dob

    @classmethod
    def from_dict(cls, dikt) -> 'PersonObj':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PersonObj of this PersonObj.  # noqa: E501
        :rtype: PersonObj
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this PersonObj.


        :return: The name of this PersonObj.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this PersonObj.


        :param name: The name of this PersonObj.
        :type name: str
        """

        self._name = name

    @property
    def ssn(self) -> float:
        """Gets the ssn of this PersonObj.


        :return: The ssn of this PersonObj.
        :rtype: float
        """
        return self._ssn

    @ssn.setter
    def ssn(self, ssn: float):
        """Sets the ssn of this PersonObj.


        :param ssn: The ssn of this PersonObj.
        :type ssn: float
        """

        self._ssn = ssn

    @property
    def dob(self) -> date:
        """Gets the dob of this PersonObj.


        :return: The dob of this PersonObj.
        :rtype: date
        """
        return self._dob

    @dob.setter
    def dob(self, dob: date):
        """Sets the dob of this PersonObj.


        :param dob: The dob of this PersonObj.
        :type dob: date
        """

        self._dob = dob