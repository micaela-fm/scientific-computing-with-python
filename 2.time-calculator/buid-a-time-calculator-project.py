def parse_time(start, duration, start_day):
    start_time = start.replace(' ', ':').split(':')
    duration_time = duration.split(':')

    start_time = { 
        'hours': int(start_time[0]), 
        'minutes': int(start_time[1]), 
        'period': start_time[2], 
        'start_day': start_day
    }

    duration_time = {
        'hours': int(duration_time[0]), 
        'minutes': int(duration_time[1])
    }

    return start_time, duration_time

def add_minutes(start_time, duration_time):
    new_time = {
        'hours': 0, 
        'minutes': start_time['minutes'] + duration_time['minutes'], 
        'period': 'AM',
        'days_later': 0, 
        'weekday': start_time['start_day']
    }

    if new_time['minutes'] >= 60: 
        new_time['minutes'] %= 60
        new_time['hours'] += 1
    return new_time

def convert_to_24_hour(start_time):
    if start_time['period'].lower() == 'pm': 
        start_time['hours'] += 12
    return start_time

def add_hours(start_time, duration_time, new_time):
    new_time['hours'] += start_time['hours'] + duration_time['hours']
    if new_time['hours'] >= 24: 
        new_time['days_later'] = new_time['hours'] // 24
        new_time['hours'] %= 24
    return new_time

def calculate_new_weekday(start_day, days_later):
    if start_day:
        days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        if start_day.capitalize() not in days_of_the_week: 
            print('You inserted an invalid day of the week, it will be ignored in the calculation')
            return
        start_day_index = days_of_the_week.index(start_day.capitalize())
        new_day_index = (start_day_index + days_later) % len(days_of_the_week)
        return days_of_the_week[new_day_index]
    return start_day

def format_new_time(new_time):
    if new_time['hours'] >= 12:
        new_time['period'] = 'PM'
        new_time['hours'] -= 12
    if new_time['hours'] == 0: 
        new_time['hours'] = 12

    new_time_string = f"{new_time['hours']}:{str(new_time['minutes']).zfill(2)} {new_time['period']}"
    if new_time['weekday']: 
        new_time_string += f", {new_time['weekday']}"
    if new_time['days_later'] == 1:
        new_time_string += f" (next day)"
    if new_time['days_later'] > 1:
        new_time_string += f" ({new_time['days_later']} days later)"
    
    return new_time_string

def add_time(start, duration, start_day = None):
    start_time, duration_time = parse_time(start, duration, start_day)
    new_time = add_minutes(start_time, duration_time)
    start_time = convert_to_24_hour(start_time)
    new_time = add_hours(start_time, duration_time, new_time)
    new_time['weekday'] = calculate_new_weekday(start_day, new_time['days_later'])
    return format_new_time(new_time)

print(add_time("6:00 AM", "93:00", "Monday"))


