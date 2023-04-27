# from tkinter import *
# import requests
 
# API_ENDPOINT = "http://127.0.0.1:8000/change_username"

# def on_change_username():
#     payload = {
#         "password" : password.get(),
#         "new username" : new_username.get()
#     }
#     response = requests.post(API_ENDPOINT, json=payload)
#     if response.ok:
#         Label(root, text="Result : " + (response.json()["status"])).grid(row=4, column=1, sticky=W,padx=5, pady=5)



# root = Tk()
# root.option_add("*Font", "impact 20")
# password = StringVar()
# new_username = StringVar()

# Label(root, text="New Username :").grid(row=0, column=0, padx=10, ipady =5, sticky=E)
# Entry(root, textvariable=new_username, width=12, justify="left").grid(row=0, column=1, padx=10)

# Label(root, text="Password :").grid(row=1, column=0, padx=10, ipady =5, sticky=E)
# Entry(root, textvariable=password, width=12, justify="left").grid(row=1, column=1, padx=10)

# Button(root, text=" Change Username ", bg="green", command=on_change_username).grid(row=5, column=0, columnspan=2)

# root.mainloop()