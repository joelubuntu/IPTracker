from tkinter import *
import urllib.request
import json

def search_button_click():
	root2 = Tk()
	req_ip = urllib.request.urlopen('http://ip-api.com/json/' + search_box.get())
	req_ip_json = json.loads(req_ip.read())
	query = Label(root2 , text='Requested IP: '+req_ip_json['query']).pack()
	status = Label(root2, text='Search status: '+req_ip_json['status']).pack()
	country = Label(root2,text='Country: '+req_ip_json['country']).pack()
	countrycode = Label(root2,text=req_ip_json['countryCode']).pack()
	region = Label(root2, text='Region: '+req_ip_json['region']).pack()
	regionaname = Label(root2,text='Region Name: ' + req_ip_json['regionName']).pack()
	city = Label(root2,text='City: '+req_ip_json['city']).pack()
	zip = Label(root2,text='Zip: ' + req_ip_json['zip']).pack()
	lat = Label(root2, text='latitude: '+str(req_ip_json['lat'])).pack()
	lon = Label(root2,text='longitude: '+str(req_ip_json['lon'])).pack()
	timezone = Label(root2,text='Timezone: '+str(req_ip_json['timezone'])).pack()
	isp = Label(root2,text='ISP: '+req_ip_json['isp']).pack()
	org = Label(root2,text='Organisation: '+req_ip_json['org']).pack()
	As = Label(root2,text=req_ip_json['as']).pack()
	close_button = Button(root2, text="Close", command=root2.destroy).pack()
	root2.mainloop()
    

try:
    user_ip = urllib.request.urlopen('https://api.ipify.org/?format=json')
    user_json_value = json.loads(user_ip.read())
    main_menu = Tk()
    user_ip_label = Label(main_menu,text= 'Your IP: ' + user_json_value['ip']).grid(row=0,column=0)
    search_box = Entry(main_menu,borderwidth=3)
    search_box.grid(row=1,column=0)
    search_button = Button(main_menu,text='Search',command=search_button_click)
    search_button.grid(row=1,column=1)
    exit_button = Button(main_menu, text="Exit", command=main_menu.destroy).grid(column=0, row=2)
    copy_button = Button(main_menu,text='Copy' ,command=main_menu.clipboard_append(user_json_value['ip'])).grid(row=0,column=1)
    main_menu.mainloop()

except:
    internet_error = Tk()
    error = Label(internet_error,text='Check Your Internet Connection!').pack()
    exit_button = Button(internet_error,text='Close',command=internet_error.destroy).pack()
    internet_error.mainloop()
