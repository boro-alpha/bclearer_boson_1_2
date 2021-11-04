from bclearer_source.b_code.substages.operations.b_evolve.universe_modification_operations.runners.universe_modification_operations_substage_runner import \
    run_universe_modification_operations_substage
from bclearer_source.b_code.substages.visualizations.instrumentation_and_visualization_runner import \
    instrument_and_visualize
from nf_common_source.code.services.reporting_service.wrappers.run_and_log_function_wrapper import run_and_log_function
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import \
    EaToolsSessionManagers
from bclearer_boson_1_2_source.b_code.configurations.getters.boson_1_2_2e_h2_configuration_getter_create_point_names import \
    get_boson_1_2_2e_h2_configuration_create_point_names
from bclearer_boson_1_2_source.b_code.configurations.getters.boson_1_2_2e_h3_configuration_getter_de_duplicate_points import \
    get_boson_1_2_2e_h3_configuration_de_duplicate_points
from bclearer_boson_1_2_source.b_code.configurations.getters.boson_1_2_2e_h6_configuration_getter_link_points_and_point_names import \
    get_boson_1_2_2e_h6_configuration_link_points_and_point_names
from bclearer_boson_1_2_source.b_code.configurations.getters.boson_1_2_2e_h1_configuration_getter_extend_direct_positions_type import \
    get_boson_1_2_2e_h1_configuration_extend_direct_positions_type
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.runners.boson_1_2_add_create_point_names_operation_substage_runner import \
    run_boson_1_2_create_point_names_operation_substage
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.runners.boson_1_2_add_de_duplicate_points_operation_substage_runner import \
    run_boson_1_2_de_duplicate_points_operation_substage
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.runners.boson_1_2_reify_link_points_and_point_names_operation_substage_runner import \
    run_boson_1_2_link_points_and_point_names_operation_substage


@run_and_log_function
def run_visualization_substage_expose_implicit_point_structure_and_names(
        ea_tools_session_manager: EaToolsSessionManagers,
        output_folder_name: str,
        content_universe: NfEaComUniverses) \
        -> NfEaComUniverses:
    direct_positions_extended_type_universe = \
        run_universe_modification_operations_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=content_universe,
            universe_modification_operation_configuration=get_boson_1_2_2e_h1_configuration_extend_direct_positions_type())

    point_names_created_universe = \
        run_boson_1_2_create_point_names_operation_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=direct_positions_extended_type_universe,
            bespoke_operation_configuration=get_boson_1_2_2e_h2_configuration_create_point_names())

    points_de_duplicated_universe = \
        run_boson_1_2_de_duplicate_points_operation_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=point_names_created_universe,
            bespoke_operation_configuration=get_boson_1_2_2e_h3_configuration_de_duplicate_points())

    exposed_implicit_point_structure_and_names_universe = \
        run_boson_1_2_link_points_and_point_names_operation_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=points_de_duplicated_universe,
            bespoke_operation_configuration=get_boson_1_2_2e_h6_configuration_link_points_and_point_names())

    instrument_and_visualize(
        output_folder_name=output_folder_name,
        visualization_substage_output_universe=exposed_implicit_point_structure_and_names_universe)

    return \
        exposed_implicit_point_structure_and_names_universe
