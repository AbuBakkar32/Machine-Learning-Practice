from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os, socket

ip = socket.gethostbyname(socket.gethostname())
os.chdir('F:\\ftp')
address = (ip,21)
authorier = DummyAuthorizer()
authorier.add_user('AbuBakkar', 'AbuBakkar32', '', perm='elradfmw')

handler = FTPHandler
handler.authorizer = authorier
server = FTPServer(address, handler)
server.serve_forever()