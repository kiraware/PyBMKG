from dataclasses import dataclass

from ...common.schemas import Coordinate
from ..enums import Type
from .name import Name

__all__ = ["Area"]


@dataclass(unsafe_hash=True, slots=True)
class Area:
    """
    `Area` schema used to store info about `id`, `coordinate`, `type`, `region`,
    `level`, `description`, `domain`, `tags`, and `names`.
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
