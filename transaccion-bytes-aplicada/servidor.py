import socket

# Logica de la transaccion
# El servidor recibe una cadena y devuelve la siguiente informacion en este formato:
# CANTIDAD_DE_CARACTERES,CANTIDAD_DE_ESPACIOS,CANTIDAD_DE_PUNTOS 
def handle_connection(client_socket):
  cadena_de_caracteres = client_socket.recv(1024).decode("utf-8") # Recibe 1024 bytes (como maximo) y los transforma a utf-8
  print(f"Cadena recibida: '{cadena_de_caracteres}'")

  caracteres,espacios,puntos = 0,0,0

  for caracter in str(cadena_de_caracteres):
    if caracter == " ":
      espacios += 1
    elif caracter == ".":
      puntos += 1
    caracteres += 1

  msg = f"{caracteres},{espacios},{puntos}".encode("utf-8") # Transformar la cadena de caracteres en bytes

  client_socket.sendall(msg)
  print(f"CARACTERES,ESPACIOS,PUNTOS: '{msg}'")

  client_socket.close()

# Puerto que usara el socket
PORT = 5000

# Setup del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost",PORT))
server_socket.listen(1)
print(f"Servidor activo en el puerto {PORT}")

while True:
  print("Esperando una conexion")
  client_socket, client_address = server_socket.accept()

  # Transaccion
  
  print("================================================")
  
  print(f"Conexion recibida desde {client_address}")

  handle_connection(client_socket)  
  
  print(f"Conexion cerrada con {client_address}")
  
  print("================================================")
