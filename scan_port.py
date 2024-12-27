import socket
def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open.")
            sock.close()
    except KeyboardInterrupt:
        print("\nExiting...")
    except socket.error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))
    scan_ports(target_ip, start, end)
