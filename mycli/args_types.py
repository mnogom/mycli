from dataclasses import dataclass
from typing import Callable, Any


@dataclass(slots=True, frozen=True)
class PositionalArg:
    description: str | None = None
    fabric: Callable[[str], Any] | None = None


@dataclass(slots=True, frozen=True)
class NamedArg:
    aliases: list[str]
    description: str | None = None


@dataclass(slots=True, frozen=True)
class FlagArg:
    aliases: list[str]
    action: Callable[[], Any]
    description: str | None = None
