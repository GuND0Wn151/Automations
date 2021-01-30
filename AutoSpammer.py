
# install this package
# pip install pyautogui
# Time module for sleeping for sometime

import pyautogui
import time

msg = "Message Here!"
# You can also input this values
n = 100# lenght of the spam


# waiting for sometimes before spaming
#waiting for 4 secs
count = 4
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("The spam has Started")

for i in range(int(n)):
	pyautogui.typewrite(msg + '\n')
	time.sleep(1)
	# sleeping for somtimes
