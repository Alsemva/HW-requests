import requests


def api_hero_request():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    response_list = response.json()
    heroes_intelligences = {}
    for item in response_list:
        if item['name'] == 'Hulk' or item['name'] == 'Captain America' or item['name'] == 'Thanos':
            heroes_intelligences[item['name']] = item['powerstats']['intelligence']
            print(f"Hero: {item['name']}, intelligence: {item['powerstats']['intelligence']}")

    return heroes_intelligences


def smartest_hero():
    heroes_intelligences = api_hero_request()
    smart_hero = max(heroes_intelligences, key=heroes_intelligences.get)
    return f'\nThe smartest hero: {smart_hero}'


if __name__ == '__main__':
    print(smartest_hero())
