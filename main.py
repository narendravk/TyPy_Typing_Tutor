#Typing Tutor Program With tkinter GUI

#Imports
import tkinter as tk
from time import perf_counter
from fetch_data import fetch_data,setup_game,record_high_score
from tkinter import messagebox, simpledialog


score = 0
wpm_list = []
wpm_avg = 0
round = 0


#Runtime
window=tk.Tk()
window.title("TyPy Typing Tutor")
window.geometry("900x500")
window.configure(bg="slate gray")
frame=tk.Frame()
frame.configure(borderwidth=10,bg="PeachPuff3")
frame.grid(row=0,column=0,padx=20,pady=20)

player_name = simpledialog.askstring("TyPy Tutor","Hey, welcome! What's your name?")

saved_data = setup_game(player_name=player_name)

screen_text=tk.Label(frame,font=("Arial",14,"normal"),width=75,bg="black",fg="white",text="Click on 'Start' button!",justify="center",height=3)
screen_text.grid(row=0,column=0,columnspan=2)

screen_input=tk.Entry(frame,font=("Arial",14,"normal"),width=75,bg="white",fg="black",justify="center")
screen_input.grid(row=1,column=0,columnspan=2)

def check_accuracy(start_time):
    global score
    global wpm_avg
    para_text = screen_text.cget("text")
    type_text = screen_input.get()
    if type_text == para_text:
        end_time = perf_counter()
        time_lapsed = end_time - start_time
        words_list = type_text.split(" ")
        wpm = len(words_list) * 60 // time_lapsed
        wpm_list.append(wpm)
        score += 1
        wpm_avg = int(sum(wpm_list) // len(wpm_list))
        user_action = messagebox.askyesno(title="TyPy Tutor", message=f"Nice, your typing speed was {int(wpm)} words per minute\n Do you want to continue?")
        if user_action == 0:
            pass
        elif user_action == 1:
            start()
        refresh_view()
        record_high_score(player_name,wpm)
        return wpm
    else:
        window.after(1000, check_accuracy,start_time)

def get_wpm(window):
    screen_input.select_range("0","end")
    screen_input.focus_set()
    start_time=perf_counter()
    wpm = check_accuracy(start_time)

def start():
    screen_text.configure(text=fetch_data())
    global round
    round+=1
    screen_input.delete(0,"end")
    screen_input.insert("end","Press Enter & start typing the sentence!")

def quit():
    window.destroy()

def refresh_view():
    wpm_label.configure(text=f"WPM Score: {wpm_avg}")
    score_label.configure(text=f"Score: {score}")
    level_label.configure(text=f"Round: {round}")

score_label=tk.Label(frame,text=f"SCORE: {score}",font=("Courier",14,"bold"),justify="left")
score_label.grid(column=0,row=2,padx=2,pady=10)

level_label=tk.Label(frame,text=f"Round: {round}",font=("Courier",14,"bold"),justify="left")
level_label.grid(column=0,row=3,padx=2,pady=10)

wpm_label=tk.Label(frame,text=f"WPM Score: {wpm_avg} ",font=("Courier",14,"bold"),justify="left")
wpm_label.grid(column=1,row=2,padx=2,pady=10)

name_label=tk.Label(frame,text=f"Player: {player_name} ",font=("Courier",14,"bold"),justify="left")
name_label.grid(column=1,row=3,padx=2,pady=10)

avgscore_label=tk.Label(frame,text=f"Avg. WPM: {wpm_avg} ",font=("Courier",14,"bold"),justify="left")
avgscore_label.grid(column=0,row=4,padx=2,pady=10, columnspan=2)

hscore_label=tk.Label(frame,text=f"Highest Score:{saved_data[1]} WPM ",font=("Courier",14,"bold"),justify="left")
hscore_label.grid(column=0,row=5,padx=2,pady=10)

hsname_label=tk.Label(frame,text=f"Highest Scorer:{saved_data[0]}",font=("Courier",14,"bold"),justify="left")
hsname_label.grid(column=1,row=5,padx=2,pady=10)

start_button = tk.Button(frame,text="Start",command=start,font=("Courier",14,"bold"),bg="darkorange")
start_button.grid(column=0,row=9,padx=10,pady=10)

start_button = tk.Button(frame,text="Quit",command=quit,font=("Courier",14,"bold"),bg="darkorange")
start_button.grid(column=1,row=9,padx=2,pady=10)

window.bind("<Return>",get_wpm)

footer_label=tk.Label(frame,text="This porgram is created by Narendra Kashikar. \n Visit me at http://narendrakashikar.life",font=("Tahoma",10,"bold"),justify="center")
footer_label.grid(column=0,row=10,padx=2,pady=20,columnspan=2)

window.mainloop()

