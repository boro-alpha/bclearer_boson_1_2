from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import NfEaComColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from pandas import Series

from bclearer_boson_1_2_source.b_code.common_knowledge.coordinate_line_dimensions import CoordinateLineDimensions
from bclearer_boson_1_2_source.b_code.common_knowledge.inspire_matched_ea_objects import InspireMatchedEaObjects


def get_coordinate_line_exemplars_from_xml_test_attributes(
        nf_ea_com_universe: NfEaComUniverses,
        dimension: CoordinateLineDimensions) \
        -> set:
    all_eastings_and_northings_names = \
        __get_all_eastings_and_northings_names(
            nf_ea_com_universe=nf_ea_com_universe)

    if dimension == CoordinateLineDimensions.EASTINGS:
        return \
            set(
                all_eastings_and_northings_names[0])

    return \
        set(
            all_eastings_and_northings_names[1])


def __get_all_eastings_and_northings_names(
        nf_ea_com_universe: NfEaComUniverses) \
        -> Series:
    ea_attributes = \
        nf_ea_com_universe.nf_ea_com_registry.get_ea_attributes()

    ea_attribute_name = \
        InspireMatchedEaObjects.XML_TEXT_ATTRIBUTE.object_name

    attribute_name_column_name = \
        NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NAME.column_name

    ea_attributes_of_name = \
        ea_attributes[ea_attributes[attribute_name_column_name] == ea_attribute_name]

    ea_attributes_of_name_series = \
        ea_attributes_of_name[NfEaComColumnTypes.ELEMENT_COMPONENTS_DEFAULT.column_name]

    all_eastings_and_northings_names = \
        ea_attributes_of_name_series.str.split(
            expand=True)

    return \
        all_eastings_and_northings_names
