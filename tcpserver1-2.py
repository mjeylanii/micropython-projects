import socket
import time
import os


def connect_tcp(ip):

    ip_addr = ip
    Port = 5041
    Soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # ip_addr=socket.gethostbyname(socket.gethostname())
    Soket.bind((ip_addr, Port))
    print("Connecting to {}".format(ip_addr))

    dir_list = os.listdir("images/")
    # print(type(dir_list))

    Soket.listen(5)
    print('listening on port for connection')
    addr = 0
    while addr == 0:
        conn, addr = Soket.accept()
    time.sleep(0.1)
    print(conn, addr)

    # conn.send(bytes(StartofPackage,'utf-8'))

    def SendStartofPackage(c):
        # StartofPackage=bytearray(0xAABBCCDD)
        sot = bytes.fromhex('AABBCCDD')
        conn.send(sot)

    counter = 0
    if conn != 0:
        while True:
            try:
                for file in dir_list:
                    if counter < len(dir_list)-1:
                        counter += 1
                        print('sending ' + str(counter))
                    else:
                        counter = 0
                        break

                    SendStartofPackage(counter)
                    imagestream = open("images/"+file, "rb")
                    print(file)
                    filesize = os.stat("images/"+file).st_size
                    fsize = filesize.to_bytes(4, byteorder='little')
                    print(str(filesize))

                    conn.send(fsize)

                    conn.send(imagestream.read(filesize))

                    time.sleep(0.175*3)
            except OSError as e:
                print(e)
                counter = 0
                Soket.listen()
                conn, addr = Soket.accept()

            # except ConnectionAbortedError:
            #     print("Connection aborted waiting for connection")
            #     counter = 0
            #     Soket.listen()
            #     conn, addr = Soket.accept()

            # except ConnectionResetError:
            #     print("Connection was forcibly closed by the remote host")
            #     counter = 0
            #     Soket.listen()
            #     conn, addr = Soket.accept()

            # except Exception as e:
            #     print(e)
