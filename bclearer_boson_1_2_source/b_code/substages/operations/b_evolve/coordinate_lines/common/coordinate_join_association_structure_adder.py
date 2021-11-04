from bclearer_source.b_code.common_knowledge.matched_objects import MatchedEaObjects
from bclearer_source.b_code.substages.operations.common.association_class_adder import \
    add_new_association_class_to_dictionary
from bclearer_source.b_code.substages.operations.common.connector_adder import add_new_connector_to_dictionary
from bclearer_source.b_code.substages.operations.common.nf_uuid_from_ea_guid_from_collection_getter import \
    get_nf_uuid_from_ea_guid_from_collection
from nf_common_source.code.constants.standard_constants import DEFAULT_NULL_VALUE
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.ea_connector_types import EaConnectorTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.collection_types.nf_ea_com_collection_types import \
    NfEaComCollectionTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.coordinate_lines.common.nf_uuid_keyed_on_name_prefix_dictionary_getter import \
    get_nf_uuid_keyed_on_name_prefix_dictionary


def add_coordinate_join_association_structure(
        nf_ea_com_universe: NfEaComUniverses,
        new_ea_objects_dictionary: dict,
        package_nf_uuid: str,
        easting_type_matched_ea_object: MatchedEaObjects,
        northing_type_matched_ea_object: MatchedEaObjects,
        point_type_matched_ea_object: MatchedEaObjects,
        join_association_type_matched_ea_object: MatchedEaObjects,
        easting_association_name: str = DEFAULT_NULL_VALUE,
        northing_association_name: str = DEFAULT_NULL_VALUE,
        point_association_name: str = DEFAULT_NULL_VALUE) \
        -> None:
    eastings_dictionary = \
        get_nf_uuid_keyed_on_name_prefix_dictionary(
            nf_ea_com_universe=nf_ea_com_universe,
            matched_type=easting_type_matched_ea_object,
            prefix_word_count=1)

    northings_dictionary = \
        get_nf_uuid_keyed_on_name_prefix_dictionary(
            nf_ea_com_universe=nf_ea_com_universe,
            matched_type=northing_type_matched_ea_object,
            prefix_word_count=1)

    points_dictionary = \
        get_nf_uuid_keyed_on_name_prefix_dictionary(
            nf_ea_com_universe=nf_ea_com_universe,
            matched_type=point_type_matched_ea_object,
            prefix_word_count=2)

    join_association_type_nf_uuid = \
        get_nf_uuid_from_ea_guid_from_collection(
            nf_ea_com_universe=nf_ea_com_universe,
            collection_type=NfEaComCollectionTypes.EA_CLASSIFIERS,
            ea_guid=join_association_type_matched_ea_object.ea_guid)

    for point_exemplar, point_nf_uuid in points_dictionary.items():
        __add_coordinate_join_association(
            new_ea_objects_dictionary=new_ea_objects_dictionary,
            point_exemplar=point_exemplar,
            point_nf_uuid=point_nf_uuid,
            eastings_dictionary=eastings_dictionary,
            northings_dictionary=northings_dictionary,
            join_association_type_nf_uuid=join_association_type_nf_uuid,
            package_nf_uuid=package_nf_uuid,
            easting_association_name=easting_association_name,
            northing_association_name=northing_association_name,
            point_association_name=point_association_name)


def __add_coordinate_join_association(
        new_ea_objects_dictionary: dict,
        point_exemplar: str,
        point_nf_uuid: str,
        eastings_dictionary: dict,
        northings_dictionary: dict,
        join_association_type_nf_uuid: str,
        package_nf_uuid: str,
        easting_association_name: str,
        northing_association_name: str,
        point_association_name: str) \
        -> None:
    easting_and_northing = \
        point_exemplar.split(' ')

    easting = \
        easting_and_northing[0]

    northing = \
        easting_and_northing[1]

    easting_nf_uuid = \
        eastings_dictionary[easting]

    northing_nf_uuid = \
        northings_dictionary[northing]

    association_nf_uuid = \
        add_new_association_class_to_dictionary(
            new_ea_objects_dictionary[NfEaComCollectionTypes.EA_CLASSIFIERS],
            package_nf_uuid=package_nf_uuid)

    add_new_connector_to_dictionary(
        new_connector_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.EA_CONNECTORS],
        place_1_nf_uuid=association_nf_uuid,
        place_2_nf_uuid=join_association_type_nf_uuid,
        connector_type=EaConnectorTypes.DEPENDENCY)

    add_new_connector_to_dictionary(
        new_connector_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.EA_CONNECTORS],
        place_1_nf_uuid=association_nf_uuid,
        place_2_nf_uuid=point_nf_uuid,
        connector_type=EaConnectorTypes.ASSOCIATION,
        connector_name=point_association_name)

    add_new_connector_to_dictionary(
        new_connector_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.EA_CONNECTORS],
        place_1_nf_uuid=association_nf_uuid,
        place_2_nf_uuid=easting_nf_uuid,
        connector_type=EaConnectorTypes.ASSOCIATION,
        connector_name=easting_association_name)

    add_new_connector_to_dictionary(
        new_connector_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.EA_CONNECTORS],
        place_1_nf_uuid=association_nf_uuid,
        place_2_nf_uuid=northing_nf_uuid,
        connector_type=EaConnectorTypes.ASSOCIATION,
        connector_name=northing_association_name)
