import cv2
import os

def count_birds_in_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Nie można wczytać obrazu: {image_path}")
        return 0

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return len(contours)

def process_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder nie istnieje: {folder_path}")
        return []

    results = []
    for filename in os.listdir(folder_path):
        image_path = os.path.join(folder_path, filename)

        print(f"Przetwarzanie pliku: {image_path}")

        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            bird_count = count_birds_in_image(image_path)
            results.append((filename, bird_count))
        else:
            print(f"Pominięto plik (nie obraz): {filename}")
    return results

folder_path = r"D:\Studia\UG_IO_2024-25\birds"

if not os.path.exists(folder_path):
    print(f"Folder nie istnieje: {folder_path}")
else:
    results = process_folder(folder_path)
    if not results:
        print("Nie znaleziono żadnych obrazów w folderze.")
    else:
        for filename, bird_count in results:
            print(f"{filename}: {bird_count} ptaków")

# Użyte filtry:
# Rozmycie - GaussianBlur
# Progowanie adaptacyjne - adaptiveThreshold
# Operacje morfologiczne
# Użyto findContours  do znalezienia konturów ptaków