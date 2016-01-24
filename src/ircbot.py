import socket
import sys

server = "irc.freenode.org"       #settings
channel = "#alextest"
botnick = "bottest"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print "connecting to:"+server
irc.connect((server, 6667))                                                         #connects to the server
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This is a fun bot!\n") #user authentication
irc.send("NICK "+ botnick +"\n")                            #sets nick
irc.send("PRIVMSG nickserv :iNOOPE\r\n")    #auth
irc.send("JOIN "+ channel +"\n")  
while True:
   data = irc.recv ( 4096 )
   if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
   if data.find ( '!botty quit' ) != -1:
      irc.send ( 'QUIT\r\n' )
   if data.find ( 'hi botty' ) != -1:
      irc.send ( 'PRIVMSG #paul :I already said hi...\r\n' )
   if data.find ( 'hello botty' ) != -1:
      irc.send ( 'PRIVMSG #paul :I already said hi...\r\n' )
   if data.find ( 'KICK' ) != -1:
      irc.send ( 'JOIN #paul\r\n' )
   if data.find ( 'cheese' ) != -1:
      irc.send ( 'PRIVMSG #paul :WHERE!!!!!!\r\n' )
   if data.find ( 'slaps botty' ) != -1:
      irc.send ( 'PRIVMSG #paul :This is the Trout Protection Agency. Please put the Trout Down and walk away with your hands in the air.\r\n' )
   print data