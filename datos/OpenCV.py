import cv2
import pyautogui
import numpy as np

# Captura la pantalla
screenshot = pyautogui.screenshot()
screenshot_np = np.array(screenshot)  # Convertir a matriz NumPy (OpenCV la necesita en este formato)

# Carga la imagen de referencia (el icono o botón que quieres encontrar)
template = cv2.imread('icono.png', cv2.IMREAD_GRAYSCALE)  # Imagen de referencia
screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)  # Convierte la captura a escala de grises

# Detección con OpenCV (Template Matching)
result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

if max_val > 0.8:  # Nivel de confianza (ajustable)
    print(f'¡Imagen encontrada en la posición: {max_loc}!')

x, y = max_loc  # Coordenadas donde se detectó la imagen
pyautogui.click(x + 10, y + 10)  # Hacer clic en el centro del cuadro
