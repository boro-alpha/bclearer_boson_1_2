from bclearer_source.b_code.common_knowledge.matched_objects import MatchedEaObjects

from bclearer_boson_1_2_source.b_code.configurations.objects.bespoke_operation_configuration_objects import \
    BespokeOperationConfigurationObjects


class BespokeCreatePointNamesConfigurationObjects(
        BespokeOperationConfigurationObjects):
    def __init__(
            self,
            direct_positions_type_matched_ea_object: MatchedEaObjects,
            subtype_name_type_instance_matched_ea_object: MatchedEaObjects,
            epsg_27700_coordinate_point_names_matched_ea_object: MatchedEaObjects):
        self.direct_positions_type_matched_ea_object = \
            direct_positions_type_matched_ea_object

        self.subtype_name_type_instance_matched_ea_object = \
            subtype_name_type_instance_matched_ea_object

        self.epsg_27700_coordinate_point_names_matched_ea_object = \
            epsg_27700_coordinate_point_names_matched_ea_object

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
