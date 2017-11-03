from socket import *
serverName = '10.148.2.148'
serverPort = 80
fo = open("logger.csv", "a+")
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
modifiedSentence = clientSocket.recv(1024)
fo.write(modifiedSentence);
fo.write("\n");
print 'From Server:', modifiedSentence
while(modifiedSentence != "END"):
	modifiedSentence = clientSocket.recv(1024)
	if(modifiedSentence != "END"):
		fo.write(modifiedSentence);
		fo.write("\n");
	print 'From Server:', modifiedSentence
fo.close();

po = open("logger2.csv", "a+")
modifiedSentence = clientSocket.recv(1024)
po.write(modifiedSentence);
po.write("\n");
print 'From Server:', modifiedSentence
while(modifiedSentence != "END"):
	modifiedSentence = clientSocket.recv(1024)
	if(modifiedSentence != "END"):
		po.write(modifiedSentence);
		po.write("\n");
	print 'From Server:', modifiedSentence
po.close();

zo = open("logger3.csv", "a+")
modifiedSentence = clientSocket.recv(1024)
zo.write(modifiedSentence);
zo.write("\n");
print 'From Server:', modifiedSentence
while(modifiedSentence != "END"):
	modifiedSentence = clientSocket.recv(1024)
	if(modifiedSentence != "END"):
		zo.write(modifiedSentence);
		zo.write("\n");
	print 'From Server:', modifiedSentence
zo.close();


clientSocket.close()