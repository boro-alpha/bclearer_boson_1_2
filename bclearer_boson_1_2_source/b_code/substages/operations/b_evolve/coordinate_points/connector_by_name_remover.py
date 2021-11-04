from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.collection_types.nf_ea_com_collection_types import NfEaComCollectionTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import NfEaComColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses


def remove_connector_by_name(
        nf_ea_com_universe: NfEaComUniverses,
        connector_name_to_delete: str) \
        -> None:
    content_collections_dictionary = \
        nf_ea_com_universe.nf_ea_com_registry.dictionary_of_collections

    connectors = \
        content_collections_dictionary[NfEaComCollectionTypes.EA_CONNECTORS]

    filtered_connectors = \
        connectors[
            connectors[NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NAME.column_name] != connector_name_to_delete]

    content_collections_dictionary[NfEaComCollectionTypes.EA_CONNECTORS] = \
        filtered_connectors
