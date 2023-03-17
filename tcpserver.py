import socket
import time
import os


def connect_tcp(ip):
    ip_addr = ""
    Port = 5000
    Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    Socket.bind((ip_addr, Port))
    print("Connecting to {}".format(ip_addr))
    Socket.listen(5)
    print('Listening on port for connection')
    addr = 0
    dir_list = os.listdir("thermal-images/")
    while addr == 0:
        conn, addr = Socket.accept()
    print('Connected to {}'.format(addr))
    counter = 0
    try:
        while True:
            for file in dir_list:
                if counter < len(dir_list):
                    counter += 1
                    print('Sending file {}: {}'.format(counter, file))
                else:
                    counter = 0
                    break
                sot = bytes.fromhex('AABBCCDD')
                conn.send(sot)
                with open("thermal-images/" + file, "rb") as f:
                    file_size = os.stat("thermal-images/" + file)[6]
                    chunk_size = 2048
                    fsize = int(file_size).to_bytes(4, 'little')
                    print('File size: {}'.format(file_size))
                    conn.send(fsize)
                    bytes_sent = 0
                    while bytes_sent < file_size:
                        chunk = f.read(chunk_size)
                        if not chunk:
                            raise ValueError("Empty chunk read")
                        conn.send(chunk)
                        bytes_sent += len(chunk)
                        print(f'Bytes sent: {bytes_sent}')
                        del chunk
                        time.sleep(0.05)
                    del f
                    time.sleep(0.5)

    except ConnectionResetError as e:
        print('Connection reset by peer')
        socket.close()
    except KeyboardInterrupt:
        print('Interrupted') 
    except OSError as e:
        print('Error:', e)
        conn.close()
        Socket.close()

    finally:
        conn.close()
        Socket.close()

# Start connection


if __name__ == '__main__':

    try:
        connect_tcp("")
    except KeyboardInterrupt:
        print('Interrupted')
