import json

def test_health_check(test_app):
    response = test_app.get("/health_check")
    assert response.status_code == 200
    assert response.json() == {"message": "im fine :D"}


def test_get_user_location_without_data(test_app):
    response_get = test_app.get("/get_user_location")
    assert response_get.status_code == 400
    assert response_get.json() == {
         "detail": "The service needs more information"
    }

def test_post_location(test_app):
    test_request_payload = {
	    "antennas":[
		    {
		        "name":"wonderfulAntena1",
		        "distance":10.1,
		        "message":["", "tengo", "", "y", "hambre"]
		    },
		    {
		        "name":"wonderfulAntena2",
		        "distance":15.6,
		        "message":["ayuda", "", "frío", "y", ""]
		    },
		    {
		        "name":"wonderfulAntena3",
		        "distance":12.9,
		        "message":["ayuda", "", "", "", "hambre"]
		    }
	    ]
    }
    test_response_payload = {
        "position": {
            "X": 3.83,
            "Y": -2.97
        },
        "message": "ayuda tengo frío y hambre"
    }

    response = test_app.post("/location/", content=json.dumps(test_request_payload),)

    assert response.status_code == 201
    assert response.json() == test_response_payload

def test_location_by_parts(test_app):
    test_request_payload = {
		        "distance":10.1,
		        "message":["", "tengo", "", "y", "hambre"]
		    }

    test_response_payload = {
        "message": "Antenna information saved successfully",
        "response": {
            "position": [-25, -10],
            "distance": 10.1,
            "message": ["", "tengo", "", "y", "hambre"]
        }
    }
    test_response_get ={
        "position": [-25,-10],
        "distance": 10.1,
        "message": ["", "tengo", "", "y", "hambre"]
    }

    response_post = test_app.post("/location_by_parts/wonderfulAntena1", content=json.dumps(test_request_payload))
    response_get = test_app.get("/location_by_parts/wonderfulAntena1")

    assert response_post.status_code == 201
    assert response_post.json() == test_response_payload
    assert response_get.status_code == 200
    assert response_get.json() == test_response_get


def test_get_user_location_with_data(test_app):
    test_response_payload = {
        "position": {
            "X": 3.83,
            "Y": -2.97
        },
        "message": "ayuda tengo frío y hambre"
    }
    response_get = test_app.get("/get_user_location")
    assert response_get.status_code == 200
    assert response_get.json() == test_response_payload