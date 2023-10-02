import customtkinter

COUNTER = 0

def bouton_clique(): 
    global COUNTER
    COUNTER+=1  
    label.configure(text="Compteur : "+str(COUNTER))
    progressbar.set(COUNTER/100)

app = customtkinter.CTk()
app.title("app")
app.geometry("400x150")

label = customtkinter.CTkLabel(app, text="Compteur : "+str(COUNTER))
label.grid(row=0, column=0, pady=(30,10))

progressbar = customtkinter.CTkProgressBar(app, orientation="horizontal")
progressbar.set(0)
progressbar.grid(row=1, column=0, pady=(10,10))

button = customtkinter.CTkButton(app, text="Appuyer ici", command=bouton_clique)
button.grid(row=2, column=0, pady=20)

app.grid_columnconfigure(0, weight=1)

app.mainloop()