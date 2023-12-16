# init
from requests import get

svg_string = get('https://streak-stats.demolab.com?user=visnowden').text
streak_number = int(svg_string[svg_string.find('<!-- Current Streak big number -->'):].split('\n')[3].strip())
print(streak_number)
