# from tkinter import *
# import requests
 
# API_ENDPOINT = "http://127.0.0.1:8000/change_password"

# def on_change_password():
#     payload = {
#         "old password" : old_password.get(),
#         "new password" : new_password.get()
#     }
#     response = requests.post(API_ENDPOINT, json=payload)
#     if response.ok:
#         Label(root, text="Result : " + response.json()["status"]).grid(row=4, column=1, sticky=W,padx=5, pady=5)



# root = Tk()
# root.option_add("*Font", "impact 20")
# old_password = StringVar()
# new_password = StringVar()

# Label(root, text="New Password :").grid(row=0, column=0, padx=10, ipady =5, sticky=E)
# Entry(root, textvariable=new_password, width=12, justify="left").grid(row=0, column=1, padx=10)

# Label(root, text="Old Password :").grid(row=1, column=0, padx=10, ipady =5, sticky=E)
# Entry(root, textvariable=old_password, width=12, justify="left").grid(row=1, column=1, padx=10)

# Button(root, text=" Change Password ", bg="green", command=on_change_password).grid(row=5, column=0, columnspan=2)

# root.mainloop()