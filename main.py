import pyautogui as pa
import time
from PIL import ImageGrab


def collide(data):
	for lwrw in range(300,430):
		for uhdh in range(600,650):
			if data[lwrw,uhdh] < 100:
				return True
	return False


time.sleep(3)

# def test():
	# image = ImageGrab.grab().convert('L')
	# data = image.load()
	# for lwrw in range(300,430):
	# 	for uhdh in range(600,650):
	# 		data[lwrw,uhdh] = 0
	# image.show()

while True:
	image = ImageGrab.grab().convert('L')
	data = image.load()
	if collide(data):
		pa.press('up')

# test()




