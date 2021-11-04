from bclearer_boson_1_2_source.b_code.configurations.objects.bespoke_operation_configurations import \
    BespokeOperationConfigurations


def get_boson_1_2_2e_i3_configuration_add_composite_names() \
        -> BespokeOperationConfigurations:
    bespoke_operation_configuration = \
        BespokeOperationConfigurations(
            short_name='2e_i3_output_composite_names_added')

    return \
        bespoke_operation_configuration
