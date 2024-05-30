import qrcode
import io

img = qrcode.make('ali')
type(img)  # qrcode.image.pil.PilImage
# Save the image to a bytes buffer instead of a file
buffer = io.BytesIO()
img.save(buffer)
print(buffer)


