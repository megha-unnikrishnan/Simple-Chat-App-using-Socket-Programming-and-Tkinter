import socket
from tkinter import *

root = Tk()

root.geometry("550x350")
def send( listbox , entry ):
    message = entry.get()
    listbox.insert('end', "client:" +message)
    entry.delete(0, END)
    s.send(bytes(message, 'utf-8'))
def receive(listbox):
    message = s.recv(200)
    listbox.insert('end',"server:" + message.decode('utf-8'))


entry = Entry( width=40)
entry.pack(side=BOTTOM)

listbox = Listbox(root,height = 10,
                  width = 50,

                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "red")
listbox.pack()

button = Button(root, text='send', command=lambda: send(listbox, entry))
button.pack(side=BOTTOM,pady=5)

rbutton = Button(root, text='Receive', command=lambda: receive(listbox))
rbutton.pack(side=BOTTOM,pady=5)

root.title("CLIENT")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 4010
s.connect((HOST_NAME, PORT))
root.mainloop()
