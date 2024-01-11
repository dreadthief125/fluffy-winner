import socket
from threading import Thread
import random
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_aderess='127.0.0.1'
port=8000
server.bind((ip_aderess,port))
server.listen()
list_of_clients=[]
questions = [" What is the average iq of a human?\n a.120\n b.105\n c.100\n d.110",
             "who is the founder of tesla? \n a.Elon Musk\n b. Stephan Hawking\n c. Jeff Bezos\n d.Ulyssyus. S Grant",
             "Which amendment states that you have freedom of speech?\n a.1st\n b.4th\n c.12th\n d.2nd",
             "What contenent contains the country Chad?\n a.Asia\n b.South America\n c. Europe\n d. Africa",
             "Where is the tallest mountain range located in?\n a.India\n b.Taiwan\n c.Russia\n d.Equador",
             "What extinct birds name starts in a D?\n a.Dovekie\n b. Dusky Grouse\n c.Dodo\n d.Dark-Billed Cuckoos",
             "What country has the most world cup wins?\n a.Brazil\n b.Morroco\n c.Argentina\n d. Germany"
]
answers=["c","a","d","a","c","a"]
def getQAnswer(conn):
  random_index=random.randint(0,len(questions)-1)
  random_question=questions[random_index]
  random_answer=answers[random_index]
  conn.send(random_question.encode('utf-8'))
  return random_index,random_question,random_answer
def removeQ(index):
  questions.pop(index)
  answers.pop(index)
def clientthread(conn):
  score=0
  conn.send("Welcome to the amazing digital trivia!".encode('utf-8'))
  conn.send("I am your quizmaker, SAIPM. You will recive a question. The answer is either a,b,c, or d".encode('utf-8'))
  conn.send("Good Luck!\n\n".encode('utf-8'))
  index,question,answer = getQAnswer(conn)
  while True:
    try:
      message=conn.recv(2048).decode('utf-8')
      if message:
        if message.lower()==answer:
          score+=1
          conn.send(f"Congrats! Your score is {score}\n\n".encode('utf-8'))
        else:
          conn.send("Incorrect D: Better luck next time!\n\n".encode('utf-8'))
        removeQ(index)
        index,question,answer=getQAnswer(conn)
    except:
      continue
while True:
  conn,addr=server.accept()
  list_of_clients.append(conn)
  print(addr[0]+'HAS CONNECTED.')
  new_thread=Thread(target=clientthread,args=(conn,addr))
  new_thread.start()