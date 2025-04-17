def ask_user_word(message, validInputs):
    """_summary_: Checks if a word is within the bounds of a list of valid inputs
    _params_: input: The word to check
              validInputs: The list of valid inputs
    _return_: True if the word is within the bounds, False otherwise
    """
    usr_input = input(message)
    while (usr_input not in validInputs):
        print("Invalid: Please try again")
        print("The options are: " + str(validInputs))
        usr_input = input("Enter a valid input: ")
    return usr_input


def ask_user_numeric(message, bounds):
    """_summary_: Asks the user for input and checks if the input is within the bounds, blocks until the user enters a valid input

    Args:
        message (_type_): _description_ The message to display to the user
        bounds (_type_): _description_ The bounds to check the input against
    Returns:
        _type_: _description_ The user input if it is within the bounds otherwise it will ask the user again
    """
    while (True):
        user_input = input(message)
        if __check_numeric_bounds(user_input, bounds.get("START"), bounds.get("END")):
            return user_input
        else:
            print("Invalid: Please try again")


def __check_numeric_bounds(val, min_val, max_val):
    """_summary_: Checks if a value is within the bounds of a min and max value
    _params_: val: The value to check
              min_val: The minimum value
              max_val: The maximum value
    _return_: True if the value is within the bounds, False otherwise
    """
    try:
        val = int(val)

    except ValueError:
        print("Invalid Value for value, please try again")
        return False

    if val < min_val or val > max_val:
        print("Value out of bounds, please try again inside the bounds of " +
              str(min_val) + " and " + str(max_val))
        return False
    return True
