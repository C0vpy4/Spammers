from tkinter import *
from tkinter.ttk import Combobox 
from tkinter import ttk
from tkinter import messagebox
import tkinter
from tkinter.ttk import Progressbar
import requests
from time import sleep

global entry_auth_id
global entry_chat_id
entry_auth_id = 'ENTER'
entry_chat_id = 'ENTER'

even_numbers=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]

#-----------------DEFS-----------------------------------------

count_auth_id_clicks = 0
def get_auth_id():
   global count_auth_id_clicks
   count_auth_id_clicks+=1
   if count_auth_id_clicks not in  even_numbers:
      fix_auth_id = "Authorization code:{}".format(entry_auth_id)
      text.configure(text=fix_auth_id)
      btn_auth_id.configure(text='Hide')
      btn_auth_id.configure(background="red")
   else:
    fix_auth_id = "Authorization code:"
    text.configure(text=fix_auth_id)
    btn_auth_id.configure(text='Show')
    btn_auth_id.configure(background="green")

count_chat_id_clicks = 0
def get_chat_id():
    global count_chat_id_clicks
    count_chat_id_clicks+=1
    if count_chat_id_clicks not in even_numbers:
        fix_chat_id = "Chat id:{}".format(entry_chat_id)
        text_chat_id.configure(text=fix_chat_id)
        btn_chat_id.configure(text='Hide')
        btn_chat_id.configure(background="red")
    else:
        fix_chat_id = "Chat id:"
        text_chat_id.configure(text=fix_chat_id)
        btn_chat_id.configure(text="Show")
        btn_chat_id.configure(background="green")    

def get_ranger():
    global range_amount
    range_amount = rang_amount_entry.get()   

def get_user_text():
    global user_text
    global koll
    koll =5
    user_text = entry_user_text.get() 

def destroy_window():
    window.destroy()
kollvo=0
def go_progress():
    global kollvo
    btn_start.configure(bg="gray")
    btn_start.configure(state=DISABLED)
    kollvo+=1
    
    while bar["value"]<100:
        bar["value"]+= 10
        window_start.update()
        sleep(0.5)
    if bar["value"]==100:
        btn_start.configure(state=ACTIVE)
    if kollvo == 2:
        window_start.destroy() 
          
      
#-----------------TK2-----------------------------------------
window_start = Tk()
window_start.eval('tk::PlaceWindow . center')
window_start.overrideredirect(1)
window_start.attributes('-toolwindow', True)
window_start.resizable(0,0) 
window_start.title('LOADING')
window_start.geometry('800x285')
window_start.resizable(width=0, height=0)


#-----------------PROGRESS------------------------------------
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')
bar = Progressbar(window_start, length=300, style='black.Horizontal.TProgressbar')  
bar['value'] = 0  
bar.place(relx=0.5, rely=0.5,anchor=CENTER )




btn_start = Button(window_start, text="START", font="Verdana", command=go_progress)
btn_start.place(relx=0.5, rely=0.6,anchor=CENTER)


text_start = Label(window_start, text='SPAMMER FOR DISCORD',bg="gray22",font="Distant",fg='#d00000', )
text_start.grid(column=0, row=3)
text_start.place(relx=0.5, rely=0.3,anchor=CENTER)

#--------------RGB---------------------------------
try:

        window_start["bg"] = "#CD5C5C"
        window_start.update()
        sleep(0.9)
        window_start["bg"] = "#F08080"
        window_start.update()
        sleep(0.9)
        window_start["bg"] = "#FA8072"
        window_start.update()
        sleep(0.9)
        window_start["bg"] = "#E9967A"
        window_start.update()
        sleep(0.9)
        window_start["bg"] = "#FFA07A"
        window_start.update()
        sleep(0.9)
        window_start["bg"] = "#DC143C"
        window_start.update()
        sleep(0.9)
        window_start["bg"] = "#FF0000"
        window_start.update()
        sleep(0.9)
        window_start["bg"] = "#B22222"
        window_start.update()
        sleep(0.9)
        window_start["bg"] = "#8B0000"
        window_start.update()
        sleep(0.9)    
