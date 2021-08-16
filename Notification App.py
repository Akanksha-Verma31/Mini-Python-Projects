#pip install plyer
import time    # from plyer import the function time
from plyer import notification

if __name__ == '__main__':
  while True:
    notification.notify(
       title = "Take a class",
       message = "I have to take python classes",
       timeout = 10
    )
    time.sleep(15)  
    # after each n every 15s it will show us a notification for 10s then it will disappear and after 15s it will again show up
    
