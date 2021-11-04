from bclearer_source.b_code.substages.operations.b_evolve.common.new_root_package_creator import create_root_package
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.ea_connector_types import EaConnectorTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import \
    EaToolsSessionManagers
from nf_ea_common_tools_source.b_code.services.session.processes.creators.empty_nf_ea_com_universe_creator import \
    create_empty_nf_ea_universe

from bclearer_boson_1_2_source.b_code.common_knowledge.inspire_matched_ea_objects import InspireMatchedEaObjects
from bclearer_boson_1_2_source.b_code.common_knowledge.os_matched_ea_objects import OsMatchedEaObjects
from bclearer_boson_1_2_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.common.b1_dataframes_dictionary_summeriser import \
    summarise_dataframes_dictionary
from bclearer_boson_1_2_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_nf_ea_com.os_open_names_to_nf_ea_com_converters.attributes_converter import \
    convert_to_attributes
from bclearer_boson_1_2_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_nf_ea_com.os_open_names_to_nf_ea_com_converters.classifiers_converter import \
    convert_to_classifiers
from bclearer_boson_1_2_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_nf_ea_com.os_open_names_to_nf_ea_com_converters.many_to_many_connectors_converter import \
    convert_many_to_many_to_connectors
from bclearer_boson_1_2_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_nf_ea_com.os_open_names_to_nf_ea_com_converters.one_to_many_connectors_converter import \
    convert_one_to_many_to_connectors


def orchestrate_os_open_names_domain_to_nf_ea_com(
        content_universe: NfEaComUniverses,
        ea_tools_session_manager: EaToolsSessionManagers,
        os_open_names_dictionary: dict,
        short_name: str) \
        -> NfEaComUniverses:
    gml_data_content_universe = \
        create_empty_nf_ea_universe(
            ea_tools_session_manager=ea_tools_session_manager,
            short_name=short_name)

    dictionary_of_collections = \
        content_universe.nf_ea_com_registry.dictionary_of_collections

    for key in dictionary_of_collections.keys():
        gml_data_content_universe.nf_ea_com_registry.dictionary_of_collections[key] = \
            dictionary_of_collections[key]

    gml_data_content_universe = \
        __convert_domain(
            nf_ea_com_universe=gml_data_content_universe,
            os_open_names_dictionary=os_open_names_dictionary)

    return \
        gml_data_content_universe


def __convert_domain(
        nf_ea_com_universe: NfEaComUniverses,
        os_open_names_dictionary: dict) \
        -> NfEaComUniverses:
    root_package_nf_uuid = \
        create_root_package(
            nf_ea_com_universe=nf_ea_com_universe,
            package_name='GML Data Model')

    nf_ea_com_universe = \
        __convert_classifiers(
            nf_ea_com_universe=nf_ea_com_universe,
            os_open_names_dictionary=os_open_names_dictionary,
            root_package_nf_uuid=root_package_nf_uuid)

    nf_ea_com_universe = \
        __convert_connectors(
            nf_ea_com_universe=nf_ea_com_universe,
            os_open_names_dictionary=os_open_names_dictionary)

    nf_ea_com_universe = \
        __convert_attributes(
            nf_ea_com_universe=nf_ea_com_universe,
            os_open_names_dictionary=os_open_names_dictionary)

    summarise_dataframes_dictionary(
        dataframes_dictionary=nf_ea_com_universe.nf_ea_com_registry.dictionary_of_collections)

    return \
        nf_ea_com_universe


def __convert_classifiers(
        nf_ea_com_universe: NfEaComUniverses,
        os_open_names_dictionary: dict,
        root_package_nf_uuid: str) \
        -> NfEaComUniverses:
    nf_ea_com_universe = \
        convert_to_classifiers(
            os_open_names_dictionary=os_open_names_dictionary,
            nf_ea_com_universe=nf_ea_com_universe,
            matched_type=OsMatchedEaObjects.NAMED_PLACE,
            os_open_names_table_name='named_places',
            root_package_nf_uuid=root_package_nf_uuid)

    nf_ea_com_universe = \
        convert_to_classifiers(
            os_open_names_dictionary=os_open_names_dictionary,
            nf_ea_com_universe=nf_ea_com_universe,
            matched_type=InspireMatchedEaObjects.GM_ENVELOPE,
            os_open_names_table_name='envelopes',
            root_package_nf_uuid=root_package_nf_uuid)

    nf_ea_com_universe = \
        convert_to_classifiers(
            os_open_names_dictionary=os_open_names_dictionary,
            nf_ea_com_universe=nf_ea_com_universe,
            matched_type=InspireMatchedEaObjects.DIRECT_POSITION,
            os_open_names_table_name='direct_positions',
            root_package_nf_uuid=root_package_nf_uuid)

    nf_ea_com_universe = \
        convert_to_classifiers(
            os_open_names_dictionary=os_open_names_dictionary,
            nf_ea_com_universe=nf_ea_com_universe,
            matched_type=InspireMatchedEaObjects.GM_POINT,
            os_open_names_table_name='points',
            root_package_nf_uuid=root_package_nf_uuid)

    return \
        nf_ea_com_universe


def __convert_connectors(
        nf_ea_com_universe: NfEaComUniverses,
        os_open_names_dictionary: dict) \
        -> NfEaComUniverses:
    nf_ea_com_universe = \
        convert_one_to_many_to_connectors(
            os_open_names_dictionary=os_open_names_dictionary,
            nf_ea_com_universe=nf_ea_com_universe,
            os_open_names_table_name='envelopes',
            connector_name='boundedBy',
            connector_type=EaConnectorTypes.ASSOCIATION.type_name)

    nf_ea_com_universe = \
        convert_one_to_many_to_connectors(
            os_open_names_dictionary=os_open_names_dictionary,
            nf_ea_com_universe=nf_ea_com_universe,
            os_open_names_table_name='points',
            connector_name='geometry',
            connector_type=EaConnectorTypes.ASSOCIATION.type_name)

    nf_ea_com_universe.nf_ea_com_registry.dictionary_of_collections = \
        convert_many_to_many_to_connectors(
            os_open_names_dictionary=os_open_names_dictionary,
            nf_ea_com_dictionary=nf_ea_com_universe.nf_ea_com_registry.dictionary_of_collections,
            os_open_names_table_name='direct_positions',
            client_nf_uuid_column_name=NfColumnTypes.NF_UUIDS.column_name,
            supplier_nf_uuid_column_name='owning_nf_uuids',
            connector_type=EaConnectorTypes.ASSOCIATION.type_name,
            connector_name_column_name='link_name_from_owning_object')

    return \
        nf_ea_com_universe


def __convert_attributes(
        nf_ea_com_universe: NfEaComUniverses,
        os_open_names_dictionary: dict) \
        -> NfEaComUniverses:
    nf_ea_com_universe = \
        convert_to_attributes(
            os_open_names_dictionary=os_open_names_dictionary,
            nf_ea_com_universe=nf_ea_com_universe,
            attribute_name='xml_text',
            initial_value_column_name='xml_text',
            os_open_names_table_name='direct_positions',
            matched_classifying_ea_classifier=InspireMatchedEaObjects.CHARACTER_STRING)

    return \
        nf_ea_com_universe
