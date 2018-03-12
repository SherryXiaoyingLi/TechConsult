from django.shortcuts import render
from django.shortcuts import render_to_response

from django.http import HttpResponse
from django.http import JsonResponse

import urllib.request
import urllib.parse
import json

# Create your views here.
def index(request):

    return HttpResponse("CS4501 Project 3, Experience layer")

# For index page
# Returns the pk of the newest consumer request
def getNewestRequestPk(request):
    response = {}
    response_data = {}
    try:
        req = urllib.request.Request('http://models-api:8000/api/v1/consumerRequests/getNewest')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        results = json.loads(resp_json)
        newest_pk = results["result"]["pk"]
        response["ok"] = True
        response_data["pk"] = newest_pk
    except:
        response["ok"] = False

    response['result'] = response_data
    return JsonResponse(response)

# For index page
# Returns the pk of the consumer request with the highest price
def getHighestRequestPk(request):
    response = {}
    response_data = {}
    try:
        req = urllib.request.Request('http://models-api:8000/api/v1/consumerRequests/getHighestPrice')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        results = json.loads(resp_json)
        newest_pk = results["result"]["pk"]
        response["ok"] = True
        response_data["pk"] = newest_pk
    except:
        response["ok"] = False

    response['result'] = response_data
    return JsonResponse(response)

# For request detail page
# Returns the request information, consumer information, and producer username
def getRequestDetail(request, consumerRequest_pk):
    response = {}
    response_data = {}

    req = urllib.request.Request('http://models-api:8000/api/v1/consumerRequests/' + str(consumerRequest_pk))
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    results = json.loads(resp_json)

    if results['ok'] == True:
        consumer_pk = results['result']['consumer']
        req2 = urllib.request.Request('http://models-api:8000/api/v1/consumers/' + str(consumer_pk))
        resp_json2 = urllib.request.urlopen(req2).read().decode('utf-8')
        results2 = json.loads(resp_json2)
        # consumer_username = results2['result']['username']

        response['ok'] = True

        response_data['title'] = results['result']['title']
        response_data['description'] = results['result']['description']
        response_data['offered_price'] = results['result']['offered_price']
        response_data['timestamp'] = results['result']['timestamp']
        response_data['availability'] = results['result']['availability']
        response_data['consumer_username'] = results2['result']['username']
        response_data['consumer_email'] = results2['result']['email']
        response_data['consumer_phone'] = results2['result']['phone']

        accepted_producer = results['result']['accepted_producer']
        if accepted_producer != None:
            req3 = urllib.request.Request('http://models-api:8000/api/v1/producers/' + str(accepted_producer))
            resp_json3 = urllib.request.urlopen(req3).read().decode('utf-8')
            results3 = json.loads(resp_json3)
            response_data['producer_username'] = results3['result']['username']
        else:
            response_data['producer_username'] = None

    else:
        response['ok'] = False

    response['result'] = response_data
    return JsonResponse(response)
