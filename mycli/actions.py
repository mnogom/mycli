from enum import StrEnum


class Actions(StrEnum):
    STORE = "store"
    STORE_CONST = "store_const"
    STORE_TRUE = "store_true"
    STORE_FALSE = "store_false"
    APPEND = "append"
    APPEND_CONST = "append_const"
    EXTEND = "extend"
    COUNT = "count"
    HELP = "help"
    VERSION = "version"
