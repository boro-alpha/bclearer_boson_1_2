from bclearer_source.b_code.common_knowledge.bclearer_matched_ea_objects import BclearerMatchedEaObjects
from bclearer_source.b_code.common_knowledge.digitialisation_level_stereotype_matched_ea_objects import \
    DigitalisationLevelStereotypeMatchedEaObjects
from bclearer_source.b_code.substages.operations.b_evolve.common.new_root_package_creator import create_root_package
from bclearer_source.b_code.substages.operations.common.new_ea_objects_dictionary_creator import \
    create_new_ea_objects_dictionary
from bclearer_source.b_code.substages.operations.common.nf_ea_com_universe_updater import \
    update_nf_ea_com_universe_with_dictionary
from bclearer_source.b_code.substages.operations.common.nf_uuid_from_ea_guid_from_collection_getter import \
    get_nf_uuid_from_ea_guid_from_collection
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.collection_types.nf_ea_com_collection_types import \
    NfEaComCollectionTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import \
    EaToolsSessionManagers
from nf_ea_common_tools_source.b_code.services.session.processes.creators.empty_nf_ea_com_universe_creator import \
    create_empty_nf_ea_universe

from bclearer_boson_1_2_source.b_code.common_knowledge.boson_1_2_matched_ea_objects import Boson12MatchedEaObjects
from bclearer_boson_1_2_source.b_code.common_knowledge.coordinate_line_dimensions import CoordinateLineDimensions
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.coordinate_lines.common.coordinate_line_exemplars_from_xml_test_attributes_getter import \
    get_coordinate_line_exemplars_from_xml_test_attributes
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.coordinate_lines.common.coordinate_line_to_structure_adder import \
    add_coordinate_line_structure_to_dictionary


def orchestrate_add_eastings(
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

    eastings_exemplars = \
        get_coordinate_line_exemplars_from_xml_test_attributes(
            nf_ea_com_universe=content_universe,
            dimension=CoordinateLineDimensions.EASTINGS)

    new_ea_objects_dictionary = \
        create_new_ea_objects_dictionary()

    package_nf_uuid = \
        create_root_package(
            nf_ea_com_universe=output_universe,
            package_name='Coordinate Lines - Eastings')

    type_nf_uuid = \
        get_nf_uuid_from_ea_guid_from_collection(
            nf_ea_com_universe=output_universe,
            collection_type=NfEaComCollectionTypes.EA_CLASSIFIERS,
            ea_guid=Boson12MatchedEaObjects.EPSG_27700_EASTING_COORDINATE_LINES.ea_guid)

    name_nf_uuid = \
        get_nf_uuid_from_ea_guid_from_collection(
            nf_ea_com_universe=output_universe,
            collection_type=NfEaComCollectionTypes.EA_CLASSIFIERS,
            ea_guid=Boson12MatchedEaObjects.EPSG_27700_EASTING_COORDINATE_LINE_NAMES.ea_guid)

    character_string_nf_uuid = \
        get_nf_uuid_from_ea_guid_from_collection(
            nf_ea_com_universe=output_universe,
            collection_type=NfEaComCollectionTypes.EA_CLASSIFIERS,
            ea_guid=BclearerMatchedEaObjects.CHARACTER_STRINGS.ea_guid)

    named_by_stereotype_nf_uuid = \
        get_nf_uuid_from_ea_guid_from_collection(
            nf_ea_com_universe=output_universe,
            collection_type=NfEaComCollectionTypes.EA_STEREOTYPES,
            ea_guid=BclearerMatchedEaObjects.NAMED_BY_STEREOTYPE.ea_guid)

    line_digitalisation_level_stereotype_nf_uuid = \
        get_nf_uuid_from_ea_guid_from_collection(
            nf_ea_com_universe=output_universe,
            collection_type=NfEaComCollectionTypes.EA_STEREOTYPES,
            ea_guid=DigitalisationLevelStereotypeMatchedEaObjects.DIGITALISATION_LEVEL_4_CLASS_STEREOTYPE.ea_guid)

    name_digitalisation_level_stereotype_nf_uuid = \
        get_nf_uuid_from_ea_guid_from_collection(
            nf_ea_com_universe=output_universe,
            collection_type=NfEaComCollectionTypes.EA_STEREOTYPES,
            ea_guid=DigitalisationLevelStereotypeMatchedEaObjects.DIGITALISATION_LEVEL_1_CLASS_STEREOTYPE.ea_guid)

    for eastings_exemplar in eastings_exemplars:
        new_ea_objects_dictionary = \
            add_coordinate_line_structure_to_dictionary(
                new_ea_objects_dictionary=new_ea_objects_dictionary,
                exemplar=eastings_exemplar,
                suffix='Easting',
                type_nf_uuid=type_nf_uuid,
                name_nf_uuid=name_nf_uuid,
                package_nf_uuid=package_nf_uuid,
                character_string_nf_uuid=character_string_nf_uuid,
                named_by_stereotype_nf_uuid=named_by_stereotype_nf_uuid,
                line_digitalisation_level_stereotype_nf_uuid=line_digitalisation_level_stereotype_nf_uuid,
                name_digitalisation_level_stereotype_nf_uuid=name_digitalisation_level_stereotype_nf_uuid)

    update_nf_ea_com_universe_with_dictionary(
        nf_ea_com_universe=output_universe,
        new_ea_objects_dictionary=new_ea_objects_dictionary)

    return \
        output_universe
