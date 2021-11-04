from bclearer_source.b_code.substages.operations.b_evolve.content_operations.runners.merge_hdf5_model_content_operations_substage_runner import \
    run_merge_hdf5_model_content_operations_substage
from bclearer_source.b_code.substages.visualizations.instrumentation_and_visualization_runner import \
    instrument_and_visualize
from nf_common_source.code.services.reporting_service.wrappers.run_and_log_function_wrapper import run_and_log_function
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import \
    EaToolsSessionManagers

from bclearer_boson_1_2_source.b_code.configurations.getters.boson_1_2_2e_c2_configuration_getter_merge_inspire_bclearer_individual_powersets import \
    get_boson_1_2_2e_c2_configuration_load_hdf5_bclearer_individual_powersets, \
    get_boson_1_2_2e_c2_configuration_merge_inspire_bclearer_individual_powersets
from bclearer_boson_1_2_source.b_code.configurations.getters.boson_1_2_2e_c3_configuration_getter_merge_inspire_bclearer_naming_pattern import \
    get_boson_1_2_2e_c3_configuration_merge_inspire_bclearer_naming_pattern, \
    get_boson_1_2_2e_c3_configuration_load_hdf5_bclearer_naming_pattern
from bclearer_boson_1_2_source.b_code.configurations.getters.boson_1_2_2e_c1_configuration_getter_merge_inspire_bclearer_top_level_ontic import \
    get_boson_1_2_2e_c1_configuration_load_hdf5_bclearer_foundation_top_level_ontic_categories
from bclearer_boson_1_2_source.b_code.configurations.getters.boson_1_2_2e_c1_configuration_getter_merge_inspire_bclearer_top_level_ontic import \
    get_boson_1_2_2e_c1_configuration_merge_inspire_bclearer_top_level_ontic_categories
from bclearer_boson_1_2_source.b_code.configurations.getters.boson_1_2_2e_d_configuration_getter_merge_inspire_bclearer_link import \
    get_boson_1_2_2e_d1_configuration_load_hdf5_inspire_bclearer_link
from bclearer_boson_1_2_source.b_code.configurations.getters.boson_1_2_2e_d_configuration_getter_merge_inspire_bclearer_link import \
    get_boson_1_2_2e_d1_configuration_merge_inspire_bclearer_link
from bclearer_boson_1_2_source.b_code.configurations.getters.boson_1_2_2e_e_configuration_getter_merge_inspire_bclearer_boson import \
    get_boson_1_2_2e_e1_configuration_load_hdf5_boson
from bclearer_boson_1_2_source.b_code.configurations.getters.boson_1_2_2e_e_configuration_getter_merge_inspire_bclearer_boson import \
    get_boson_1_2_2e_e1_configuration_merge_inspire_bclearer_boson


@run_and_log_function
def run_visualization_substage_generalise(
        ea_tools_session_manager: EaToolsSessionManagers,
        output_folder_name: str,
        content_universe: NfEaComUniverses) \
        -> NfEaComUniverses:
    os_inspire_merged_bclearer_top_level_ontic_categories_universe = \
        run_merge_hdf5_model_content_operations_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe_from_input=content_universe,
            load_hdf5_model_configuration=get_boson_1_2_2e_c1_configuration_load_hdf5_bclearer_foundation_top_level_ontic_categories(),
            content_operation_configuration=get_boson_1_2_2e_c1_configuration_merge_inspire_bclearer_top_level_ontic_categories())

    instrument_and_visualize(
        output_folder_name=output_folder_name,
        visualization_substage_output_universe=os_inspire_merged_bclearer_top_level_ontic_categories_universe)

    os_inspire_merged_bclearer_individual_powerset_component_universe = \
        run_merge_hdf5_model_content_operations_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe_from_input=os_inspire_merged_bclearer_top_level_ontic_categories_universe,
            load_hdf5_model_configuration=get_boson_1_2_2e_c2_configuration_load_hdf5_bclearer_individual_powersets(),
            content_operation_configuration=get_boson_1_2_2e_c2_configuration_merge_inspire_bclearer_individual_powersets())

    instrument_and_visualize(
        output_folder_name=output_folder_name,
        visualization_substage_output_universe=os_inspire_merged_bclearer_individual_powerset_component_universe)

    os_inspire_merged_bclearer_naming_pattern_component_universe = \
        run_merge_hdf5_model_content_operations_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe_from_input=os_inspire_merged_bclearer_individual_powerset_component_universe,
            load_hdf5_model_configuration=get_boson_1_2_2e_c3_configuration_load_hdf5_bclearer_naming_pattern(),
            content_operation_configuration=get_boson_1_2_2e_c3_configuration_merge_inspire_bclearer_naming_pattern())

    instrument_and_visualize(
        output_folder_name=output_folder_name,
        visualization_substage_output_universe=os_inspire_merged_bclearer_naming_pattern_component_universe)

    os_inspire_linked_bclearer_universe = \
        run_merge_hdf5_model_content_operations_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe_from_input=os_inspire_merged_bclearer_naming_pattern_component_universe,
            load_hdf5_model_configuration=get_boson_1_2_2e_d1_configuration_load_hdf5_inspire_bclearer_link(),
            content_operation_configuration=get_boson_1_2_2e_d1_configuration_merge_inspire_bclearer_link())

    instrument_and_visualize(
        output_folder_name=output_folder_name,
        visualization_substage_output_universe=os_inspire_linked_bclearer_universe)

    os_inspire_bclearer_merged_boson_universe = \
        run_merge_hdf5_model_content_operations_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe_from_input=os_inspire_linked_bclearer_universe,
            load_hdf5_model_configuration=get_boson_1_2_2e_e1_configuration_load_hdf5_boson(),
            content_operation_configuration=get_boson_1_2_2e_e1_configuration_merge_inspire_bclearer_boson())

    instrument_and_visualize(
        output_folder_name=output_folder_name,
        visualization_substage_output_universe=os_inspire_bclearer_merged_boson_universe)

    return \
        os_inspire_bclearer_merged_boson_universe
