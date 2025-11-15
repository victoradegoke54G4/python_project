import pyautogui, time, webbrowser


url = 'https://docs.google.com/forms/d/e/1FAIpQLScmxT0lAm3RMThA8K6Nw-TLeGFlMr9ykUlIlDmkbkKSvFkGMA/viewform'


form_data = [{'name': 'Alice', 'position': 'Python Developer', 'language': 'Python', 'agree_disagree': 4,
              'comments': 'I Love Python.'},
             {'name': 'John', 'position': 'IT Analyst', 'language': 'Swift', 'agree_disagree': 4, 'comments': 'n/a'},
             {'name': 'Edy', 'position': 'Project Manager', 'language': 'Java', 'agree_disagree': 1,
              'comments': 'I prefer Java over Python'},
             {'name': 'Redy', 'position': 'QA Tester', 'language': 'Python', 'agree_disagree': 5,
              'comments': 'Python is the best'},
             ]


print('Opening Form...(Press Ctrl + C to terminate the automation)')
time.sleep(5)
webbrowser.open(url)

def form_filler():
    global form_data
    pyautogui.PAUSE = 0.5
    print('Ensure that the browser window is active and the form is loaded!\n')

    z= 0.1
    print('Iniating automation...\n')
    for person in range(len(form_data)):
        time.sleep(4)

        pyautogui.typewrite('\t'*3, interval=z)
        pyautogui.typewrite(form_data[person]['name'], interval=z)

        pyautogui.typewrite('\t', interval=z)
        pyautogui.typewrite(form_data[person]['position'], interval=z)

        pyautogui.typewrite('\t', interval=z)

        if form_data[person]['language'] == 'Python':
            pyautogui.press(['space','tab','tab'])

        elif form_data[person]['language'] == 'Java':
            pyautogui.press(['right', 'tab', 'tab'])

        elif form_data[person]['language'] == 'Javascript':
            pyautogui.press(['right', 'right' 'tab', 'tab'])

        elif form_data[person]['language'] == 'Swift':
            pyautogui.press(['right', 'right', 'right', 'tab', 'tab'])
            
        else:
            pyautogui.press('tab')

        if form_data[person]['agree_disagree'] == 1:
            pyautogui.press(['space','tab','tab'], interval=z)

        elif form_data[person]['agree_disagree'] == 2:
            pyautogui.press(['right', 'tab','tab'])
            
        elif form_data[person]['agree_disagree'] == 3:
            pyautogui.press(['right', 'right', 'tab','tab'])

        elif form_data[person]['agree_disagree'] == 4:
            pyautogui.press(['right', 'right', 'right', 'tab','tab'])

        elif form_data[person]['agree_disagree'] == 5:
            pyautogui.press(['right', 'right', 'right', 'right', 'tab','tab'])

        else:
            pyautogui.press('tab')

        pyautogui.write(form_data[person]['comments'],interval=z )
            
        #clicking submit button
        pyautogui.press('tab')
        pyautogui.press('Enter')

        # #submit another response
        print(f'{form_data[person]['name']}\'s form Submitted')
        if person != len(form_data)-1:
            time.sleep(2)
            pyautogui.press('tab')
            pyautogui.press('Enter')

    print('\nAutomation terminated...')
    print('The bot says, thank you')

if __name__ =='__main__':
    form_filler()