from bclearer_source.b_code.common_knowledge.bclearer_constants import NAME_INSTANCE_ATTRIBUTE_NAME
from bclearer_source.b_code.substages.operations.common.attribute_adder import add_new_attribute_to_dictionary
from bclearer_source.b_code.substages.operations.common.class_adder import add_new_class_to_dictionary
from bclearer_source.b_code.substages.operations.common.connector_adder import add_new_connector_to_dictionary
from bclearer_source.b_code.substages.operations.common.stereotype_adder import add_new_stereotype_usage_to_dictionary
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.ea_connector_types import EaConnectorTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.collection_types.nf_ea_com_collection_types import \
    NfEaComCollectionTypes


def add_coordinate_line_structure_to_dictionary(
        new_ea_objects_dictionary: dict,
        exemplar: str,
        suffix: str,
        type_nf_uuid: str,
        name_nf_uuid: str,
        package_nf_uuid: str,
        character_string_nf_uuid: str,
        named_by_stereotype_nf_uuid: str,
        line_digitalisation_level_stereotype_nf_uuid: str,
        name_digitalisation_level_stereotype_nf_uuid: str) \
        -> dict:
    coordinate_line_class_nf_uuid = \
        __add_object_with_matched_type(
            new_ea_objects_dictionary=new_ea_objects_dictionary,
            type_nf_uuid=type_nf_uuid,
            class_name=exemplar + ' ' + suffix,
            package_nf_uuid=package_nf_uuid)

    add_new_stereotype_usage_to_dictionary(
        new_stereotype_usage_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.STEREOTYPE_USAGE],
        client_nf_uuid=coordinate_line_class_nf_uuid,
        client_collection_type=NfEaComCollectionTypes.EA_CLASSIFIERS,
        stereotype_nf_uuid=line_digitalisation_level_stereotype_nf_uuid)

    coordinate_line_name_class_nf_uuid = \
        __add_object_with_matched_type(
            new_ea_objects_dictionary=new_ea_objects_dictionary,
            type_nf_uuid=name_nf_uuid,
            class_name=exemplar + ' ' + suffix + ' Name',
            package_nf_uuid=package_nf_uuid)

    add_new_stereotype_usage_to_dictionary(
        new_stereotype_usage_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.STEREOTYPE_USAGE],
        client_nf_uuid=coordinate_line_name_class_nf_uuid,
        client_collection_type=NfEaComCollectionTypes.EA_CLASSIFIERS,
        stereotype_nf_uuid=name_digitalisation_level_stereotype_nf_uuid)

    __add_name_instance_attribute(
        new_ea_objects_dictionary=new_ea_objects_dictionary,
        name_nf_uuid=coordinate_line_name_class_nf_uuid,
        name_instance_exemplar=exemplar,
        character_string_nf_uuid=character_string_nf_uuid)

    __add_named_by_association(
        new_ea_objects_dictionary,
        named_object_nf_uuid=coordinate_line_class_nf_uuid,
        name_nf_uuid=coordinate_line_name_class_nf_uuid,
        named_by_stereotype_nf_uuid=named_by_stereotype_nf_uuid)

    return \
        new_ea_objects_dictionary


def __add_object_with_matched_type(
        new_ea_objects_dictionary: dict,
        type_nf_uuid: str,
        class_name: str,
        package_nf_uuid: str) \
        -> str:
    new_class_nf_uuid = \
        add_new_class_to_dictionary(
            new_classifier_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.EA_CLASSIFIERS],
            package_nf_uuid=package_nf_uuid,
            class_name=class_name)

    add_new_connector_to_dictionary(
        new_connector_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.EA_CONNECTORS],
        place_1_nf_uuid=new_class_nf_uuid,
        place_2_nf_uuid=type_nf_uuid,
        connector_type=EaConnectorTypes.DEPENDENCY)

    return \
        new_class_nf_uuid


def __add_named_by_association(
        new_ea_objects_dictionary: dict,
        named_object_nf_uuid: str,
        name_nf_uuid: str,
        named_by_stereotype_nf_uuid: str) \
        -> None:
    association_nf_uuid = \
        add_new_connector_to_dictionary(
            new_connector_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.EA_CONNECTORS],
            place_1_nf_uuid=name_nf_uuid,
            place_2_nf_uuid=named_object_nf_uuid,
            connector_type=EaConnectorTypes.ASSOCIATION)

    add_new_stereotype_usage_to_dictionary(
        new_stereotype_usage_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.STEREOTYPE_USAGE],
        client_nf_uuid=association_nf_uuid,
        client_collection_type=NfEaComCollectionTypes.EA_CONNECTORS,
        stereotype_nf_uuid=named_by_stereotype_nf_uuid)


def __add_name_instance_attribute(
        new_ea_objects_dictionary: dict,
        name_nf_uuid: str,
        name_instance_exemplar: str,
        character_string_nf_uuid: str) \
        -> None:
    add_new_attribute_to_dictionary(
        new_ea_attributes_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.EA_ATTRIBUTES],
        name_object_nf_uuid=name_nf_uuid,
        attribute_value=name_instance_exemplar,
        attribute_name=NAME_INSTANCE_ATTRIBUTE_NAME,
        attribute_type_nf_uuid=character_string_nf_uuid)
