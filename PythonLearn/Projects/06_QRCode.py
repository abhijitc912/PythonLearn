# pip install pyqrcode
# pip install pypng

import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
git = "https://github.com/abhijitc912/PythonLearn/tree/master/PythonLearn"
pythoncert = "https://www.sololearn.com/certificates/CT-AWQIJOMR"
golangcert= "https://www.sololearn.com/certificates/CT-U7Y2USS1"


# Generate QR code 
url_git = pyqrcode.create(git)
url_py = pyqrcode.create(pythoncert)
url_go = pyqrcode.create(golangcert)
  
# Create and save the png file naming "myqr.png" 
url_git.svg("Projects/gitsvg.svg", scale = 8) 
url_git.png("Projects/gitpng.png", scale = 8) 
url_py.png("Projects/pycertpng.png", scale = 8)
url_go.png("Projects/gocert.png", scale = 8)
