import requests
import configparser

# API_KEY = 'VF.6325dad1047b6a0007cb6801.2nlYtdJ7K7nuaRJc' # it should look like this: VF.DM.XXXXXXX.XXXXXX... keep this a secret!
# API_KEY = 'VF.DM.63260b35047b6a0007cb681b.e3mYIV9HWjQkbuv4'
# versionID = '6325da5c64484143a984ae38'

config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config['settings']['api_key']
versionID = config['settings']['versionID']



user_id = 'user1'

url = f"https://general-runtime.voiceflow.com/state/user/{user_id}/interact"
payload = {
    "action": {
        # Launch
        #"type": "launch"

        "type": "text",
        "payload": "I want dumplings"

        # Need Items
        # 'type': 'path-k0kt3oln', 'payload': {'label': 'I need some items', 'actions': []}
        # 'type': 'path-u0uj3ofh', 'payload': {'label': 'Pillow', 'actions': []}
        # 'type': 'path-kr1kb3o3g', 'payload': {'label': '2', 'actions': []}

        # Order
        # 'type': 'path-9anj3omb', 'payload': {'label': 'I want to order food and drinks', 'actions': []}

        # Location
        # 'type': 'path-qsnv3obl', 'payload': {'label': 'I want to check location and opening hours of facilities and services', 'actions': []}
        
        # Redo?
        # 'type': 'path-al1pj3ojz', 'payload': {'label': 'Yes', 'actions': []}
        # 'type': 'path-vw1ty3o9u', 'payload': {'label': 'No', 'actions': []}
    },
    "config": {
        "tts": False,
        "stripSSML": True,
        "stopAll": True,
        "excludeTypes": ["block", "debug", "flow"]
    }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    'Authorization': API_KEY,
    'versionID':'development'
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())

# --------
"""
# meant for Python 3, will not work with Python 2
import requests # pip install requests


# user_id defines who is having the conversation, e.g. steve, john.doe@gmail.com, username_464
def interact(user_id, request):
    response = requests.post(
        f'https://general-runtime.voiceflow.com/state/user/{user_id}/interact',
        json={ 'request': request },
        headers={ 'Authorization': api_key },
    )

    for trace in response.json():
        if trace['type'] == 'speak' or trace['type'] == 'text':
            print(trace['payload']['message'])
        elif trace['type'] == 'end':
            # an end trace means the the voiceflow dialog has ended
            return False
    return True

name = input('> What is your name?\n')
isRunning = interact(name, { 'type': 'launch' })

while (isRunning):
    nextInput = input('> Say something\n')
    # send a simple text type request with the user input
    isRunning = interact(name, { 'type': 'text', 'payload': nextInput })

input('The end! Start me again with `python index.py` or `python3 index.py`')"""