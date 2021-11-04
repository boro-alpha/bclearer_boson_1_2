from enum import auto
from enum import unique

from bclearer_source.b_code.common_knowledge.matched_objects import MatchedEaObjects


@unique
class Boson12MatchedEaObjects(
        MatchedEaObjects):
    BOSON_NAMES = \
        auto()

    GML_FILE_NAMES = \
        auto()

    INSPIRE_OBJECT_NAMES = \
        auto()

    OS_GAZETTEER_OBJECT_NAMES = \
        auto()

    MODEL_PACKAGE = \
        auto()

    EPSG_27700_COORDINATE_POINT_NAME_INSTANCES = \
        auto()

    SUBTYPE_NAME_TYPE_INSTANCE = \
        auto()

    EPSG_27700_COORDINATE_POINT_NAMES = \
        auto()

    EPSG_27700_COORDINATE_POINTS = \
        auto()

    EPSG_27700_EASTING_COORDINATE_LINE_NAMES = \
        auto()

    EPSG_27700_EASTING_COORDINATE_LINES = \
        auto()

    EPSG_27700_NORTHING_COORDINATE_LINE_NAMES = \
        auto()

    EPSG_27700_NORTHING_COORDINATE_LINES = \
        auto()

    EPSG_27700_COORDINATE_POINT_NAME_COMPOSED_OFS = \
        auto()

    EPSG_27700_COORDINATE_LINE_INTERSECTIONS = \
        auto()

    DIRECT_POSITION_POWERTYPE = \
        auto()

    def __object_name(
            self) \
            -> str:
        object_name = \
            object_name_mapping[self]

        return \
            object_name

    def __ea_guid(
            self) \
            -> str:
        ea_guid = \
            ea_guid_mapping[self]

        return \
            ea_guid

    object_name = \
        property(
            fget=__object_name)

    ea_guid = \
        property(
            fget=__ea_guid)


object_name_mapping = \
    {
        Boson12MatchedEaObjects.BOSON_NAMES: 'bOSON Names',
        Boson12MatchedEaObjects.GML_FILE_NAMES: 'GML File Names',
        Boson12MatchedEaObjects.INSPIRE_OBJECT_NAMES: 'INSPIRE Object Names',
        Boson12MatchedEaObjects.OS_GAZETTEER_OBJECT_NAMES: 'OS Gazetteer Object Names',
        Boson12MatchedEaObjects.MODEL_PACKAGE: 'bOSON_1 Package',
        Boson12MatchedEaObjects.EPSG_27700_COORDINATE_POINT_NAME_INSTANCES: 'EPSG 27700 Coordinate Point Name Instances',
        Boson12MatchedEaObjects.SUBTYPE_NAME_TYPE_INSTANCE: 'subtype name type instance',
        Boson12MatchedEaObjects.EPSG_27700_COORDINATE_POINT_NAMES: 'EPSG 27700 Coordinate Point Names',
        Boson12MatchedEaObjects.EPSG_27700_COORDINATE_POINTS: 'EPSG 27700 Coordinate Points',
        Boson12MatchedEaObjects.EPSG_27700_EASTING_COORDINATE_LINE_NAMES: 'EPSG 27700 Easting Coordinate Line Names',
        Boson12MatchedEaObjects.EPSG_27700_EASTING_COORDINATE_LINES: 'EPSG 27700 Easting Coordinate Lines',
        Boson12MatchedEaObjects.EPSG_27700_NORTHING_COORDINATE_LINE_NAMES: 'EPSG 27700 Easting Coordinate Line Names',
        Boson12MatchedEaObjects.EPSG_27700_NORTHING_COORDINATE_LINES: 'EPSG 27700 Easting Coordinate Lines',
        Boson12MatchedEaObjects.EPSG_27700_COORDINATE_POINT_NAME_COMPOSED_OFS: 'epsg 27700 coordinate point name composed ofs',
        Boson12MatchedEaObjects.EPSG_27700_COORDINATE_LINE_INTERSECTIONS: 'epsg 27700 coordinate line intersections',
        Boson12MatchedEaObjects.DIRECT_POSITION_POWERTYPE: 'DirectPosition Powertype'
    }


ea_guid_mapping = \
    {
        Boson12MatchedEaObjects.BOSON_NAMES: '{79F53CC0-26DE-439f-9BBB-32E72842514F}',
        Boson12MatchedEaObjects.GML_FILE_NAMES: '{36FC597B-8B35-4a01-9476-0819D1D37657}',
        Boson12MatchedEaObjects.INSPIRE_OBJECT_NAMES: '{0D83D74E-0BE8-4fda-85B2-DC4BD3882C86}',
        Boson12MatchedEaObjects.OS_GAZETTEER_OBJECT_NAMES: '{83AF5403-09D5-4305-B050-7688D5FDBD23}',
        Boson12MatchedEaObjects.MODEL_PACKAGE: '{B4F3C8D8-AA28-4f65-9346-7C38D91A43D3}',
        Boson12MatchedEaObjects.EPSG_27700_COORDINATE_POINT_NAME_INSTANCES: '{5460213E-B0C8-4b4e-B8BD-9931A459A117}',
        Boson12MatchedEaObjects.SUBTYPE_NAME_TYPE_INSTANCE: '{2EA9B396-5932-4280-972A-6610CC1E295D}',
        Boson12MatchedEaObjects.EPSG_27700_COORDINATE_POINT_NAMES: '{BAB375B8-F1B0-46c2-A345-314B4105DBF9}',
        Boson12MatchedEaObjects.EPSG_27700_COORDINATE_POINTS: '{F53ABAAA-9029-45e8-8A90-2D04737EF395}',
        Boson12MatchedEaObjects.EPSG_27700_EASTING_COORDINATE_LINE_NAMES: '{26583A38-CBB4-4071-9338-ECC4968A4C32}',
        Boson12MatchedEaObjects.EPSG_27700_EASTING_COORDINATE_LINES: '{F1D529C8-7C36-4659-AC37-B401C694AC9B}',
        Boson12MatchedEaObjects.EPSG_27700_NORTHING_COORDINATE_LINE_NAMES: '{59B7E53C-ED00-497d-8323-582E02860D80}',
        Boson12MatchedEaObjects.EPSG_27700_NORTHING_COORDINATE_LINES: '{EF18571D-8B0E-484a-8FA5-28D3600B81D0}',
        Boson12MatchedEaObjects.EPSG_27700_COORDINATE_POINT_NAME_COMPOSED_OFS: '{23707C56-49E0-437d-A84D-17ED38BBF59C}',
        Boson12MatchedEaObjects.EPSG_27700_COORDINATE_LINE_INTERSECTIONS: '{ECB12BE6-9E21-4497-BB33-5B326773107E}',
        Boson12MatchedEaObjects.DIRECT_POSITION_POWERTYPE: '{E04D428D-D969-4b8d-952F-C4A45921FA88}'
    }
