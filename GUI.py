from tkinter import * 
import tkinter as tk
import tkinter.font
import datetime
import tkinter.messagebox
from datetime import timedelta
import os
import hashlib
import binascii
from PIL import Image, ImageTk

#from tkinter import ttk
#from tkinter import messagebox
#win=Tk()
#win.geometry("70*35")


def intersection():
	#f=open("CarData.txt","r")
	#lines=f.readlines()
	result=[]
	result1=[]
	c=[]
	#for x in lines:
    	#result.append(x.split('|')[0])
	result = [x.split('|')[0] for x in open("CarData.txt").readlines()]
	result1 = [x.split('|')[0] for x in open("BikeData.txt").readlines()]
	#f.close()
	#print(result)
	#print(result1)

	c = [value for value in result if value in result1] 

	with open('file4.txt', 'a') as outfile:

	# Iterate through list
		for names in c:
		# Open each file in read mode
			#with open(names) as infile:
			# read the data from file1 and
			# file2 and write it in file3
				outfile.write(names)
				outfile.write("\n")

	#print(c)


def merger():
	#messagebox.showinfo("Message", "click okay to Proceed")
	filenames = ['CarData.txt', 'BikeData.txt']

    # Open file3 in write mode
	with open('file3.txt', 'w') as outfile:

	# Iterate through list
		for names in filenames:
		# Open each file in read mode
			with open(names) as infile:
			# read the data from file1 and
			# file2 and write it in file3
				outfile.write(infile.read())
				outfile.write("\n")
		# Add '\n' to enter data of file2
		# from next line
		

#ttk.Button(login_menu, text = "Open", command = merge).pack()
#win.mainloop()	

#def index_common():


def refresh() :
	refresh_button= Button(root, text="Refresh",command =refresh,font='bold', width=6) 
	refresh_button.pack(anchor=center)

def login_in():
	global id_input_login
	global password_input_login
	global login_menu
    
	login_menu=Tk()

	#Label(login_menu, text ="Click to open").pack(pady=15)

	login_menu.wm_title("Login")
	login_menu.geometry('1500x1500')
	login_menu.resizable(True,True)
	login_menu.configure(bg="#5ea8a1")
	canvas = Canvas(
        login_menu, 
        width = 800, 
        height = 450
        )  
	canvas.pack() 
	k_font = tkinter.font.Font(family='Times new roman', size=16, weight=tkinter.font.BOLD)
	orionLabel=Label(login_menu, text="Welcome to Automobile Showroom Management",bg="#5ea8a1",fg='#ffffff',font=("Castellar", "30","bold",))
	subLabel=Label(login_menu, text="A PLACE FOR ALL YOUR COMMUTE PROBLEMS!",bg="#5ea8a1",fg='#ffffff',font=("Castellar", "16","bold","italic"))
	id_label=Label(login_menu,text="ID:",height=3, font=k_font,bg="#5ea8a1",fg='#ffffff')
	password_label=Label(login_menu,text="Password:",height=3,font=k_font,bg="#5ea8a1",fg='#ffffff')
	id_input_login=Entry(login_menu, width=30)
	password_input_login=Entry(login_menu, width=30)
	#img = PhotoImage(file="./carShowroom.jpg")
	img = ImageTk.PhotoImage(Image.open('carShowroom.jpg'))
	loginbutton1=Button(login_menu,command=login_check,text=" Login ",bg='#b85d4f',height='1',width='8',fg='#ffffff', font=k_font,  bd = '5',borderwidth=0,highlightbackground="#5ea8a1")
	registerbutton=Button(login_menu,command=register_in,text=" Register ",bg='#b85d4f',height='1',width='8',font=k_font,fg='#ffffff', bd = '5',borderwidth='0',highlightbackground="#5ea8a1")
	feedbackbutton=Button(login_menu,command=feedback_read,text=" Feedback ",bg='#b85d4f',height='2',width='11',font=k_font,fg='#ffffff', bd = '5',borderwidth='0',highlightbackground="#5ea8a1")
	adminbutton=Button(login_menu,command=admin_in,text=" Admin Login ",height='2',width='11',font=k_font,bg='#b85d4f',fg='#ffffff', bd = '5',borderwidth='0',highlightbackground="#5ea8a1")
	password_input_login.config(show="*")

	orionLabel.place(x=210, y=50)
	canvas.create_image(
        0, 
        0, 
        anchor=NW, 
        image=img
        ) 
	canvas.place(x=60,y=250)
	subLabel.place(x=470, y=130)
	id_label.place(x=950,y=330)
	id_input_login.place(x=1100,y=355)
	password_label.place(x=950,y=400)
	password_input_login.place(x=1100,y=425)
	loginbutton1.place(x=1000,y=510)
	registerbutton.place(x=1150,y=510)
	adminbutton.place(x=500,y=900)
	feedbackbutton.place(x=900,y=900)

	login_menu.mainloop()

