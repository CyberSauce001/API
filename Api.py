import requests
import json

api_token = '[insert account token]'
account_id = '[insert account id]'
api_url_base = '[insert account url]'

def get_account():
    api_url = ('{0}/?id='+account_id +'&token=' + api_token ).format(api_url_base)
    response = requests.get(api_url)
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
def account_status():
    account_info = get_account()

    if account_info is not None:
        print("Account Info: ")
        for k, v in account_info.items():
            print('{0}:{1}'.format(k,v))
    else:
        print('Error!! Request Failed')

print ("1 for Status code or 2 for account info")
choose = int(input("Choose input:" ))

if choose == 1:
    check = True
    get_account()
elif choose == 2:
    check = False
    account_status()
else:
    print ("Debug: Error #2")
