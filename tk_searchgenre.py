from tkinter import *
import requests

API_ENDPOINT_SEARCH_GENRE = "http://127.0.0.1:8000/search_genre"

def on_click_search_genre():
    payload = {
        "genre" : select_opt.get()
    }
    response = requests.post(API_ENDPOINT_SEARCH_GENRE, json=payload)
    if response.ok:
        for i in range (len(response.json())):
            Button(root, text=str(response.json()[str(i)]),bg="white").grid(row=2+i, column=0, columnspan=2)

root = Tk()
root.option_add("*Font", "impact 18")
select_opt = StringVar()

data_list = ["science","math","entertain","business"]
om = OptionMenu(root, select_opt, *data_list)
om.grid(row=0, column=0)
om.config(width=15)

Button(root, text=" Search Genre", bg="green", command=on_click_search_genre).grid(row=1, column=0, columnspan=2)

root.mainloop()