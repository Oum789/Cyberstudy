from tkinter import *
import requests

API_ENDPOINT_SEARCH_TITLE = "http://127.0.0.1:8000/search_title"

def on_click_search_title():
    payload = {
        "title" : title.get()
    }
    response = requests.post(API_ENDPOINT_SEARCH_TITLE, json=payload)
    if response.ok:
        if response.json() == {}:
            Button(root, text="Result Not Found",bg="white").grid(row=2, column=0, columnspan=2)
        else:
            for i in range (len(response.json())):
               Button(root, text=str(response.json()[str(i)]),bg="white").grid(row=2+i, column=0, columnspan=2)

root = Tk()
root.option_add("*Font", "impact 18")
title = StringVar()

Label(root, text="Search Title :").grid(row=0, column=0, padx=10, ipady=5, sticky='W')
Entry(root, textvariable=title, width=100, justify="left").grid(row=0, column=1, padx=10)
title.set("")

Button(root, text=" Search ", bg="green", command=on_click_search_title).grid(row=1, column=0, columnspan=2)

root.mainloop()