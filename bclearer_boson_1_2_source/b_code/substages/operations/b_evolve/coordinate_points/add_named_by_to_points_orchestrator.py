from bclearer_source.b_code.common_knowledge.bclearer_matched_ea_objects import BclearerMatchedEaObjects
from bclearer_source.b_code.substages.operations.common.connector_adder import add_new_connector_to_dictionary
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
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.coordinate_lines.common.nf_uuid_keyed_on_name_prefix_dictionary_getter import \
    get_nf_uuid_keyed_on_name_prefix_dictionary


def orchestrate_add_named_by_to_points(
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

    points_keyed_on_exemplars = \
        get_nf_uuid_keyed_on_name_prefix_dictionary(
            nf_ea_com_universe=output_universe,
            matched_type=Boson12MatchedEaObjects.EPSG_27700_COORDINATE_POINTS,
            prefix_word_count=2)

    point_names_keyed_on_exemplars = \
        get_nf_uuid_keyed_on_name_prefix_dictionary(
            nf_ea_com_universe=output_universe,
            matched_type=Boson12MatchedEaObjects.EPSG_27700_COORDINATE_POINT_NAMES,
            prefix_word_count=2)

    named_by_stereotype_nf_uuid = \
        get_nf_uuid_from_ea_guid_from_collection(
            nf_ea_com_universe=output_universe,
            collection_type=NfEaComCollectionTypes.EA_STEREOTYPES,
            ea_guid=BclearerMatchedEaObjects.NAMED_BY_STEREOTYPE.ea_guid)

    for point_exemplar, point_nf_uuid in points_keyed_on_exemplars.items():
        __add_named_by(
            new_ea_objects_dictionary=new_ea_objects_dictionary,
            point_exemplar=point_exemplar,
            point_nf_uuid=point_nf_uuid,
            point_names_keyed_on_exemplars=point_names_keyed_on_exemplars,
            named_by_stereotype_nf_uuid=named_by_stereotype_nf_uuid)

    update_nf_ea_com_universe_with_dictionary(
        nf_ea_com_universe=output_universe,
        new_ea_objects_dictionary=new_ea_objects_dictionary)

    return \
        output_universe


def __add_named_by(
        new_ea_objects_dictionary: dict,
        point_exemplar: str,
        point_nf_uuid: str,
        point_names_keyed_on_exemplars: dict,
        named_by_stereotype_nf_uuid: str) \
        -> None:
    point_name_nf_uuid = \
        point_names_keyed_on_exemplars[point_exemplar]

    named_by_association_nf_uuid = \
        add_new_connector_to_dictionary(
            new_connector_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.EA_CONNECTORS],
            place_1_nf_uuid=point_name_nf_uuid,
            place_2_nf_uuid=point_nf_uuid,
            connector_type=EaConnectorTypes.ASSOCIATION)

    add_new_stereotype_usage_to_dictionary(
        new_stereotype_usage_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.STEREOTYPE_USAGE],
        client_nf_uuid=named_by_association_nf_uuid,
        client_collection_type=NfEaComCollectionTypes.EA_CONNECTORS,
        stereotype_nf_uuid=named_by_stereotype_nf_uuid)