def login_check():
	global id
	id=id_input_login.get()
	password=password_input_login.get()

	pos = binary_search('index.txt', id)
	if pos == -1:
		tkinter.messagebox.showinfo("Login"," Username is incorrect.Please reenter")
		return(login_in)
	else:
		f2 = open ('Userprofile.txt', 'r')
		f2.seek(int(pos))
		l = f2.readline()
		l = l.rstrip()
		word = l.split('|')
		if(verify_password(word[1], password)):
			tkinter.messagebox.showinfo("Login","Login Successful!")
			login_menu.destroy()
			Main_Menu()
		else:
			tkinter.messagebox.showinfo("Login"," Password that you have entered is incorrect.Please reenter")
			return(login_in)
		f2.close()


def register_in():
	global id_input
	global name_input
	global email_input
	global password_input
	global register_menu

	register_menu=Tk()
	register_menu.wm_title("Register")
	register_menu.geometry('400x400')
	register_menu.resizable(0,0)
	register_menu.configure(bg='#5ea8a1')
	k_font = tkinter.font.Font(family='Lucida Calligraphy', size=10, weight=tkinter.font.BOLD)

	id_label=Label(register_menu,text="Your ID")
	name_label=Label(register_menu,text="Full Name")
	email_label=Label(register_menu,text="Email")
	password_label=Label(register_menu,text="Password")
	login_label=Label(register_menu,text="Already have an account?")
	id_input=Entry(register_menu,width=30)
	name_input=Entry(register_menu,width=30)
	email_input=Entry(register_menu,width=30)
	password_input=Entry(register_menu,width=30)
	loginbutton1=Button(register_menu,command=login_in,text=" Login ",bg='light blue',height=1,width=9,font=k_font)
	registerbutton=Button(register_menu,command=register_check,text=" Register ",bg='dark blue', fg='white',height=1,width=7,font=k_font, bd='5')
	password_input.config(show="*")

	id_label.grid(row=3, column = 4, pady = (10,10),padx=(10, 10))
	id_input.grid(row=3,column=5, sticky=E)
	name_label.grid(row=4, column = 4, pady = (10,10),padx=(10, 10))
	name_input.grid(row=4, column = 5, sticky=E)
	email_label.grid(row=5, column = 4, pady = (10,10),padx=(10, 10))
	email_input.grid(row=5,column=5, sticky=E)
	password_label.grid(row=6, column = 4, pady = (10,10),padx=(10, 10))
	password_input.grid(row=6,column=5, sticky=E)
	login_label.grid(row=8, column = 4, pady = (10,10),padx=(10, 10))
	registerbutton.grid(row =7, column = 5, pady = (10,10),padx=(10, 10))
	loginbutton1.grid(row =8, column = 5, pady = (10,10),padx=(10, 10))

	register_menu.mainloop()

def register_check():
	global id

	id=id_input.get()
	name=name_input.get()
	email=email_input.get()
	password=password_input.get()

	if len(id)==0 or len(name) == 0 or len(email) == 0 or len(password) == 0:
		tkinter.messagebox.showinfo("Register","You left one or more fields blank, please fill it up.")
		register_menu.lift()
		return(register_in)

	pos = binary_search('index.txt', id)
	if pos != -1:
		tkinter.messagebox.showinfo("Register","Already registered. Choose a different ID")
		register_menu.destroy()

	f2 = open ('Userprofile.txt', 'a')
	pos = f2.tell()
	f3 = open ('index.txt', 'a')
	buf = id + '|' + hash_password(password) + '|' + name + '|' + email + '|'+ '#'
	f2.write(buf)
	f2.write('\n')
	buf = id + '|' + str(pos) + '|' + '#'
	f3.write(buf)
	f3.write('\n')
	f3.close()
	f2.close()
	key_sort('index.txt')
	tkinter.messagebox.showinfo("Register","Registration Successful!Please Login again")
	register_menu.destroy()


def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


def admin_in():
		global id_admin
		global password_admin
		global admin_menu

		admin_menu=Tk()
		admin_menu.wm_title("Admin")
		admin_menu.geometry('250x250')
		admin_menu.resizable(0,0)
		k_font = tkinter.font.Font(family='Times new roman', size=10, weight=tkinter.font.BOLD)

		admin_label=Label(admin_menu,text="Admin ID")
		admin_password_label=Label(admin_menu,text="Password")
		id_admin=Entry(admin_menu)
		password_admin=Entry(admin_menu)
		loginbutton2=Button(admin_menu,command=admin_check,text=" Login ",bg='light blue',height=1,width=7,font=k_font, bd='5')
		password_admin.config(show="*")

		admin_label.grid(row=0,sticky=E, pady = (10,10),padx=(10, 10))
		id_admin.grid(row=0,column=1)
		admin_password_label.grid(row=3,sticky=E, pady = (10,10),padx=(10, 10))
		password_admin.grid(row=3,column=1)
		loginbutton2.grid(row =5, column = 1, pady = (10,10),padx=(10, 10))

		admin_menu.mainloop()

def admin_check():
	global admin_id

	admin_id=id_admin.get()
	admin_password=password_admin.get()

	if admin_id=="admin" and admin_password=="admin":
		tkinter.messagebox.showinfo("Login","Admin Login Successful!")
		admin_menu.destroy()
		login_menu.destroy()
		Admin_Opt()
	else:
		tkinter.messagebox.showinfo("Login","Admin id or password INCORRECT. Please re-enter")
