from bclearer_source.b_code.common_knowledge.bclearer_matched_ea_objects import BclearerMatchedEaObjects
from bclearer_source.b_code.common_knowledge.digitialisation_level_stereotype_matched_ea_objects import \
    DigitalisationLevelStereotypeMatchedEaObjects
from bclearer_source.b_code.substages.operations.b_evolve.common.new_root_package_creator import create_root_package
from bclearer_source.b_code.substages.operations.common.class_adder import add_new_class_to_dictionary
from bclearer_source.b_code.substages.operations.common.connector_adder import add_new_connector_to_dictionary
from bclearer_source.b_code.substages.operations.common.connector_to_connector_adder import \
    add_new_connector_to_connector_to_dictionary
from bclearer_source.b_code.substages.operations.common.new_ea_objects_dictionary_creator import \
    create_new_ea_objects_dictionary
from bclearer_source.b_code.substages.operations.common.nf_ea_com_universe_updater import \
    update_nf_ea_com_universe_with_dictionary
from bclearer_source.b_code.substages.operations.common.nf_uuid_from_ea_guid_from_collection_getter import \
    get_nf_uuid_from_ea_guid_from_collection
from bclearer_source.b_code.substages.operations.common.stereotype_adder import add_new_stereotype_usage_to_dictionary
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.ea_connector_types import EaConnectorTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.collection_types.nf_ea_com_collection_types import \
    NfEaComCollectionTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import \
    EaToolsSessionManagers
from nf_ea_common_tools_source.b_code.services.session.processes.creators.empty_nf_ea_com_universe_creator import \
    create_empty_nf_ea_universe
from bclearer_boson_1_2_source.b_code.common_knowledge.boson_1_2_matched_ea_objects import Boson12MatchedEaObjects
from bclearer_boson_1_2_source.b_code.configurations.objects.bespoke_create_point_names_configuration_objects import \
    BespokeCreatePointNamesConfigurationObjects
from bclearer_boson_1_2_source.b_code.configurations.objects.bespoke_operation_configurations import \
    BespokeOperationConfigurations
from bclearer_boson_1_2_source.b_code.substages.operations.b_evolve.coordinate_lines.common.nf_uuid_sets_keyed_on_name_prefix_dictionary_getter import \
    get_nf_uuid_sets_keyed_on_name_prefix_dictionary


def run_boson_1_2_create_point_names_operation_substage(
        content_universe: NfEaComUniverses,
        ea_tools_session_manager: EaToolsSessionManagers,
        bespoke_operation_configuration: BespokeOperationConfigurations) \
        -> NfEaComUniverses:
    log_message(
        message='CONTENT OPERATION: Create point names - ' +
                bespoke_operation_configuration.short_name + ' - started')

    output_universe = \
        create_empty_nf_ea_universe(
            ea_tools_session_manager=ea_tools_session_manager,
            short_name=bespoke_operation_configuration.short_name)

    output_universe.nf_ea_com_registry.dictionary_of_collections = \
        content_universe.nf_ea_com_registry.dictionary_of_collections.copy()

    __create_point_names(
        output_universe=output_universe,
        bespoke_operation_configuration=bespoke_operation_configuration)

    log_message(
            message='CONTENT OPERATION: Create point names - ' +
                    bespoke_operation_configuration.short_name + ' - finished')

    return \
        output_universe


