import cv2
import pyautogui
import numpy as np
import time

def detectar_y_hacer_clic(imagen_referencia, umbral=0.8):
    # Captura la pantalla
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)  # Convertir a matriz NumPy

    # Cargar la imagen de referencia (el objeto que buscas)
    template = cv2.imread(imagen_referencia, cv2.IMREAD_GRAYSCALE)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

    # Realizar la detección
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val > umbral:
        print(f'¡Imagen encontrada! Coordenadas: {max_loc}')
        x, y = max_loc
        pyautogui.click(x + 10, y + 10)  # Clic en el centro de la imagen detectada
        return True
    else:
        print('No se encontró la imagen.')
        return False

# Ejecutar el bot cada 5 segundos
while True:
    detectar_y_hacer_clic('icono.png', umbral=0.8)
    time.sleep(5)  # Esperar 5 segundos antes de la siguiente búsqueda
