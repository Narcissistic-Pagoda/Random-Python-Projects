import pyautogui as auto
print('Press Ctrl-C to quit!')
try:
    while True:
        print(auto.position())
except KeyboardInterrupt:
    print('\nDone')