import socket
import time
#=========================================================
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 20002))
s.listen()
print('Start')
#=========================================================
id = ''

#=========================================================
conn, addr = s.accept()
#=========================================================
def comanda_fun(test):
    
    if test == '0x1001':
        conn.send(b'\x04\x00\x01\x10')
    elif test == '0x10ed':
        id = pismo[4:]
        print('айди-',id)
    elif test == '0x10cc':
        coord = pismo[4:]
        print('коордитаты-',coord)
    elif test == '0x1055':
        conn.send(b'$\x00\x01\x10U\x10http://45.9.43.62/firmware.bin'
0x6e69622e657261776d7269662f32362e33342e392e35342f2f3a70747468105510010024)
#=========================================================
while True:
    print('Connacted -', addr)
    pismo = conn.recv(4096)
    try:
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        dlin= int.from_bytes(pismo[0:2],byteorder="little")
        comm= list(pismo[2:4])
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        test = (hex(comm[1]) + hex(comm[0]))
        test = test[0:4]+test[6:]
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        comanda_fun(test)
        print(test)

        if not test == '0x1001':
            conn.send(b'\x04\x00\x01\x10')
    except:
        #conn.send(b'\x04\x00\xff\x10')
        print('ошибочка')
    time.sleep(5)
#=========================================================