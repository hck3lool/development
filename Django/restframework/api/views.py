from .models import RestRight
from .models import RestLeft
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .decode import Decode
from jose.exceptions import JWTError


@api_view(["POST"])
def json_rest(request, id_request_json, side):
    dict_data_encoded = request.data["data"]
    decode = Decode()
    try:
        decode_request = decode.decoding(dict_data_encoded)
        if side == "right":
            new_document = RestRight(data=decode_request["message"], id=id_request_json)
            new_document.save()
            response = {
                'message': 'Document created',
                'endpoint': 'right',
                'id': id_request_json
            }
            return JsonResponse(response, safe=False)
        else:
            new_document = RestLeft(data=decode_request["message"], id=id_request_json)
            new_document.save()
            response = {
                'message': 'Document created',
                'endpoint': 'left',
                'id': id_request_json
            }
            return JsonResponse(response, safe=False)

    except JWTError:
        response = {
            "JWTError": "Your token could not be verified."
        }
        return JsonResponse(response, safe=False)

    except KeyError:
        response = {
            "KeyError": "key name 'message' not exist, unable to process document."
        }
        return JsonResponse(response, safe=False)


@api_view(["GET"])
def compare_rest(request, id_request_json):
    try:
        queryset_right = RestRight.objects.get(pk=id_request_json)
        queryset_left = RestLeft.objects.get(pk=id_request_json)
        dictionary = {}
        counter = 0

        if queryset_left.data == queryset_right.data and len(queryset_right.data) == len(queryset_left.data):
            response = {
                "diffblock": "false",
                "equal_content": "true",
                "equal_size": "true",
                "id": id_request_json
            }
            return JsonResponse(response, safe=False)

        elif len(queryset_right.data) != len(queryset_left.data):
            response = {
                "diffblock": "true",
                "equal_content": "false",
                "equal_size": "false",
                "id": id_request_json
            }
            return JsonResponse(response, safe=False)
        else:
            for i, j in zip(queryset_left.data, queryset_right.data):
                counter += 1
                if i == j:
                    dictionary["pos" + str(counter)] = 0
                else:
                    dictionary["pos" + str(counter)] = 1
            response = {
                "diffblock": dictionary,
                "equal_content": "false",
                "equal_size": "true",
                "id": id_request_json
            }
            return JsonResponse(response, safe=False)

    except RestRight.DoesNotExist:
        response = {
            "FileError": "Unable to process the documents. File not found on right server."
        }
        return JsonResponse(response, safe=False)
    except RestLeft.DoesNotExist:
        response = {
            "FileError": "Unable to process the documents. File not found on left server."
        }
        return JsonResponse(response, safe=False)
