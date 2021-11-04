from bclearer_source.b_code.configurations.run_configurations import RunConfigurations

from bclearer_boson_1_2_source.b_code.orchestrators.boson_1_2_bclearer_orchestrator import orchestrate_boson_1_2_bclearer


if __name__ == '__main__':
    RunConfigurations.hdf5_output = \
        True

    orchestrate_boson_1_2_bclearer()
