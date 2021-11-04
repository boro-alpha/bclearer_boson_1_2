from bclearer_source.b_code.common_knowledge.universe_modification_operation_types import \
    UniverseModificationOperationTypes
from bclearer_source.b_code.configurations.add_dependency_to_instances_of_type_configuration_objects import \
    AddDependencyToInstancesOfTypeConfigurationObjects
from bclearer_source.b_code.configurations.universe_modification_operation_configurations import \
    UniverseModificationOperationConfigurations

from bclearer_boson_1_2_source.b_code.common_knowledge.boson_1_2_matched_ea_objects import Boson12MatchedEaObjects
from bclearer_boson_1_2_source.b_code.common_knowledge.inspire_matched_ea_objects import InspireMatchedEaObjects


def get_boson_1_2_2e_h1_configuration_extend_direct_positions_type() \
        -> UniverseModificationOperationConfigurations:
    add_dependency_to_instances_of_type_configuration_object = \
        AddDependencyToInstancesOfTypeConfigurationObjects(
            matched_target_type=Boson12MatchedEaObjects.EPSG_27700_COORDINATE_POINT_NAME_INSTANCES,
            matched_source_objects_type=InspireMatchedEaObjects.DIRECT_POSITION)

    add_dependency_to_instances_of_type_operation_type = \
        UniverseModificationOperationTypes.ADD_DEPENDENCY_TO_INSTANCES_OF_TYPE

    universe_modification_operation_configuration = \
        UniverseModificationOperationConfigurations(
            universe_modification_operation_type=add_dependency_to_instances_of_type_operation_type,
            output_universe_short_name='2e_h1_extend_direct_positions_type',
            universe_modification_configuration_object=add_dependency_to_instances_of_type_configuration_object)

    return \
        universe_modification_operation_configuration
