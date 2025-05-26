from rembg import remove
from PIL import Image
import io

# Charger l'image originale
with open("ayanogoat.jpg", "rb") as input_file:
    input_data = input_file.read()

# Supprimer le fond
output_data = remove(input_data)

# Convertir les données en image et sauvegarder
output_image = Image.open(io.BytesIO(output_data))
output_image.save("image_sans_fond.png")