def Admin_Opt():
		global opt_menu

		opt_menu=Tk()
		opt_menu.wm_title("Admin_menu")
		opt_menu.geometry('1500x1500')
		opt_menu.resizable(0,0)
		opt_menu.configure(bg="#5ea8a1")
		k_font = tkinter.font.Font(family='Times new roman', size=13, weight=tkinter.font.BOLD)
		canvas = Canvas(
        opt_menu, 
        width = 900, 
        height = 500
        )  

		addCarbutton=Button(opt_menu,command=add_car,text=" Add Car ",height=2,width=12,font=k_font,bg='#b85d4f',fg='#ffffff', bd = '5',borderwidth='0',highlightbackground="#5ea8a1")
		
		allusersbutton = Button(opt_menu,command=merger,text=" All Users ",height=2,width=15,font=k_font,bg='#b85d4f',fg='#ffffff', bd = '5',borderwidth='0',highlightbackground="#5ea8a1")
		intersectbutton=Button(opt_menu,command=intersection,text=" Common Users ",height=2,width=15,font=k_font,bg='#b85d4f',fg='#ffffff', bd = '5',borderwidth='0',highlightbackground="#5ea8a1")

		delCarbutton=Button(opt_menu,command=del_car,text=" Remove Car ",height=2,width=12,font=k_font,bg='#b85d4f',fg='#ffffff', bd = '5',borderwidth='0',highlightbackground="#5ea8a1")
		addBikebutton=Button(opt_menu,command=add_student,text=" Add Bike ",height=2,width=12,font=k_font,bg='#b85d4f',fg='#ffffff', bd = '5',borderwidth='0',highlightbackground="#5ea8a1")
		img = ImageTk.PhotoImage(Image.open('admin.jpg').resize((900,500)))
		delBikebutton=Button(opt_menu,command=del_student,text=" Remove Car ",height=2,width=12,font=k_font,bg='#b85d4f',fg='#ffffff', bd = '5',borderwidth='0',highlightbackground="#5ea8a1")
		backbutton=Button(opt_menu,command=reopen_login,text=" Log out ",height=2,width=10,font=k_font,bg='#b85d4f',fg='#ffffff', bd = '5',borderwidth='0',highlightbackground="#5ea8a1")
		canvas.create_image(
        0, 
        0, 
        anchor=NW, 
        image=img
        ) 
		canvas.place(x=300,y=150)
		addCarbutton.place(height=50, x=270, y=750)
		delCarbutton.place(height=50, x=540, y=750)
		addBikebutton.place(height=50, x=810, y=750)
		delBikebutton.place(height=50, x=1080, y=750)

		allusersbutton.place(height=50, x=500, y=850)
		intersectbutton.place(height=50, x=800, y=850)
		backbutton.place(height=50, x=1350, y=30)
		opt_menu.mainloop()

def reopen_login():
	tkinter.messagebox.showinfo("Login","Admin Logout Successful!")
	opt_menu.destroy()

	f7=open('CarIndex.txt','r')
	lines1=f7.readlines()
	f7.close()
	f8=open('CarIndex.txt','w')
	for line1 in lines1:
		if line1.startswith('*'):
			continue
		else:
			f8.write(line1)
	f8.close()

	login_in()


def key_sort(fname):
	t=list()
	fin=open(fname,'r')
	for line in fin:
		line=line.rstrip('\n')
		words=line.split('|')
		t.append((words[0],words[1]))
	fin.close()
	t.sort()
	with open("temp.txt",'w') as fout:
		for pkey,addr in t:
			pack=pkey+"|"+addr+"|#"
			fout.write(pack+'\n')
	os.remove(fname)
	os.rename("temp.txt",fname)


def binary_search(fname, search_key):
	t = []
	fin = open(fname,'r')
	for lx in fin:
		lx = lx.rstrip()
		wx = lx.split('|')
		t.append((wx[0], wx[1]))
	fin.close()
	l = 0
	r = len(t) - 1
	while l <= r:
		mid = (l + r)//2
		if t[mid][0] == search_key:
			return int(t[mid][1])
		elif t[mid][0] <= search_key:
			l = mid + 1
		else:
			r = mid - 1
	return -1

# add car

def add_car():
	global car_id
	global car_name
	global class_name_section
	global add_menu
	global car_a

	add_menu=Tk()
	add_menu.wm_title("Add Car")
	add_menu.geometry('450x400')
	add_menu.resizable(0,0)
	k_font = tkinter.font.Font(family='Times new roman', size=15, weight=tkinter.font.BOLD)

	car_id_label=Label(add_menu,font=k_font,text="Car ID (Should have 5 digits)")
	car_a_label=Label(add_menu,font=k_font,text="User AADHAR (Should have 12 digits)")
	car_name_label=Label(add_menu,font=k_font,text="Class Name")
	class_info=Label(add_menu,font=k_font,text="City")
	car_id=Entry(add_menu,width=30)
	car_name=Entry(add_menu,width=30)
	class_name_section=Entry(add_menu,width=30)
	car_a=Entry(add_menu,width=30)
	addbutton=Button(add_menu,command=add_car_check,text=" Add Car ",bg='dark orange',height=1,width=12,font=k_font)


	car_id_label.grid(row=1,sticky=E)
	car_id.grid(row=1,column=1)
	car_name_label.grid(row=2,sticky=E)
	car_name.grid(row=2,column=1)
	class_info.grid(row=3,sticky=E)
	class_name_section.grid(row=3,column=1)
	#
	car_a_label.grid(row=4,sticky=E)
	car_a.grid(row=4,column=1)
