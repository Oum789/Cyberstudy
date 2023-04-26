from tkinter import *
import requests

API_ENDPOINT_LOGIN = "http://127.0.0.1:8000/login"

def on_click_login():
    payload = {
        "email" : email.get(),
        "password" : password.get()
    }
    response = requests.post(API_ENDPOINT_LOGIN, json=payload)
    if response.ok:
        Label(root, text=str(response.json()["status"])).grid(row=4, column=0, columnspan=2)

root = Tk()
root.option_add("*Font", "impact 18")
email = StringVar()
password = StringVar()

Label(root, text="Login").grid(row=0, column=0, padx=10, ipady=5)

Label(root, text="Email :").grid(row=1, column=0, padx=10, ipady=5, sticky='W')
Entry(root, textvariable=email, width=100, justify="left").grid(row=1, column=1, padx=10)

Label(root, text="Password :").grid(row=2, column=0, padx=10, ipady=5, sticky='W')
Entry(root, textvariable=password, width=100, justify="left").grid(row=2, column=1, padx=10)
email.set("")
password.set("")

Button(root, text=" Login ", bg="green", command=on_click_login).grid(row=3, column=0, columnspan=2)

root.mainloop()