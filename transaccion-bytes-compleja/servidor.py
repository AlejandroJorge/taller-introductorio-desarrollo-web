import socket

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
  # Secuencia de envios: cliente -> servidor -> cliente -> cliente 

  print("================================================")
  
  print(f"Conexion recibida desde {client_address}")

  data = client_socket.recv(1024).decode("utf-8") # Recibe 1024 bytes (como maximo) y los transforma a utf-8
  print(f"Data recibida: '{data}'")

  msg = "Mensaje del cliente".encode("utf-8") # Respuesta del servidor en bytes
  client_socket.sendall(msg)
  print(f"Data enviada: '{msg}'")

  data = client_socket.recv(1024).decode("utf-8") # Recibe 1024 bytes (como maximo) y los transforma a utf-8
  print(f"Data recibida: '{data}'")

  data = client_socket.recv(1024).decode("utf-8") # Recibe 1024 bytes (como maximo) y los transforma a utf-8
  print(f"Data recibida: '{data}'")

  client_socket.close()
  
  print(f"Conexion cerrada con {client_address}")
  
  print("================================================")
