# Ejemplo de interfaz grafica montada en Tkinter
import tkinter as tk
from tkinter import messagebox

# Función para mostrar el mensaje de bienvenida
def mostrar_bienvenida():
    nombre = entrada_nombre.get()
    if nombre:
        messagebox.showinfo("Bienvenido", f"¡Hola, {nombre}! Bienvenido a la aplicación.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa tu nombre.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Saludo al usuario")

# Crear y colocar los widgets
etiqueta = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta.pack(pady=10)

entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=10)

boton_bienvenida = tk.Button(ventana, text="Saludar", command=mostrar_bienvenida)
boton_bienvenida.pack(pady=10)

# Ejecutar el bucle principal
ventana.mainloop()
