# Imports
import struct
import threading
import binascii
import serial
import socket

# Local Imports
from Communications.CommsProtocol import create_constant_colour_message, create_fade_message, create_rgb_message, create_hsb_message
from Communications.Types import CHANNEL, COLOUR, FADE_TYPE
from UserInput import ask_user_numeric, ask_user_word


def ask_user_for_hue(channel, mode):
    """_summary_: Gets the message to send to the hardware to change the hue mode
    Args:
        channel (_type_): _description_ The channel to change
        mode (_type_): _description_ The mode to change to
    Returns:
        _type_: _description_ The message to send to the hardware
    """
    user_bounds = {"START": 0, "END": 360}
    user_message = "Please select the Hue value you would like to choose: ("+str(
        user_bounds.get("START")) + " - "+str(user_bounds.get("END"))+")"
    hue = int(ask_user_numeric(user_message, user_bounds))

    user_bounds = {"START": 0, "END": 100}
    user_message = "Please select the Saturation value you would like to choose: ("+str(
        user_bounds.get("START")) + " - "+str(user_bounds.get("END"))+")"
    saturation = int(ask_user_numeric(user_message, user_bounds))

    user_message = "Please select the Brightness value you would like to choose: ("+str(
        user_bounds.get("START")) + " - "+str(user_bounds.get("END"))+")"
    brightness = int(ask_user_numeric(user_message, user_bounds))
    return create_hsb_message(channel, hue, saturation, brightness)


def ask_user_for_rgb(channel, mode):
    """_summary_: Gets the message to send to the hardware to change the rgb mode
    Args:
        channel (_type_): _description_ The channel to change
        mode (_type_): _description_ The mode to change to
    Returns:
        _type_: _description_ The message to send to the hardware
    """
    user_bounds = {"START": 0, "END": 255}
    user_message = "Please select the Red value you would like to choose: ("+str(
        user_bounds.get("START")) + " - "+str(user_bounds.get("END"))+")"
    red = int(ask_user_numeric(user_message, user_bounds))

    user_message = "Please select the Green value you would like to choose: ("+str(
        user_bounds.get("START")) + " - "+str(user_bounds.get("END"))+")"
    green = int(ask_user_numeric(user_message, user_bounds))

    user_message = "Please select the Blue value you would like to choose: ("+str(
        user_bounds.get("START")) + " - "+str(user_bounds.get("END"))+")"
    blue = int(ask_user_numeric(user_message, user_bounds))
    return create_rgb_message(channel, red, green, blue)


def ask_user_for_colour(channel, mode):
    """_summary_: Gets the message to send to the hardware to change the colour mode
    Args:
        channel (_type_): _description_ The channel to change
        mode (_type_): _description_ The mode to change to
        colour (_type_): _description_ The colour to change to
        brightness (_type_): _description_ The brightness to change to
    Returns:
        _type_: _description_ The message to send to the hardware
    """

    # Ask the user for the colour and brightness
    user_bounds = {"START": 0, "END": 12}
    user_message = "Please select the colour you would like to have on this channel: ("+str(
        user_bounds.get("START")) + " - "+str(user_bounds.get("END"))+")"
    colour = int(ask_user_numeric(user_message, user_bounds))

    # Ask the user for the brightness
    user_bounds = {"START": 0, "END": 100}
    user_message = "Please select the brightness you would like to have on this channel: ("+str(
        user_bounds.get("START")) + " - "+str(user_bounds.get("END"))+")"
    brightness = int(ask_user_numeric(user_message, user_bounds))

    # Ask the user for the period
    period = 0
    message = None
    if mode != FADE_TYPE.NONE:
        user_bounds = {"START": 0, "END": 4294967295}
        user_message = "Please select the period of the fade in ms: ("+str(
            user_bounds.get("START")) + " - "+str(user_bounds.get("END"))+")"
        period = int(ask_user_numeric(user_message, user_bounds))
        message = create_fade_message(
            channel, mode, colour, brightness, period)
    else:
        message = create_constant_colour_message(channel, colour, brightness)
    return message


def user_loop(communicator):
    """_summary_: The main loop of the program

    Args:
        communicator (_type_): _description_ The communicator to use to send messages
    """
    while True:
        tx_msg = None
        # Ask user for channel
        user_bounds = {"START": 1, "END": 3}
        user_message = "Please select the channel you would like to change: ("+str(
            user_bounds.get("START")) + " - "+str(user_bounds.get("END"))+")"
        channel = CHANNEL(int(ask_user_numeric(user_message, user_bounds)))

        # Ask user for mode
        user_bounds = {"START": 0, "END": 7}
        user_message = "Please select the mode you would like to choose: ("+str(
            user_bounds.get("START")) + " - "+str(user_bounds.get("END"))+")"
        mode = FADE_TYPE(int(ask_user_numeric(user_message, user_bounds)))

        if mode == FADE_TYPE.HUE_CTRL:
            tx_msg = ask_user_for_hue(channel, mode)
        elif mode == FADE_TYPE.RGB_CTRL:
            tx_msg = ask_user_for_rgb(channel, mode)
        else:
            tx_msg = ask_user_for_colour(channel, mode)

        # Add padding to the message and send it
        if(isinstance(communicator, socket.socket)):
           communicator.sendall(tx_msg)
        elif(isinstance(communicator, serial.Serial)):
            communicator.write(tx_msg)
        print("Sent Message")
        print(binascii.hexlify(tx_msg))


def main():
    """_summary_: The main function of the program
    """
    communicator = None
    communicator_options = {"TCP-IP", "Serial"}
    user_message = "Please select the communication method you would like to use: ("+str(
        communicator_options)+")"
    chosen_comms = ask_user_word(user_message, communicator_options)
    if chosen_comms == "TCP-IP":
        connected = False
        while(connected == False):
            ip = input("What IP is the hardware connected on?")
            port = input("What port is the hardware connected on?")
            try:
                communicator = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                communicator.connect((ip, int(port)))
                connected = True
            except socket.error:
                print("Could not connect to the hardware on IP: "+ip +
                      " and port: "+port)
    elif chosen_comms== "Serial":
        connected =False
        while(connected == False):
            port = input("What port is the hardware connected on?")
            try:
                communicator = serial.Serial(port)
                communicator.parity = serial.PARITY_EVEN
                communicator.timeout = 1
                communicator.stopbits = serial.STOPBITS_ONE
                communicator.bytesize = serial.EIGHTBITS
                communicator.baudrate = 115200
                connected = True
            except serial.SerialException:
                print("Could not connect to the hardware on port: "+port)
            

    user_loop(communicator)


if __name__ == "__main__":
    main()
