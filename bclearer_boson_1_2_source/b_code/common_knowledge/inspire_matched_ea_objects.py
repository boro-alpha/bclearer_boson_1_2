from enum import auto
from enum import unique

from bclearer_source.b_code.common_knowledge.matched_objects import MatchedEaObjects
from nf_common_source.code.constants.standard_constants import DEFAULT_NULL_VALUE


@unique
class InspireMatchedEaObjects(
        MatchedEaObjects):
    NAMED_PLACE = \
        auto()

    CHARACTER_STRING = \
        auto()

    IDENTIFIER = \
        auto()

    MODEL_PACKAGE = \
        auto()

    LOCAL_ID_ATTRIBUTE = \
        auto()

    TEXT_ATTRIBUTE = \
        auto()

    XML_TEXT_ATTRIBUTE = \
        auto()

    GM_ENVELOPE = \
        auto()

    DIRECT_POSITION = \
        auto()

    GM_POINT = \
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
        InspireMatchedEaObjects.NAMED_PLACE: 'NamedPlace',
        InspireMatchedEaObjects.CHARACTER_STRING: 'CharacterString',
        InspireMatchedEaObjects.IDENTIFIER: 'Identifier',
        InspireMatchedEaObjects.MODEL_PACKAGE: 'INSPIRE Consolidated UML Model - keep',
        InspireMatchedEaObjects.LOCAL_ID_ATTRIBUTE: 'localId',
        InspireMatchedEaObjects.TEXT_ATTRIBUTE: 'text',
        InspireMatchedEaObjects.XML_TEXT_ATTRIBUTE: 'xml_text',
        InspireMatchedEaObjects.GM_ENVELOPE: 'GM_Envelope',
        InspireMatchedEaObjects.DIRECT_POSITION: 'DirectPosition',
        InspireMatchedEaObjects.GM_POINT: 'GM_Point'
    }


ea_guid_mapping = \
    {
        InspireMatchedEaObjects.NAMED_PLACE: '{8C3D164C-2A8F-4df9-A35F-C5CFBDE23ABC}',
        InspireMatchedEaObjects.CHARACTER_STRING: '{AF7C81A6-B1C1-4469-A09F-B97989024A14}',
        InspireMatchedEaObjects.IDENTIFIER: '{CB20C133-5AA4-4671-80C7-8ED2879AB0D9}',
        InspireMatchedEaObjects.MODEL_PACKAGE: '{85FDCAF5-BB31-493a-ADE6-CEA426E6F42C}',
        InspireMatchedEaObjects.LOCAL_ID_ATTRIBUTE: '{A63416FC-693C-47d3-9E52-BCF2165F806B}',
        InspireMatchedEaObjects.TEXT_ATTRIBUTE: '{803EBE76-48DF-4391-9523-5BA48A3CA5E0}',
        InspireMatchedEaObjects.XML_TEXT_ATTRIBUTE: DEFAULT_NULL_VALUE,
        InspireMatchedEaObjects.GM_ENVELOPE: '{900414E6-2847-4018-B28F-76674D7A1551}',
        InspireMatchedEaObjects.DIRECT_POSITION: '{60E248A7-445A-4dbe-9A3B-0135CC35AE91}',
        InspireMatchedEaObjects.GM_POINT: '{3CC5A3E8-2ECA-4e42-B09C-935BD5D3B64A}'
    }
