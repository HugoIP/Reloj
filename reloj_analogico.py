from tkinter import Canvas, Tk, ttk,Frame ,LAST
from time import strftime
from math import cos, sin, radians, pi
import winsound

ventana = Tk()
ventana.title('Reloj Analogico')
ventana.geometry('420x420')
ventana.config(bg='white')
ventana.minsize(width=420, height=420)
ventana.columnconfigure(0, weight = 1)
ventana.rowconfigure(0, weight = 1)
#frame = ttk.Frame(ventana, padding=10)

frame = Frame(ventana, height=400, width =420,  bg= 'black', relief ='sunken')
frame.grid(column=0,row=0)
canvas = Canvas(frame, bg= 'black', width = 400, height =385, relief ='raised', bd =10)
canvas.grid( padx=5, pady = 5)

hr =0
mi =0
se =0

flagSound = False
flagSoundEnd= 0;
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

def eventSounds(h,m,s):
	global flagSound
	global flagSoundEnd
	if not flagSound:
		if(m==18):#if is miising one minuto prepare to sound
			print("Init Sound at minute ",m)
			flagSound=True
			flagSoundEnd=m+1; #5 is dutarion of sound
			winsound.PlaySound("assets/bell1.wav",winsound.SND_FILENAME)
	elif flagSound:
		if m>=flagSoundEnd:
			flagSound=False
			print("Stop Sound at minute ",m)

def tiempo():
	global hr, mi, se	
	h = int(strftime('%H'))
	m = int(strftime('%M'))
	s = int(strftime('%S'))
	hr = (h/12)*360
	mi = (m/60)*360
	se = (s/60)*360
	reloj(hr,mi,se)
	eventSounds(h,m,s)
	canvas.after(1000,tiempo)
tiempo()
ventana.mainloop()