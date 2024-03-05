from datetime import datetime;from requests import get;from time import sleep,time;streak_number=i=''
while int(datetime.now().strftime("%H:%M:%S")[:2])>12:
 start=time()
 try:
  svg_string=get('https://streak-stats.demolab.com?user=visnowden').text;streak_number=int(svg_string[svg_string.find('<!-- Current Streak big number -->'):].split('\n')[3].strip())
  if streak_number!=i:f=open('log', 'a+');f.write(f'{datetime.now().strftime("%H:%M:%S")} - {streak_number}');i=streak_number;sleep(60-(time()-start))
 finally:f.close()
