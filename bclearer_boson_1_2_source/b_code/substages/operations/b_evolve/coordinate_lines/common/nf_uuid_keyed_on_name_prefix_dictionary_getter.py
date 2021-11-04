from bclearer_source.b_code.common_knowledge.matched_objects import MatchedEaObjects
from bclearer_source.b_code.substages.operations.common.nf_uuid_from_ea_guid_from_collection_getter import \
    get_nf_uuid_from_ea_guid_from_collection
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_common_source.code.services.dataframe_service.dataframe_mergers import left_merge_dataframes
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.ea_connector_types import EaConnectorTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.collection_types.nf_ea_com_collection_types import \
    NfEaComCollectionTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import NfEaComColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from pandas import DataFrame


def get_nf_uuid_keyed_on_name_prefix_dictionary(
        nf_ea_com_universe: NfEaComUniverses,
        matched_type: MatchedEaObjects,
        prefix_word_count: int) \
        -> dict:
    exemplar_and_nf_uuids_columns = \
        __get_instances_of_type(
            nf_ea_com_universe=nf_ea_com_universe,
            matched_type=matched_type,
            prefix_word_count=prefix_word_count)

    nf_uuids_indexed_on_exemplars_dictionary = \
        __convert_dataframe_to_dictionary(
            exemplar_and_nf_uuids_columns=exemplar_and_nf_uuids_columns)

    return \
        nf_uuids_indexed_on_exemplars_dictionary


def __get_instances_of_type(
        nf_ea_com_universe: NfEaComUniverses,
        matched_type: MatchedEaObjects,
        prefix_word_count: int) \
        -> DataFrame:
    matched_type_nf_uuid = \
        get_nf_uuid_from_ea_guid_from_collection(
            nf_ea_com_universe=nf_ea_com_universe,
            collection_type=NfEaComCollectionTypes.EA_CLASSIFIERS,
            ea_guid=matched_type.ea_guid)

    ea_connectors = \
        nf_ea_com_universe.nf_ea_com_registry.get_ea_connectors()

    ea_dependencies = \
        ea_connectors[ea_connectors[NfEaComColumnTypes.CONNECTORS_ELEMENT_TYPE_NAME.column_name] == EaConnectorTypes.DEPENDENCY.type_name]

    filtered_dependencies = \
        ea_dependencies[ea_dependencies[NfEaComColumnTypes.ELEMENTS_CLIENT_PLACE2_END_CONNECTORS.column_name] == matched_type_nf_uuid]

    ea_classifiers = \
        nf_ea_com_universe.nf_ea_com_registry.get_ea_classifiers()

    nf_uuids_column_name = \
        NfColumnTypes.NF_UUIDS.column_name

    name_column_name = \
        NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NAME.column_name

    instances_of_coordinate_point_type = \
        left_merge_dataframes(
            master_dataframe=filtered_dependencies,
            master_dataframe_key_columns=[NfEaComColumnTypes.ELEMENTS_SUPPLIER_PLACE1_END_CONNECTORS.column_name],
            merge_suffixes=['_dependency', '_classifier'],
            foreign_key_dataframe=ea_classifiers,
            foreign_key_dataframe_fk_columns=[nf_uuids_column_name],
            foreign_key_dataframe_other_column_rename_dictionary=
            {
                name_column_name: 'names'
            })

    instances_of_coordinate_point_type['Prefixes'] = \
        instances_of_coordinate_point_type['names'].str.split().str[0:prefix_word_count].str.join(' ')

    prefix_and_nf_uuids_columns = \
        instances_of_coordinate_point_type[['Prefixes', NfEaComColumnTypes.ELEMENTS_SUPPLIER_PLACE1_END_CONNECTORS.column_name]]

    return \
        prefix_and_nf_uuids_columns


def __convert_dataframe_to_dictionary(
        exemplar_and_nf_uuids_columns: DataFrame) \
        -> dict:
    columns_indexed_on_exemplars = \
        exemplar_and_nf_uuids_columns.set_index(
            'Prefixes')

    columns_indexed_on_exemplars_dictionary = \
        columns_indexed_on_exemplars.to_dict()

    nf_uuids_indexed_on_exemplars_dictionary = \
        columns_indexed_on_exemplars_dictionary[NfEaComColumnTypes.ELEMENTS_SUPPLIER_PLACE1_END_CONNECTORS.column_name]

    return \
        nf_uuids_indexed_on_exemplars_dictionary
