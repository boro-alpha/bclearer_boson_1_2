from bclearer_source.b_code.common_knowledge.convention_shift_operation_types import ConventionShiftOperationTypes
from bclearer_source.b_code.configurations.convention_shift_operation_configurations import \
    ConventionShiftOperationConfigurations


def get_boson_1_2_2e_j1_configuration_separate_standard_names_and_instances() \
        -> ConventionShiftOperationConfigurations:
    convention_shift_operation_configuration = \
        ConventionShiftOperationConfigurations(
            convention_shift_operation_type=ConventionShiftOperationTypes.SEPARATE_STANDARD_NAMES_AND_INSTANCES,
            output_universe_short_name='2e_j1_output_sep_standard_instances',
            package_name='2e_j1_new_objects_sep_standard_instances')

    return \
        convention_shift_operation_configuration


def get_boson_1_2_2e_j2_configuration_bespoke_standard_names_and_instances() \
        -> ConventionShiftOperationConfigurations:
    convention_shift_operation_configuration = \
        ConventionShiftOperationConfigurations(
            convention_shift_operation_type=ConventionShiftOperationTypes.SEPARATE_BESPOKE_NAMES_AND_INSTANCES,
            output_universe_short_name='2e_j2_output_sep_bespoke_instances',
            list_of_configuration_objects=[],
            package_name='2e_j2_new_objects_sep_bespoke_instances')

    return \
        convention_shift_operation_configuration
