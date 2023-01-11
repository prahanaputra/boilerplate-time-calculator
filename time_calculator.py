def add_time(*data):
    data_split = [item.split() for item in data]
    hour_start = int(data_split[0][0].split(":")[0])
    minute_start = int(data_split[0][0].split(":")[1])
    am_pm_start = data_split[0][1]
    add_hour = int(data_split[1][0].split(":")[0])
    add_minute = int(data_split[1][0].split(":")[1])
    
    if am_pm_start == "PM":
        hour_start += 12
    
    hour_end = hour_start + add_hour + ((minute_start + add_minute) // 60)
    minute_end = minute_start + add_minute
    hour_show = hour_end  % 12
    minute_show = minute_end % 60

    if hour_show == 0:
        hour_show = 12

    days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

    if len(data) == 3:
        day_start = data_split[2][0].lower()
        for i in days:
            if i == day_start:
                today_position = days.index(i)
        next_day_position = today_position + (hour_end // 24)
        if next_day_position < 6:
            next_day =  next_day_position
        else:
            next_day = next_day_position % 7
    
    
    if (hour_end % 24) < 12:
        am_pm_next = "AM"
    else:
        am_pm_next = "PM" 
    
    if len(data) == 2:
        if (hour_end // 24) == 1:
            return f'{hour_show}:{minute_show:02d} {am_pm_next} (next day)'
        elif (hour_end // 24) > 1:
            return f'{hour_show}:{minute_show:02d} {am_pm_next} ({hour_end // 24} days later)'
        else:
            return f'{hour_show}:{minute_show:02d} {am_pm_next}'

    
    if len(data) == 3:
        if (hour_end // 24) == 1:
            return f'{hour_show}:{minute_show:02d} {am_pm_next}, {days[next_day].title()} (next day)'
        elif (hour_end // 24) > 1:
            return f'{hour_show}:{minute_show:02d} {am_pm_next}, {days[next_day].title()} ({hour_end // 24} days later)'
        else:
            return f'{hour_show}:{minute_show:02d} {am_pm_next}, {days[next_day].title()}'
