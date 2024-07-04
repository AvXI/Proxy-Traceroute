import requests
import re

# Set the URL of the website to trace
url = "https://www.example.com"

# Set the proxy server to use
proxy = {
    'http': 'http://user:password@proxyserver:port',
    'https': 'https://user:password@proxyserver:port'
}

# Send a GET request to the website using the proxy server
response = requests.get(url, proxies=proxy)

# Extract the IP address of the proxy server from the response headers
proxy_ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', response.headers['proxy-connection'])[0]

# Print the IP address of the proxy server
print("Proxy server IP address:", proxy_ip)

# Trace the route from the client to the proxy server
traceroute_url = "https://api.hackertarget.com/mtr/?q=" + proxy_ip
traceroute_response = requests.get(traceroute_url)

# Print the traceroute results
print(traceroute_response.text)