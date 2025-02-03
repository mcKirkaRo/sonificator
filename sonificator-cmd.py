#Mido is a library required - pip install mido - https://pypi.org/project/mido/
#development + Nikitin Alexander, astromc@ya.ru
#for perpetual motion eth:arb1:oeth:0xf08a5db47355cde223f1801fcfbb272a142361f1
#dogecoin:DRTnrKz7BEy8HcMtFQBRN1nBgteztJeYz5
#файлы только c кодировкой UTF 
#UTF-8,txt/csv only
#---------------------------------------------------------
from mido import Message, MidiFile, MidiTrack
#---------------------------------------------------------
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)
#---------------------------------------------------------
print(" файлы только формата txt/csv c кодировкой UTF-8 \n enter the full name of the input data file.(UTF-8,txt/csv only) ")
print(" введите имя файла для сонификации   e.g. name.txt or name.csv")
name_file_in = input ()
print(" введите имя озвученного файла \n enter the name of the audio file e.g. out.mid ")
name_file_out = input ()
# получим объект файла get the file object
with open(name_file_in, "r") as file1:
#with open("2.txt", "r") as file1:
    # итерация по строкам iteration line by line
    for line in file1:
#        print(line.strip())
#------------------------------------------------------        
#for i in range( len( myArray)):
         track.append(Message('program_change', program = 12, time= 0))
         track.append(Message('note_on', note = int(line.strip()), velocity = 64, time = 32))
         track.append(Message('note_off', note = int(line.strip()), velocity = 64, time = 32))

mid.save(name_file_out)
