import itertools
from typing import Tuple
from app.model import antennas, get_antenna_information, get_antenna_message

def get_location() -> Tuple[float, float]:
    """
    Calculates the coordinates (x, y) of the message's origin based on the distances between the antennas and the origin.

    Returns:
        The (x, y) coordinates of the message's origin.
    """
    total_distance = 0
    position_x = 0
    position_y = 0
    for antennas_name in antennas:
        distance = get_antenna_information(antennas_name, "distance")
        total_distance += distance
        position = get_antenna_information(antennas_name, "position")
        position_x += position[0] * distance
        position_y += position[1] * distance
    position_x /= total_distance
    position_y /= total_distance
    return (round(position_x, 2), round(position_y, 2))


def get_first_non_empty(tuple: Tuple):
    """
    Returns the first non-empty element in a tuple.

    Args:
        tuple (tuple): The input tuple.

    Returns:
        The first non-empty element in the tuple, or `None` if there are no non-empty elements.
    """
    for element in tuple:
        if element:
            return element
    return None

def get_message() -> str:
    """
    Returns the original message from the words received on each antenna.

    Returns:
        The original message as a string.
    """

    antenna_words = [
        ("wonderfulAntena1", get_antenna_message("wonderfulAntena1")),
        ("wonderfulAntena2", get_antenna_message("wonderfulAntena2")),
        ("wonderfulAntena3", get_antenna_message("wonderfulAntena3")),
    ]
    tuples = itertools.zip_longest(*[words for _, words in antenna_words])
    message = [get_first_non_empty(tuple) for tuple in tuples]
    return " ".join(message)



