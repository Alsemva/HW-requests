import time
import datetime


def get_dates():
    today = datetime.date.today()
    day_before_yesterday = today - datetime.timedelta(days=2)
    return today, day_before_yesterday


def date_to_unix(date):
    return int(time.mktime(time.strptime(f'{date} 06:00:00', '%Y-%m-%d %H:%M:%S')))


def unix_dates():
    today, day_before_yesterday = get_dates()
    return {'db_yesterday': date_to_unix(day_before_yesterday), 'today': date_to_unix(today)}


if __name__ == '__main__':
    u_dates = unix_dates()
    print(u_dates)

