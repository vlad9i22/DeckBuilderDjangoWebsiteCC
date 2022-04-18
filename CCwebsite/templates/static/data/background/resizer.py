from PIL import Image

Image.open("background.png").resize((4000, 4000)).save("background.png")