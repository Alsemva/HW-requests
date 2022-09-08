import time
import datetime
import requests


def get_dates():
    today = datetime.date.today()
    day_before_yesterday = today - datetime.timedelta(days=2)
    return today, day_before_yesterday


def date_to_unix(date):
    return int(time.mktime(time.strptime(f'{date} 06:00:00', '%Y-%m-%d %H:%M:%S')))


def unix_dates():
    today, day_before_yesterday = get_dates()
    return {'db_yesterday': date_to_unix(day_before_yesterday), 'today': date_to_unix(today)}


def api_stackoverflow_request(u_dates, tag):
    url = f'https://api.stackexchange.com/2.3/questions?fromdate={u_dates["db_yesterday"]}&todate={u_dates["today"]}\
    &order=desc&sort=activity&tagged={tag}&site=stackoverflow'
    response = requests.get(url)
    response.raise_for_status()
    response_dict = response.json()
    for title in response_dict['items']:
        print(title['title'].replace('&#39;', "'"))


if __name__ == '__main__':
    u_dates = unix_dates()
    tag = 'python'
    api_stackoverflow_request(u_dates, tag)
