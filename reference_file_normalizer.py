import os
import tkinter as tk
from tkinter import filedialog
from googletrans import Translator

def translate_name(name):
    # Inicializar el traductor
    translator = Translator()
    try:
        # Traducir el nombre del archivo al español
        translated = translator.translate(name, src='en', dest='es')
        return translated.text
    except Exception as e:
        print(f"Error en la traducción: {e}")
        return name  # Devolver el nombre original en caso de error

def rename_files(file_paths):
    # Crear una instancia del traductor
    translator = Translator()

    # Recorrer todos los archivos seleccionados
    for file_path in file_paths:
        file_name = os.path.basename(file_path)  # Obtener solo el nombre del archivo
        file_dir = os.path.dirname(file_path)  # Obtener el directorio del archivo

        # Separar el nombre del archivo de la extensión
        name, extension = os.path.splitext(file_name)

        # Reemplazar "_" y "-" por espacios, y eliminar los signos de exclamación y comillas
        # También reemplazamos puntos y comas en el nombre, no en la extensión
        new_name = (
            name.replace("_", " ")
                .replace("-", " ")
                .replace(".", " ")
                .replace(",", " ")
                .replace("!", "")
                .replace("'", "")
                .replace('"', "")
                .lower()  # Convertir a minúsculas
        )

        # Traducir el nombre al español
        new_name = translate_name(new_name)

        # Capitalizar la primera letra de cada palabra
        new_name = new_name.title()

        # Crear el nuevo nombre del archivo (sin tocar la extensión)
        new_file_name = f"{new_name}{extension}"

        # Verificar si se hizo algún cambio (para evitar renombrar innecesariamente)
        if new_file_name != file_name:
            # Crear la nueva ruta con el nuevo nombre del archivo
            new_file_path = os.path.join(file_dir, new_file_name)

            # Renombrar el archivo
            os.rename(file_path, new_file_path)
            
            print(f"Archivo renombrado: '{file_name}' -> '{new_file_name}'")
        else:
            print(f"El archivo '{file_name}' ya está correctamente formateado.")

# Crear la ventana principal de tkinter para seleccionar archivos
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Abrir el cuadro de diálogo para seleccionar uno o más archivos
file_paths = filedialog.askopenfilenames(title="Selecciona uno o varios archivos")

# Ejecutar la función para renombrar archivos
if file_paths:
    rename_files(file_paths)
else:
    print("No se seleccionaron archivos.")
