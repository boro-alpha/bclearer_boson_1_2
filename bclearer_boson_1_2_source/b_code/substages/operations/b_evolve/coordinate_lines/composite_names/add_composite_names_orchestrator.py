from bclearer_source.b_code.substages.operations.b_evolve.common.new_root_package_creator import create_root_package
from bclearer_source.b_code.substages.operations.common.new_ea_objects_dictionary_creator import \
    create_new_ea_objects_dictionary
from bclearer_source.b_code.substages.operations.common.nf_ea_com_universe_updater import \
    update_nf_ea_com_universe_with_dictionary
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import \
    EaToolsSessionManagers
from nf_ea_common_tools_source.b_code.services.session.processes.creators.empty_nf_ea_com_universe_creator import \
    create_empty_nf_ea_universe
from bclearer_boson_1_2_source.b_code.common_knowledge.boson_1_2_matched_ea_objects import Boson12MatchedEaObjects
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.coordinate_lines.common.coordinate_join_association_structure_adder import \
    add_coordinate_join_association_structure


def orchestrate_add_composite_names(
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

    package_nf_uuid = \
        create_root_package(
            nf_ea_com_universe=output_universe,
            package_name='Coordinate Lines - Composite Names')

    add_coordinate_join_association_structure(
        nf_ea_com_universe=output_universe,
        new_ea_objects_dictionary=new_ea_objects_dictionary,
        package_nf_uuid=package_nf_uuid,
        easting_type_matched_ea_object=Boson12MatchedEaObjects.EPSG_27700_EASTING_COORDINATE_LINE_NAMES,
        northing_type_matched_ea_object=Boson12MatchedEaObjects.EPSG_27700_NORTHING_COORDINATE_LINE_NAMES,
        point_type_matched_ea_object=Boson12MatchedEaObjects.EPSG_27700_COORDINATE_POINT_NAMES,
        join_association_type_matched_ea_object=Boson12MatchedEaObjects.EPSG_27700_COORDINATE_POINT_NAME_COMPOSED_OFS,
        easting_association_name='first component',
        northing_association_name='second component',
        point_association_name='composite')

    update_nf_ea_com_universe_with_dictionary(
        nf_ea_com_universe=output_universe,
        new_ea_objects_dictionary=new_ea_objects_dictionary)

    return \
        output_universe
