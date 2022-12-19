from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from app.controller import get_location, get_message
from app.model import antennas, update_antenna_information

app = FastAPI()

class BaseAntenna(BaseModel):
  distance: float
  message: List[str]

class Antenna(BaseAntenna):
  name: str

class Input(BaseModel):
  antennas: List[Antenna]

@app.get("/health_check")
async def health_check():
    """
    This function returns a message indicating that the service is working properly.

    Returns:
        A dictionary with a message indicating that the service is working properly.
    """
    return {"message": "im fine :D"}

@app.post("/location", status_code=201)
async def location(input: Input):
    """
    This function updates the information of multiple antennas with the data provided
    in the request and returns the user's location and the message received by the antennas.

    Args:
        input (Input): An object containing the information of multiple antennas.

    Returns:
        A dictionary containing the user's location as a tuple and the message.
    """
    for antena in input.antennas:
        update_antenna_information(antena.distance, antena.message, antena.name)
    location = get_location()
    message = get_message()
    return {
        "position": {
            "X": location[0],
            "Y": location[1],
        },
        "message": message
    }

@app.post("/location_by_parts/{name}", status_code=201)
async def post_location_by_parts(name: str, input: BaseAntenna):
    """
    This function updates the information of a specific antenna with the data provided in the request.

    Args:
        name (str): The identifier of the antenna.
        input (AntennaPost): An object containing the distance and message of the antenna.

    Returns:
        A dictionary with a message confirming that the antenna information was saved successfully and the updated information of the antenna.
    """
    response = update_antenna_information(input.distance, input.message, name)
    return {
        "message": "Antenna information saved successfully",
        "response": response
    }

@app.get("/location_by_parts/{name}")
async def get_location_by_parts(name: str):
    """
    This function returns the information of a specific antenna.

    Args:
        name (str): The identifier of the antenna.
    Returns:
        The information of the antenna with the given identifier.
    """
    return antennas[name]

@app.get("/get_user_location")
async def get_user_location():
    """
    This function returns the user's location and the message received by the antennas.
    The function first checks if all the antenna information is available.
    Then, it retrieves the user's location using the `get_location` function and the message using the `get_message` function.
    Finally, it returns a dictionary containing the user's location as a tuple and the message.
    """
    check_antenna_info()
    location = get_location()
    message = get_message()
    return {
        "position": {
            "X": location[0],
            "Y": location[1],
        },
        "message": message
    }

def check_antenna_info():
    """
    This function checks if all the values for each antenna in the `antennas` dictionary are not `None`.
    If any of the values is `None`, a HTTPException is raised.
    """
    for _, antenna_values in antennas.items():
        if not all(valor is not None for valor in antenna_values.values()):
            raise HTTPException(status_code=400, detail="The service needs more information")