#
	addbutton.place(x=140, y=100)

	add_menu.mainloop()

def add_car_check():
	global t_id
	a_id=car_a.get()
	t_id=car_id.get()
	t_name=car_name.get().upper()
	c_id=class_name_section.get()

	if len(t_name)==0:
		tkinter.messagebox.showinfo("Add Car","You did not type a car's name.")
		add_menu.lift()
		return(add_car)
     #timepass
	if len(a_id)!=12 or t_id.isdigit()==False:
		tkinter.messagebox.showinfo("Add Car","Please re-enter the details(a-ID should be 12 positive integers)")
		add_menu.lift()
		return(add_car)	
    #
	if len(t_id)!=5 or t_id.isdigit()==False:
		tkinter.messagebox.showinfo("Add Car","Please renter the details(ID should be 5 positive integers)")
		add_menu.lift()
		return(add_car)

	if len(c_id) == 0:
		c_id = "No class alloted"

	pos = binary_search('CarIndex.txt', t_id)
	#pos1 = binary_search('BikeIndex.txt',t_id)
	if pos != -1: #or pos1 !=-1:
		tkinter.messagebox.showinfo("car","This car id already exists.Please try again")
		add_menu.lift()
		return(add_car)

    #pos = binary_search('CarIndex.txt', t_id)
	pos1 = binary_search('BikeIndex.txt',t_id)
	if pos1 !=-1:
		tkinter.messagebox.showinfo("Car","This bike id already exists.Please try again")
		add_menu.lift()
		return(add_car)

	f11 = open ('CarData.txt', 'a')
	pos = f11.tell()
	f00 = open ('CarIndex.txt', 'a')
	buf = a_id+'|'+t_id + '|' + t_name + '|' + c_id + '|' + '#'
	f11.write(buf)
	f11.write('\n')
	buf = t_id + '|' + str(pos) + '|' + '#'
	f00.write(buf)
	f00.write('\n')
	f00.close()
	f11.close()
	key_sort('CarIndex.txt')
	tkinter.messagebox.showinfo("Add Car","Car added Successfully!")
	add_menu.destroy()

# add student

def add_student():
	global student_id
	global student_name
	global class_name
	global add_details
	global student_a

	add_details=Tk()
	add_details.wm_title("Add Student")
	add_details.geometry('450x400')
	add_details.resizable(0,0)
	k_font = tkinter.font.Font(family='Helvetica', size=15, weight=tkinter.font.BOLD)

	student_id_label=Label(add_details,font=k_font,text="bike id (Should be 5 digits)")
	student_a_label=Label(add_details,font=k_font,text="bike id (Should be 12 digits)")
	student_label=Label(add_details,font=k_font,text="Student Name")
	class_label=Label(add_details,font=k_font,text="Class")
	student_id=Entry(add_details, width=30)
	student_name=Entry(add_details, width=30)
	class_name=Entry(add_details, width=30)
	student_a=Entry(add_details,width=30)
	addbutton1=Button(add_details,command=add_student_check,text=" Add Student ",bg='#0059b3', fg='white', height=1,width=10,font=k_font)

	student_id_label.grid(row=1,sticky=E)
	student_id.grid(row=1,column=1)
	student_label.grid(row=2,sticky=E)
	student_name.grid(row=2,column=1)
	class_label.grid(row=3,sticky=E)
	class_name.grid(row=3,column=1)
	#
	student_a_label.grid(row=4,sticky=E)
	student_a.grid(row=4,column=1)
#
	addbutton1.place(x=140, y=100)


	add_details.mainloop()

def add_student_check():
	global s_id
	s_id=student_id.get()
	s_name=student_name.get().upper()
	c_id=class_name.get()
	a_id=student_a.get()

	if len(s_name)==0:
		tkinter.messagebox.showinfo("Add Bike","You did not type any bike's name ")
		add_details.lift()
		return(add_student)

	#timepass
	if len(a_id)!=12 or a_id.isdigit()==False:
		tkinter.messagebox.showinfo("Add Bike","Please re-enter the details(a-ID should be 12 positive integers)")
		add_menu.lift()
		return(add_student)	
    #	

	if len(s_id)!=5 or s_id.isdigit()==False:
		tkinter.messagebox.showinfo("Add Bike","Please renter the details(ID should be 5 positive integers)")
		add_details.lift()
		return(add_student)

	if len(c_id) == 0:
		c_id = "No class alloted"

	pos = binary_search('BikeIndex.txt', s_id)
	if pos != -1:
		tkinter.messagebox.showinfo("Add Bike","This Bike already exists.Please try again")
		add_details.lift()
		return(add_student)

	f11 = open ('BikeData.txt', 'a')
	pos = f11.tell()
	f00 = open ('BikeIndex.txt', 'a')
	buf = a_id+'|'+s_id + '|' + s_name + '|' + c_id + '|' + '#'
	f11.write(buf)
	f11.write('\n')
	buf = s_id + '|' + str(pos) + '|' + '#'
	f00.write(buf)
	f00.write('\n')
	f00.close()
	f11.close()
	key_sort('BikeIndex.txt')
	tkinter.messagebox.showinfo("Add Bike","Bike added Successfully!")
	add_details.destroy()

