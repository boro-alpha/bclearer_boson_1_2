from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import \
    EaToolsSessionManagers

from bclearer_boson_1_2_source.b_code.configurations.objects.bespoke_operation_configurations import \
    BespokeOperationConfigurations
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.coordinate_lines.eastings.add_eastings_orchestrator import \
    orchestrate_add_eastings


def run_boson_1_2_add_eastings_operation_substage(
        content_universe: NfEaComUniverses,
        ea_tools_session_manager: EaToolsSessionManagers,
        bespoke_operation_configuration: BespokeOperationConfigurations) \
        -> NfEaComUniverses:
    log_message(
        message='CONTENT OPERATION: Add eastings to universe - ' +
                bespoke_operation_configuration.short_name + ' - started')

    output_universe = \
        orchestrate_add_eastings(
            content_universe=content_universe,
            ea_tools_session_manager=ea_tools_session_manager,
            short_name=bespoke_operation_configuration.short_name)

    log_message(
            message='CONTENT OPERATION: Add eastings to universe - ' +
                    bespoke_operation_configuration.short_name + ' - finished')

    return \
        output_universe
