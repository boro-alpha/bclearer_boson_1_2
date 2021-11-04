from bclearer_source.b_code.common_knowledge.digitialisation_level_stereotype_matched_ea_objects import \
    DigitalisationLevelStereotypeMatchedEaObjects
from bclearer_source.b_code.substages.operations.b_evolve.common.new_root_package_creator import create_root_package
from bclearer_source.b_code.substages.operations.common.class_adder import add_new_class_to_dictionary
from bclearer_source.b_code.substages.operations.common.connector_adder import add_new_connector_to_dictionary
from bclearer_source.b_code.substages.operations.common.instances_nf_uuids_getter import \
    get_instances_nf_uuids_of_matched_type
from bclearer_source.b_code.substages.operations.common.new_ea_objects_dictionary_creator import \
    create_new_ea_objects_dictionary
from bclearer_source.b_code.substages.operations.common.nf_ea_com_universe_updater import \
    update_nf_ea_com_universe_with_dictionary
from bclearer_source.b_code.substages.operations.common.nf_uuid_from_ea_guid_from_collection_getter import \
    get_nf_uuid_from_ea_guid_from_collection
from bclearer_source.b_code.substages.operations.common.stereotype_adder import add_new_stereotype_usage_to_dictionary
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.ea_connector_types import EaConnectorTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.collection_types.nf_ea_com_collection_types import \
    NfEaComCollectionTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import \
    EaToolsSessionManagers
from nf_ea_common_tools_source.b_code.services.session.processes.creators.empty_nf_ea_com_universe_creator import \
    create_empty_nf_ea_universe
from bclearer_boson_1_2_source.b_code.common_knowledge.boson_1_2_matched_ea_objects import Boson12MatchedEaObjects
from bclearer_boson_1_2_source.b_code.common_knowledge.inspire_matched_ea_objects import InspireMatchedEaObjects
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.coordinate_lines.common.coordinate_point_exemplars_from_xml_test_attributes_getter import \
    get_coordinate_point_exemplars_from_xml_test_attributes
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.coordinate_lines.common.nf_uuid_sets_keyed_on_name_prefix_dictionary_getter import \
    get_nf_uuid_sets_keyed_on_name_prefix_dictionary
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.coordinate_points.connector_by_name_remover import \
    remove_connector_by_name
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.coordinate_points.nf_uuid_sets_by_association_keyed_on_name_prefix_dictionary_getter import \
    get_nf_uuid_sets_by_association_keyed_on_name_prefix_dictionary
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.coordinate_points.original_points_remover import \
    remove_original_gm_points


def orchestrate_deduplicate_points(
        content_universe: NfEaComUniverses,
        ea_tools_session_manager: EaToolsSessionManagers,
        short_name: str) \
        -> NfEaComUniverses:
    output_universe = \
        create_empty_nf_ea_universe(
            ea_tools_session_manager=ea_tools_session_manager,
            short_name=short_name)

    output_universe.nf_ea_com_registry.dictionary_of_collections = \
        content_universe.nf_ea_com_registry.dictionary_of_collections.copy()

    new_ea_objects_dictionary = \
        create_new_ea_objects_dictionary()

    original_gm_points = \
        get_instances_nf_uuids_of_matched_type(
            nf_ea_com_universe=content_universe,
            matched_type=InspireMatchedEaObjects.GM_POINT)

    __add_new_objects(
        output_universe=output_universe,
        new_ea_objects_dictionary=new_ea_objects_dictionary)

    remove_original_gm_points(
        output_universe=output_universe,
        original_gm_points=original_gm_points)

    remove_connector_by_name(
        nf_ea_com_universe=output_universe,
        connector_name_to_delete='lowerCorner')

    remove_connector_by_name(
        nf_ea_com_universe=output_universe,
        connector_name_to_delete='upperCorner')

    return \
        output_universe


