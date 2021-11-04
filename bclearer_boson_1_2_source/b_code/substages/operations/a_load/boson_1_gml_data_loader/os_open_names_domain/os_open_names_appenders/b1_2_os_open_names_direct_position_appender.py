from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes


def append_direct_position(
        os_open_names_dictionary: dict,
        direct_position_nf_uuid: str,
        direct_position_xml_text: str,
        owning_object_nf_uuid: str,
        link_name_from_owning_object: str) \
        -> None:

    os_open_names_dictionary['direct_positions'][direct_position_nf_uuid] = \
        {
            NfColumnTypes.NF_UUIDS.column_name: direct_position_nf_uuid,
            'name': direct_position_xml_text + ' Direct Position',
            'owning_nf_uuids': owning_object_nf_uuid,
            'link_name_from_owning_object': link_name_from_owning_object,
            'xml_text': direct_position_xml_text
        }
