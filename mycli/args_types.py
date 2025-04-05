from dataclasses import dataclass
from typing import Callable, Any
from abc import ABC


class ArgProtocol(ABC):
    pass

@dataclass(slots=True, frozen=True)
class PositionalArg(ArgProtocol):
    help: str | None = None


@dataclass(slots=True, frozen=True)
class NamedArg(ArgProtocol):
    dash_names: list[str]
    help: str | None = None


@dataclass(slots=True, frozen=True)
class FlagArg(ArgProtocol):
    dash_names: list[str]
    action: str | Callable
    help: str | None = None
