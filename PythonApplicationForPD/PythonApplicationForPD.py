import tkinter as tk
import math

def ResValueD():
	#Qr = 2 * math.pi * float(k.get()) * float(h.get()) * (float(Pk.get()) - float(Ps.get())) / (float(μ.get()) * math.log(float(Rk.get())/float(Rs.get())))
	#Qr = 2 * math.pi * float(k.get()) * float(h.get()) * (float(Pk.get()) - float(Ps.get())) / float(μ.get()) 
	#Qr = eval("2 * math.pi * k.get() * h.get() * (Pk.get() - Ps.get()) / (μ.get() * math.log(Rk.get()/Rs.get()))")

	k_value = k.get() 
	h_value = h.get() 
	Pk_value = Pk.get() 
	Ps_value = Ps.get() 
	μ_value = μ.get() 
	Rk_value = Rk.get() 
	Rs_value = Rs.get()

	if k_value != '' and h_value != '' and Pk_value != '' and Ps_value != '' and μ_value != '' and Rk_value != '' and Rs_value != '' and (((float(μ_value) * math.log(float(Rk_value) * float(Rs_value)))) != 0) and float(Rk_value) != 0 and float(Rs_value) != 0: 
		Qr = 2 * math.pi * float(k_value) * float(h_value) * (float(Pk_value) - float(Ps_value)) / ((float(μ_value) * math.log(float(Rk_value) * float(Rs_value))))
		labelResD = tk.Label(text = "Дебит скважины = " +  str(round(Qr,3)), fg = '#82c7a5', font = (5), bg = '#1b212c')
		labelResD.place(x = 100, y = 200)
	else:	
		labelError = tk.Label(text = "Неверно введены данные либо деление на ноль",fg = 'black', font = 20, bg = '#1b212c')
		labelError.place(x = 100, y = 200)

def ResValueZ():
	
	A_value = A.get()
	phi_value = phi.get()
	S_oi_value = S_oi.get()
	S_o_value = S_o.get()

	if A_value != '' and phi_value != '' and S_oi_value != '' and S_o_value != '': 
		Mb = float(A_value) * float(phi_value) * (float(S_oi_value) -  float(S_o_value))
		labelResZ = tk.Label(text = "Изменение запасов нефти = " +  str(round(Mb,3)), fg = '#82c7a5', font = (5), bg = '#1b212c')
		labelResZ.place(x = 480, y = 140)
	else:	
		labelError = tk.Label(text = "Неверно введены данные",fg = 'black', font = 20, bg = '#1b212c')
		labelError.place(x = 480, y = 140)

def Help():
	winH = tk.Toplevel(win)
	winH.geometry("500x200+700+300")
	winH.title('Сведение о программе')
	winH['bg'] = '#1b212c'
	winH.resizable(False, False)
	labelInfo = tk.Label(winH, text="Разработчик: Самар А. А.\nГруппа: ИИПб-23-3\nПрограмма разработана в рамках проекта по ПД\nГруппа:Самар А.А.\nДубровин С.Н.\nФайзуллин Д.Р.\nКаверин Е.Д.\nТема:Моделирование притока к вертикальным нефтяным скважинам\nТюменский инудстриальный университет (с) 2023\nВысшая школа цифровых технологий (с) 2023", bg = '#1b212c',fg = 'white', font = ('Courier New',10))
	labelInfo.pack()
	#btnHelpC = tk.Button(winH, text = "Закрыть", font = (5), bd = 3, activebackground = "grey", command = close_winH)
	#btnHelpC.place(x = 300, y = 150)
	winH.mainloop()
	


def close_win():
	win.destroy()



def close_winH():
	winH.destroy()





win = tk.Tk()
win.title("Калькулятор для моделирования притока")
win.geometry("800x300+700+300")
win['bg'] = '#1b212c'
win.resizable(False, False)
photo = tk.PhotoImage(file = "Капля.png")
win.iconphoto(False, photo)


k = tk.Entry(win)
k.place(x = 240, y = 0)
h = tk.Entry(win)
h.place(x = 240, y = 20)
Pk = tk.Entry(win)
Pk.place(x = 240, y = 40)
Ps = tk.Entry(win)
Ps.place(x = 240, y = 60)
μ = tk.Entry(win)
μ.place(x = 240, y = 80)
Rk = tk.Entry(win)
Rk.place(x = 240, y = 100)
Rs = tk.Entry(win)
Rs.place(x = 240, y = 120)

labelk = tk.Label(win, text="Коэффициент проницаемости:", bg = '#1b212c',fg = 'white', font = ('Courier New',10))
labelk.place(x=20, y=-1)
labelk = tk.Label(win, text="Мощность пласта:", bg = '#1b212c',fg = 'white', font = ('Courier New',10))
labelk.place(x=100, y=19)
labelk = tk.Label(win, text="Давление на контуре питания:", bg = '#1b212c',fg = 'white', font = ('Courier New',10))
labelk.place(x=5, y=39)
labelk = tk.Label(win, text="Давление в скважине:", bg = '#1b212c',fg = 'white', font = ('Courier New',10))
labelk.place(x=68, y=59)
labelk = tk.Label(win, text="Вязкость жидкости:", bg = '#1b212c',fg = 'white', font = ('Courier New',10))
labelk.place(x=84, y=79)
labelk = tk.Label(win, text="Радиус контура питания:", bg = '#1b212c',fg = 'white', font = ('Courier New',10))
labelk.place(x=44, y=99)
labelk = tk.Label(win, text="Радиус скважины:", bg = '#1b212c',fg = 'white', font = ('Courier New',10))
labelk.place(x=100, y=119)

btnDoneDebit = tk.Button(win, text = "Выполнить расчет", font = ("Courier New", 15), bd = 5, activebackground = "grey", command = ResValueD)
btnDoneDebit.place(x = 120, y = 145)

A = tk.Entry(win)
A.place(x = 640, y = 0)
phi = tk.Entry(win)
phi.place(x = 640, y = 20)
S_oi = tk.Entry(win)
S_oi.place(x = 640, y = 40)
S_o = tk.Entry(win)
S_o.place(x = 640, y = 60)

labelk = tk.Label(win, text="Площадь месторождения:", bg = '#1b212c',fg = 'white', font = ('Courier New',10))
labelk.place(x=451, y=-1)
labelk = tk.Label(win, text="Пористость:", bg = '#1b212c',fg = 'white', font = ('Courier New',10))
labelk.place(x=539, y=19)
labelk = tk.Label(win, text="Начальная насыщенность нефти:", bg = '#1b212c',fg = 'white', font = ('Courier New',10))
labelk.place(x=395, y=39)
labelk = tk.Label(win, text="Текущая насыщенность нефти:", bg = '#1b212c',fg = 'white', font = ('Courier New',10))
labelk.place(x=411, y=59)

btnDoneZapas = tk.Button(win, text = "Выполнить расчет", font = ("Courier New", 15), bd = 5, activebackground = "grey", command = ResValueZ)
btnDoneZapas.place(x = 520, y = 85)

btnHelp = tk.Button(win, text = "?", font = (25), bd = 3, activebackground = "grey", command = Help)
btnHelp.place(x = 770, y = 220)

btnC = tk.Button(win, text = "Закрыть", font = (5), bd = 3, activebackground = "grey", command = close_win)
btnC.place(x = 715, y = 260)



win.mainloop()


