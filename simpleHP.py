import socket
import telnetlib

def honeypot(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(5)
    print(f"[*] Listening on 0.0.0.0:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[*] Connection from: {addr[0]}:{addr[1]}")
        
        with open("honeypot.log", "a") as log_file:
            log_file.write(f"Connection from: {addr[0]}:{addr[1]}\n")
        
        # Send a fake banner to the client
        client_socket.send(b"Welcome to the HoneyPot!\n")
        
        # Create a Telnet object for the connection
        tn = telnetlib.Telnet()
        tn.sock = client_socket
        
        # Wait for some time and then close the connection
        tn.interact()
        tn.close()
        client_socket.close()

if __name__ == '__main__':
    port = 22

    try:
        honeypot(port)
    except KeyboardInterrupt:
        print("\n[*] Stopping the HoneyPot")
