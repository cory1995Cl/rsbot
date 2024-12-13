import tkinter as tk  # Interfaz gráfica
import pyautogui  # Captura de pantalla y clics
import datetime  # Para nombrar la captura con la fecha y hora
import os  # Para manejar directorios
import pandas as pd  # Para registrar acciones en CSV
import pygetwindow as gw  # Para controlar múltiples ventanas del juego
import random  # Para generar tiempos de espera aleatorios
import time  # Para pausar la ejecución entre clics

# ---------------------------
# Configuración inicial
# ---------------------------
DIRECTORIO_CAPTURAS = 'captura'
DIRECTORIO_DATOS = 'datos'
ARCHIVO_ACCIONES = os.path.join(DIRECTORIO_DATOS, 'acciones.csv')
os.makedirs(DIRECTORIO_CAPTURAS, exist_ok=True)  # Crear carpeta de capturas si no existe
os.makedirs(DIRECTORIO_DATOS, exist_ok=True)  # Crear carpeta de datos si no existe

# ---------------------------
# Funciones de los botones
# ---------------------------

def capturar_pantalla():
    """Captura la pantalla y la guarda con el nombre basado en la fecha y hora actual en la carpeta 'captura'"""
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Formato: 2024-12-12_14-35-22
    nombre_archivo = f"captura_{fecha_hora}.png"
    ruta_archivo = os.path.join(DIRECTORIO_CAPTURAS, nombre_archivo)  # Ruta de la captura dentro de la carpeta
    
    captura = pyautogui.screenshot()  # Captura de pantalla
    captura.save(ruta_archivo)  # Guarda la captura como archivo de imagen
    print(f"Captura de pantalla guardada en {ruta_archivo}")


def registrar_accion(ventana_id, accion, coordenadas=None):
    """Registra una acción realizada por el bot en un archivo CSV"""
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    datos = {'ventana_id': ventana_id, 'accion': accion, 'coordenadas': coordenadas, 'fecha_hora': fecha_hora}
    df = pd.DataFrame([datos])  # Crea un DataFrame con una sola fila
    if not os.path.isfile(ARCHIVO_ACCIONES):
        df.to_csv(ARCHIVO_ACCIONES, index=False)  # Crea el archivo CSV si no existe
    else:
        df.to_csv(ARCHIVO_ACCIONES, mode='a', index=False, header=False)  # Añade la fila al CSV existente
    print(f"Acción registrada: {datos}")


def listar_ventanas():
    """Lista las ventanas activas del sistema y selecciona las relacionadas con RuneLite"""
    ventanas = gw.getAllTitles()
    ventanas_juego = [ventana for ventana in ventanas if 'RuneLite' in ventana]  # Filtrar ventanas con 'RuneLite' en el título
    print(f"Ventanas detectadas: {ventanas_juego}")
    return ventanas_juego


# ---------------------------
# Interfaz gráfica (GUI) con Tkinter
# ---------------------------

def main():
    """Función principal para crear la ventana e inicializar los botones"""
    
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Bot de Automatización de Videojuegos")
    ventana.geometry("400x600")  # Tamaño de la ventana
    
    # Crear un título o etiqueta
    titulo = tk.Label(ventana, text="Bot de Automatización de Videojuegos", font=("Arial", 16))
    titulo.pack(pady=10)  # Espaciado superior
    
    # Botón para capturar la pantalla
    boton_capturar = tk.Button(ventana, text="Capturar Pantalla", command=capturar_pantalla, bg="lightblue", font=("Arial", 12))
    boton_capturar.pack(pady=10)  
    
    # Botón para listar ventanas activas
    boton_listar_ventanas = tk.Button(ventana, text="Listar Ventanas", command=listar_ventanas, bg="lightgreen", font=("Arial", 12))
    boton_listar_ventanas.pack(pady=10)  
    
    # Botón para realizar la acción de "Kill Chicken"
    boton_kill_chicken = tk.Button(ventana, text="Kill Chicken", command=lambda: realizar_clics_en_imagenes_en_todas_ventanas(['captura/inventory.png', 'captura/logout.png', 'captura/equip.png']), bg="lightcoral", font=("Arial", 12))
    boton_kill_chicken.pack(pady=10)  
    
    # Botón para salir de la aplicación
    boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy, bg="red", font=("Arial", 12))
    boton_salir.pack(pady=10)  
    
    # Inicia el loop principal de la interfaz
    ventana.mainloop()

# Ejecutar la aplicación principal
if __name__ == "__main__":
    main()
