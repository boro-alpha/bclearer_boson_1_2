from bclearer_source.b_code.common_knowledge.content_operation_types import ContentOperationTypes
from bclearer_source.b_code.configurations.content_operation_configurations import ContentOperationConfigurations
from bclearer_source.b_code.configurations.load_hdf5_model_configurations import LoadHdf5ModelConfigurations

from bclearer_boson_1_2_source.b_code.configurations.resource_constants.resources_filename_constants import \
    CONTENT_UNIVERSE_BCLEARER_OS_INSPIRE_LINK_FILENAME_HDF5
from bclearer_boson_1_2_source.b_code.configurations.resource_constants.resources_namespace_constants import \
    CONTENT_OPERATIONS_RESOURCES_NAMESPACE


def get_boson_1_2_2e_d1_configuration_load_hdf5_inspire_bclearer_link() \
        -> LoadHdf5ModelConfigurations:
    load_hdf5_model_configuration = \
        LoadHdf5ModelConfigurations(
            resource_namespace=CONTENT_OPERATIONS_RESOURCES_NAMESPACE,
            resource_file_name=CONTENT_UNIVERSE_BCLEARER_OS_INSPIRE_LINK_FILENAME_HDF5,
            universe_short_name='2e_d1_input_cont_uni_bclearer_link')

    return \
        load_hdf5_model_configuration


def get_boson_1_2_2e_d1_configuration_merge_inspire_bclearer_link() \
        -> ContentOperationConfigurations:
    content_operation_configuration = \
        ContentOperationConfigurations(
            content_operation_type=ContentOperationTypes.MERGE_UNIVERSES,
            output_universe_short_name='2e_d1_output_merge_bclearer_link')

    return \
        content_operation_configuration
