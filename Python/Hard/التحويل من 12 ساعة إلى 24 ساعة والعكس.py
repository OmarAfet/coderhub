
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def convert_time(time: str) -> str:
    if 'am' in time:
        time = time.replace('am', '').strip()
        if time == '12:00':
            time = '0:00'
        return time
    elif 'pm' in time:
        time = time.replace('pm', '').strip()
        if time == '12:00':
            return '12:00'
        hours, minutes = time.split(':')
        return str(int(hours) + 12) + ':' + minutes
    else:
        hours, minutes = time.split(':')
        if int(hours) > 12:
            return str(int(hours) - 12) + ':' + minutes + ' pm'
        elif int(hours) == 12:
            return time + ' pm'
        elif int(hours) == 0:
            return '12:' + minutes + ' am'
        else:
            return time + ' am'