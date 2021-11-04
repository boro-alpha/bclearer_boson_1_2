import untangle
from nf_common_source.code.services.file_system_service.objects.files import Files
from nf_common_source.code.services.identification_services.uuid_service.uuid_helpers.uuid_factory import \
    create_new_uuid
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message

from bclearer_boson_1_2_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_domain.os_open_names_appenders.b1_2_os_open_names_named_place_appender import \
    append_named_place


def append_os_open_names_dictionary(
        os_open_names_dictionary: dict,
        file: Files) \
        -> dict:
    log_message(
        message='loading ' + file.absolute_path_string)

    data = \
        untangle.parse(
            file.absolute_path_string)

    log_message(
        message='parsing ' + file.absolute_path_string)

    gml_feature_member_count = 1

    file_uuid = \
        create_new_uuid()

    for gml_featureMember in data.gml_FeatureCollection.gml_featureMember:
        gml_feature_member_count += 1

        os_open_names_dictionary = \
            append_named_place(
                os_open_names_dictionary=os_open_names_dictionary,
                named_place=gml_featureMember.names_NamedPlace,
                file_uuid=file_uuid)

    log_message(
        message='parsed ' + str(gml_feature_member_count - 1) + ' feature members')

    return \
        os_open_names_dictionary
