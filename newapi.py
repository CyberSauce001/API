import requests
import json
from urllib.request import urlopen

#global variable
api_token = ['insert token']
account_id = ['insert id']
api_url_base = ['insert url']
#this takes account id and the account token (does not work for all api url, so use the above
api_url = ('{0}/?id='+account_id +'&token=' + api_token ).format(api_url_base)

response = requests.get(api_url)
#get account url and status code, if 200 it means it is active
def get_account():
    if check == True:
        print(api_url)
        print(response.status_code)
    elif check == False:
        data = response.status_code
        if data == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None
    else:
        print('Debug: Error #1')


#get further details about the account status and its response
def account_status():
    account_info = get_account()

    if account_info is not None:
        print("Account Info: ")
        print(response.text)
    else:
        print('Error!! Request Failed')


#parse in response
def get_company():
    response = urlopen(api_url)
    r = response.read().decode('utf-8')
    r_obj = json.loads(r)
    for item in r_obj['response']:
        print("[insert response name]: {}".format(item['insert response parse array']))








#debugging purpose
print ("1 for Status code or 2 for account info or 3 for other")
choose = int(input("Choose input:" ))

if choose == 1:
    check = True
    get_account()
elif choose == 2:
    check = False
    account_status()
elif choose == 3:
    get_company()
else:
    print ("Debug: Error #2")
