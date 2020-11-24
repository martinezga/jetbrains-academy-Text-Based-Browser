from sys import argv
from os import path, mkdir
import requests
from bs4 import BeautifulSoup


visited_webs = []


def main():
    if 1 < len(argv) < 3:
        repeat_input = True
        while repeat_input:
            input_url = input()
            if input_url == 'exit':
                repeat_input = False
            elif input_url == 'back':
                visited_url = show_visited()
                for line in get_content(visited_url):
                    print(line)
            else:
                if check_dot(input_url) and verify_response(input_url):
                    web_content = get_content(input_url)
                    for line in web_content:
                        print(line)
                    create_folder(argv[1])
                    create_file(input_url, web_content)
                    visited_webs.append(input_url)
    else:
        print('Error')


def check_dot(url):
    if url.rfind('.') == -1:
        print('error')
        return 0
    else:
        return 1


def check_url(url):
    if (url.rfind('http://') and url.rfind('https://')) == -1:
        return 'https://' + url
    else:
        return url


def verify_response(url):
    new_url = check_url(url)
    try:
        req = requests.get(new_url)
        if 200 <= req.status_code < 400:
            return 1
        else:
            print('error')
            return 0
    except:
        print('error')


def get_content(url):
    new_url = check_url(url)
    req = requests.get(new_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    tag_list = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'a', 'ul', 'ol', 'li'])
    cleaned_list = []
    for line in tag_list:
        if line.text != '' and line.text != '\n':
            cleaned_list.append(line.text)
    return cleaned_list


def create_folder(dir_name):
    if not path.exists(dir_name):
        mkdir(dir_name)
        # print('created', dir_name)


def create_file(url, content):
    if (url.rfind('http://') and url.rfind('https://')) == 0:
        pre_name = url.rsplit('//')
    else:
        pre_name = ['', url]
    web_name = pre_name[1].rsplit('.')
    with open(f'./{argv[1]}/{web_name[0]}.txt', 'w', encoding='utf-8') as web:
        for line in content:
            web.write(line + '\n')


def show_visited():
    current_web = len(visited_webs) - 1
    before_current = current_web - 1
    if len(visited_webs) > 1:
        return visited_webs[before_current]


main()
