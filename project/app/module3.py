from pyzbar.pyzbar import decode
import cv2

# Read the image
img = cv2.imread('../data/img/test.png')
# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect and decode the QRs within the image
QRs = decode(gray_img)

# Print the results
for QR in QRs:
    print('Data:', QR.data.decode('utf-8'))
    print('Bounding Box:', QR.rect)

    print('Quality:', QR.quality * 100 , '%')