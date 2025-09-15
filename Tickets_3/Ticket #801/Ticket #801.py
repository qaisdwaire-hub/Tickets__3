import tkinter as tk
import requests
import threading

def get_weather():
 city = entry.get()
 data = requests.get(f"https://wttr.in/{city}?format=3").text

 if not city.replace(" ", "").isalpha():
     label.config(text="error", font=('arial', 20, 'bold'), anchor='center')
     return

 label.config(text=data, font=('arial', 20, 'bold'), anchor='center')

root = tk.Tk()
root.geometry('500x500')
root.configure(bg="lightblue")

entry = tk.Entry(root,bg="honeydew"); entry.pack()
button = tk.Button(root, text="Get Weather",bg="steelblue",command=lambda:threading.Thread(target=get_weather()).start()); button.pack()
label = tk.Label(root, text="",font=('arial',20),bg="lightblue",anchor='center'); label.pack()

root.mainloop()