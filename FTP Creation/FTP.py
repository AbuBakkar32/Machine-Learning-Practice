from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os, socket

ip = socket.gethostbyname(socket.gethostname())
os.chdir('F:\\')
address = (ip, 21)
authorier = DummyAuthorizer()
authorier.add_user('AbuBakkar', 'AbuBakkar32', 'E://', perm='elradfmwMT', msg_login="Login successful.",
                   msg_quit="Goodbye.")

handler = FTPHandler
handler.authorizer = authorier
server = FTPServer(address, handler)
server.serve_forever()
