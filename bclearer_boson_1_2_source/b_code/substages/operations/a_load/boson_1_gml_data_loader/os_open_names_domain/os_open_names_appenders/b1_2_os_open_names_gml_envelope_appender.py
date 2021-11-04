import untangle
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_common_source.code.services.identification_services.uuid_service.uuid_helpers.uuid_factory import \
    create_new_uuid

from bclearer_boson_1_2_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_domain.os_open_names_appenders.b1_2_os_open_names_direct_position_appender import \
    append_direct_position


def append_gml_envelope(
        os_open_names_dictionary: dict,
        gml_bounded_by: untangle.Element,
        named_place_uuid: str) \
        -> dict:
    gml_envelope_nf_uuid = \
        create_new_uuid()

    envelope_srs_name = \
        gml_bounded_by.gml_Envelope['srsName']

    envelope_lower_corner_xml_text = \
        gml_bounded_by.gml_Envelope.gml_lowerCorner.cdata

    lower_corner_direct_position_nf_uuid = \
        create_new_uuid()

    envelope_upper_corner_xml_text = \
        gml_bounded_by.gml_Envelope.gml_upperCorner.cdata

    upper_corner_direct_position_nf_uuid = \
        create_new_uuid()

    envelope_name = \
        os_open_names_dictionary['named_places'][named_place_uuid]['name'] + ' Envelope'

    os_open_names_dictionary['envelopes'][gml_envelope_nf_uuid] = \
        {
            NfColumnTypes.NF_UUIDS.column_name: gml_envelope_nf_uuid,
            'owning_nf_uuids': named_place_uuid,
            'name': envelope_name,
            'srsName': envelope_srs_name,
            'lower_corner_nf_uuids': lower_corner_direct_position_nf_uuid,
            'upper_corner_nf_uuids': upper_corner_direct_position_nf_uuid
        }

    __append_corners_direct_positions(
        os_open_names_dictionary=os_open_names_dictionary,
        owning_gml_envelope_nf_uuid=gml_envelope_nf_uuid,
        lower_corner_direct_position_nf_uuid=lower_corner_direct_position_nf_uuid,
        envelope_lower_corner_xml_text=envelope_lower_corner_xml_text,
        upper_corner_direct_position_nf_uuid=upper_corner_direct_position_nf_uuid,
        envelope_upper_corner_xml_text=envelope_upper_corner_xml_text)

    return \
        os_open_names_dictionary


def __append_corners_direct_positions(
        os_open_names_dictionary: dict,
        owning_gml_envelope_nf_uuid: str,
        lower_corner_direct_position_nf_uuid: str,
        envelope_lower_corner_xml_text: str,
        upper_corner_direct_position_nf_uuid: str,
        envelope_upper_corner_xml_text: str) \
        -> None:
    append_direct_position(
        os_open_names_dictionary=os_open_names_dictionary,
        owning_object_nf_uuid=owning_gml_envelope_nf_uuid,
        direct_position_nf_uuid=lower_corner_direct_position_nf_uuid,
        direct_position_xml_text=envelope_lower_corner_xml_text,
        link_name_from_owning_object='lowerCorner')

    append_direct_position(
        os_open_names_dictionary=os_open_names_dictionary,
        owning_object_nf_uuid=owning_gml_envelope_nf_uuid,
        direct_position_nf_uuid=upper_corner_direct_position_nf_uuid,
        direct_position_xml_text=envelope_upper_corner_xml_text,
        link_name_from_owning_object='upperCorner')
