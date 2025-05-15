from enum import IntEnum


class MessageType(IntEnum):
    DATA = 0x01
    PRESENCE = 0x02
    ACTION = 0x03
    REQUEST = 0x04
    CONFIG = 0x05
    ALERT = 0x06


class DataID(IntEnum):
    # Pour type DATA (0x01)
    TEMP = 0x01
    HUM = 0x02
    PRESENCE = 0x03


class PresenceID(IntEnum):
    # Pour type PRESENCE (0x02)
    PRESENCE_SIMPLE = 0x04


class ActionID(IntEnum):
    # Pour type ACTION (0x03)
    LIGHT_ON = 0x10
    LIGHT_OFF = 0x11


class RequestID(IntEnum):
    # Pour type REQUEST (0x04)
    TEMP = 0x01
    HUM = 0x02
    PRESENCE = 0x03
    ALL = 0xFF


class ConfigID(IntEnum):
    # Pour type CONFIG (0x05)
    SET_INTERVAL = 0x20
    GET_INTERVAL = 0x21
    SET_TEMP_THRESH = 0x22
    SET_SENSOR_STATE = 0x23
    SET_BAUDRATE = 0x24
    GET_FW_VERSION = 0x25


class AlertID(IntEnum):
    # Pour type ALERT (0x06)
    CONFIG_UPDATED = 0x30
    SENSOR_TIMEOUT = 0x32
