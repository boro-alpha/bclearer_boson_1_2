from enum import Enum
from enum import auto
from enum import unique


@unique
class CoordinateLineDimensions(
        Enum):
    EASTINGS = \
        auto()

    NORTHINGS = \
        auto()
