# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1624
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from finbourne_access.configuration import Configuration


class AddPolicyCollectionToRoleRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'policy_collections': 'list[PolicyCollectionId]'
    }

    attribute_map = {
        'policy_collections': 'policyCollections'
    }

    required_map = {
        'policy_collections': 'required'
    }

    def __init__(self, policy_collections=None, local_vars_configuration=None):  # noqa: E501
        """AddPolicyCollectionToRoleRequest - a model defined in OpenAPI"
        
        :param policy_collections:  Identifiers of policy collections to add to a role (required)
        :type policy_collections: list[finbourne_access.PolicyCollectionId]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._policy_collections = None
        self.discriminator = None

        self.policy_collections = policy_collections

    @property
    def policy_collections(self):
        """Gets the policy_collections of this AddPolicyCollectionToRoleRequest.  # noqa: E501

        Identifiers of policy collections to add to a role  # noqa: E501

        :return: The policy_collections of this AddPolicyCollectionToRoleRequest.  # noqa: E501
        :rtype: list[finbourne_access.PolicyCollectionId]
        """
        return self._policy_collections

    @policy_collections.setter
    def policy_collections(self, policy_collections):
        """Sets the policy_collections of this AddPolicyCollectionToRoleRequest.

        Identifiers of policy collections to add to a role  # noqa: E501

        :param policy_collections: The policy_collections of this AddPolicyCollectionToRoleRequest.  # noqa: E501
        :type policy_collections: list[finbourne_access.PolicyCollectionId]
        """
        if self.local_vars_configuration.client_side_validation and policy_collections is None:  # noqa: E501
            raise ValueError("Invalid value for `policy_collections`, must not be `None`")  # noqa: E501

        self._policy_collections = policy_collections

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddPolicyCollectionToRoleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddPolicyCollectionToRoleRequest):
            return True

        return self.to_dict() != other.to_dict()