def __create_point_names(
        output_universe: NfEaComUniverses,
        bespoke_operation_configuration: BespokeOperationConfigurations) \
        -> None:
    bespoke_operation_configuration_object = \
        bespoke_operation_configuration.bespoke_operation_configuration_object

    if not isinstance(
            bespoke_operation_configuration_object,
            BespokeCreatePointNamesConfigurationObjects):
        raise TypeError

    nf_uuid_sets_keyed_on_name_exemplars = \
        get_nf_uuid_sets_keyed_on_name_prefix_dictionary(
            nf_ea_com_universe=output_universe,
            matched_type=Boson12MatchedEaObjects.EPSG_27700_COORDINATE_POINT_NAME_INSTANCES,
            prefix_word_count=2)

    new_ea_objects_dictionary = \
        create_new_ea_objects_dictionary()

    package_nf_uuid = \
        create_root_package(
            nf_ea_com_universe=output_universe,
            package_name='Coordinate Points - Names')

    subtype_name_type_instance_nf_uuid = \
        get_nf_uuid_from_ea_guid_from_collection(
            nf_ea_com_universe=output_universe,
            collection_type=NfEaComCollectionTypes.EA_CLASSIFIERS,
            ea_guid=Boson12MatchedEaObjects.SUBTYPE_NAME_TYPE_INSTANCE.ea_guid)

    coordinate_point_names_nf_uuid = \
        get_nf_uuid_from_ea_guid_from_collection(
            nf_ea_com_universe=output_universe,
            collection_type=NfEaComCollectionTypes.EA_CLASSIFIERS,
            ea_guid=Boson12MatchedEaObjects.EPSG_27700_COORDINATE_POINT_NAMES.ea_guid)

    name_types_instances_stereotype_nf_uuid = \
        get_nf_uuid_from_ea_guid_from_collection(
            nf_ea_com_universe=output_universe,
            collection_type=NfEaComCollectionTypes.EA_STEREOTYPES,
            ea_guid=BclearerMatchedEaObjects.NAME_TYPES_INSTANCES_STEREOTYPE.ea_guid)

    digitalisation_level_stereotype_nf_uuid = \
        get_nf_uuid_from_ea_guid_from_collection(
            nf_ea_com_universe=output_universe,
            collection_type=NfEaComCollectionTypes.EA_STEREOTYPES,
            ea_guid=DigitalisationLevelStereotypeMatchedEaObjects.DIGITALISATION_LEVEL_1_CLASS_STEREOTYPE.ea_guid)

    for name_exemplar, nf_uuid_set in nf_uuid_sets_keyed_on_name_exemplars.items():
        __create_point_name(
            new_ea_objects_dictionary=new_ea_objects_dictionary,
            direct_position_instance_nf_uuid_set=nf_uuid_set,
            name_exemplar=name_exemplar,
            subtype_name_type_instance_nf_uuid=subtype_name_type_instance_nf_uuid,
            epsg_27700_coordinate_point_names_nf_uuid=coordinate_point_names_nf_uuid,
            package_nf_uuid=package_nf_uuid,
            name_types_instances_stereotype_nf_uuid=name_types_instances_stereotype_nf_uuid,
            digitalisation_level_stereotype_nf_uuid=digitalisation_level_stereotype_nf_uuid)

    update_nf_ea_com_universe_with_dictionary(
        nf_ea_com_universe=output_universe,
        new_ea_objects_dictionary=new_ea_objects_dictionary)


def __create_point_name(
        new_ea_objects_dictionary: dict,
        direct_position_instance_nf_uuid_set: set,
        name_exemplar: str,
        subtype_name_type_instance_nf_uuid: str,
        epsg_27700_coordinate_point_names_nf_uuid: str,
        package_nf_uuid: str,
        name_types_instances_stereotype_nf_uuid: str,
        digitalisation_level_stereotype_nf_uuid: str) \
        -> None:
    new_point_name_nf_uuid = \
        add_new_class_to_dictionary(
            new_classifier_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.EA_CLASSIFIERS],
            package_nf_uuid=package_nf_uuid,
            class_name=name_exemplar + ' Point Name')

    add_new_stereotype_usage_to_dictionary(
        new_stereotype_usage_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.STEREOTYPE_USAGE],
        client_nf_uuid=new_point_name_nf_uuid,
        client_collection_type=NfEaComCollectionTypes.EA_CLASSIFIERS,
        stereotype_nf_uuid=digitalisation_level_stereotype_nf_uuid)

    add_new_connector_to_dictionary(
        new_connector_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.EA_CONNECTORS],
        place_1_nf_uuid=new_point_name_nf_uuid,
        place_2_nf_uuid=epsg_27700_coordinate_point_names_nf_uuid,
        connector_type=EaConnectorTypes.DEPENDENCY)

    for direct_position_instance_nf_uuid in direct_position_instance_nf_uuid_set:
        __add_point_name_to_name_instance(
            new_point_name_nf_uuid=new_point_name_nf_uuid,
            new_ea_objects_dictionary=new_ea_objects_dictionary,
            direct_position_instance_nf_uuid=direct_position_instance_nf_uuid,
            subtype_name_type_instance_nf_uuid=subtype_name_type_instance_nf_uuid,
            package_nf_uuid=package_nf_uuid,
            name_types_instances_stereotype_nf_uuid=name_types_instances_stereotype_nf_uuid)


def __add_point_name_to_name_instance(
        new_point_name_nf_uuid: str,
        new_ea_objects_dictionary: dict,
        direct_position_instance_nf_uuid: str,
        subtype_name_type_instance_nf_uuid: str,
        package_nf_uuid: str,
        name_types_instances_stereotype_nf_uuid: str) \
        -> None:
    connector_nf_uuid = \
        add_new_connector_to_dictionary(
            new_connector_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.EA_CONNECTORS],
            place_1_nf_uuid=direct_position_instance_nf_uuid,
            place_2_nf_uuid=new_point_name_nf_uuid,
            connector_type=EaConnectorTypes.DEPENDENCY)

    add_new_connector_to_connector_to_dictionary(
        new_ea_objects_dictionary=new_ea_objects_dictionary,
        package_nf_uuid=package_nf_uuid,
        connector_nf_uuid=connector_nf_uuid,
        class_nf_uuid=subtype_name_type_instance_nf_uuid)

    add_new_stereotype_usage_to_dictionary(
        new_stereotype_usage_dictionary=new_ea_objects_dictionary[NfEaComCollectionTypes.STEREOTYPE_USAGE],
        client_nf_uuid=connector_nf_uuid,
        client_collection_type=NfEaComCollectionTypes.EA_CONNECTORS,
        stereotype_nf_uuid=name_types_instances_stereotype_nf_uuid)
