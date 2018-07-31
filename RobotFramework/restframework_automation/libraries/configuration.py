import requests
import json


def get_request(url_request):
    request = requests.get(url=url_request)
    status = request.status_code
    if status == 404:
        print("Checks the url name is valid")
    else:
        json_response = request.json()
        if status == 200 and "FileError" not in json_response:
            print("The get request was successful:", json_response)
        else:
            print("Unable compare the documents")
            return json_response
    return status


def post_request(url_request, url_data):
    json_decode = json.loads(url_data)
    request = requests.post(url=url_request, json=json_decode)
    status = request.status_code
    if status == 404:
        print("Checks the url name is valid")
        return status
    else:
        json_response = request.json()
        if "JWTError" not in json_response:
            if "KeyError" not in json_response:
                print("The post request was successful:", json_response)
            else:
                print("Checks the data contains the key 'message'")
                return json_response
            return status
        else:
            print("The encoded token could not be verified")
            return json_response


def get_evaluate_request(url_request):
    get_request(url_request)
    request = requests.get(url=url_request)
    json_response = request.json()
    if json_response["diffblock"] == "false":
        print("The strings are equals")
        return json_response["diffblock"]
    else:
        print("The strings do not equals")
        return json_response["diffblock"]
