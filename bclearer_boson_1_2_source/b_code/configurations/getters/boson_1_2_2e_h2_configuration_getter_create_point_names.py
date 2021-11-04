from bclearer_boson_1_2_source.b_code.common_knowledge.boson_1_2_matched_ea_objects import Boson12MatchedEaObjects
from bclearer_boson_1_2_source.b_code.common_knowledge.inspire_matched_ea_objects import InspireMatchedEaObjects
from bclearer_boson_1_2_source.b_code.configurations.objects.bespoke_create_point_names_configuration_objects import \
    BespokeCreatePointNamesConfigurationObjects
from bclearer_boson_1_2_source.b_code.configurations.objects.bespoke_operation_configurations import \
    BespokeOperationConfigurations


def get_boson_1_2_2e_h2_configuration_create_point_names() \
        -> BespokeOperationConfigurations:
    bespoke_create_point_names_configuration_object = \
        BespokeCreatePointNamesConfigurationObjects(
            direct_positions_type_matched_ea_object=InspireMatchedEaObjects.DIRECT_POSITION,
            subtype_name_type_instance_matched_ea_object=Boson12MatchedEaObjects.SUBTYPE_NAME_TYPE_INSTANCE,
            epsg_27700_coordinate_point_names_matched_ea_object=Boson12MatchedEaObjects.EPSG_27700_COORDINATE_POINT_NAMES)

    bespoke_operation_configuration = \
        BespokeOperationConfigurations(
            short_name='2e_h2_create_point_names',
            bespoke_operation_configuration_object=bespoke_create_point_names_configuration_object)

    return \
        bespoke_operation_configuration
