# from datetime import datetime, timedelta
ShiftTypes = [
    ('morning', 'Morning'),
    ('evening', 'Evening'),
]
#def WorkHours(shifts):
 #   TotalWorkHours = timedelta()
    
 #  for shift in shifts:
    #    start_time = datetime.strptime(shift['start'], '%Y-%m-%d %H:%M:%S')
  #      end_time = datetime.strptime(shift['end'], '%Y-%m-%d %H:%M:%S')
    #    # Calculating the duration of the shift
    #    shift_duration = end_time - start_time
    #    
        # Adding the shift to total hours
    #    TotalWorkHours += shift_duration
    
    # Converting total work hours to sec and hours
   # total_hours = TotalWorkHours.total_seconds() // 3600
  #  total_minutes = (TotalWorkHours.total_seconds() % 3600) // 60
    
  #  return total_hours, total_minutes

# Example usage
#morning ={'start': '2024-05-19 08:00:00', 'end': '2024-05-19 16:00:00'},
#evening ={'start': '2024-05-19 12:00:00', 'end': '2024-05-19 20:00:00'},

#hours, minutes = WorkHours(morning or evening)
#print(f"Total working hours: {int(hours)} hours and {int(minutes)} minutes")