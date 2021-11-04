import untangle
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_common_source.code.services.identification_services.uuid_service.uuid_helpers.uuid_factory import \
    create_new_uuid
from bclearer_boson_1_2_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_domain.os_open_names_appenders.b1_2_os_open_names_gml_envelope_appender import \
    append_gml_envelope
from bclearer_boson_1_2_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_domain.os_open_names_appenders.b1_2_os_open_names_gml_identifier_appender import \
    append_gml_identifier
from bclearer_boson_1_2_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_domain.os_open_names_appenders.b1_2_os_open_names_gml_point_appender import \
    append_gml_point


def append_named_place(
        os_open_names_dictionary: dict,
        named_place: untangle.Element,
        file_uuid: str) \
        -> dict:
    named_place_uuid = \
        create_new_uuid()

    if isinstance(named_place.gn_name, list):
        presentation_prefix = named_place.gn_name[0].gn_GeographicalName.gn_spelling.gn_SpellingOfName.gn_text.cdata

    else:
        presentation_prefix = named_place.gn_name.gn_GeographicalName.gn_spelling.gn_SpellingOfName.gn_text.cdata

    os_open_names_dictionary['named_places'][named_place_uuid] = \
        {
            NfColumnTypes.NF_UUIDS.column_name: named_place_uuid,
            'file_uuids': file_uuid,
            'name': presentation_prefix + ' Named Place'
        }

    os_open_names_dictionary = \
        append_gml_identifier(
            os_open_names_dictionary=os_open_names_dictionary,
            gml_identifier=named_place.gml_identifier,
            named_place_uuid=named_place_uuid)

    try:
        gml_bounded_by = \
            named_place.gml_boundedBy

        os_open_names_dictionary = \
            append_gml_envelope(
                os_open_names_dictionary=os_open_names_dictionary,
                gml_bounded_by=gml_bounded_by,
                named_place_uuid=named_place_uuid)

    except AttributeError:
        pass

    gml_point = \
        named_place.gn_geometry.gml_Point

    append_gml_point(
        os_open_names_dictionary=os_open_names_dictionary,
        owning_named_place_nf_uuid=named_place_uuid,
        gml_point=gml_point)

    return \
        os_open_names_dictionary
