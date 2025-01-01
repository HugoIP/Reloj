from tkinter import Canvas, Tk, ttk,Frame ,LAST
from time import strftime
from playsound import playsound
from math import cos, sin, radians, pi
import winsound
import serial,time

ard = serial.Serial('COM7',9600)
ventana = Tk()
ventana.title('Santa Catariva Villanueva, Quecholac, Puebla, Mex. Reloj Analogico')
ventana.geometry('420x450')
ventana.config(bg='white')
ventana.minsize(width=420, height=420)
ventana.columnconfigure(0, weight = 1)
ventana.rowconfigure(0, weight = 1)
#frame = ttk.Frame(ventana, padding=10)

frame = Frame(ventana, height=450, width =420,  bg= 'black', relief ='sunken')
frame.grid(column=0,row=0)
canvas = Canvas(frame, bg= 'black', width = 450, height =385, relief ='raised', bd =10)
canvas.grid( padx=5, pady = 5)

hr =0
mi =0
se =0

flagSound = False
flagSoundEnd= 0
def reloj(h,m,s): 
	canvas.create_oval(50,50,350,350, fill='black', outline='white', width=6, activeoutline='gray', activefill='gray12')
	numeros = [11,10,9,8,7,6,5,4,3,2,1,12]
	for i in range(0,len(numeros)):		
		canvas.create_text(200-120*sin(((i+1)*2*pi)/12), 200- 120*cos(((i+1)*2*pi)/12), text= numeros[i], font=('Arial',12, 'bold'), fill ='white')
	for y in range(60):
		canvas.create_text(200-140*sin(((y+1)*2*pi)/60), 200- 140*cos(((y+1)*2*pi)/60), text= '•', font=('Arial',12, 'bold'), fill ='deep sky blue')
	for x in range(12):
		canvas.create_text(200-140*sin(((x+1)*2*pi)/12), 200- 140*cos(((x+1)*2*pi)/12), text= '•', font=('Arial',25, 'bold'), fill ='red')
    	#Agujas del reloj horas, minutos, segundos ☼
	canvas.create_line(200,200,200 + 60*sin(radians(hr)), 200 - 60*cos(radians(hr)), fill='white',width=9,arrow= LAST,arrowshape=(9,0,0))
	canvas.create_line(200,200,200 + 80*sin(radians(mi)), 200 - 80*cos(radians(mi)), fill='cyan',width=6,arrow= LAST,arrowshape=(6,0,0))
	canvas.create_line(200,200,200 + 120*sin(radians(se)), 200 - 120*cos(radians(se)), fill='white',width=3,arrow= LAST,arrowshape=(3,0,0))	
	canvas.create_oval(190,190,210,210, fill='white' , outline ='black', width=2)
	hh = int(strftime('%H'))
	mm = int(strftime('%M'))
	ss = int(strftime('%S'))
	#canvas.create_text(200, 380, text=(hh,":",mm,":",ss), fill="white", font=('Helvetica 15 bold'))


def eventSounds(h,m,s):
	global flagSound
	global flagSoundEnd 
	global track

	if not flagSound:
		if(track!="No"):
			#if is miising one minuto prepare to sound
			flagSound=True
			flagSoundEnd=m+2 #5 is dutarion of sound
			#Start extrern audio system
			#call init external sound system
			hardwareOn()
			#init track
			playsound("C:/RelojMonumental/Reloj/assets/O2/"+track)

			#Stop estern audio system
	elif flagSound:
		if m>=flagSoundEnd:
			flagSound=False
			flagSoundEnd=0
			track="No"
			hardwareOff()
		
def tiempo():
	global hr, mi, se, track
	track="No"	
	h = int(strftime('%H'))
	m = int(strftime('%M'))
	s = int(strftime('%S'))
	hr = (h/12)*360
	mi = (m/60)*360
	se = (s/60)*360
	reloj(hr,mi,se)
	track=timeCondition(h,m,s)
	
	eventSounds(h,m,s)
	canvas.after(1000,tiempo)
def timeCondition(h,m,s):
	#variable answer
	answer="No"
	if(m==0):
		match h:
			case 1:
				answer="1AM.mp3"
			case 2:
				answer="2AM.mp3"
			case 3:
				answer="3AM.mp3"
			case 4:
				answer="4AM.mp3"
			case 5:
				answer="5AM.mp3"
			case 6:
				answer="6AM.mp3"
			case 7:
				answer="7AM.mp3"
			case 8:
				answer="8AM.mp3"
			case 9:
				answer="9AM.mp3"
			case 10:
				answer="10AM.mp3"
			case 11:
				answer="11AM.mp3"
			case 12:
				answer="12PM.mp3"
			case 13:
				answer="1PM.mp3"
			case 14:
				answer="2PM.mp3"
			case 15:
				answer="3PM.mp3"
			case 16:
				answer="4PM.mp3"
			case 17:
				answer="5PM.mp3"
			case 18:
				answer="6PM.mp3"
			case 19:
				answer="7PM.mp3"
			case 20:
				answer="8PM.mp3"
			case 21:
				answer="9PM.mp3"
			case 22:
				answer="10PM.mp3"
			case 23:
				answer="11PM.mp3"
			case 24:
				answer="12AM.mp3"

	#every half hour
	#check thas not is rest time
	if((h>=4) and h<22):
		if(m==30):
			answer ="HALF.mp3"
	if(m==34):
			answer ="30m.mp3"
	if(m==45):
			answer ="15m.mp3"
	if(m==50):
			answer ="TEST.mp3"
	if(m==55):
			answer ="5M.mp3"
	return answer

def hardwareOn():
	if not ard.isOpen():
		ard.open()

	time.sleep(5)
	ard.write(b'1')
	ard.close()
def hardwareOff():
	if not ard.isOpen():
		ard.open()
	ard.write(b'5')
	ard.close()


tiempo()
ventana.mainloop()