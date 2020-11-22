from sys import argv
from os import path, mkdir

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
websites = {
    'nytimes.com': nytimes_com,
    'bloomberg.com': bloomberg_com
}
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
                print(websites.get(visited_url))
            else:
                if check_dot(input_url) and check_url(input_url):
                    print(websites.get(input_url))
                    create_folder(argv[1])
                    create_file(input_url)
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
    if url in websites:
        return 1
    else:
        print('error')
        return 0


def create_folder(dir_name):
    if not path.exists(dir_name):
        mkdir(dir_name)
        # print('created', dir_name)


def create_file(url):
    web_name = url.rsplit('.')
    with open(f'./{argv[1]}/{web_name[0]}', 'w') as web:
        web.write(f'{websites.get(url)}')


def show_visited():
    current_web = len(visited_webs) - 1
    before_current = current_web - 1
    if len(visited_webs) > 1:
        return visited_webs[before_current]


main()
