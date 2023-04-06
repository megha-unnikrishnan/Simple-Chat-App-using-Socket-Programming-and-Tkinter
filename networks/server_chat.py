import socket
from tkinter import *

root = Tk()
root.geometry("550x350")

def send( listbox , entry ):
    message = entry.get()
    listbox.insert('end',"server:" + message)
    entry.delete(0, END)
    client.send(bytes(message, 'utf-8'))

def receive(listbox):
    message_to_client = client.recv(200)
    listbox.insert('end',"client:" + message_to_client.decode('utf-8'))


entry = Entry( width=40)
entry.pack(side=BOTTOM)

listbox = Listbox(root,height = 10,width = 50,activestyle = 'dotbox',font = "Helvetica" , fg = "red")
listbox.pack()

button = Button(root, text='send', command=lambda: send(listbox, entry))
button.pack(side=BOTTOM,pady=5)

rbutton = Button(root, text='Receive', command=lambda: receive(listbox))
rbutton.pack(side=BOTTOM,pady=5)

root.title("SERVER")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 4010
s.bind((HOST_NAME, PORT))
s.listen(4)
client, address = s.accept()
root.mainloop()
