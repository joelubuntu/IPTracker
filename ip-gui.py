from json.tool import main
from tkinter import *
import urllib.request , json , os , sys , platform
from datetime import datetime

def restart(window):
    file_name = sys.argv[0]
    if window == 'internet_error':
        internet_error.destroy()
    elif window == 'main_menu':
        main_menu.destroy()
    try:
        try:
            os.system('python '+ file_name)
        except:
            os.system('python3 '+ file_name)
    except:
        print('error occured while restarting')

def make_history():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    his_file = open('.history.txt','a')
    his_file.write(dt_string + ' - ' + search_box.get() + '\n')
    his_file.close()
    if platform.system() == 'Windows':
        os.system("attrib +h .history.txt")
    search_results()

def search_results():
	root2 = Tk()
	req_ip = urllib.request.urlopen('http://ip-api.com/json/' + search_box.get())
	req_ip_json = json.loads(req_ip.read())
	Label(root2 , text='Requested IP: '+req_ip_json['query']).pack()
	Label(root2, text='Search status: '+req_ip_json['status']).pack()
	Label(root2,text='Country: '+ req_ip_json['country']).pack()
	Label(root2,text='Country code: ' + req_ip_json['countryCode']).pack()
	Label(root2, text='Region: '+req_ip_json['region']).pack()
	Label(root2,text='Region Name: ' + req_ip_json['regionName']).pack()
	Label(root2,text='City: '+req_ip_json['city']).pack()
	Label(root2,text='Zip: ' + req_ip_json['zip']).pack()
	Label(root2, text='latitude: '+str(req_ip_json['lat'])).pack()
	Label(root2,text='longitude: '+str(req_ip_json['lon'])).pack()
	Label(root2,text='Timezone: '+str(req_ip_json['timezone'])).pack()
	Label(root2,text='ISP: '+req_ip_json['isp']).pack()
	Label(root2,text='Organisation: '+req_ip_json['org']).pack()
	Label(root2,text=req_ip_json['as']).pack()
	Button(root2, text="Close", command=root2.destroy).pack()
	root2.mainloop()

def clear_history():
	hist_file = open(".history.txt","w")
	hist_file.write("Searched History:")
	hist_file.close()

def show_history():
    try:
        list = open('.history.txt','r')
    except:
        create = open('.history.txt','a')
        create.write("Searched History:")
        create.close()
        if platform.system() == 'Windows':
            os.system("attrib +h .history.txt")
        show_history()
    history = Tk()
    Label(history,text=list.read()).pack()
    Button(history,text="Clear History",command=clear_history).pack()
    Button(history,text="Exit",command=history.destroy).pack()
    list.close()

try:
    user_ip = urllib.request.urlopen('https://api.ipify.org/?format=json')
    user_json_value = json.loads(user_ip.read())
    main_menu = Tk()
    user_ip_label = Label(main_menu,text= 'Your IP: ' + user_json_value['ip']).grid(row=0,column=0)
    search_box = Entry(main_menu,borderwidth=3)
    search_box.grid(row=1,column=0)
    Button(main_menu,text='Search',command=make_history).grid(row=1,column=1)
    Button(main_menu, text="Exit", command=main_menu.destroy).grid(column=1, row=2)
    Button(main_menu,text='Copy' ,command=main_menu.clipboard_append(user_json_value['ip'])).grid(row=0,column=1)
    Button(main_menu,text='Show History', command=show_history).grid(column=0 , row=2)   
    main_menu.title('Main Menu')
    main_menu.mainloop()

except:
    internet_error = Tk()
    Label(internet_error,text='Check Your Internet Connection!').pack()
    Button(internet_error,text='Close',command=internet_error.destroy).pack()
    Button(internet_error,text='Restart',command=restart('internet_error')).pack()
    internet_error.title('Error!')
    internet_error.mainloop()
