from tkinter import *
import requests

API_ENDPOINT_SEARCH_DURATION = "http://127.0.0.1:8000/search_duration"

def on_click_search_duration():
    payload = {
        "min" : int(minimum.get()),
        "max" : int(maximum.get())
    }
    response = requests.post(API_ENDPOINT_SEARCH_DURATION, json=payload)
    if response.ok:
        if response.json() == {}:
            Button(root, text="Result Not Found",bg="white").grid(row=4, column=0, columnspan=2)
        else:
            for i in range (len(response.json())):
               Button(root, text=str(response.json()[str(i)]),bg="white").grid(row=4+i, column=0, columnspan=2)

root = Tk()
root.option_add("*Font", "impact 18")
minimum = StringVar()
maximum = StringVar()

Label(root, text="Search Durartion :").grid(row=0, column=0, padx=10, ipady=5, sticky='W')

Label(root, text="Minimun :").grid(row=1, column=0, padx=10, ipady=5, sticky='W')
Entry(root, textvariable=minimum, width=100, justify="left").grid(row=1, column=1, padx=10)

Label(root, text="Maximum :").grid(row=2, column=0, padx=10, ipady=5, sticky='W')
Entry(root, textvariable=maximum, width=100, justify="left").grid(row=2, column=1, padx=10)
minimum.set("")
maximum.set("")

Button(root, text=" Search ", bg="green", command=on_click_search_duration).grid(row=3, column=0, columnspan=2)

root.mainloop()