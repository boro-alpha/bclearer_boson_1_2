from bclearer_source.b_code.common_knowledge.convention_shift_operation_types import ConventionShiftOperationTypes
from bclearer_source.b_code.configurations.convention_shift_operation_configurations import \
    ConventionShiftOperationConfigurations


def get_boson_1_2_2e_l_configuration_shift_universe_to_semantically_grounded() \
        -> ConventionShiftOperationConfigurations:
    convention_shift_operation_configuration = \
        ConventionShiftOperationConfigurations(
            convention_shift_operation_type=ConventionShiftOperationTypes.UNIVERSE_TO_SEMANTICALLY_GROUNDED_DIGITALISATION_LEVEL,
            output_universe_short_name='2e_l_output_semantic_grounded',
            package_name=None)

    return \
        convention_shift_operation_configuration
