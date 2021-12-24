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


class RoleCreationRequest(object):
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
        'code': 'str',
        'description': 'str',
        'resource': 'RoleResourceRequest',
        'when': 'WhenSpec'
    }

    attribute_map = {
        'code': 'code',
        'description': 'description',
        'resource': 'resource',
        'when': 'when'
    }

    required_map = {
        'code': 'required',
        'description': 'optional',
        'resource': 'required',
        'when': 'required'
    }

    def __init__(self, code=None, description=None, resource=None, when=None, local_vars_configuration=None):  # noqa: E501
        """RoleCreationRequest - a model defined in OpenAPI"
        
        :param code:  The code of the role (required)
        :type code: str
        :param description:  The description of the role
        :type description: str
        :param resource:  (required)
        :type resource: finbourne_access.RoleResourceRequest
        :param when:  (required)
        :type when: finbourne_access.WhenSpec

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._description = None
        self._resource = None
        self._when = None
        self.discriminator = None

        self.code = code
        self.description = description
        self.resource = resource
        self.when = when

    @property
    def code(self):
        """Gets the code of this RoleCreationRequest.  # noqa: E501

        The code of the role  # noqa: E501

        :return: The code of this RoleCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this RoleCreationRequest.

        The code of the role  # noqa: E501

        :param code: The code of this RoleCreationRequest.  # noqa: E501
        :type code: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9-_ +]{2,100}$', code)):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9-_ +]{2,100}$/`")  # noqa: E501

        self._code = code

    @property
    def description(self):
        """Gets the description of this RoleCreationRequest.  # noqa: E501

        The description of the role  # noqa: E501

        :return: The description of this RoleCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RoleCreationRequest.

        The description of the role  # noqa: E501

        :param description: The description of this RoleCreationRequest.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1024):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def resource(self):
        """Gets the resource of this RoleCreationRequest.  # noqa: E501


        :return: The resource of this RoleCreationRequest.  # noqa: E501
        :rtype: finbourne_access.RoleResourceRequest
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this RoleCreationRequest.


        :param resource: The resource of this RoleCreationRequest.  # noqa: E501
        :type resource: finbourne_access.RoleResourceRequest
        """
        if self.local_vars_configuration.client_side_validation and resource is None:  # noqa: E501
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource

    @property
    def when(self):
        """Gets the when of this RoleCreationRequest.  # noqa: E501


        :return: The when of this RoleCreationRequest.  # noqa: E501
        :rtype: finbourne_access.WhenSpec
        """
        return self._when

    @when.setter
    def when(self, when):
        """Sets the when of this RoleCreationRequest.


        :param when: The when of this RoleCreationRequest.  # noqa: E501
        :type when: finbourne_access.WhenSpec
        """
        if self.local_vars_configuration.client_side_validation and when is None:  # noqa: E501
            raise ValueError("Invalid value for `when`, must not be `None`")  # noqa: E501

        self._when = when

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
        if not isinstance(other, RoleCreationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoleCreationRequest):
            return True

        return self.to_dict() != other.to_dict()