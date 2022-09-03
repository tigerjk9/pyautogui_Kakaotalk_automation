import pyautogui
import os

#경로를 .py파일을 실행하는 경로로 이동합니다. pyautogui에서 한글을 인식하지 못하기 때문에 현재 경로로 이동하였습니다.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

picPosition = pyautogui.locateOnScreen('pic1.png')  # pic1.png 파일과 동일한 그림을 찾아 좌표를 출력합니다. 
print(picPosition)

if  picPosition is None:    # pic1.png 파일과 동일한 그림을 찾지 못했다면 pic2.png 파일과 동일한 그림을 찾아 좌표를 출력합니다.
    picPosition = pyautogui.locateOnScreen('pic2.png')
    print(picPosition)

if  picPosition is None:    # pic1, pic2.png 파일과 동일한 그림을 찾지 못했다면 pic3.png 파일과 동일한 그림을 찾아 좌표를 출력합니다.
    picPosition = pyautogui.locateOnScreen('pic3.png')
    print(picPosition)