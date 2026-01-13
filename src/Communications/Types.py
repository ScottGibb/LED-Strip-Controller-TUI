from enum import Enum

# Buffer Sizes
RX_MSG_CNT = 14
TX_MSG_SIZE = 10


class COLOUR(Enum):
    """Colour enumeration specifying each colour the system can display."""
    RED = 0
    GREEN = 1
    BLUE = 2
    WHITE = 3
    ROSE = 4
    MAGENTA = 5
    VIOLET = 6
    AZURE = 7
    CYAN = 8
    AQUAMARINE = 9
    CHARTREUSE = 10
    YELLOW = 11
    ORANGE = 12
    NUM_COLOURS = 13


class FADE_TYPE(Enum):
    """Fade type enumeration representing each of the modes the system can perform."""
    NONE = 0
    SINE = 1
    SQUARE = 2
    TRIANGLE = 3
    SAWTOOTH = 4
    COLOUR_CHANGE = 5
    RGB_CTRL = 6
    HUE_CTRL = 7
    SIZE = 8


class CHANNEL(Enum):
    """Channel enumeration representing each of the channels and their IDs."""
    CHANNEL_NS = 0
    CHANNEL_1 = 1
    CHANNEL_2 = 2
    CHANNEL_3 = 3
    NUM_CHANNELS = 3


class TX_MSG_ID(Enum):
    """TX message ID enumeration defining different messages the hardware can send."""
    LED_UPDATE = 0
    PWR_UPDATE = 1


class CTRL_CMD_ID(Enum):
    """Control command ID enumeration defining messages that can be sent to the hardware."""
    LED_CHANGE = 0
