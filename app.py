import tkinter as tk
from tkinter import filedialog
import tkinter.scrolledtext
from tkinter.ttk import *
from LSBAudioStego import LSBAudioStego


root = tk.Tk()


# create window using from in Tkinter
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)
        # reference to the master widget, which is the tk window
        self.master = master
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Audio Steganography")
        self.Enocoding()
        self.Decoding()



    def Enocoding(self):
        # encode Label
        self.encodeVar = tk.StringVar()
        self.encodelabel = Label(root, textvariable=self.encodeVar, font=('open sans', 26,'bold'), relief='flat', background='#A83EB8', foreground='white', padding=8)
        self.encodelabel.place(x=20, y=50)
        self.encodeVar.set("ENCODE")

        # creating a button instance
        self.selectFileButton = tk.Button(root,image=dwnd,borderwidth=0, highlightthickness=0, bd=0, background='#662CCA', command=self.selectFile)
        self.selectFileButton.place(x=20, y=140)

        # file location label
        self.var = tk.StringVar()
        self.label = Label(root, textvariable=self.var)
        self.label.place(x=20, y=185)

        # entry box
        self.textBox = tk.scrolledtext.ScrolledText(root, height=10, width=45)
        self.textBox.insert('insert',"Enter secret message.")
        self.textBox.place(x=20, y=230)

        # encode Button
        self.encodeButton = tk.Button(root, image=dwnd_en, borderwidth=0, highlightthickness=0, bd =0, background='#662CCA', command=self.encode)
        self.encodeButton.place(x=20, y=450)

        # encoded  location label
        self.enocdedLocation = tk.StringVar()
        self.locationOfEncodeFile = Label(root, textvariable=self.enocdedLocation)
        self.locationOfEncodeFile.place(x=20, y=420)

    def retrieve_input(self):
            inputValue = self.textBox.get("1.0", "end-1c")
            print(inputValue)
            return inputValue

    def Decoding(self):
        # decode Label
        self.decodeVar = tk.StringVar()
        self.decodelabel = Label(root, textvariable=self.decodeVar, font=('open sans', 26,'bold'), relief='flat', background='#A83EB8', foreground='white', padding=8)
        self.decodelabel.place(x=500, y=50)
        self.decodeVar.set("DECODE")


        # creating a button instance
        self.selectFileDecodeButton = tk.Button(root, image=dwnd_decode, borderwidth=0, highlightthickness=0, bd=0, background='#662CCA', command=self.selectFileDecode)
        self.selectFileDecodeButton.place(x=500, y=140)

        # file location label
        self.decodeFileVar = tk.StringVar()
        self.decodeFileLabel = Label(root, textvariable=self.decodeFileVar)
        self.decodeFileLabel.place(x=500, y=185)

        #decode button
        self.decodeButton = tk.Button(root, image=dwnd_de,borderwidth=0, highlightthickness=0, bd=0, background='#662CCA', command=self.decode)
        self.decodeButton.place(x=500, y=450)

        # decoded text label
        self.decodedString = tk.StringVar()
        self.textBox_decode= tk.scrolledtext.ScrolledText(root, height=10, width=45)
        self.textBox_decode.place(x=500, y=230)


    def selectFile(self):
        # file selection
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("jpeg files", "*.wav"), ("all files", "*.*")))
        self.fileSelected = root.filename
        self.var.set(root.filename)

    def selectFileDecode(self):
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("jpeg files", "*.wav"), ("all files", "*.*")))
        self.fileSelcetedForDecode = root.filename
        self.decodeFileVar.set(root.filename)

    def encode(self):
        # select algo to encode
        algo = LSBAudioStego()
        result = algo.encodeAudio(self.fileSelected, self.retrieve_input())
        self.enocdedLocation.set(result)

    def decode(self):
        # select algo to decode
        algo = LSBAudioStego()
        result = algo.decodeAudio(self.fileSelcetedForDecode)
        self.decodedString.set(result)
        self.textBox_decode.insert(tk.END, result)


# resolution
root.geometry("900x700")

#set background color
root.config(bg='#49A')


bg = tk.PhotoImage(file = "C:\\Users\\Pemila\\Downloads\\backimg.png")
background_label = Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


dwnd = tk.PhotoImage(file='C:\\Users\\Pemila\\Downloads\\button_select-file-to-encode.png')
dwnd_decode = tk.PhotoImage(file='C:\\Users\\Pemila\\Downloads\\button_select-file-to-decode.png')
dwnd_en = tk.PhotoImage(file='C:\\Users\\Pemila\\Downloads\\button_encode.png')
dwnd_de = tk.PhotoImage(file='C:\\Users\\Pemila\\Downloads\\button_decode.png')


# creation of an instance of window
app = Window(root)

# mainloop
root.mainloop()