#del car
def del_car():
	global dt_id
	global del_menu

	del_menu=Tk()
	del_menu.wm_title("Delete")
	del_menu.geometry('800x600')
	del_menu.resizable(0,0)
	k_font = tkinter.font.Font(family='Helvetica', size=12, weight=tkinter.font.BOLD)

	carId=[]
	carName = []
	carClassAndSection = []

	f1 = open('CarIndex.txt', 'r')
	f = open ("CarData.txt", 'r')
	norecord = 0

	for line in f1:
		if not line.startswith('*'):
			norecord += 1
			line = line.rstrip('\n')
			word = line.split('|')
			f.seek(int(word[1]))
			line1 = f.readline().rstrip()
			word1 = line1.split('|')
			carId.append(word1[0])
			carName.append(word1[1])
			carClassAndSection.append(word1[2])
	f.close()


	car_list=Listbox(del_menu,height=50,width=20)
	car_list2=Listbox(del_menu,height=50,width=50)
	car_list3=Listbox(del_menu,height=50,width=50)

	for num in range(0,norecord):
		car_list.insert(0,carId[num])
		car_list2.insert(0,carName[num])
		car_list3.insert(0,carClassAndSection[num])


	b_label=Label(del_menu,text="car id",font=k_font)
	dt_id=Entry(del_menu)
	delbutton1=Button(del_menu,command=del_car_check,text=" Remove Car ",bg='red',height=1,width=13,font=k_font)
	car_list2.configure(background="pink")
	car_list3.configure(background="pink")
	car_list.configure(background="light grey")

	car_label=Label(del_menu,font=k_font,text="Id")
	car_label2=Label(del_menu,font=k_font,text="Name")
	car_label3=Label(del_menu,font=k_font,text="Class and Section")

	car_label.grid(row=7,column=0,pady=20)
	car_label2.grid(row=7,column=1,pady=20)
	car_label3.grid(row=7,column=3,pady=20)

	car_list.grid(row=8,column=0)
	car_list2.grid(row=8,column=1)
	car_list3.grid(row=8,column=3)

	b_label.grid(row=0,sticky=E)
	dt_id.grid(row=0,column=1)
	delbutton1.place(x=360)

	del_menu.mainloop()

def del_car_check():

	global del_id
	del_id=dt_id.get()

	if len(del_id)==0:
		tkinter.messagebox.showinfo("Delete Car","You did not type anything O_O")
		del_menu.lift()
		return(del_car)

	pos = binary_search('CarIndex.txt', del_id)
	if(pos == -1):
		tkinter.messagebox.showinfo("Delete","Car not found.Please re-enter")
		del_menu.destroy()
		return(del_car)

	index = -1

	with open('CarIndex.txt','r') as file:
		for line in file:
			words=line.split("|")
			if(words[0]==del_id):
				index=int(words[1])

	index=0
	with open("CarIndex.txt",'r+') as file:
		line=file.readline()
		while line:
			words=line.split("|")
			if words[0]==del_id:
				file.seek(index,0)
				file.write("*")
				break
			else:
				index=file.tell()
				line=file.readline()
	tkinter.messagebox.showinfo("Delete","Car is removed from the list successfully ")
	del_menu.destroy()

