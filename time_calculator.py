def add_time(start, duration, day=None):
  #print("start: ", start)
  #print("duration: ", duration)

  week = {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
  
  # get the number for the day of the week at the start
  day_num_of_week = 0
  if (day != None):
    for k, v in week.items():
      if (v == day.title()):
        day_num_of_week = k

  num_of_days = 0
  am_or_pm = start[-2:]
  new_time = ""
  start_colon = start.find(":")
  duration_colon = duration.find(":")
  
  current_hour = start[0:start_colon]
  current_minute = start[start_colon+1: -3]
  
  hour_to_add = duration[0: duration_colon]
  minutes_to_add = duration[-2:]

  current_hour = int(current_hour)
  current_minute = int(current_minute)
  
  total_hours = current_hour + int(hour_to_add)
  final_hours_time = (current_hour + int(hour_to_add))% 12
  final_minutes_time = (current_minute + int(minutes_to_add))

  # add up the minutes to hours
  while (final_minutes_time >= 60) :
    final_hours_time += 1 
    total_hours += 1
    final_minutes_time -= 60

  # determine number of days
  num_of_days += int(hour_to_add) // 24
  if (am_or_pm == "PM" and (current_hour + int(hour_to_add)) >= 12):
    num_of_days += 1

  #update day_num_of_week
  if (day_num_of_week != 0):
    day_num_of_week = (day_num_of_week + num_of_days) % 7
    if (day_num_of_week == 0):
      day_num_of_week = 7

  # determine am or pm
  increment  = total_hours // 12
  while (increment > 0):
    if (am_or_pm == "PM"):
      am_or_pm = "AM"
      increment -= 1
    else:
      am_or_pm = "PM"
      increment -= 1
  
  # output formatting
  new_time += str(final_hours_time) + ":"

  if (len(str(final_minutes_time)) < 2):
    new_time += "0" + str(final_minutes_time)
  else:
    new_time += str(final_minutes_time)
  
  new_time += " " + am_or_pm
  if (day != None and num_of_days < 1):
    new_time += ", " + day 

  if (num_of_days > 0):
    if (num_of_days == 1):
      if (day != None):
        new_time += ", " + week.get(day_num_of_week)
      new_time += " (next day)"
    else:
      if (day != None):
        new_time += ", " + week.get(day_num_of_week)
      new_time += " (" + str(num_of_days) + " days later" + ")"

  #print("final time: ", new_time)
  return new_time