import pyautogui

# screenWidth, screenHeight = pyautogui.size()  # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
# print('Screen width, height:', screenWidth, screenHeight)
# currentMouseX, currentMouseY = pyautogui.position()  # Returns two integers, the x and y of the mouse cursor's current position.
# print('Mouse position:', currentMouseX, currentMouseY)
# pyautogui.moveTo(100, 150)  # Move the mouse to the x, y coordinates 100, 150.
# pyautogui.click()  # Click the mouse at its current location.
# pyautogui.click(200, 220)  # Click the mouse at the x, y coordinates 200, 220.
# pyautogui.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
# pyautogui.doubleClick()  # Double click the mouse at the
# pyautogui.moveTo(500, 500, duration=2,
#                  tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
# pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
# pyautogui.press('esc')  # Simulate pressing the Escape key.
# pyautogui.keyDown('shift')
# pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
# pyautogui.keyUp('shift')
# pyautogui.hotkey('ctrl', 'c')
# pyautogui.screenshot('test.png')  # Take a screenshot of the active monitor.
# pyautogui.screenshot('test.png', region=(100, 100, 200, 200))  # Take a screenshot of a specific region on the screen.

"""
    For more information on pyautogui, see:
"""

# pyautogui.alert('This is an alert box.')
# pyautogui.confirm('Shall I proceed?')
# pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
# pyautogui.prompt('What is your name?')
# pyautogui.password('Enter password (text will be hidden)')

"""
    find out image location
"""
# im1 = pyautogui.screenshot()
# im1.save('button.png')
# button7location = pyautogui.locateOnScreen('button.png')  # returns (left, top, width, height) of matching region
# buttonx, buttony = pyautogui.center(button7location)
# pyautogui.click(buttonx, buttony)

pyautogui.moveTo(400, 800)
x, y = pyautogui.position()
pyautogui.click(x, y)
pyautogui.typewrite("Hello Friends! I'm here to let you know about france visa!", interval=0.10)
pyautogui.countdown(5)
# pyautogui.press('enter')
