from bclearer_source.b_code.common_knowledge.digitialisation_level_stereotype_matched_ea_objects import \
    DigitalisationLevelStereotypeMatchedEaObjects
from bclearer_source.b_code.configurations.load_hdf5_model_configurations import LoadHdf5ModelConfigurations

from bclearer_boson_1_2_source.b_code.configurations.resource_constants.resources_filename_constants import \
    CONTENT_UNIVERSE_OS_INSPIRE_FILENAME_HDF5
from bclearer_boson_1_2_source.b_code.configurations.resource_constants.resources_namespace_constants import \
    CONTENT_OPERATIONS_RESOURCES_NAMESPACE


def get_boson_1_2_1l_a_configuration_load_hdf5_os_inspire_filtered() \
        -> LoadHdf5ModelConfigurations:
    load_hdf5_model_configuration = \
        LoadHdf5ModelConfigurations(
            resource_namespace=CONTENT_OPERATIONS_RESOURCES_NAMESPACE,
            resource_file_name=CONTENT_UNIVERSE_OS_INSPIRE_FILENAME_HDF5,
            universe_short_name='1l_a_input_cont_uni_os_inspire',
            default_digitalisation_level_stereotype=DigitalisationLevelStereotypeMatchedEaObjects.DIGITALISATION_LEVEL_5_CLASS_STEREOTYPE)

    return \
        load_hdf5_model_configuration
