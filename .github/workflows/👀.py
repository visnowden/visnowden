from datetime import datetime;from requests import get;from time import sleep,time;streak_number=i=''
while datetime.now().strftime("%H:%M:%S")[:5]!='13:00':
 start=time()
 try:
  svg_string=get('https://streak-stats.demolab.com?user=visnowden').text;streak_number=int(svg_string[svg_string.find('<!-- Current Streak big number -->'):].split('\n')[3].strip())
  if streak_number!=i:print(f'{datetime.now().strftime("%H:%M:%S")} - {streak_number}');i=streak_number;sleep(60-(time()-start))
 except:pass
