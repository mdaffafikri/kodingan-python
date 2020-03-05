import tkinter as tk

root = tk.Tk()
root.title("Judul")

warna_bg = "#111d4a"
warna_font = "white"

root.minsize(1280, 720)
root.configure(bg=warna_bg)

inilabel = tk.Label(root, 
		 text="Green Text in Helvetica Font",
		 fg = "white",
		 bg = warna_bg,
		 font = "Helvetica 16 bold",
         pady = +50)
inilabel.pack()

myword = "Great clouds all over the hills bringing darkness from above"
msg = tk.Message(root,
            text = myword
            )
msg.config(bg=warna_bg, fg= warna_font, font=("Times", 30, "italic"), width= 700)
msg.pack()

def pushed():
	global warna_font
	print(myword)
	if	warna_font=="white":
		warna_font="skyblue"

	elif warna_font=="skyblue":
		warna_font="white"
		#msg.config(fg = warna_font)
	msg.config(fg=warna_font)

b = tk.Button(root, 
		text="Push",
		command=pushed)
b.pack()

root.mainloop()