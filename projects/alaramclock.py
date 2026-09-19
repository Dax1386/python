import pygame
import time
import datetime

def set_alarm(alarm_time):
    print(f"set time is {alarm_time}")
    set_music = "projects/alarm.mp3"
    is_running = True
    pygame.mixer.init()
    
    while is_running :
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if current_time == alarm_time:
            pygame.mixer.music.load(set_music)
            pygame.mixer.music.play()
            print("Alarm ringing!")
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False
        time.sleep(1)

    
if __name__ == "__main__":
    alarm_time = input("your alarm time(hh:mm:ss): ")
    set_alarm(alarm_time)