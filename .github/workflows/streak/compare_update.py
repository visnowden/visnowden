# init
from os import listdir, getcwd, system
from requests import get

print(f'Files and directories: {listdir()}')
print(f'Current directory: {getcwd()}')
print(getcwd())

svg_string = get('https://streak-stats.demolab.com?user=visnowden').text
streak_number = int(svg_string[svg_string.find('<!-- Current Streak big number -->'):].split('\n')[3].strip())
print(streak_number)
