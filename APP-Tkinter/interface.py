import customtkinter as ctk
import pyautogui
import time

def pegarTexto():
    a = entrada1.get()
    z = int(entrada2.get())
    x = 0

    time.sleep(5)  # Espera 5 segundos antes de começar a digitar
    while x < z:
        pyautogui.write(f'{a}\n')
        x += 1

# Inicializa o aplicativo
ctk.set_appearance_mode("light")  # Modo claro
ctk.set_default_color_theme("blue")  # Tema azul

root = ctk.CTk()  # Usando CustomTkinter

root.geometry("400x500")
root.title("MyApp")
root.config(bg="lightblue")


# Entradas
entrada1 = ctk.CTkEntry(root, width=200)
entrada1.place(relx=0.32, rely=0.05)

entrada2 = ctk.CTkEntry(root, width=200)
entrada2.place(relx=0.32, rely=0.1)

# Botão
btn = ctk.CTkButton(root, text="Enviar", 
                     fg_color="darkgreen", 
                     text_color="white",
                     command=pegarTexto)
btn.place(relx=0.45, rely=0.15)

root.mainloop()
