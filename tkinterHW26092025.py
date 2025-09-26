from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

root= Tk()
root.title("Codingal's Text Editor ")
root.geometry("600x500")
root.rowconfigure(0,minsize=800,weight=1)
root.columnconfigure(1,minsize=800,weight=1)


def open_file():

    fileaddress= askopenfilename(
        filetypes=[("Text Files","*.txt"),("All Files","8_+")]
    )
    if not fileaddress:
        return
    text_editing.delete(1,0,END)
    with open(fileaddress,"r") as input_file:
        text=input_file.read()
        text_editing.insert(END,text)
        input_file.close()
    root.title(f"Codingal's Text Editor- {fileaddress}")
def save_file():
    filepath=asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt"),("All Files","*.*")],
    )
    if not filepath:
        return
    with open(filepath,"w") as output_file:
        text=text_editing.get(1.0,END)
        output_file.write(text)
    root.title(f"Codingal's Text Editor - {filepath}")   
text_editing= Text(root) 
button=Frame(root,relief=RAISED,bd=2)
button_open =Button(button,text="Open",command=open_file)
button_save =Button(button,text="Save As....",command=save_file)
button_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
button_save.grid(row=1,column=0,sticky="ew",padx=5)
button.grid(row=0,column=0,sticky="ns")
text_editing.grid(row=0,column=1,sticky="nsew")
root.mainloop()
    