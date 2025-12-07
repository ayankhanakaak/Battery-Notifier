import psutil
import time
import threading
from plyer import notification
import sys

def monitor_battery(low_threshold, high_threshold):
    '''Monitor battery level and send notifications when it crosses thresholds'''
    print(f"Starting battery monitor with thresholds: {low_threshold}%-{high_threshold}%")
    print("Press Ctrl+C to stop monitoring")
    
    last_notification = {"low": 0, "high": 0}
    
    '''5 minutes between same-type notifications'''
    notification_cooldown = 300
    
    try:
        while True:
            battery = psutil.sensors_battery()
            if battery:
                percent = battery.percent
                plugged = battery.power_plugged
                current_time = time.time()
                
                '''Notify when battery is high and plugged in'''
                if percent > (high_threshold-1) and plugged:
                    '''
                    if current_time - last_notification["high"] > notification_cooldown:
                    '''
                    message = "Please do not charge to preserve battery health."
                    send_notification(f"Battery at {percent}% 👍🏻", message)
                    last_notification["high"] = current_time
                
                #Notify when battery is low and not plugged in
                elif percent < (low_threshold+1) and not plugged:
                    '''
                    if current_time - last_notification["low"] > notification_cooldown:
                    '''
                    message = f"It's charging time."
                    send_notification(f"Battery at {percent}% ⚠️", message)
                    last_notification["low"] = current_time
            
            '''Check every 60 seconds'''
            time.sleep(60)
            
    except KeyboardInterrupt:
        print("\nStopping battery monitor")
        sys.exit(0)

def send_notification(title, message):
    '''Send system notification using plyer (cross-platform)'''
    try:
        notification.notify(
            title=title,
            message=message,
            timeout=10,  #Notification stays for 10 seconds
            app_name="Battery Monitor"
        )
    except Exception as e:
        print(f"Failed to send notification: {e}")

if __name__ == "__main__":
    '''Set your desired thresholds here'''
    LOW_THRESHOLD = 20
    HIGH_THRESHOLD = 80
    
    '''Start monitoring in a background thread'''
    monitor_thread = threading.Thread(
        target=monitor_battery,
        args=(LOW_THRESHOLD, HIGH_THRESHOLD),
        daemon=True
    )
    monitor_thread.start()
    
    '''Keep the main thread alive'''
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting battery monitor")