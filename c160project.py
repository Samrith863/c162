from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import messagebox
import os
root=Tk()
root.title("NotePad")
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background="yellow")

label1=Label(root,text="File Name")
input_1=Entry(root)
text_area=Text(root,height=35,width=80)

name=""
def openFile():
    global name
    text_area.delete(1.0,END)
    input_1.delete(0,END)
    file_path=filedialog.askopenfilename(title="Open Files",filetypes=(("text files","*.txt"),))
    print(file_path)
    file_basename=os.path.basename(file_path)
    print(file_basename)
    file_format=file_basename.split('.')[0]
    input_1.insert(END,file_format)
    root.title(file_format)
    text_file=open(file_basename,'r')
    paragraph=text_file.read()
    text_area.insert(END,paragraph)
    text_file.close()
    
def closeWindow():
    root.destroy()
                  


def saveFile():
    file_name=input_1.get()
    open_file=open(file_name+".txt","w")
    value_textarea=text_area.get("1.0",END)
    print(value_textarea)
    open_file.write(value_textarea)
    input_1.delete(0,END)
    text_area.delete(1.0,END)
    messagebox.showinfo("Update!","File Saved: Successfully!")
    
    

                       
open_btn=Button(root,text="Open",command=openFile)
close_btn=Button(root,text="Close",command=closeWindow)
save_btn=Button(root,text="Save",command=saveFile)
close_btn.place(relx=0.20,rely=0.03,anchor=CENTER)
save_btn.place(relx=0.15,rely=0.03,anchor=CENTER)
open_btn.place(relx=0.11,rely=0.03,anchor=CENTER)

label1.place(relx=0.28,rely=0.03,anchor=CENTER)
input_1.place(relx=0.46,rely=0.03,anchor=CENTER)
text_area.place(relx=0.5,rely=0.55,anchor=CENTER)
root.mainloop()

