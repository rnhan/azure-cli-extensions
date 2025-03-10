# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "container-storage pool volume create",
)
class Create(AAZCommand):
    """Create a Volume

    :example: Create a Volume.
        az container-storage pool volume create -g "rg" --pool-name "pool" -n "volume" --capacity-gi-b 2
    """

    _aaz_info = {
        "version": "2023-07-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.containerstorage/pools/{}/volumes/{}", "2023-07-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.pool_name = AAZStrArg(
            options=["--pool-name"],
            help="Pool Object",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]$",
                max_length=253,
                min_length=3,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.volume_name = AAZStrArg(
            options=["-n", "--name", "--volume-name"],
            help="Volume Resource",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]$",
                max_length=253,
                min_length=3,
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.capacity_gi_b = AAZIntArg(
            options=["--capacity-gi-b"],
            arg_group="Properties",
            help="Requested capacity in GiB",
            fmt=AAZIntArgFormat(
                maximum=65536,
                minimum=1,
            ),
        )
        _args_schema.labels = AAZDictArg(
            options=["--labels"],
            arg_group="Properties",
            help="String KV pairs indicating labels",
        )

        labels = cls._args_schema.labels
        labels.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.VolumesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class VolumesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerStorage/pools/{poolName}/volumes/{volumeName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "poolName", self.ctx.args.pool_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "volumeName", self.ctx.args.volume_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-07-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("capacityGiB", AAZIntType, ".capacity_gi_b", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("labels", AAZDictType, ".labels", typ_kwargs={"flags": {"required": True}})

            labels = _builder.get(".properties.labels")
            if labels is not None:
                labels.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.capacity_gi_b = AAZIntType(
                serialized_name="capacityGiB",
                flags={"required": True},
            )
            properties.labels = AAZDictType(
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.status = AAZObjectType()
            properties.volume_type = AAZObjectType(
                serialized_name="volumeType",
            )

            labels = cls._schema_on_200_201.properties.labels
            labels.Element = AAZStrType()

            status = cls._schema_on_200_201.properties.status
            status.message = AAZStrType()
            status.state = AAZStrType(
                flags={"required": True},
            )

            volume_type = cls._schema_on_200_201.properties.volume_type
            volume_type.elastic_san = AAZObjectType(
                serialized_name="elasticSan",
            )

            elastic_san = cls._schema_on_200_201.properties.volume_type.elastic_san
            elastic_san.target_iqn = AAZStrType(
                serialized_name="targetIqn",
                flags={"required": True},
            )
            elastic_san.target_portal_hostname = AAZStrType(
                serialized_name="targetPortalHostname",
                flags={"required": True},
            )
            elastic_san.target_portal_port = AAZIntType(
                serialized_name="targetPortalPort",
                flags={"required": True},
            )

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
