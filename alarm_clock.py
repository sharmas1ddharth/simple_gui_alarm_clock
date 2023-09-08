from datetime import datetime

 

class AlarmClock:
    def __init__(self, alarm_time):
        self.alarm_time = alarm_time
        
    def check_if_alarm_time(self):
        current_time = datetime.now().strftime("%H:%M")
        if current_time == self.alarm_time:
            return True
        return False
        
        
