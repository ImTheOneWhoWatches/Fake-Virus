import rotatescreen
import time

def rotate_screen_to(screen, angle):
    screen.rotate_to(angle)
    time.sleep(0.5)  # Pause for 2 seconds between each rotation

if __name__ == "__main__":
    screen = rotatescreen.get_primary_display()
    
    # Rotate to 90 degrees
    rotate_screen_to(screen, 90)

    # Rotate to 180 degrees
    rotate_screen_to(screen, 180)
    
    # Rotate to 270 degrees
    rotate_screen_to(screen, 270)


    # Rotate to 0 degrees (back to default)
    rotate_screen_to(screen, 0)
