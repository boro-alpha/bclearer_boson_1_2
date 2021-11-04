from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_common_source.code.services.dataframe_service.dataframe_mergers import left_merge_dataframes
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.ea_connector_types import EaConnectorTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import NfEaComColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from pandas import DataFrame


def get_nf_uuid_sets_by_association_keyed_on_name_prefix_dictionary(
        nf_ea_com_universe: NfEaComUniverses,
        association_name: str) \
        -> dict:
    exemplar_and_nf_uuids_columns = \
        __get_names_and_nf_uuid_sets_by_association(
            nf_ea_com_universe=nf_ea_com_universe,
            association_name=association_name)

    nf_uuids_indexed_on_exemplars_dictionary = \
        __convert_dataframe_to_dictionary(
            exemplar_and_nf_uuids_columns=exemplar_and_nf_uuids_columns)

    return \
        nf_uuids_indexed_on_exemplars_dictionary


def __get_names_and_nf_uuid_sets_by_association(
        nf_ea_com_universe: NfEaComUniverses,
        association_name: str) \
        -> DataFrame:
    ea_connectors = \
        nf_ea_com_universe.nf_ea_com_registry.get_ea_connectors()

    ea_associations = \
        ea_connectors[ea_connectors[NfEaComColumnTypes.CONNECTORS_ELEMENT_TYPE_NAME.column_name] == EaConnectorTypes.ASSOCIATION.type_name]

    filtered_associations = \
        ea_associations[ea_associations[NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NAME.column_name] == association_name]

    ea_classifiers = \
        nf_ea_com_universe.nf_ea_com_registry.get_ea_classifiers()

    nf_uuids_column_name = \
        NfColumnTypes.NF_UUIDS.column_name

    name_column_name = \
        NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NAME.column_name

    instances_of_coordinate_point_type = \
        left_merge_dataframes(
            master_dataframe=filtered_associations,
            master_dataframe_key_columns=[NfEaComColumnTypes.ELEMENTS_CLIENT_PLACE2_END_CONNECTORS.column_name],
            merge_suffixes=['_association', '_classifier'],
            foreign_key_dataframe=ea_classifiers,
            foreign_key_dataframe_fk_columns=[nf_uuids_column_name],
            foreign_key_dataframe_other_column_rename_dictionary=
            {
                name_column_name: 'names'
            })

    instances_of_coordinate_point_type['Prefixes'] = \
        instances_of_coordinate_point_type['names'].str.split().str[0:2].str.join(' ')

    prefix_and_nf_uuids_columns = \
        instances_of_coordinate_point_type[['Prefixes', NfEaComColumnTypes.ELEMENTS_SUPPLIER_PLACE1_END_CONNECTORS.column_name]]

    return \
        prefix_and_nf_uuids_columns


def __convert_dataframe_to_dictionary(
        exemplar_and_nf_uuids_columns: DataFrame) \
        -> dict:
    nf_uuids_grouped_by_names = \
        exemplar_and_nf_uuids_columns.groupby('Prefixes')[NfEaComColumnTypes.ELEMENTS_SUPPLIER_PLACE1_END_CONNECTORS.column_name].apply(set)

    nf_uuid_sets_keyed_on_names = \
        nf_uuids_grouped_by_names.to_dict()

    return \
        nf_uuid_sets_keyed_on_names
