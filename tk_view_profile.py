# from tkinter import *
# import requests
 
# API_ENDPOINT = "http://127.0.0.1:8000/view_profile"

# def on_view_profile():
#     response = requests.get(API_ENDPOINT)
#     if response.ok:
#         Label(root, text="Result : " + str(response.json())).grid(row=4, column=1, sticky=W,padx=5, pady=5)



# root = Tk()
# root.option_add("*Font", "impact 20")

# Button(root, text=" View Profile ", bg="green", command=on_view_profile).grid(row=0, column=0, columnspan=2)

# root.mainloop()