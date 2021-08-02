def add_time(start, duration, day_of_week = False):
  days_of_the_week_index = {"moonday":0, "tuesday":1, "wednesday":2, "thursday":3, "friday":4, "saturday":5, "sunday": 6}
  days_of_the_week_array = ["Moonday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  duration_tuple = duration.partition(":")  
  duration_hours = int(duration_tuple[0])
  duration_minutes = int(duration_tuple[2])  

  tempo = start.partition(":")
  tempo_minutes_tuple = tempo[2].partition(" ")
  hours = int(tempo[0])
  minutes = int(tempo_minutes_tuple[0])

  am_or_pm = tempo_minutes_tuple[2]
  am_or_pm_flip = {"AM": "PM", "PM": "AM"}

  qnt_of_days = int(duration_hours/24)

  new_minutes = minutes + duration_minutes

  if (new_minutes >= 60):
    hours += 1
    new_minutes = int(new_minutes) % 60
  qnt_am_or_pm_flips = int((hours + duration_hours) / 12)
  final_hours = (hours + duration_hours) % 12

  
 
  if new_minutes > 9:  
    new_minutes = new_minutes
  else:
    new_minutes = "0" + str(new_minutes)
  
  if final_hours == 0:
    final_hours = 12
  else:
    final_hours = final_hours
  
  if(am_or_pm == "PM" and hours + (duration_hours % 12) >= 12):
    qnt_of_days +=1
  
  if qnt_am_or_pm_flips % 2 == 1:
    am_or_pm = am_or_pm_flip[am_or_pm]
  else:
    am_or_pm = am_or_pm

  new_time = str(final_hours) + ":" + str(new_minutes) + " " + am_or_pm

  if(day_of_week):
    day_of_week = day_of_week.lower()
    index = int((days_of_the_week_index[day_of_week]) + qnt_of_days) % 7
    new_day = days_of_the_week_array[index]
    new_time += ", " + new_day

  if (qnt_of_days == 1):
    return new_time + " " + "(next day)"
  elif (qnt_of_days > 1):
    return new_time + " (" + str(qnt_of_days) + " days later)"
    
  return new_time

print(add_time("11:06 PM", "2:02"))
print(add_time("3:30 PM", "2:12"))
print(add_time("11:55 AM", "3:12"))
print(add_time("9:15 PM", "5:30"))

print(add_time("11:40 AM", "0:25"))
print(add_time("2:59 AM", "24:00"))
print(add_time("11:59 PM", "24:05"))
print(add_time("8:16 PM", "466:02"))
print(add_time("8:16 PM", "466:02"))