import pyautogui, time, random



def looking_busy(is_meeting = True):
    """This function moves your mouse to avoid idleness"""
    while is_meeting:

        x = random.randint(-5,5)
        y = random.randint(-5,5)
        pyautogui.moveRel(x,y,2)
        time.sleep(8)
        
        if x == y:
            is_meeting = False

    print('You are out of business.')
    
if __name__ == '__main__':
    looking_busy()