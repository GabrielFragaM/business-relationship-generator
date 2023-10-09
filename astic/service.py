import requests
import json
import base64
import os

def asticaAPI(endpoint, payload, timeout):
    response = requests.post(endpoint, data=json.dumps(payload), timeout=timeout, headers={ 'Content-Type': 'application/json', })
    if response.status_code == 200:
        return response.json()
    else:
        return {'status': 'error', 'error': 'Failed to connect to the API.'}


def get_prompt_image(asticaAPI_key: str, httpsImage: str):
    # API configurations
    asticaAPI_key = asticaAPI_key
    asticaAPI_timeout = 60 # in seconds. "gpt" or "gpt_detailed" require increased timeouts
    asticaAPI_endpoint = 'https://vision.astica.ai/describe'
    asticaAPI_modelVersion = '2.1_full' # '1.0_full', '2.0_full', or '2.1_full'

    asticaAPI_input = httpsImage # use https image input (faster)

    # vision parameters:  https://astica.ai/vision/documentation/#parameters
    asticaAPI_visionParams = 'gpt_detailed,describe'  # comma separated, defaults to "all". 
    asticaAPI_gpt_prompt = '' # only used if visionParams includes "gpt" or "gpt_detailed"
    asticaAPI_prompt_length = '150' # number of words in GPT response

    # Define payload dictionary
    asticaAPI_payload = {
        'tkn': asticaAPI_key,
        'modelVersion': asticaAPI_modelVersion,
        'visionParams': asticaAPI_visionParams,
        'input': asticaAPI_input,
    }

    # call API function and store result
    asticaAPI_result = asticaAPI(asticaAPI_endpoint, asticaAPI_payload, asticaAPI_timeout)

    # Handle asticaAPI response
    if 'status' in asticaAPI_result:
        prompt = ''
        # Output Error if exists
        if asticaAPI_result['status'] == 'error':
            print('Output:\n', asticaAPI_result['error'])
        # Output Success if exists
        if asticaAPI_result['status'] == 'success':
            if 'caption' in asticaAPI_result and asticaAPI_result['caption']['text'] != '':
                print('=================')
                print('Caption:', asticaAPI_result['caption']['text'])
                prompt = 'Resume about the Image: ' + str(asticaAPI_result['caption']['text'])
            if 'caption_GPTS' in asticaAPI_result and asticaAPI_result['caption_GPTS'] != '':
                print('=================')
                print('GPT Caption:', asticaAPI_result['caption_GPTS'])
                prompt = prompt + '\nDescription about the Image: ' + str(asticaAPI_result['caption_GPTS'])

            return prompt
    else:
        return 'Error'