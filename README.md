**Sonification - convert a file in txt or csv format on MIDI file**


The script allows you to convert a file txt or csv format   
with a given series of numbers into an audio file, creating a MIDI file.  
 This process is called sonification.  

It is preferable to prepare a file, use integers of the order of 20 to 120,   
depending on the degree of sound perception,   
low frequencies and too high ones can be poorly perceived.  

for example  
45  
46  
56  
76  
54  
35  
etc.



Python >3.7

**compact version for terminal**    
Mido is a library required - https://pypi.org/project/mido/ 
    
`pip install mido`  
     
run  windows `python sonificator-cmd.py`  
  
run linux `python3 sonificator-cmd.py`  
  
 or
  
**GUI version**  
Mido is a library required - https://pypi.org/project/mido/  
Pygame is a library required - https://pypi.org/project/pygame/ 
    
`pip install mido pygame`  

run windows  `python sonificator.py`  
  
run linux  `python3 sonificator.py`  

https://github.com/user-attachments/assets/55a83cfe-9f6e-408c-a59a-8718d2d11a1a

