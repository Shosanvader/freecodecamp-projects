def add_time(start, duration, start_day=None):
        # Parse the start time
        start, period = start.split()
        start_hour, start_minute = map(int, start.split(':'))

        # Parse the duration
        duration_hour, duration_minute = map(int, duration.split(':'))

        # Calculate the total minutes
        total_minutes = start_hour * 60 + start_minute + (duration_hour * 60 + duration_minute)

        # Calculate the new time
        new_hour = (total_minutes // 60) % 12
        new_minute = total_minutes % 60

        # Determine the period (AM or PM)
        # new_period = 'PM' if total_minutes // 60 >= 12 else 'AM'

        if period == 'AM':


        new_period = 'PM' if (start_hour + duration_hour) < 12 or start_hour + duration_hour >= 24 else 'AM'
        # new_period = 'PM' if (start_hour + duration_hour) < 12 or start_hour + duration_hour >= 24 else 'AM'
        # new_period = 'PM' if (total_minutes // 60) % 24 >= 12 else 'AM'


        # Calculate the number of days later
        days_later = total_minutes // (24 * 60)

        # Determine the day of the week if start_day is provided
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day_index = days_of_week.index(start_day.title()) if start_day else None

        # Calculate the new day of the week
        new_day_index = (start_day_index + days_later) % 7 if start_day_index is not None else None

        # Prepare the new_time string
        new_time = f"{new_hour:02d}:{new_minute:02d} {new_period}"

        if start_day:
            new_time += f", {days_of_week[new_day_index]}"

        if days_later == 1:
            new_time += " (next day)"
        elif days_later > 1:
            new_time += f" ({days_later} days later)"

        return new_time

print(add_time("03:30 AM", "12:10"))
print(add_time("11:55 AM", "3:10"))
print(add_time("9:15 PM", "5:30"))
print(add_time("10:10 PM", "3:30", "Monday"))