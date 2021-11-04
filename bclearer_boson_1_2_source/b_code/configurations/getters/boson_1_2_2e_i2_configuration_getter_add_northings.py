from bclearer_boson_1_2_source.b_code.configurations.objects.bespoke_operation_configurations import \
    BespokeOperationConfigurations


def get_boson_1_2_2e_i2_configuration_add_northings() \
        -> BespokeOperationConfigurations:
    bespoke_operation_configuration = \
        BespokeOperationConfigurations(
            short_name='2e_i2_output_northings_added')

    return \
        bespoke_operation_configuration
