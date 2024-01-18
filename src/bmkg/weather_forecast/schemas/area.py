from dataclasses import dataclass

from ...common.schemas import Coordinate
from ..enums import Type
from .name import Name

__all__ = ["Area"]


@dataclass(unsafe_hash=True, slots=True)
class Area:
    """
    A schema used to store info about area.

    Attributes:
        id: id of an area.
        coordinate: coordinate of an area.
        type: type of an area.
        region: region of an area.
        level: level of an area.
        description: description of an area.
        domain: domain of an area.
        tags: tags of an area.
        names: names of an area.
    """

    id: str
    coordinate: Coordinate
    type: Type
    region: str
    level: str
    description: str
    domain: str
    tags: str
    names: Name
