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
    "container-storage pool show",
)
class Show(AAZCommand):
    """Get a Pool

    :example: Get a Storage Pool.
        az container-storage pool show -g "rg" -n "pool"
    """

    _aaz_info = {
        "version": "2023-07-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.containerstorage/pools/{}", "2023-07-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.pool_name = AAZStrArg(
            options=["-n", "--name", "--pool-name"],
            help="Pool Object",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]$",
                max_length=253,
                min_length=3,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.PoolsGet(ctx=self.ctx)()
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

    class PoolsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerStorage/pools/{poolName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

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
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.assignments = AAZListType()
            properties.pool_type = AAZObjectType(
                serialized_name="poolType",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.reclaim_policy = AAZStrType(
                serialized_name="reclaimPolicy",
            )
            properties.resources = AAZObjectType()
            properties.status = AAZObjectType()
            properties.zones = AAZListType()

            assignments = cls._schema_on_200.properties.assignments
            assignments.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.assignments.Element
            _element.id = AAZStrType(
                flags={"required": True},
            )
            _element.status = AAZObjectType()

            status = cls._schema_on_200.properties.assignments.Element.status
            status.message = AAZStrType()
            status.state = AAZStrType(
                flags={"required": True},
            )

            pool_type = cls._schema_on_200.properties.pool_type
            pool_type.azure_disk = AAZObjectType(
                serialized_name="azureDisk",
            )
            pool_type.elastic_san = AAZObjectType(
                serialized_name="elasticSan",
            )
            pool_type.ephemeral_disk = AAZObjectType(
                serialized_name="ephemeralDisk",
            )

            azure_disk = cls._schema_on_200.properties.pool_type.azure_disk
            azure_disk.disks = AAZListType()
            azure_disk.encryption = AAZObjectType()
            azure_disk.resource_group = AAZStrType(
                serialized_name="resourceGroup",
                flags={"read_only": True},
            )
            azure_disk.sku_name = AAZStrType(
                serialized_name="skuName",
            )

            disks = cls._schema_on_200.properties.pool_type.azure_disk.disks
            disks.Element = AAZObjectType()
            _ShowHelper._build_schema_disk_read(disks.Element)

            encryption = cls._schema_on_200.properties.pool_type.azure_disk.encryption
            encryption.identity = AAZObjectType()
            _ShowHelper._build_schema_managed_service_identity_read(encryption.identity)
            encryption.key_name = AAZStrType(
                serialized_name="keyName",
                flags={"required": True},
            )
            encryption.key_vault_uri = AAZStrType(
                serialized_name="keyVaultUri",
                flags={"required": True},
            )

            elastic_san = cls._schema_on_200.properties.pool_type.elastic_san
            elastic_san.encryption = AAZObjectType()
            elastic_san.resource_group = AAZStrType(
                serialized_name="resourceGroup",
                flags={"read_only": True},
            )
            elastic_san.sku_name = AAZStrType(
                serialized_name="skuName",
            )

            encryption = cls._schema_on_200.properties.pool_type.elastic_san.encryption
            encryption.identity = AAZObjectType()
            _ShowHelper._build_schema_managed_service_identity_read(encryption.identity)
            encryption.key_name = AAZStrType(
                serialized_name="keyName",
                flags={"required": True},
            )
            encryption.key_vault_uri = AAZStrType(
                serialized_name="keyVaultUri",
                flags={"required": True},
            )

            ephemeral_disk = cls._schema_on_200.properties.pool_type.ephemeral_disk
            ephemeral_disk.disks = AAZListType()
            ephemeral_disk.replicas = AAZIntType()

            disks = cls._schema_on_200.properties.pool_type.ephemeral_disk.disks
            disks.Element = AAZObjectType()
            _ShowHelper._build_schema_disk_read(disks.Element)

            resources = cls._schema_on_200.properties.resources
            resources.requests = AAZObjectType()

            requests = cls._schema_on_200.properties.resources.requests
            requests.storage = AAZIntType()

            status = cls._schema_on_200.properties.status
            status.message = AAZStrType()
            status.state = AAZStrType(
                flags={"required": True},
            )

            zones = cls._schema_on_200.properties.zones
            zones.Element = AAZStrType()

            system_data = cls._schema_on_200.system_data
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

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_disk_read = None

    @classmethod
    def _build_schema_disk_read(cls, _schema):
        if cls._schema_disk_read is not None:
            _schema.id = cls._schema_disk_read.id
            _schema.reference = cls._schema_disk_read.reference
            return

        cls._schema_disk_read = _schema_disk_read = AAZObjectType()

        disk_read = _schema_disk_read
        disk_read.id = AAZStrType(
            flags={"required": True},
        )
        disk_read.reference = AAZStrType(
            flags={"required": True},
        )

        _schema.id = cls._schema_disk_read.id
        _schema.reference = cls._schema_disk_read.reference

    _schema_managed_service_identity_read = None

    @classmethod
    def _build_schema_managed_service_identity_read(cls, _schema):
        if cls._schema_managed_service_identity_read is not None:
            _schema.principal_id = cls._schema_managed_service_identity_read.principal_id
            _schema.tenant_id = cls._schema_managed_service_identity_read.tenant_id
            _schema.type = cls._schema_managed_service_identity_read.type
            _schema.user_assigned_identities = cls._schema_managed_service_identity_read.user_assigned_identities
            return

        cls._schema_managed_service_identity_read = _schema_managed_service_identity_read = AAZObjectType()

        managed_service_identity_read = _schema_managed_service_identity_read
        managed_service_identity_read.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )
        managed_service_identity_read.tenant_id = AAZStrType(
            serialized_name="tenantId",
            flags={"read_only": True},
        )
        managed_service_identity_read.type = AAZStrType(
            flags={"required": True},
        )
        managed_service_identity_read.user_assigned_identities = AAZDictType(
            serialized_name="userAssignedIdentities",
        )

        user_assigned_identities = _schema_managed_service_identity_read.user_assigned_identities
        user_assigned_identities.Element = AAZObjectType()

        _element = _schema_managed_service_identity_read.user_assigned_identities.Element
        _element.client_id = AAZStrType(
            serialized_name="clientId",
            flags={"read_only": True},
        )
        _element.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )

        _schema.principal_id = cls._schema_managed_service_identity_read.principal_id
        _schema.tenant_id = cls._schema_managed_service_identity_read.tenant_id
        _schema.type = cls._schema_managed_service_identity_read.type
        _schema.user_assigned_identities = cls._schema_managed_service_identity_read.user_assigned_identities


__all__ = ["Show"]
