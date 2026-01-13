def ask_user_word(message: str, validInputs: set[str]) -> str:
    """Ask the user for a word input and validate it against a set of valid options.

    Args:
        message: The message to display to the user prompting for input.
        validInputs: A set of valid input options to check against.

    Returns:
        The validated user input string.
    """
    usr_input = input(message)
    while (usr_input not in validInputs):
        print("Invalid: Please try again")
        print("The options are: " + str(validInputs))
        usr_input = input("Enter a valid input: ")
    return usr_input


def ask_user_numeric(message: str, bounds: dict[str, int]) -> str:
    """Ask the user for numeric input and validate it against specified bounds.

    Continuously prompts the user until valid input is provided within the
    specified START and END bounds.

    Args:
        message: The message to display to the user prompting for input.
        bounds: A dictionary with 'START' and 'END' keys specifying the valid range.

    Returns:
        The validated user input as a string.
    """
    while (True):
        user_input = input(message)
        if __check_numeric_bounds(user_input, bounds.get("START"), bounds.get("END")):
            return user_input
        else:
            print("Invalid: Please try again")


def __check_numeric_bounds(val: str, min_val: int | None, max_val: int | None) -> bool:
    """Check if a string value can be converted to an integer within specified bounds.

    Args:
        val: The string value to check and convert.
        min_val: The minimum allowed value (inclusive).
        max_val: The maximum allowed value (inclusive).

    Returns:
        True if the value is valid and within bounds, False otherwise.
    """
    if min_val is None or max_val is None:
        print("Invalid bounds configuration")
        return False

    try:
        int_val = int(val)

    except ValueError:
        print("Invalid Value for value, please try again")
        return False

    if int_val < min_val or int_val > max_val:
        print("Value out of bounds, please try again inside the bounds of " +
              str(min_val) + " and " + str(max_val))
        return False
    return True
