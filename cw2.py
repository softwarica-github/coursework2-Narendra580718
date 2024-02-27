import tkinter as tk
import socket
from threading import Thread

class IDS_GUI:
    def __init__(self, master):
        self.master = master
        master.title("Intrusion Detection System")

        self.output_text = tk.Text(master, height=50, width=100, background="black", foreground="white")
        self.output_text.pack()

        self.start_button = tk.Button(master, text="Start Server", command=self.start_server,font=("Times New Roman", 14), background="cyan")
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Server", command=self.stop_server, state=tk.DISABLED, font=("Times New Roman", 14), background="red")
        self.stop_button.pack()

        self.server_socket = None
        self.server_thread = None

    def detect_intrusion(self, data):
        keywords = ['hack', 'attack', 'malware', 'virus']
        for keyword in keywords:
            if keyword in data:
                return True
        return False

    def handle_connection(self, conn, addr):
        self.output_text.insert(tk.END, "Connection from: {}\n".format(addr))

        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break

            self.output_text.insert(tk.END, "Received: {}\n".format(data))

            if self.detect_intrusion(data):
                self.output_text.insert(tk.END, "Intrusion detected from: {}\n".format(addr))
                print("Alert! Intrusion detected from:", addr)

        conn.close()

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('127.0.0.1', 9999))
        self.server_socket.listen(5)

        self.output_text.insert(tk.END, "Intrusion Detection System started on 127.0.0.1:9999\n")
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.server_thread = Thread(target=self.accept_connections)
        self.server_thread.start()

    def accept_connections(self):
        while True:
            try:
                conn, addr = self.server_socket.accept()
                thread = Thread(target=self.handle_connection, args=(conn, addr))
                thread.start()
            except OSError:
                # Socket closed, likely due to stopping the server
                break

    def stop_server(self):
        if self.server_socket:
            self.server_socket.close()
            self.output_text.insert(tk.END, "Server Stopped\n")
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    gui = IDS_GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
