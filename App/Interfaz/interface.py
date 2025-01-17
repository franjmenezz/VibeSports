import tkinter as tk
from tkinter import messagebox
import os

# Funciones de registro e inicio de sesión
def register_user(username_entry, password_entry, register_window):
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        with open("users.txt", "a") as file:
            file.write(f"{username},{password}\n")
        messagebox.showinfo("Registro", "Usuario registrado exitosamente.")
        register_window.destroy()
        main_interface()  # Ir directamente a la interfaz principal tras registrar
    else:
        messagebox.showwarning("Error", "Por favor completa todos los campos.")

# Ventana de registro
def register_window():
    window = tk.Tk()
    window.title("Registro")
    window.geometry("300x200")

    username_label = tk.Label(window, text="Usuario:")
    username_label.pack(pady=5)
    username_entry = tk.Entry(window)
    username_entry.pack(pady=5)

    password_label = tk.Label(window, text="Contraseña:")
    password_label.pack(pady=5)
    password_entry = tk.Entry(window, show="*")
    password_entry.pack(pady=5)

    register_button = tk.Button(window, text="Registrar", command=lambda: register_user(username_entry, password_entry, window))
    register_button.pack(pady=10)

    # Botón para regresar a la ventana principal
    def go_back():
        window.destroy()
        select_action_window()

    back_button = tk.Button(window, text="Volver", command=go_back)
    back_button.pack(pady=5)

    window.mainloop()

def login_user(username_entry, password_entry, login_window):
    username = username_entry.get()
    password = password_entry.get()

    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            users = file.readlines()
            for user in users:
                stored_username, stored_password = user.strip().split(",")
                if username == stored_username and password == stored_password:
                    messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso.")
                    login_window.destroy()
                    main_interface()  # Llama a la interfaz principal
                    return
    
    messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

# Ventana de inicio de sesión
def login_window():
    window = tk.Tk()
    window.title("Inicio de sesión")
    window.geometry("300x200")

    username_label = tk.Label(window, text="Usuario:")
    username_label.pack(pady=5)
    username_entry = tk.Entry(window)
    username_entry.pack(pady=5)

    password_label = tk.Label(window, text="Contraseña:")
    password_label.pack(pady=5)
    password_entry = tk.Entry(window, show="*")
    password_entry.pack(pady=5)

    login_button = tk.Button(window, text="Iniciar sesión", command=lambda: login_user(username_entry, password_entry, window))
    login_button.pack(pady=10)

    # Botón para regresar a la ventana principal
    def go_back():
        window.destroy()
        select_action_window()

    back_button = tk.Button(window, text="Volver", command=go_back)
    back_button.pack(pady=5)

    window.mainloop()

# Interfaz principal
def main_interface():
    def like_post(post_id):
        messagebox.showinfo("Like", f"Has dado like al post {post_id}.")

    def open_post(post_id):
        messagebox.showinfo("Post", f"Abriendo el post {post_id}.")

    def create_post(frame, post_id, content):
        post_frame = tk.Frame(frame, borderwidth=1, relief="solid")
        post_frame.pack(padx=10, pady=10, anchor="center")

        # Contenido del post
        content_label = tk.Label(post_frame, text=content, wraplength=400, anchor="center", justify="center")
        content_label.pack(padx=5, pady=5, anchor="center")

        # Botón de Like
        like_button = tk.Button(post_frame, text="Like", command=lambda: like_post(post_id))
        like_button.pack(pady=5, anchor="center")

    # Configuración principal
    root = tk.Tk()
    root.title("Interfaz de Noticias y Social")
    root.geometry("800x600")

    # Menú superior
    menu_frame = tk.Frame(root, borderwidth=1, relief="solid")
    menu_frame.pack(side="top", fill="x")

    menu_frame.grid_columnconfigure(0, weight=1)
    menu_frame.grid_columnconfigure(1, weight=1)

    noticias_button = tk.Button(menu_frame, text="NOTICIAS", relief="flat")
    noticias_button.grid(row=0, column=0, padx=10, pady=5)

    social_button = tk.Button(menu_frame, text="SOCIAL", relief="flat")
    social_button.grid(row=0, column=1, padx=10, pady=5)

    # Barra de búsqueda
    search_frame = tk.Frame(root)
    search_frame.pack(pady=20)

    search_entry = tk.Entry(search_frame, width=50)
    search_entry.pack(side="left", padx=5)

    search_button = tk.Button(search_frame, text="🔍")
    search_button.pack(side="left")

    # Área de publicaciones
    posts_frame = tk.Frame(root)
    posts_frame.pack(fill="both", expand=True, pady=20)

    # Crear dos posts
    create_post(posts_frame, 1, "Este es el contenido del post número 1. Aquí puedes leer información interesante sobre este post.")
    create_post(posts_frame, 2, "Este es el contenido del post número 2. Aquí puedes leer información interesante sobre este post.")

    # Botón flotante en la esquina inferior derecha
    def floating_button_action():
        messagebox.showinfo("Botón flotante", "Has presionado el botón flotante.")

    floating_button = tk.Button(root, text="+", command=floating_button_action, width=4, height=2, bg="lightblue", font=("Arial", 14, "bold"))
    floating_button.place(relx=0.95, rely=0.9, anchor="center")

    # Ejecutar la aplicación
    root.mainloop()

# Ventana de selección de acción
def select_action_window():
    window = tk.Tk()
    window.title("Selecciona una acción")
    window.geometry("300x200")

    def open_register_window():
        window.destroy()
        register_window()

    def open_login_window():
        window.destroy()
        login_window()

    # Botones para seleccionar acción
    register_button = tk.Button(window, text="Registrarse", command=open_register_window, width=20)
    register_button.pack(pady=10)

    login_button = tk.Button(window, text="Iniciar sesión", command=open_login_window, width=20)
    login_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    select_action_window()
