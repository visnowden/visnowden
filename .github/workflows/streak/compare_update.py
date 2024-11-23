from os import listdir, getcwd
from requests import get

print(f'Files and directories: {listdir()}')
print(f'Current directory: {getcwd()}')

svg_string = get('https://streak-stats.demolab.com?user=visnowden').text
print(svg_string[svg_string.find('<!-- Current Streak big number -->'):].split('\n')[3].strip())
