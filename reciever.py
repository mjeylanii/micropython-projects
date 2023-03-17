import socket
import os

SERVER_IP = "192.168.1.10"
SERVER_PORT = 5000
FILE_NAME = "test.jpg"
DEST_PATH = os.path.join(os.path.expanduser(
    "~"), "OneDrive/Desktop", FILE_NAME)

#file size in aabbccdd format
def receive_file_size(s):
    file_size_bytes = s.recv(4)
    file_size = int.from_bytes(file_size_bytes, 'little')
    return file_size

def receive_file():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, SERVER_PORT))
            with open(DEST_PATH, "wb") as f:
                # receive the size of the file
                file_size_bytes = s.recv(4)
                file_size = int.from_bytes(file_size_bytes, 'little')
                # receive the file data
                bytes_received = 0
                while bytes_received < file_size:
                    chunk = s.recv(2048)
                    if not chunk:
                        raise ValueError("Empty chunk read")
                    if chunk == file_size:
                        break
                    f.write(chunk)
                    bytes_received += len(chunk)
                    print(
                        f"Received {bytes_received} bytes of {file_size} bytes")
    except ConnectionRefusedError:
        print("Error: connection refused.")
    except OSError as e:
        print(f"Error: {e}.")
    except ValueError as e:
        print(f"Error: {e}.")
    except KeyboardInterrupt:
        print("Operation cancelled by user.")
    else:
        print(f"File received successfully and saved to {DEST_PATH}.")


if __name__ == '__main__':
    receive_file()