def __add_new_objects(
        output_universe: NfEaComUniverses,
        new_ea_objects_dictionary: dict) \
        -> None:
    package_nf_uuid = \
        create_root_package(
            nf_ea_com_universe=output_universe,
            package_name='Coordinate Points - Unique Points')

    point_boson_type_nf_uuid = \
        get_nf_uuid_from_ea_guid_from_collection(
            nf_ea_com_universe=output_universe,
            collection_type=NfEaComCollectionTypes.EA_CLASSIFIERS,
            ea_guid=Boson12MatchedEaObjects.EPSG_27700_COORDINATE_POINTS.ea_guid)

    point_inspire_type_nf_uuid = \
        get_nf_uuid_from_ea_guid_from_collection(
            nf_ea_com_universe=output_universe,
            collection_type=NfEaComCollectionTypes.EA_CLASSIFIERS,
            ea_guid=InspireMatchedEaObjects.GM_POINT.ea_guid)

    point_exemplars = \
        get_coordinate_point_exemplars_from_xml_test_attributes(
            nf_ea_com_universe=output_universe)

    geometry_associated_nf_uuids = \
        get_nf_uuid_sets_by_association_keyed_on_name_prefix_dictionary(
            nf_ea_com_universe=output_universe,
            association_name='geometry')

    lower_corner_associated_nf_uuids = \
        get_nf_uuid_sets_by_association_keyed_on_name_prefix_dictionary(
            nf_ea_com_universe=output_universe,
            association_name='lowerCorner')

    upper_corner_associated_nf_uuids = \
        get_nf_uuid_sets_by_association_keyed_on_name_prefix_dictionary(
            nf_ea_com_universe=output_universe,
            association_name='upperCorner')

    point_name_instances_dictionary = \
        get_nf_uuid_sets_keyed_on_name_prefix_dictionary(
            nf_ea_com_universe=output_universe,
            matched_type=Boson12MatchedEaObjects.EPSG_27700_COORDINATE_POINT_NAME_INSTANCES,
            prefix_word_count=2)

    digitalisation_level_stereotype_nf_uuid = \
        get_nf_uuid_from_ea_guid_from_collection(
            nf_ea_com_universe=output_universe,
            collection_type=NfEaComCollectionTypes.EA_STEREOTYPES,
            ea_guid=DigitalisationLevelStereotypeMatchedEaObjects.DIGITALISATION_LEVEL_5_CLASS_STEREOTYPE.ea_guid)

    for point_exemplar in point_exemplars:
        __add_point_to_dictionary(
            new_ea_objects_dictionary=new_ea_objects_dictionary,
            point_exemplar=point_exemplar,
            type_nf_uuids={point_boson_type_nf_uuid, point_inspire_type_nf_uuid},
            package_nf_uuid=package_nf_uuid,
            geometry_associated_nf_uuids=geometry_associated_nf_uuids,
            lower_corner_associated_nf_uuids=lower_corner_associated_nf_uuids,
            upper_corner_associated_nf_uuids=upper_corner_associated_nf_uuids,
            point_name_instances_dictionary=point_name_instances_dictionary,
            digitalisation_level_stereotype_nf_uuid=digitalisation_level_stereotype_nf_uuid)

    update_nf_ea_com_universe_with_dictionary(
        nf_ea_com_universe=output_universe,
        new_ea_objects_dictionary=new_ea_objects_dictionary)


def __add_point_to_dictionary(
        new_ea_objects_dictionary: dict,
        point_exemplar: str,
        type_nf_uuids: set,
        package_nf_uuid: str,
        geometry_associated_nf_uuids: dict,
        lower_corner_associated_nf_uuids: dict,
        upper_corner_associated_nf_uuids: dict,
        point_name_instances_dictionary: dict,
        digitalisation_level_stereotype_nf_uuid: str) \
        -> None:
    point_name_nf_uuid = \
        add_new_class_to_dictionary(
            new_ea_objects_dictionary[NfEaComCollectionTypes.EA_CLASSIFIERS],
            package_nf_uuid=package_nf_uuid,
            class_name=point_exemplar + ' Point')

    add_new_stereotype_usage_to_dictionary(
        new_stereotype_usage_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.STEREOTYPE_USAGE],
        client_nf_uuid=point_name_nf_uuid,
        client_collection_type=NfEaComCollectionTypes.EA_CLASSIFIERS,
        stereotype_nf_uuid=digitalisation_level_stereotype_nf_uuid)

    for type_nf_uuid in type_nf_uuids:
        add_new_connector_to_dictionary(
            new_connector_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.EA_CONNECTORS],
            place_1_nf_uuid=point_name_nf_uuid,
            place_2_nf_uuid=type_nf_uuid,
            connector_type=EaConnectorTypes.DEPENDENCY)

    if point_exemplar in geometry_associated_nf_uuids:
        for associated_geometry_nf_uuid in geometry_associated_nf_uuids[point_exemplar]:
            add_new_connector_to_dictionary(
                new_connector_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.EA_CONNECTORS],
                place_1_nf_uuid=associated_geometry_nf_uuid,
                place_2_nf_uuid=point_name_nf_uuid,
                connector_type=EaConnectorTypes.ASSOCIATION,
                connector_name='geometry')

    if point_exemplar in lower_corner_associated_nf_uuids:
        for associated_lower_corner_nf_uuid in lower_corner_associated_nf_uuids[point_exemplar]:
            add_new_connector_to_dictionary(
                new_connector_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.EA_CONNECTORS],
                place_1_nf_uuid=associated_lower_corner_nf_uuid,
                place_2_nf_uuid=point_name_nf_uuid,
                connector_type=EaConnectorTypes.ASSOCIATION,
                connector_name='lowerCornerPoint')

    if point_exemplar in upper_corner_associated_nf_uuids:
        for associated_upper_corner_nf_uuid in upper_corner_associated_nf_uuids[point_exemplar]:
            add_new_connector_to_dictionary(
                new_connector_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.EA_CONNECTORS],
                place_1_nf_uuid=associated_upper_corner_nf_uuid,
                place_2_nf_uuid=point_name_nf_uuid,
                connector_type=EaConnectorTypes.ASSOCIATION,
                connector_name='upperCornerPoint')

    if point_exemplar in point_name_instances_dictionary:
        for point_name_instance_nf_uuid in point_name_instances_dictionary[point_exemplar]:
            add_new_connector_to_dictionary(
                new_connector_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.EA_CONNECTORS],
                place_1_nf_uuid=point_name_nf_uuid,
                place_2_nf_uuid=point_name_instance_nf_uuid,
                connector_type=EaConnectorTypes.ASSOCIATION,
                connector_name='pos')