#del student
def del_student():
	global ds_id
	global del_item

	del_item=Tk()
	del_item.wm_title("Delete Student")
	del_item.geometry('800x600')
	del_item.resizable(0,0)
	k_font = tkinter.font.Font(family='Helvetica', size=12, weight=tkinter.font.BOLD)

	StId=[]
	StName = []
	StClass = []

	# f3 = open('BikeIndex.txt', 'r')
	# f2 = open ("BikeData.txt", 'r')
	# norecord = 0
	# for line0 in f3:
	# 	if not line0.startswith('*'):
	# 		norecord += 1
	# 		line0 = line0.rstrip('\n')
	# 		word0 = line0.split('|')
	# 		f2.seek(int(word0[1]))
	# 		line2 = f2.readline().rstrip()
	# 		word2 = line2.split('|')
	# 		Id.append(word2[0])
	# 		Name.append(word2[1])
	# 		Class_Section.append(word2[2])

	# f2.close()

	f2 = open('BikeIndex.txt', 'r')
	f3 = open ("BikeData.txt", 'r')
	norecords = 0
	for lin in f2:
		norecords += 1
		lin = lin.rstrip('\n')
		words = lin.split('|')
		f3.seek(int(words[1]))
		line0 = f3.readline().rstrip()
		word0 = line0.split('|')
		StId.append(word0[0])
		StName.append(word0[1])
		StClass.append(word0[2])

	f3.close()

	student_list=Listbox(del_item,height=50,width=20)
	student_list2=Listbox(del_item,height=50,width=50)
	student_list3=Listbox(del_item,height=50,width=50)

	for num in range(0,norecords):
		student_list.insert(0,StId[num])
		student_list2.insert(0,StName[num])
		student_list3.insert(0,StClass[num])


	s_label=Label(del_item,text="bike id",font=k_font)
	ds_id=Entry(del_item)
	delbutton2=Button(del_item,command=del_check,text=" Remove Student ",bg='black', fg='white', height=1,width=13,font=k_font)
	student_list2.configure(background="bisque")
	student_list3.configure(background="bisque")
	student_list.configure(background="light grey")

	student_label=Label(del_item,font=k_font,text="Id")
	student_label2=Label(del_item,font=k_font,text="Student Name")
	student_label3=Label(del_item,font=k_font,text="Class and Section")


	student_label.grid(row=7,column=0,pady=(20,10))
	student_label2.grid(row=7,column=1,pady=(20,10))
	student_label3.grid(row=7,column=3,pady=(20,10))

	student_list.grid(row=8,column=0)
	student_list2.grid(row=8,column=1)
	student_list3.grid(row=8,column=3)

	s_label.grid(row=0,sticky=E)
	ds_id.grid(row=0,column=1)
	delbutton2.place(x=360)

	del_item.mainloop()

def del_check():

	global del_id
	del_id=ds_id.get()

	if len(del_id)==0:
		tkinter.messagebox.showinfo("Delete Student","You did not type anything ;)")
		del_item.lift()
		return(del_student)

	pos = binary_search('BikeIndex.txt', del_id)
	if(pos == -1):
		tkinter.messagebox.showinfo("Delete","Student not present.Please reenter:-)")
		del_item.destroy()
		return(del_student)

	index = -1

	with open('BikeIndex.txt','r') as file:
		for line in file:
			words=line.split("|")
			if(words[0]==del_id):
					index=int(words[1])

	index=0
	with open("BikeIndex.txt",'r+') as file:
		line=file.readline()
		while line:
			words=line.split("|")
			if words[0]==del_id:
				file.seek(index,0)
				file.write("*")
				break
			else:
				index=file.tell()
				line=file.readline()
	tkinter.messagebox.showinfo("Delete","Student Successfully removed from the list")
	del_item.destroy()

#------------------------------------------------------

def Main_Menu():
	global base
	base = Tk()
	#Window title and size optimization
	base.wm_title("BRING HOME YOUT HAPPINESS")
	base.geometry('1500x1500')
	base.configure(bg="#5ea8a1")

	in_font = tkinter.font.Font(family='Lucida Calligraphy', size=15, weight=tkinter.font.BOLD)
	current_time1=datetime.datetime.now()
	current_time=str(current_time1)

	#Bunch of labels
	status = Label(base,text=("Date and time logged in: " + current_time),bd=1,relief=SUNKEN,anchor=W,bg='light pink')
	orionLabel=Label(base, text="AUTOMOBILE SERVICES",bg="#5ea8a1",font=("Castellar", "50","bold","italic",),fg="#ffffff")
	backbutton=Button(base,command=student_logout,text=" Log out ",bg='#b85d4f',fg='#ffffff',height=2,width=10,font=in_font,borderwidth='0',highlightbackground="#5ea8a1")
	welcomeLabel=Label(base,text=("Welcome "+id+"!"),font=("Freestyle Script","30","bold"),bg="#5ea8a1",fg="#ffffff")
	img = ImageTk.PhotoImage(Image.open('car_rent1.jpg').resize((550,290)))
	topFrame=Frame(base)
	bottomFrame=Frame(base)

	#Positioning of labels
	status.pack(side=BOTTOM,fill=X)
	orionLabel.place(x=300,y=30)
	backbutton.place(height=35,width=100,x=1350, y=20)
	welcomeLabel.place(x=600,y=130)
	Label(base, image=img).place(x=480,y=300)
	topFrame.pack()
	bottomFrame.pack(side=BOTTOM)

	#Buttons
	view1=Button(base,text="View cars",font=in_font,height=2,width=15,command=view_car,bg='#b85d4f',fg='#ffffff', bd = '5',borderwidth='0',highlightbackground="#5ea8a1")
	view2=Button(base,text="View Bike",font=in_font,height=2,width=15,command=view_student,bg='#b85d4f',fg='#ffffff', bd = '5',borderwidth='0',highlightbackground="#5ea8a1")
	search_butn1=Button(base,text="Search for a Car",font=in_font,height=2,width=16,command=search_car,bg='#b85d4f',fg='#ffffff', bd = '5',borderwidth='0',highlightbackground="#5ea8a1")
	search_butn2=Button(base,text="Search for a Bike",font=in_font,height=2,width=16,command=search_student,bg='#b85d4f',fg='#ffffff', bd = '5',borderwidth='0',highlightbackground="#5ea8a1")	
	feedback_butn=Button(base,text="Feedback",font=in_font,height=2,width=15,command=feedback_in,bg='#b85d4f',fg='#ffffff', bd = '5',borderwidth='0',highlightbackground="#5ea8a1")
	
	
	#ttk.Button(login_menu, text = "Open", command = merge).pack()
	#Positioning of buttons
	# view1.pack(side=LEFT)
	view1.place(x=90,y=350)
	view2.place(x=90,y=500)
	feedback_butn.place(x=670,y=900)
	search_butn1.place(x=1150,y=350)
	search_butn2.place(x=1150,y=500)
	base.mainloop()

