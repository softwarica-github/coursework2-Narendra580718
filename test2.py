import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 9999         # The port used by the server

def send_pdf_file(filename):
    with open(filename, 'rb') as file:
        pdf_data = file.read()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(pdf_data)

if __name__ == "__main__":
    pdf_filename = 'new.pdf'
    send_pdf_file(pdf_filename)
