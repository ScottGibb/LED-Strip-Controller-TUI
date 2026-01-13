# Local Imports
from Communications.Types import COLOUR, CTRL_CMD_ID
from Communications.Types import CHANNEL
from Communications.Types import FADE_TYPE
from Communications.Types import TX_MSG_SIZE


def create_constant_colour_message(channel: CHANNEL, colour: COLOUR, brightness: int) -> bytearray:
    """Create a message to send to the hardware to set a constant colour on a channel.

    Args:
        channel: The channel to change.
        colour: The colour to set.
        brightness: The brightness level (0-255).

    Returns:
        The formatted message as a bytearray to send to the hardware.
    """
    bytes = bytearray([CTRL_CMD_ID.LED_CHANGE.value, channel.value,
                       FADE_TYPE.NONE.value, colour, brightness]+ [0] * 4)
    return _add_padding(bytes)


def create_fade_message(channel: CHANNEL, fade_type: FADE_TYPE, colour: COLOUR, brightness: int, period: int) -> bytearray:
    """Create a message to send to the hardware to set a fading colour effect on a channel.

    Args:
        channel: The channel to change.
        fade_type: The type of fade effect to use.
        colour: The colour to set.
        brightness: The brightness level (0-255).
        period: The period of the fade effect in milliseconds.

    Returns:
        The formatted message as a bytearray to send to the hardware.
    """
    bytes = bytearray([CTRL_CMD_ID.LED_CHANGE.value, channel.value,
                       fade_type.value, colour, brightness]) + period.to_bytes(4, "big")
    return _add_padding(bytes)


def create_rgb_message(channel: CHANNEL, red: int, green: int, blue: int) -> bytearray:
    """Create a message to send to the hardware to set RGB colour values on a channel.

    Args:
        channel: The channel to change.
        red: The red component value (0-255).
        green: The green component value (0-255).
        blue: The blue component value (0-255).

    Returns:
        The formatted message as a bytearray to send to the hardware.
    """
    bytes = bytearray([CTRL_CMD_ID.LED_CHANGE.value,
                       channel.value, FADE_TYPE.RGB_CTRL.value, red, green, blue])
    return _add_padding(bytes)


def create_hsb_message(channel: CHANNEL, hue: int, saturation: int, brightness: int) -> bytearray:
    """Create a message to send to the hardware to set HSB colour values on a channel.

    Args:
        channel: The channel to change.
        hue: The hue value (0-360 degrees).
        saturation: The saturation level (0-100).
        brightness: The brightness level (0-255).

    Returns:
        The formatted message as a bytearray to send to the hardware.
    """
    hue_bytes = hue.to_bytes(2, "big")
    bytes = bytearray([CTRL_CMD_ID.LED_CHANGE.value, channel.value, FADE_TYPE.HUE_CTRL.value]) + \
        hue_bytes + bytearray([saturation, brightness])
    return _add_padding(bytes)


def _add_padding(bytes: bytearray) -> bytearray:
    """Add padding to the message to ensure it matches the required transmission size.

    Args:
        bytes: The message bytearray to pad.

    Returns:
        The padded message as a bytearray.
    """
    padding_len = TX_MSG_SIZE - len(bytes)
    if padding_len > 0:
        bytes = bytes + bytearray([0] * padding_len)
    return bytes
