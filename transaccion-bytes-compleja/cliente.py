import socket

# Puerto con el que se comunicara el socket cliente
PORT = 5000

# Setup del cliente
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Transaccion
# Secuencia de envios: servidor -> cliente -> servidor -> servidor 

print("================================================")

client_socket.connect(("localhost",PORT))

msg = "Primer mensaje del cliente".encode("utf-8") # Transformar la cadena de caracteres en bytes
print(f"Data enviada: '{msg}'")
client_socket.sendall(msg) # Enviar al servidor la cantidad de bytes deseada

data = client_socket.recv(1024).decode("utf-8") # Recibe 1024 bytes (como maximo) y los transforma a utf-8
print(f"Data recibida: '{data}'")

msg = "Segundo mensaje del cliente".encode("utf-8") # Transformar la cadena de caracteres en bytes
print(f"Data enviada: '{msg}'")
client_socket.sendall(msg) # Enviar al servidor la cantidad de bytes deseada

msg = "Tercer mensaje del servidor".encode("utf-8") # Transformar la cadena de caracteres en bytes
print(f"Data enviada: '{msg}'")
client_socket.sendall(msg) # Enviar al servidor la cantidad de bytes deseada

print("================================================")
