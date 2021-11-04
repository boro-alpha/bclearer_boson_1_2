from bclearer_boson_1_2_source.b_code.configurations.objects.bespoke_operation_configurations import \
    BespokeOperationConfigurations


def get_boson_1_2_2e_i4_configuration_add_coordinate_intersections() \
        -> BespokeOperationConfigurations:
    bespoke_operation_configuration = \
        BespokeOperationConfigurations(
            short_name='2e_i4_output_coordinate_intersections_added')

    return \
        bespoke_operation_configuration
