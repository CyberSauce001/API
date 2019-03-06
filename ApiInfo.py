import json
import requests

api_token = 'your api token'
api_url_base = 'base url' 

#dictionary containing request headers if any

headers= {'Content-Type': 'application/json',
          'Authorization': 'Bearer {0}'.format(api_token)}


#Getting Information from the Web API
def get_account_info():
    api_url = '{0}account'.format(api_url_base)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.load(response.content.decode('utf-8'))
    else:
        return None

account_info = get_account_info()

if account_info is not None:
    print("Here's your info: ")
    for k,v in account_info['account'].items():
        print('{0}:{1}'.format(k,v))
else:
    print('[!] Request Failed')

#Modifying Information on the Server
def get_ssh_keys():
    api_url = '{0}account/keys'.format(api_url_base)

    response = requests.get(api_url, headers=headers)

    if response.status_code >=500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code,api_url))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code == 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
        return None
    elif response.status_code == 200:
        ssh_keys = json.loads(response.content.decode('utf-8'))
        return ssh_keys
    else :
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
        return None

ssh_keys = get_ssh_keys()

if ssh_keys is not None:
    print('Here are your keys: ')
    for key, details in enumerate(ssh_keys['ssh_keys']):
        print('Key {}:'.format(key))
        for k,v in details.item():
            print('  {0}:{1}'.format(k,v))
else:
    print('[!] Request Failed')

#Add SSH KEY
def add_ssh_key(name,filename):
    api_url = '{0}account/keys'.format(api_url_base)

    with open(filename, 'r') as f:
        ssh_key = f.readline()

    ssh_key = {'name':name, 'public_key': ssh_key}

    response =- requests.post(api_url, headers=headers, json=ssh_key)

    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404 :
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code, api_url))
        return None
    elif response.status_code == 401 :
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code >= 400 :
        print('[!] [{0}] Bad Request'.format(response.status_code))
        print(ssh_key)
        print(response.content)
        return None
    elif response.status_code >= 300 :
        print('[!] [{0}] Unexpected redirect.'.format(response.status_code))
        return None
    elif response.status_code == 201 :
        added_key = json.loads(response.content)
        return added_key
    else :
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
        return None

    add_response = add_ssh_key('tutorial_key', '/home/path/to/.ssh/.pub')

    if add_response is not None:
        print('Your key was added: ')
        for k, v in add_response.items():
            print('  {0}:{1}'.format(k,v))
    else:
        print('[!] Request Failed')
