from rembg import remove
from PIL import Image

urt = Image.open ('img.jpg')
output = remove(url)
output.save('imgl.png')
