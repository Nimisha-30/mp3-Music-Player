from pygame import mixer
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd 
from PIL import ImageTk, Image
import os

def play():
    currentSong=playlist.get(ACTIVE)
    print(currentSong)
    mixer.music.load(currentSong)
    songstatus.set("Playing..")
    mixer.music.play()

def pause():
    songstatus.set("Paused..")
    mixer.music.pause()

def resume():
    songstatus.set("Resuming..")
    mixer.music.unpause()

def stop():
    songstatus.set("Stopped..")
    mixer.music.stop()

def forward():
    nextsong=playlist.curselection()
    nextsong=nextsong[0]+1
    currentsong=playlist.get(nextsong)
    if(currentsong==''):
        nextsong=0
        currentsong=playlist.get(nextsong)
    print(currentsong)
    mixer.music.load(currentsong)
    mixer.music.play()

    playlist.selection_clear(0,END)
    playlist.activate(nextsong)#highlighing next song
    playlist.selection_set(nextsong,last=None)
    
def backward():
    prevsong=playlist.curselection()
    print(prevsong)
    prevsong=prevsong[0]-1
    currentsong=playlist.get(prevsong)
    if(currentsong==''):
        i=-1
        for s in songs:
            i=i+1
            
        prevsong=i
        currentsong=playlist.get(prevsong)
    print(currentsong)
    mixer.music.load(currentsong)
    mixer.music.play()
    
    playlist.selection_clear(0,END)
    playlist.activate(prevsong)#highlighing next song
    playlist.selection_set(prevsong,last=None)

def callback():
    name= fd.askdirectory()
    os.chdir((name))

root1=Tk()
root1.title('Choose folder')
root1.geometry('500x500')
choosebtn=Button(text='Click to Open Folder', command=callback, font=('Helvetica', 20), relief=SUNKEN).pack(fill=tk.X)
tk.mainloop()

root=tk.Tk()
root.title('Music Player')
mixer.init()
songstatus=StringVar()
songstatus.set("Selecting song..")
playlist=Listbox(root, bg="black", bd=5, font=('Helvetica', 20), fg="cyan", height=15, selectmode="SINGLE", width=80, highlightcolor="white", highlightthickness=5, relief=RAISED)
playlist.grid(columnspan=20)
songs=os.listdir()
for s in songs:
    playlist.insert(END, s)
    
"""
playbtn=Button(root, text="Play", command=play)
playbtn.config(font=('Helvetica', 20), bg="cyan", fg="black", padx=10, pady=10, highlightbackground="white", activebackground="white", activeforeground="white", highlightcolor="white", relief=SUNKEN, borderwidth=5, highlightthickness=5)
playbtn.grid(row=1, column=0)
pausebtn=Button(root, text="Pause", command=pause)
pausebtn.config(font=('Helvetica', 20), bg="cyan", fg="black", padx=10, pady=10, highlightbackground="white", activebackground="white", activeforeground="white", highlightcolor="white", relief=SUNKEN, borderwidth=5, highlightthickness=5)
pausebtn.grid(row=1, column=1)
resumebtn=Button(root, text="Resume", command=resume)
resumebtn.config(font=('Helvetica', 20), bg="cyan", fg="black", padx=10, pady=10, highlightbackground="white", activebackground="white", activeforeground="white", highlightcolor="white", relief=SUNKEN, borderwidth=5, highlightthickness=5)
resumebtn.grid(row=1, column=2)
stopbtn=Button(root, text="Stop", command=stop)
stopbtn.config(font=('Helvetica', 20), bg="cyan", fg="black", padx=10, pady=10, highlightbackground="white", activebackground="white", activeforeground="white", highlightcolor="white", relief=SUNKEN, borderwidth=5, highlightthickness=5)
stopbtn.grid(row=1, column=3)
forwardbtn=Button(root, text="Forward", command=forward)
forwardbtn.config(font=('Helvetica', 20), bg="cyan", fg="black", padx=10, pady=10, highlightbackground="white", activebackground="white", activeforeground="white", highlightcolor="white", relief=SUNKEN, borderwidth=5, highlightthickness=5)
forwardbtn.grid(row=1, column=4)
backwardbtn=Button(root, text="Backward", command=backward)
backwardbtn.config(font=('Helvetica', 20), bg="cyan", fg="black", padx=10, pady=10, highlightbackground="white", activebackground="white", activeforeground="white", highlightcolor="white", relief=SUNKEN, borderwidth=5, highlightthickness=5)
backwardbtn.grid(row=1, column=5)
mainloop()
"""

root.geometry('1400x700')
playlist.pack(pady=20)
backbtn=ImageTk.PhotoImage(Image.open('C:/Users/mnimi/Documents/20XT26 PYTHON LAB/Package/back.png'))
forwardbtn=ImageTk.PhotoImage(Image.open('C:/Users/mnimi/Documents/20XT26 PYTHON LAB/Package/forward.png'))
pausebtn=ImageTk.PhotoImage(Image.open('C:/Users/mnimi/Documents/20XT26 PYTHON LAB/Package/pause.png'))
playbtn=ImageTk.PhotoImage(Image.open('C:/Users/mnimi/Documents/20XT26 PYTHON LAB/Package/play.png'))
stopbtn=ImageTk.PhotoImage(Image.open('C:/Users/mnimi/Documents/20XT26 PYTHON LAB/Package/stop.png'))
resumebtn=ImageTk.PhotoImage(Image.open('C:/Users/mnimi/Documents/20XT26 PYTHON LAB/Package/play.png'))

controls_frame=Frame(root)
controls_frame.pack()

backbutton=Button(controls_frame, image=backbtn, borderwidth=0, command=backward)
forwardbutton=Button(controls_frame, image=forwardbtn, borderwidth=0, command=forward)
pausebutton=Button(controls_frame, image=pausebtn, borderwidth=0, command=pause)
playbutton=Button(controls_frame, image=playbtn, borderwidth=0, command=play)
resumebutton=Button(controls_frame, image=resumebtn, borderwidth=0, command=resume)
stopbutton=Button(controls_frame, image=stopbtn, borderwidth=0, command=stop)

backbutton.grid(row=0, column=0)
playbutton.grid(row=0, column=1)
pausebutton.grid(row=0, column=2)
resumebutton.grid(row=0, column=3)
stopbutton.grid(row=0, column=4)
forwardbutton.grid(row=0, column=5)

root.mainloop()
