from typing import List

antennas = {
    "wonderfulAntena1": {
        "position": (-25, -10),
  		"distance": None,
		"message": None
 	},
    "wonderfulAntena2": {
        "position": (5, -5),
        "distance": None,
		"message": None
	},
    "wonderfulAntena3": {
        "position": (25, 5),
		"distance": None,
		"message": None
    },
}

def update_antenna_information(distance: float, message: list, name: str):
    """
    This function is responsible for updating the data provided by the user

    Args:
        distance (float): The distance of the antenna from JP.
        message (list): The message captured by the antenna.
        name (str): The identifier of the antenna.

    Returns:
        The antenna information
    """
    new_data = {
        "distance": distance,
        "message": message,
    }
    antennas[name].update(new_data)
    return antennas[name]

def get_antenna_message(name: str) -> List[str]:
    """
    Returns a list of words obtained from the specified antenna.

    Args:
        name (str): The identifier of the antenna.

    Returns:
        A list of words obtained from the antenna.
    """
    return get_antenna_information(name, "message")

def get_antenna_information(name: str, info: str):
    """
    Returns the requested information for a specific antenna.

    Args:
        name (str): The identifier of the antenna.
        info (str): The name of the information to be returned.

    Returns:
        The requested information for the antenna.
    """
    return antennas[name][info]