except:
    pass

        





window_start.mainloop()

#-----------------TK------------------------------------------
window = Tk()
window.eval('tk::PlaceWindow . center')
#first_window = tkinter.Toplevel(window)
#window.eval(f'tk::PlaceWindow {str(first_window)} center')
window.overrideredirect(1)
window.attributes('-toolwindow', True)
window.resizable(0,0) 
window.title('SPAMMER')
window.geometry('800x285')
window.resizable(width=0, height=0)

window["bg"] = "gray22"


#window.attributes('-fullscreen', True)

#--------------Support_1--------------------------------------
support_text_one = Label(window, text="YIUYyuuu",height=1, bg="#9c0000",font='AcmeFont',fg='#9c0000')
support_text_one.place(relx=0.36, rely=0.5,anchor=CENTER)

support_text_two = Label(window, text="YIUYyq",height=1, bg="#9c0000",font='AcmeFont',fg='#9c0000')
support_text_two.place(relx=0.37, rely=0.6,anchor=CENTER)

#-----------------LABELS--------------------------------------
text = Label(window, text='Authorization code:', bg="gray22",font="Bookman",fg='#d00000')
text.grid(column=0, row=0)
text.place(relx=0.5, rely=0.1,anchor=CENTER)

text_chat_id = Label(window,text='Chat id:', bg="gray22",font="Bookman",fg='#d00000')
text_chat_id.grid(column=0, row=1)
text_chat_id.place(relx=0.5, rely=0.3,anchor=CENTER)

text_user = Label(window,text='Your word:', bg="gray22",font="Bookman",fg='#d00000')
text_user.grid(column=0, row=2)
text_user.place(relx=0.36, rely=0.5,anchor=CENTER)
#rgb(115, 255, 255);
text_range = Label(window, text='Range:',bg="gray22",font="Bookman",fg='#d00000', )
text_range.grid(column=0, row=3)
text_range.place(relx=0.37, rely=0.6,anchor=CENTER)



#-----------------ENTRY----------------------------------------
rang_amount_entry = Combobox(window)  
rang_amount_entry['values'] = (1, 2, 3, 4, 5)  
rang_amount_entry.current(1)   
rang_amount_entry.grid(column=1, row=3)
rang_amount_entry.place(relx=0.51, rely=0.6,anchor=CENTER)


entry_user_text = Entry(window, width=23)
entry_user_text.grid(column=1,row=2)
entry_user_text.place(relx=0.51, rely=0.5,anchor=CENTER)





#-----------------BUTTONS--------------------------------------

btn_auth_id = Button(window, text="Show",background="green",foreground="#ccc", font="Verdana", command=get_auth_id)
btn_auth_id.place(relx=0.5, rely=0.2,anchor=CENTER)

btn_chat_id = Button(window, text="Show",background="green",foreground="#ccc", font="Verdana", command=get_chat_id)
btn_chat_id.place(relx=0.5, rely=0.4,anchor=CENTER)

btn_user_text = Button(window, text="Ok", font="Verdana", command=get_user_text)
btn_user_text.place(relx=0.64, rely=0.5,anchor=CENTER)

btn_range = Button(window, text="Ok", font="Verdana", command=get_ranger)
btn_range.place(relx=0.64, rely=0.6,anchor=CENTER)

btn_destroy = Button(window, text="Go",background="red",foreground="#ccc",font="Verdana",command=destroy_window)
btn_destroy.place(relx=0.5, rely=0.8, anchor=CENTER)








window.mainloop()




header = {
    'authorization': entry_auth_id
    }
payload = {
    'content': user_text
    }

range = int(range_amount)
while range > 0:
    range-=1
    r = requests.post(entry_chat_id,data=payload, headers=header)
