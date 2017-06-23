# wizard GUI
import nicoController as control

from Tkinter import *

#create the window
root = Tk()

#modify root window
root.title("Wizard GUI")
#sets the width/height of window
root.geometry("500x465")

def main():

	def call(code):
		cmd = str(code)
		control.sendCmd(cmd) 

	#Buttons for every built-in dialog option

	# greetings
	greetings = Label(root, text = "Greetings")
	greetings.grid(row = 0, column = 1)

	b1 = Button(root, text = 'Hi!', command = lambda: call(1), width = 17)
	b1.grid(row = 1,column = 0)

	b16 = Button(root, text = 'I\'m excited!', command = lambda: call(16), width = 17)
	b16.grid(row = 1,column = 1)

	b20 = Button(root, text = 'I want to solve this', command = lambda: call(20), width = 17)
	b20.grid(row = 1,column = 2)


	# prompting the user to go on
	goOn = Label(root, text = "Go On")
	goOn.grid(row = 2,column = 1)

	b18 = Button(root, text = 'Okay!', command = lambda: call(18), width = 17)
	b18.grid(row = 3)

	b2 = Button(root, text = 'How do you solve this?', command = lambda: call(2), width = 17)
	b2.grid(row = 3,column = 1)

	b5 = Button(root, text = 'What\'s next?', command = lambda: call(5), width = 17)
	b5.grid(row = 3,column = 2)

	b8 = Button(root, text = 'How do we do that?', command = lambda: call(8), width = 17)
	b8.grid(row = 4)

	b13 = Button(root, text = 'Nevermind, go on.', command = lambda: call(13), width = 17)
	b13.grid(row = 4,column = 1)

	# Math
	mathL = Label(root, text = "Math")
	mathL.grid(row = 5,column = 1)

	b3 = Button(root, text = 'We multiply?', command = lambda: call(3), width = 17)
	b3.grid(row = 6)

	b19 = Button(root, text = 'We divide?', command = lambda: call(19), width = 17)
	b19.grid(row = 6,column = 1)

	b4 = Button(root, text = 'We add?', command = lambda: call(4), width = 17)
	b4.grid(row = 6,column = 2)

	b21 = Button(root, text = 'How\'d we get that #?', command = lambda: call(21), width = 17)
	b21.grid(row = 7)

	# ask for explanation
	explain = Label(root, text = "Ask for explanation")
	explain.grid(row = 8,column = 1)

	b7 = Button(root, text = 'That was a lot.', command = lambda: call(7), width = 17)
	b7.grid(row = 9)

	b11 = Button(root, text = 'Seems complicated.', command = lambda: call(11), width = 17)
	b11.grid(row = 9,column = 1)

	b12 = Button(root, text = 'Explain that again?', command = lambda: call(12), width = 17)
	b12.grid(row = 9,column = 2)

	b15 = Button(root, text = 'Don\'t know. Hint?', command = lambda: call(15), width = 17)
	b15.grid(row = 10)

	# endro
	endL = Label(root, text = "End Interaction")
	endL.grid(row = 11,column = 1)

	b6 = Button(root, text = 'I understand now', command = lambda: call(6), width = 17)
	b6.grid(row = 12)

	b9 = Button(root, text = 'Solved the problem!', command = lambda: call(9), width = 17)
	b9.grid(row = 12,column = 1)

	b10 = Button(root, text = 'Thank you!', command = lambda: call(10), width = 17)
	b10.grid(row = 12,column = 2)

	b14 = Button(root, text = 'Getting tired. Later?', command = lambda: call(14), width = 17)
	b14.grid(row = 13)

	#Misc
	other = Label(root, text = "Other")
	other.grid(row = 14,column = 1)

	b17 = Button(root, text = 'Green paint?', command = lambda: call(17), width = 17)
	b17.grid(row = 15,column = 1)

	# Make Nico turn his head to face forward
	b0 = Button(root, text = "Face forward", command = lambda: call(0), width = 17)
	b0.grid(row = 15)

	# Enter anything for Nico to say
	eLabel =  Label(root,text = "Enter text:")
	eLabel.grid(row = 16)
	entry = Entry()
	entry.grid(row = 16,column = 1)

	eText = ""

	def onclick(event = None):
		eText = entry.get()
		call(eText)
		entry.delete(0,END)

	root.bind('<Return>', onclick)

	button = Button(root, text = "Enter", command = onclick, width = 17)
	button.grid(row = 16,column = 2)

	# End the program immediately.
	bEnd = Button(root, text = "End program", command = exit, width = 17, bg = 'red')
	bEnd.grid(row = 17, column = 1)

	#kick off the event loop
	root.mainloop()

if __name__ ==  "__main__":
	main()
	"""
	filepath = "/home/nao/programs/move.top"
	#ad.main()
	args = shlex.split('python adialog_new.py')
	#subprocess.Popen(["python", "adialog_new.py"])
	p = subprocess.call(['gnome-terminal', '-x', 'bash', '-c','python adialog.py'])
	#Thread(target = func2).start()
	subprocess.kill()
	"""