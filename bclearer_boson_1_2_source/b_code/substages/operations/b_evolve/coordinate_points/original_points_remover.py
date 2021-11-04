from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.collection_types.nf_ea_com_collection_types import NfEaComCollectionTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import NfEaComColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from pandas import DataFrame


def remove_original_gm_points(
        output_universe: NfEaComUniverses,
        original_gm_points: set) \
        -> None:
    content_collections_dictionary = \
        output_universe.nf_ea_com_registry.dictionary_of_collections

    for content_collection_type, content_collection_table in content_collections_dictionary.items():
        __process_content_collection(
            content_collection_type=content_collection_type,
            content_collection_table=content_collection_table,
            original_gm_points=original_gm_points,
            output_universe=output_universe)


def __process_content_collection(
        content_collection_type: NfEaComCollectionTypes,
        content_collection_table: DataFrame,
        original_gm_points: set,
        output_universe: NfEaComUniverses) \
        -> None:
    output_collections_dictionary = \
        output_universe.nf_ea_com_registry.dictionary_of_collections

    if content_collection_type == NfEaComCollectionTypes.EA_CLASSIFIERS:
        output_collections_dictionary[content_collection_type] = \
            __get_filtered_collection(
                nf_uuids_to_be_removed=original_gm_points,
                content_collection_table=content_collection_table,
                ea_guid_column_name=NfColumnTypes.NF_UUIDS.column_name)

    elif content_collection_type == NfEaComCollectionTypes.EA_CONNECTORS:
        place1_removed_table = \
            __get_filtered_collection(
                nf_uuids_to_be_removed=original_gm_points,
                content_collection_table=content_collection_table,
                ea_guid_column_name=NfEaComColumnTypes.ELEMENTS_SUPPLIER_PLACE1_END_CONNECTORS.column_name)

        output_collections_dictionary[content_collection_type] = \
            __get_filtered_collection(
                nf_uuids_to_be_removed=original_gm_points,
                content_collection_table=place1_removed_table,
                ea_guid_column_name=NfEaComColumnTypes.ELEMENTS_CLIENT_PLACE2_END_CONNECTORS.column_name)

    elif content_collection_type == NfEaComCollectionTypes.STEREOTYPE_USAGE:
        output_collections_dictionary[content_collection_type] = \
            __get_filtered_collection(
                nf_uuids_to_be_removed=original_gm_points,
                content_collection_table=content_collection_table,
                ea_guid_column_name=NfEaComColumnTypes.STEREOTYPE_CLIENT_NF_UUIDS.column_name)

    else:
        output_collections_dictionary[content_collection_type] = \
            content_collection_table


def __get_filtered_collection(
        nf_uuids_to_be_removed: set,
        content_collection_table: DataFrame,
        ea_guid_column_name: str) \
        -> DataFrame:
    filtered_collection = \
        content_collection_table[
            ~content_collection_table[ea_guid_column_name].isin(nf_uuids_to_be_removed)]

    return \
        filtered_collection
