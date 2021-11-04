from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_common_source.code.services.identification_services.uuid_service.uuid_helpers.uuid_factory import \
    create_new_uuid
from untangle import Element

from bclearer_boson_1_2_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_domain.os_open_names_appenders.b1_2_os_open_names_direct_position_appender import \
    append_direct_position


def append_gml_point(
        os_open_names_dictionary: dict,
        owning_named_place_nf_uuid: str,
        gml_point: Element) \
        -> None:
    direct_position_nf_uuid = \
        create_new_uuid()

    gml_point_nf_uuid = \
        create_new_uuid()

    gml_pos = \
        gml_point.gml_pos.cdata

    append_direct_position(
        os_open_names_dictionary=os_open_names_dictionary,
        direct_position_nf_uuid=direct_position_nf_uuid,
        direct_position_xml_text=gml_pos,
        owning_object_nf_uuid=gml_point_nf_uuid,
        link_name_from_owning_object='pos')

    srs_name = \
        gml_point['srsName']

    gml_id = \
        gml_point['gml:id']

    os_open_names_dictionary['points'][gml_point_nf_uuid] = \
        {
            NfColumnTypes.NF_UUIDS.column_name: gml_point_nf_uuid,
            'name': gml_pos + ' Point',
            'srsName': srs_name,
            'gml:id': gml_id,
            'owning_nf_uuids': owning_named_place_nf_uuid,
            'direct_position_nf_uuids': direct_position_nf_uuid
        }
