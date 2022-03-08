import pyautogui #pip install PyAutoGUI
import time
a = 0
while a <= 1000:
    time.sleep(3)
    pyautogui.typewrite('hello')
    pyautogui.press('enter')
    a += 1

    
    
    
    
    
    
    
    import pyautogui #pip install PyAutoGUI
import time

run = 0
while run <= 5:
    time.sleep(2)
    def Convert(string):
        list1=[]
        list1[:0]=string
        return list1

    str1="ABCD"
    split = Convert(str1)





    range = 0
    # run_2 = 0
    # while run_2 <= 10:
    for i in split:
        pyautogui.typewrite(split[range])
        time.sleep(2)
        pyautogui.press('enter')
    print(split)
    run += 1
    range += 1
    # run_2 += 1
