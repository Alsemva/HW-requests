import time
import datetime


# def time_to_unix():


if __name__ == '__main__':
    today = datetime.date.today()
    print(today)
    after_yesterday = today - datetime.timedelta(days=2)
    print(after_yesterday)
    print(int(time.mktime(time.strptime(f'{today} 06:00:00', '%Y-%m-%d %H:%M:%S'))))
    print(int(time.mktime(time.strptime(f'{after_yesterday} 06:00:00', '%Y-%m-%d %H:%M:%S'))))
