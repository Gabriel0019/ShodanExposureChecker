import os
import shodan
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("SHODAN_API_KEY")

if not api_key:
    print("Error: SHODAN_API_KEY not found in environment variables.")
    exit(1)

api = shodan.Shodan(api_key)
print("Shodan API initialized successfully.")

ip = input("Enter an IP address to check: ")

try: 
    host = api.host(ip)
    print(f"IP: {host['ip_str']}")
    print(f"Organization: {host.get('org', 'n/a')}")
    print(f"Operating System: {host.get('os', 'n/a')}")
    print("Services:")
    for service in host['data']:
        print(f"Port: {service.get('port', 'n/a')}, Banner: {service.get('data', 'n/a')}")
        print(f"Transport: {service.get('transport', 'n/a')}, Product: {service.get('product', 'n/a')}")
        print(f"Version: {service.get('version', 'n/a')}, Hostnames: {service.get('hostnames', 'n/a')}")
        
except shodan.APIError as e:
    print(f"Error: {e}")