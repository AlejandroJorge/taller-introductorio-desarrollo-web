import socket

# Logica de la transaccion
def handle_connection(client_socket):
  cadena = "Lor.em i.psum."
  msg = f"{cadena}".encode("utf-8") # Transformar la cadena de caracteres en bytes
  print(f"Cadena enviada: '{cadena}'")
  client_socket.sendall(msg)

  parametros_de_la_cadena = client_socket.recv(1024).decode("utf-8") # Recibe 1024 bytes (como maximo) y los transforma a utf-8
  print(f"CARACTERES,ESPACIOS,PUNTOS: '{parametros_de_la_cadena}'")

# Puerto con el que se comunicara el socket cliente
PORT = 5000

# Setup del cliente
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Transaccion
print("================================================")

client_socket.connect(("localhost",PORT))

handle_connection(client_socket)

print("================================================")
