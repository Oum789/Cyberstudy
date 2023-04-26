from tkinter import *
import requests

API_ENDPOINT_SEARCH_DIFF = "http://127.0.0.1:8000/search_diff"

def on_click_search_diff():
    payload = {
        "diff" : int(diff.get())
    }
    response = requests.post(API_ENDPOINT_SEARCH_DIFF, json=payload)
    if response.ok:
        if response.json() == {}:
            Button(root, text="Result Not Found",bg="white").grid(row=2, column=0, columnspan=2)
        else:
            for i in range (len(response.json())):
               Button(root, text=str(response.json()[str(i)]),bg="white").grid(row=2+i, column=0, columnspan=2)

root = Tk()
root.option_add("*Font", "impact 18")
diff = StringVar()

Label(root, text="Search Difficulty :").grid(row=0, column=0, padx=10, ipady=5, sticky='W')
Entry(root, textvariable=diff, width=100, justify="left").grid(row=0, column=1, padx=10)
diff.set("")

Button(root, text=" Search ", bg="green", command=on_click_search_diff).grid(row=1, column=0, columnspan=2)

root.mainloop()