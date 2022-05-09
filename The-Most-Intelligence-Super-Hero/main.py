import requests

TOKEN = '2619421814940190'
url = [
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Hulk',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Thanos',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Captain%America',
    ]  # список адресов


def requests_get(url_all):
    # принимает список адресов
    r = (requests.get(urll) for urll in url_all)
    return r


def SuperHero():
    # функция парсинга интелекта
    super_man = []
    for item in requests_get(url):
        intelligence = item.json()
        try:
            for power_stats in intelligence["results"]:
                super_man.append({
                    "name": power_stats["name"],
                    "intelligence": power_stats["powerstats"]["intelligence"],
                })
        except KeyError:
            print(f"Проверте ссылки url: {url}")

    intelligence_super_hero = 0
    name = ""
    for intelligence_hero in super_man:
        if intelligence_super_hero < int(intelligence_hero["intelligence"]):
            intelligence_super_hero = int(intelligence_hero["intelligence"])
            name = intelligence_hero["name"]
    print(f"""
    Самый умный: {name} 
    Интелект: {intelligence_super_hero}""")

if __name__ == "__main__":
    SuperHero()