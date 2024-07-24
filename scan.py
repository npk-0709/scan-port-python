import socket
import threading

def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = scanner.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is open")
    scanner.close()

def scan_ports(ip, start_port, end_port):
    print(f"Scanning IP: {ip} from port {start_port} to {end_port}")
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("Scan complete")


target_ip = input("Enter IP address to scan: ").strip()
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))


scan_ports(target_ip, start_port, end_port)
