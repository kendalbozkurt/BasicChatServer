import socket
import threading

host=''
port=8000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(10)

print "Server Started..."
class myThread(threading.Thread):
	def __init__(self,connection,addr):
		threading.Thread.__init__(self)
		self.connection=connection
		self.addr=addr
	def run(self):		
		while True:
			try:
				data=self.connection.recv(1024)
				if "Quit" in str(data):
					break
				print "send by "+self.addr[0]+":"+data
			except:
				pass
# gelen connectionlara gore threadlar olusturuyorum
while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    t=myThread(conn,addr)
    t.start()
s.close()
