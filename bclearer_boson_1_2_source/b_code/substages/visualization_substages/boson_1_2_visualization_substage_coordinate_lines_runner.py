from bclearer_source.b_code.substages.visualizations.instrumentation_and_visualization_runner import \
    instrument_and_visualize
from nf_common_source.code.services.reporting_service.wrappers.run_and_log_function_wrapper import run_and_log_function
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import \
    EaToolsSessionManagers

from bclearer_boson_1_2_source.b_code.configurations.getters.boson_1_2_2e_i1_configuration_getter_add_eastings import \
    get_boson_1_2_2e_i1_configuration_add_eastings
from bclearer_boson_1_2_source.b_code.configurations.getters.boson_1_2_2e_i2_configuration_getter_add_northings import \
    get_boson_1_2_2e_i2_configuration_add_northings
from bclearer_boson_1_2_source.b_code.configurations.getters.boson_1_2_2e_i3_configuration_getter_add_composite_names import \
    get_boson_1_2_2e_i3_configuration_add_composite_names
from bclearer_boson_1_2_source.b_code.configurations.getters.boson_1_2_2e_i4_configuration_getter_add_coordinate_intersections import \
    get_boson_1_2_2e_i4_configuration_add_coordinate_intersections
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.runners.boson_1_2_add_composite_names_operation_substage_runner import \
    run_boson_1_2_add_composite_names_operation_substage
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.runners.boson_1_2_add_coordinate_intersections_operation_substage_runner import \
    run_boson_1_2_add_coordinate_intersections_operation_substage
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.runners.boson_1_2_add_eastings_operation_substage_runner import \
    run_boson_1_2_add_eastings_operation_substage
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.runners.boson_1_2_add_northings_operation_substage_runner import \
    run_boson_1_2_add_northings_operation_substage


@run_and_log_function
def run_visualization_substage_coordinate_names(
        ea_tools_session_manager: EaToolsSessionManagers,
        output_folder_name: str,
        content_universe: NfEaComUniverses) \
        -> NfEaComUniverses:
    eastings_added_universe = \
        run_boson_1_2_add_eastings_operation_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=content_universe,
            bespoke_operation_configuration=get_boson_1_2_2e_i1_configuration_add_eastings())

    northings_added_universe = \
        run_boson_1_2_add_northings_operation_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=eastings_added_universe,
            bespoke_operation_configuration=get_boson_1_2_2e_i2_configuration_add_northings())

    composite_names_added_universe = \
        run_boson_1_2_add_composite_names_operation_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=northings_added_universe,
            bespoke_operation_configuration=get_boson_1_2_2e_i3_configuration_add_composite_names())

    coordinate_intersections_added_universe = \
        run_boson_1_2_add_coordinate_intersections_operation_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=composite_names_added_universe,
            bespoke_operation_configuration=get_boson_1_2_2e_i4_configuration_add_coordinate_intersections())

    instrument_and_visualize(
        output_folder_name=output_folder_name,
        visualization_substage_output_universe=coordinate_intersections_added_universe)

    return \
        coordinate_intersections_added_universe
