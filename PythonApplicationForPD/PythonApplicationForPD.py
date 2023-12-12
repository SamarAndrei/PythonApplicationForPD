import tkinter as tk
import math

def ResValue():
	#Qr = 2 * math.pi * float(k.get()) * float(h.get()) * (float(Pk.get()) - float(Ps.get())) / (float(μ.get()) * math.log(float(Rk.get())/float(Rs.get())))
	#Qr = 2 * math.pi * float(k.get()) * float(h.get()) * (float(Pk.get()) - float(Ps.get())) / float(μ.get()) 
	#Qr = eval("2 * math.pi * k.get() * h.get() * (Pk.get() - Ps.get()) / (μ.get() * math.log(Rk.get()/Rs.get()))") пизда сука 3 вариации и нихуя. с послденими 2-мя переменными че то я не ебу вахуи бляяяяяяяяяяяяяяяяяяяяяяяяяяяяяяя

	k_value = k.get() 
	h_value = h.get() 
	Pk_value = Pk.get() 
	Ps_value = Ps.get() 
	μ_value = μ.get() 
	Rk_value = Rk.get() 
	Rs_value = Rs.get()

	if k_value != '' and h_value != '' and Pk_value != '' and Ps_value != '' and μ_value != '' and Rk_value != '' and Rs_value != '' and (((float(μ_value) * math.log(float(Rk_value) * float(Rs_value)))) != 0) and float(Rk_value) != 0 and float(Rs_value) != 0: 
		Qr = 2 * math.pi * float(k_value) * float(h_value) * (float(Pk_value) - float(Ps_value)) / ((float(μ_value) * math.log(float(Rk_value) * float(Rs_value))))
		labelRes = tk.Label(text = "Дебит скважины = " +  str(round(Qr,3)), fg = 'black', font = (5), bg = '#708090')
		labelRes.pack()
	else:	
		labelError = tk.Label(text = "Неверно введены данные либо деление на ноль",fg = 'black', font = 20, bg = '#708090')
		labelError.pack()

win = tk.Tk()
win.title("Калькулятор для моделирования притока")
win.geometry("600x500+700+300")
win['bg'] = '#708090'
win.resizable(False, False)
photo = tk.PhotoImage(file = "Капля.png")
win.iconphoto(False, photo)


k = tk.Entry(win)
k.pack()
h = tk.Entry(win)
h.pack()
Pk = tk.Entry(win)
Pk.pack()
Ps = tk.Entry(win)
Ps.pack()
μ = tk.Entry(win)
μ.pack()
Rk = tk.Entry(win)
Rk.pack()
Rs = tk.Entry(win)
Rs.pack()

labelk = tk.Label(win, text="Коэффициент проницаемости:", bg = '#708090', font = ('Courier New',10))
labelk.place(x=20, y=0)
labelk = tk.Label(win, text="Мощность пласта:", bg = '#708090', font = ('Courier New',10))
labelk.place(x=100, y=18)
labelk = tk.Label(win, text="Давление на контуре питания:", bg = '#708090', font = ('Courier New',10))
labelk.place(x=5, y=37)
labelk = tk.Label(win, text="Давление в скважине:", bg = '#708090', font = ('Courier New',10))
labelk.place(x=68, y=55)
labelk = tk.Label(win, text="Вязкость жидкости:", bg = '#708090', font = ('Courier New',10))
labelk.place(x=84, y=75)
labelk = tk.Label(win, text="Радиус контура питания:", bg = '#708090', font = ('Courier New',10))
labelk.place(x=44, y=94)
labelk = tk.Label(win, text="Радиус скважины:", bg = '#708090', font = ('Courier New',10))
labelk.place(x=100, y=113)




btnDone = tk.Button(win, text = "Выполнить расчет", font = ("Courier New", 15), bd = 5, activebackground = "grey", command = ResValue)
btnDone.pack()









win.mainloop()


