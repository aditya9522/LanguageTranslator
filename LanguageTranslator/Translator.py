import googletrans
from langdetect import detect
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyttsx3

root = Tk()
root.minsize(950,600)
root.maxsize(950,600)
root.title("Translator")
root.configure(bg="white")
source = StringVar()
destination = StringVar()
auto_source = IntVar()
auto_source.set(0)

top_title = Label(root, text="Language Translator", fg="white", bg="steel blue",font=("arial", 20, 'bold'), pady=10)
top_title.pack(side=TOP, fill=BOTH)

def translation():
    translator = googletrans.Translator()
    text = base_lan_text.get("1.0", "end-1c")
    if not text:                                                             # can also write text == ''       same meaning
        base_lan_text.configure(relief="solid", borderwidth=2, highlightbackground="red")
        messagebox.showerror("Error", "Please write something for translation!")
    else:
        base_lan_text.configure(highlightbackground="black", bg="light gray", relief="groove", borderwidth=1)

        auto_lan_detect()
        if auto_source.get():
            s = detect(text)
        else:
            s = lan_dict.get(source.get())

        d = lan_dict.get(destination.get())

        if not s:
            messagebox.showwarning("Warning", "Please select source language!")    
        elif not d:
            messagebox.showwarning("Warning", "Please select destination language!")
        else:
            trans_text = translator.translate(text, src=s, dest= d)
            translated_lan_text.delete("1.0", "end")
            translated_lan_text.insert("1.0", trans_text.text)

def speak_base():
    engine = pyttsx3.init()
    text = base_lan_text.get("1.0","end-1c")
    engine.say(text)
    engine.runAndWait()

def speak_trans():
    engine = pyttsx3.init()
    text = translated_lan_text.get("1.0","end-1c")
    engine.say(text)
    engine.runAndWait()

def auto_lan_detect():
    Auto_detect_lan = Checkbutton(root, text="Auto Detect Language", cursor="target", font=("arial", 11), background="white", activebackground="white", variable= auto_source, onvalue=True, offvalue= False)
    return Auto_detect_lan

def clear_base_lan_text():
    base_lan_text.delete("1.0", "end-1c")

lan_dict = googletrans.LANGCODES
languages = [lan for lan in lan_dict.keys()]
base_lan_box = ttk.Combobox(root, textvariable=source, cursor="hand2", font=("arial", 12, "bold"), values = languages, width=15)
base_lan_box.set("Select language")
base_lan_box.place(x=250, y=200)

to_lebel = Label(root, text= "To", font=("arial", 12, "bold"), bg="white")
to_lebel.place(x=470,y=200)

translated_lan_box = ttk.Combobox(root, textvariable=destination, cursor="hand2", font=("arial", 12, "bold"), values = languages, width=15)
translated_lan_box.set("Select language")
translated_lan_box.place(x=550, y=200)

# auto_source.set('')
auto_lan_detect().place(x=35, y=220)


base_lan_text = Text(root, fg="black",bg="white", font=("calibri", 15), borderwidth=1, relief="groove", background="light gray", highlightbackground="black", width=35, height=6, padx=10, pady=10)
base_lan_text.pack(side=LEFT, padx=20)

clear_button = Button(root, text="X", cursor="hand2",borderwidth=0,activebackground="light gray", pady=0, padx=0, bg="light gray", command= clear_base_lan_text)
clear_button.place(x=358, y=2, in_=base_lan_text, bordermode="outside")

speaker_button_base_lan = Button(root, text="📢", cursor="hand2", font=("calibri", 18, 'bold'), bg="white", borderwidth=0, command= speak_base)
speaker_button_base_lan.place(x=45, y=410)

translated_lan_text = Text(root,fg="black",bg="white", font=("calibri", 15), borderwidth=1, relief="groove", background="light gray", highlightbackground="black", width=35, height=6, padx=10, pady=10)
translated_lan_text.pack(side=RIGHT, padx=20)

speaker_button_translated_lan = Button(root, text="📢", cursor="hand2",font=("calibri", 18, 'bold'), bg="white", borderwidth=0, command= speak_trans)
speaker_button_translated_lan.place(x=590, y=410)

translate_button = Button(root, text="Translate", cursor="hand2", fg="black",bg="white", font=("arial", 12, "bold"), command= translation)
translate_button.place(x=430, y=310)

footer_data = Label(root, text = "Language Translator | copyright ©, All Rights Reserved." , width=80, bg = "steel blue", fg = "white", font = ('Times New Roman', 15,'bold'), pady=10) 
footer_data.place(x=0, y=555)
root.mainloop()