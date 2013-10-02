import Tkinter
import pySphereClient

def ende():
	main.destroy()

def callback(server,username,password,vmname):
	print "clicked!"
	server = e.get()
	username = e1.get()
	password = e2.get()
	vmname = vme.get()
	print server, username, password, vmname
	result = pySphereClient.viConnect(server,username,password,vmname)
	print result['name']
	for a in result:
		listbox.insert(0,result[a])

main = Tkinter.Tk()
main.title("pySphere Client")
main.minsize(400,300)

server = "192.168.219.129"
username = "root"
password = "vmware"
vmname = ""

frame = Tkinter.Frame(main)

lb1 = Tkinter.Label(frame, text = "server: ")
lb1["font"] = "Arial 11 normal"
lb1["justify"] = "left"
lb1.pack(side="left")

e = Tkinter.Entry(frame, width=30)
e.insert(0,server)
e.pack()

frame.pack()
frame1 = Tkinter.Frame(main)

lb2 = Tkinter.Label(frame1, text = "username: ")
lb2["font"] = "Arial 11 normal"
lb2.pack(side="left")

e1 = Tkinter.Entry(frame1, width=30)
e1.insert(0,username)
e1.pack()

frame1.pack()
frame2 = Tkinter.Frame()

lb3 = Tkinter.Label(frame2, text = "password: ")
lb3["font"] = "Arial 11 normal"
lb3.pack(side="left")

e2 = Tkinter.Entry(frame2, width=30, show="*")
e2.insert(0,password)
e2.pack(side="right")

frame2.pack()

search = Tkinter.Frame()

vml = Tkinter.Label(search, text = "VM to search: ")
vml["font"] = "Arial 11 normal"
vml.pack(side="left")

vme = Tkinter.Entry(search, width=30)
vme.pack()

search.pack()

frame3 = Tkinter.Frame(main)

a = Tkinter.Button(frame3, text = "Submit", command = lambda: callback(server,username,password,vmname))
a.pack(side="left")

b = Tkinter.Button(frame3, text = "Ende", command = ende)
b.pack(side="right")

frame3.pack()
frame4 = Tkinter.Frame(main)

lb4 = Tkinter.Label(frame4)
lb4.pack()

listbox = Tkinter.Listbox(main, width=70)
listbox.pack(padx=3,pady=3)

frame4.pack()

main.mainloop()
