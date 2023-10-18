import requests
from bs4 import BeautifulSoup

name = None


def get(url):


    global name
    name = url

    url_words = url.split()
    print(url_words)
    i = len(url_words)
    q = 0
    d = 0
    main_url = 'https://rur.hitmotop.com/search?q='
    while True:
        if q == i:
            break
        elif (q + 1) == i:
            main_url = main_url + url_words[q]
        else:

            main_url = main_url + url_words[q] + '+'
        q += 1

    try:
        page = requests.get(main_url)
        print(page)
        find_a_tag(page)
    except:
        pass


def find_a_tag(parsed_page):
    soup = BeautifulSoup(parsed_page.text, 'html.parser')
    search_music = soup.find('a', class_='track__download-btn')
    search_music_url = search_music.get('href')
    print(search_music_url)
    file = requests.get(search_music_url)
    print(file)
    with open(f'D:/SOUNDs/{name}.mp3', 'wb') as f:
        print(5)
        f.write(file.content)
