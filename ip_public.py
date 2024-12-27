import requests
def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        ip = response.json().get("ip")
        return ip
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
ip = get_public_ip()
if ip:
    print(f"Your public IP address is: {ip}")
else:
    print("Could not fetch public IP address.")
