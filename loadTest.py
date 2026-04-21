import threading
import requests 
#     rsp = requests.get('http://dev.eshra7ly.net', stream=True)
#     print(rsp.raw._fp.fp.raw._sock.getpeername()[0])
class LoadTest():
    def bing(self, host, count):
        try:
            while True:
                rsp = requests.get(host, stream=True)
                if str(rsp.status_code) == '200':
                    print(f"{rsp.status_code}, {count}")
                    continue
        except Exception:
            print("[-] ERROR: Disconnected!!!")
            
load_test = LoadTest()
site = input("[!] Please Enter The Site: ")
thread_number = int(input("[!] Please Enter The Threads Number: "))

for i in range(thread_number):
    threads = threading.Thread(target=load_test.bing, args=(site, i + 1, ))
    threads.start()