def student_logout():
	tkinter.messagebox.showinfo("Login","User Logout Successful!")
	base.destroy()

	f7=open('CarIndex.txt','r')
	lines1=f7.readlines()
	f7.close()
	f8=open('CarIndex.txt','w')
	for line1 in lines1:
		if line1.startswith('*'):
			continue
		else:
			f8.write(line1)
	f8.close()

	login_in()

def view_car():
	# global borrow_entry1
	global car_menu

	car_menu=Tk()

	car_menu.wm_title("View cars")
	car_menu.minsize(900,550)
	car_menu.maxsize(1200,550)
	car_menu.resizable(0,0)

	Id=[]
	Tname = []
	TClass = []

	f1 = open('CarIndex.txt', 'r')
	f = open ("CarData.txt", 'r')
	norecord = 0
	for line in f1:
		norecord += 1
		line = line.rstrip('\n')
		word = line.split('|')
		print(word)
		f.seek(int(word[1]))
		line1 = f.readline().rstrip()
		print("car line 1", line1)
		word1 = line1.split('|')
		Id.append(word1[0])
		Tname.append(word1[1])
		TClass.append(word1[2])
		print(word1)

	f.close()
	t_list=Listbox(car_menu,height=50,width=20)
	t_list1=Listbox(car_menu,height=50,width=50)
	t_list2=Listbox(car_menu,height=50,width=50)

	for num in range(0,norecord):
		t_list.insert(0,Id[num])
		t_list1.insert(0,Tname[num])
		t_list2.insert(0,TClass[num])

	t_list.configure(background="light grey")
	t_list1.configure(background="pink")
	t_list2.configure(background="pink")
	t_label=Label(car_menu,text="Id")
	t_label2=Label(car_menu,text="car Name")
	t_label3=Label(car_menu,text="Class")

	t_label.grid(row=3,column=0)
	t_label2.grid(row=3,column=1)
	t_label3.grid(row=3,column=4)

	t_list.grid(row=4,column=0)
	t_list1.grid(row=4,column=1)
	t_list2.grid(row=4,column=4)

	car_menu.mainloop()

def view_student():
	# global borrow_entry1
	global student_menu

	student_menu=Tk()

	student_menu.wm_title("View students")
	student_menu.minsize(900,550)
	student_menu.maxsize(1200,550)
	student_menu.resizable(0,0)

	StId=[]
	Stname = []
	StClass = []

	f2 = open('BikeIndex.txt', 'r')
	f3 = open ("BikeData.txt", 'r')
	norecords = 0
	for lin in f2:
		norecords += 1
		lin = lin.rstrip('\n')
		words = lin.split('|')
		f3.seek(int(words[1]))
		line0 = f3.readline().rstrip()
		word0 = line0.split('|')
		StId.append(word0[0])
		Stname.append(word0[1])
		StClass.append(word0[2])
		print(word0)

	f3.close()
	s_list=Listbox(student_menu,height=50,width=20)
	s_list1=Listbox(student_menu,height=50,width=50)
	s_list2=Listbox(student_menu,height=50,width=50)

	for num in range(0,norecords):
		s_list.insert(0,StId[num])
		s_list1.insert(0,Stname[num])
		s_list2.insert(0,StClass[num])

	s_list.configure(background="light grey")
	s_list1.configure(background="pink")
	s_list2.configure(background="pink")
	s_label=Label(student_menu,text="Id")
	s_label2=Label(student_menu,text="Student's Name")
	s_label3=Label(student_menu,text="Class")

	s_label.grid(row=3,column=0)
	s_label2.grid(row=3,column=1)
	s_label3.grid(row=3,column=4)

	s_list.grid(row=4,column=0)
	s_list1.grid(row=4,column=1)
	s_list2.grid(row=4,column=4)

	student_menu.mainloop()


#car search
def search_car():
	global search_car_entry
	global search_menu
	search_menu=Tk()
	search_menu.geometry('400x400')
	search_menu.wm_title("Search car")
	search_menu.resizable(0,0)

	#search car
	search_label1=Label(search_menu,text="To search a car, please enter his or her ID",font=("Times", "12","bold","italic"),bg="light blue")
	search_label1.pack(side=TOP)

	search_car_entry = Entry(search_menu,width=20)
	search_car_entry.pack(side=TOP)

	search_button1=Button(search_menu,text="Search",command=car_check,font=("Times new roman","12","bold"),bg="magenta")
	search_button1.pack(side=TOP)

	search_menu.mainloop()

