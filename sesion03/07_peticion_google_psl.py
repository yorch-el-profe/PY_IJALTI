import http.client

server = "www.google.com"
url = "/"

# Abriendo una conexión con los servidores de Google
connection = http.client.HTTPSConnection(server)

# Visitando la página principal de Google
connection.request("GET", url)

response = connection.getresponse()
html = response.read()

print(html)