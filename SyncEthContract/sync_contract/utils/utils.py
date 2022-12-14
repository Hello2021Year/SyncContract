import requests
import json




def build_header_masterKey(master_key):
    headers = {
                'X-Parse-Master-Key': master_key,
                'Content-Type': 'application/json',
               }
    return headers

def builder_header_apiKey(api_key):
    headers = {
                'X-API-Key': api_key,
                'Content-Type': 'application/json',
                 'accept': 'application/json',

               }
    return headers

def builder_header_hook(config):
    headers =   {
                'X-Parse-Application-Id': config.application_id,
                'X-Parse-Master-Key': config.master_key,
                'Content-Type': 'application/json'
                }
    return  headers