#
#Mido is a library required - pip install mido - https://pypi.org/project/mido/
#Pygame is a library required - pip install pygame - https://pypi.org/project/pygame/
#development + Nikitin Alexander, astromc@ya.ru
#
#
#
from tkinter import *
import tkinter.messagebox
import os
import os.path
import subprocess
#---------------------------------------------------------
from mido import Message, MidiFile, MidiTrack
import pygame
#---------------------------------------------------------
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)
#---------------------------------------------------------------
#надо определить кодировку, если UTF-8 - далее открытие-обработка, если нет - предупреждение
#encoding detection, if UTF-8 - further opening-processing, if not - warning
def output(event):
    # получаем содержимое текстового поля get the contents of the text field
    s = ent.get()
    sd = ent_out.get()
    
    try:
        txt = open(s, "r", encoding="utf-8")
        content = txt.read()
        tex.delete(1.0, END)
        tex.insert(END, content)
        try:   
        
             with open(s, "r", encoding="utf-8" ) as file1:
                 for line in file1:
                     track.append(Message('program_change', program = 12, time= 0))
                     track.append(Message('note_on', note = int(line.strip()), velocity = 64, time = 32))
                     track.append(Message('note_off', note = int(line.strip()), velocity = 64, time = 32))
             mid.save(sd)
             
        except:
            tex.delete(1.0, END)
            tex.insert(END, "Нет имени озвученного файла! Введите имя файла! \n  There is no name for the midi file! input name file!") 

   
    except:
        tex.delete(1.0, END)
        tex.insert(END, "Файл не существует или неверное имя файла! \n missing file or invalid file name!")

#---------------------------------------------------------
def play_music(midi_filename):
    sd = ent_out.get()
    '''Stream music_file in a blocking manner'''
    clock = pygame.time.Clock()
    pygame.mixer.music.load(midi_filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(30) # check if playback has finished
             
def play (self):
    sd = ent_out.get()
    
    try:
        midi_filename = open (sd, "r")
        # mixer config
        freq = 44100  # audio CD quality
        bitsize = -16   # unsigned 16 bit
        channels = 1  # 1 is mono, 2 is stereo
        buffer = 1024   # number of samples
        pygame.mixer.init(freq, bitsize, channels, buffer)
        # optional volume 0 to 1.0
        pygame.mixer.music.set_volume(0.8)
        # listen for interruptions
        try:
            # use the midi file you just saved
            play_music(midi_filename)
        except KeyboardInterrupt:
            # if user hits Ctrl/C then exit
            # (works only in console mode)
            tex.delete(1.0, END)
            tex.insert(END, "Файл не существует или неверное имя файла! \n missing file or invalid file name!")
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.stop()
            raise SystemExit
    except:
        tex.delete(1.0, END)
        tex.insert(END, "Файл не существует или неверное имя файла! \n missing file or invalid file name! ")
#---------------------------------------------------------
def helpme(self):
    tkinter.messagebox.showinfo(title="development",
                                message="Nikitin Alexander. \n astromc@ya.ru",
                                )      
#---------------------------------------------------------      
def erase_in ():
    ent.delete (0, END) #очистка поля in erase
#----
def erase_out ():
    ent_out.delete (0, END) #очистка поля out erase   
#---------------------------------------------------------
# Создать окно приложения    create window
root = tkinter.Tk() #окно
root.title("Сонификатор/Sonificator") #название окна name
root.minsize(width=430, height=280) #размеры окна 
#---------------------------------------------------------
# создаем виджеты create widgets
labelName=tkinter.Label(root,
                        text='in.txt/csv Введите полное имя входного файла с данными.(UTF-8,txt/csv только). \n  Enter the full name of the input data file.(UTF-8,txt/csv only)',
                        justify=tkinter.CENTER,
                        anchor='e',
                        width=400)
labelName.place(x=10,y=5,width=400,height=30) # Поместить компонент в указанную область окна layout
#----
labelName_out=tkinter.Label(root,
                        text='Введите полное имя выходного файла.mid \n Enter the full name of the output file.mid',
                        justify=tkinter.CENTER,
                        anchor='e',
                        width=250)
labelName_out.place(x=10,y=60,width=250,height=30) # Поместить компонент в указанную область окна layout
#---
ent = Entry(root, width=380)
ent.place(x=10,y=40,width=380,height=20) #размещение in layout
#---
but_cancel_in = Button(root, text="X", command = erase_in)
but_cancel_in.place(x=400,y=40,width=20,height=20) #размещение in erase layout
#---
ent_out = Entry(root, width=380)
ent_out.place(x=10,y=95,width=380,height=20) #размещение out layout
#---
but_cancel_out = Button(root, text="X", command = erase_out )
but_cancel_out.place(x=400,y=95,width=20,height=20) #размещение out erase layout
#---
but = Button(root, text="Открыть&Обработать \n Open&Process")
but.place(x=10,y=125,width=140,height=40)
#---
but_process = Button(root, text="Прослушать \n Play")
but_process.place(x=160,y=125,width=80,height=40)
#---
but_helpme = Button(root, text="О программе \n About program")
but_helpme.place(x=250,y=125,width=100,height=40)
#--
tex = Text(root, width=80, height=30, font="Courier 10", wrap=WORD)
tex.insert(END, "Введите имя файла для озвучивания и нажмите кнопку Открыть&Обработать/ Enter the file name for the audio and click the Open&Process button \n for perpetual motion ")
tex.place(x=10,y=175,width=380,height=80)
# размещаем виджеты в окне программы Place widgets in the program window
#ent.grid(row=0, column=0)
#but.grid(row=2, column=0)
#tex.grid(row=1, column=0)
#---------------------------------------------------------------

# устанавливаем обработчик событий set up an event handler
but.bind("<Button-1>", output)
but_process.bind("<ButtonRelease-1>", play )
but_helpme.bind("<ButtonRelease-1>", helpme)
# запускаем программу start the program
root.mainloop()