#student search
def search_student():
	global search_student_entry
	global search_list
	search_list=Tk()
	search_list.geometry('400x400')
	search_list.wm_title("Search Student")
	search_list.resizable(0,0)

	#search student
	search_label1=Label(search_list,text="To search a student, please enter his or her ID ",font=("Times", "12","bold","italic"),bg="light blue")
	search_label1.pack(side=TOP, fill=Y)

	search_student_entry = Entry(search_list,width=20)
	search_student_entry.pack(side=TOP, fill=Y)

	search_button2=Button(search_list,text="Search",command=student_check,font=("Times new roman","12","bold"),bg="blue", fg="white")
	search_button2.pack(side=TOP, fill=Y)

	search_list.mainloop()

#car check
def car_check():
	search_word=search_car_entry.get().upper()
	search_menu.destroy()

	if len(search_word) == 0:
		tkinter.messagebox.showinfo("Search","You did not search anything O_O")
		return(search_car)

	pos = binary_search('CarIndex.txt', search_word)

	if (pos == -1):
		tkinter.messagebox.showinfo("Search","Sorry,this automobile does not exist in our school")
	else:
		search_menu1=Tk()
		search_menu1.wm_title("Search")
		search_menu1.attributes("-topmost",True)
		tkinter.messagebox.showinfo("Search","Automobile Found!")

		search_result1=Listbox(search_menu1,height=10,width=50)
		f2 = open('CarData.txt', 'r')
		f2.seek(pos)
		l1 = f2.readline()
		l1 = l1.rstrip()
		w1 = l1.split('|')
		t_id = w1[0]
		t_name = w1[1]
		class_name= w1[2]
		f2.close()

		search_result1.insert(1,"ID:" + t_id)
		search_result1.insert(2,"car's Name:" + t_name)
		search_result1.insert(3,"Class:" + class_name)

		search_result1.pack()
		search_menu1.mainloop()

#student check
def student_check():
	search_keyword=search_student_entry.get().upper()
	search_list.destroy()

	if len(search_keyword) == 0:
		tkinter.messagebox.showinfo("Search","You did not search anything O_O")
		return(search_student)

	pos = binary_search('BikeIndex.txt', search_keyword)

	if (pos == -1):
		tkinter.messagebox.showinfo("Search","Sorry,this automobile does not exist in our school")
	else:
		search_list2=Tk()
		search_list2.wm_title("Search")
		search_list2.attributes("-topmost",True)
		tkinter.messagebox.showinfo("Search","Automobile found!")

		search_result=Listbox(search_list2,height=10,width=50)
		f2 = open('BikeData.txt', 'r')
		f2.seek(pos)
		l1 = f2.readline()
		l1 = l1.rstrip()
		w1 = l1.split('|')
		s_id = w1[0]
		s_name = w1[1]
		class_details = w1[2]
		f2.close()

		search_result.insert(1,"ID:" + s_id)
		search_result.insert(2,"Student's Name:" + s_name)
		search_result.insert(3,"Class:" + class_details)

		search_result.pack()
		search_list2.mainloop()


def feedback_in():
	global feedback_bar
	global feedback_menu
	global feedback_input

	feedback_menu=Tk()
	feedback_menu.wm_title("Feedback")
	feedback_menu.geometry('450x400')
	feedback_menu.resizable(0,0)

	feedback_bar=Entry(feedback_menu,width=40)
	feedback_label=Label(feedback_menu,text= "We improve from your valuable feedback.Thank you!",font=("Roboto","13","italic"),bg="light blue", width=40)
	button1=Button(feedback_menu, text="Submit feedback",command=feedback_check,font=("Times new roman","10","bold"),bg="dark orange")

	feedback_bar.place(x=100,y=30)
	feedback_label.place(x=20,y=60 )
	button1.place(x=170, y=100)
	feedback_menu.mainloop()

def feedback_check():
	user_feedback=feedback_bar.get()
	if len(feedback_bar.get())==0:
		tkinter.messagebox.showinfo("Feedback","You did not type anything O_O")
		feedback_menu.lift()
		return(feedback_in)
	else:
		tkinter.messagebox.showinfo("Feedback","Thank you for your valuable feedback! >_<")
		file = open('Feedback.txt', 'a')
		file.write(user_feedback + "\n")
		file.close()
		feedback_menu.destroy()


def feedback_read():
	read_feedback_menu=Tk()
	read_feedback_menu.geometry('400x400')
	read_feedback_menu.resizable(0,0)
	read_feedback_menu.wm_title("Users' feedback")

	list=Listbox(read_feedback_menu)
	file = open('Feedback.txt' , 'r')
	num_feedback = len(file.readlines())
	file.close()
	file = open('Feedback.txt' , 'r')
	count = 1
	feedback = file.readlines()
	for i in range(0, num_feedback):
		list_feedback =str(count) + ('.') + (feedback[count - 1])
		list.insert(count,list_feedback)
		count += 1
	file.close()

	list.pack(side=TOP,fill=X,expand=1)
	read_feedback_menu.mainloop()

login_in()
