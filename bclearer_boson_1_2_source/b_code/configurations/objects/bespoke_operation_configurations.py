from bclearer_boson_1_2_source.b_code.configurations.objects.bespoke_operation_configuration_objects import \
    BespokeOperationConfigurationObjects


class BespokeOperationConfigurations:
    def __init__(
            self,
            short_name: str,
            bespoke_operation_configuration_object: BespokeOperationConfigurationObjects = None):
        self.short_name = \
            short_name

        self.bespoke_operation_configuration_object = \
            bespoke_operation_configuration_object

    def __enter__(
            self):
        return \
            self

    def __exit__(
            self,
            exception_type,
            exception_value,
            traceback):
        pass
