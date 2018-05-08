import os
import sys
import subprocess
cmd ="cd"
os.system(cmd)
cmd= "sudo apt install tesseract-ocr"
os.system(cmd)
cmd = "sudo apt install libtesseract-dev"
os.system(cmd)
cmd = "cd /usr/share/tesseract-ocr/4.00"
os.system(cmd)
cmd = "firefox https://github.com/tesseract-ocr/tessdata/blob/master/guj.traineddata"
os.system(cmd)

cmd = "tesseract 1.png 1_out -l guj"
os.system(cmd)

cmd = "tesseract 2.png 2_out -l guj"
os.system(cmd)

cmd = "tesseract 3.png 4_out -l guj"
os.system(cmd)
