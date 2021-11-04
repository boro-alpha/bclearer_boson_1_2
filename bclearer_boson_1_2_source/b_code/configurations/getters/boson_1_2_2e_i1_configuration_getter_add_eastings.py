from bclearer_boson_1_2_source.b_code.configurations.objects.bespoke_operation_configurations import \
    BespokeOperationConfigurations


def get_boson_1_2_2e_i1_configuration_add_eastings() \
        -> BespokeOperationConfigurations:
    bespoke_operation_configuration = \
        BespokeOperationConfigurations(
            short_name='2e_i1_output_eastings_added')

    return \
        bespoke_operation_configuration
