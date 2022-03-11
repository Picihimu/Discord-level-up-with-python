
import pyautogui  # pip install PyAutoGUI
import time
import random

run = 0
# def Convert(string):
#         list1 = []
#         list1[:0] = string
#         return list1

str1 ="Tohelpmakthiseasierwehavereatedprintablecardsothatyoucanwriteyourownkindnessquote tosend to a friend relative or even co-worker. Check out our featured Sunny Sentiments bouquet browse our collection of"
# split = Convert(str1)
bday = "happy birthday Nomaan Mia" #<@!760875948290736188>
# print(split)

a = 0
while a <= 10000:
    # text = random.choice(str1)
    response_delay = random.randint(3, 7)
    time.sleep(response_delay)

    pyautogui.typewrite(bday)
    time.sleep(response_delay)
    pyautogui.press('enter')
    a += 1



    # range = 0
    # # run_2 = 0
    # # while run_2 <= 10:
    # for i in split:
    #     range += 1
    #     pyautogui.typewrite(split[range])
    #     time.sleep(2)
    #     # pyautogui.press('enter')
    # print(split[range])
    # run += 1
    #

    # run_2 += 1
