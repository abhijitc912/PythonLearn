import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://github.com/abhijitc912/PythonLearn/tree/master/PythonLearn"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("Projects/qrcode.svg", scale = 8) 
