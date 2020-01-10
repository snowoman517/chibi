import sys
import io
import datetime
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')*2

#現在の日付

b = datetime.date.today()
print(b)
#b='2020-01-10'

if  b == '2020-05-17':
     print('Iwamoto Hikaru')
elif  b == '2020-05-05':
     print('深澤辰哉の誕生日')
elif  b == '2020-06-21':
     print('向井康二の誕生日')
elif  b == '2020-06-27':
     print('ラウールの誕生日')
elif  b == '2020--07-05':
     print('佐久間大介の誕生日')
#elif  b == '2020-11-05':
#      print('渡辺翔太の誕生日')
#elif  b == '2020-11-27':
#      print('阿部亮平の誕生日')
#elif  b == '2020-02-16':
#      print('目黒蓮の誕生日')
#elif  b = '2020-03-25':
 #     print('宮舘涼太の誕生日')
#elif  b == '2020-06-11':
#      print('ジェシーの誕生日')
#elif  b == '2020-06-15':
#      print('田中樹の誕生日')
#elif  b == '2020-06-18':
#      print('松村北斗の誕生日')
#elif  b == '2020-07-15':
 #     print('森本慎太郎の誕生日')
#elif  b == '2020-12-03':
  #    print('京本大我の誕生日')
#elif  b = '2020-03-08':
#      print('高地優吾の誕生日')
#elif  b = '2020-06-17':
#      print('五関晃一の誕生日')
#elif  b = '2020-07-15':
 #     print('橋本良亮の誕生日')
#elif  b = '2020-10-20':
 #     print('河合郁人の誕生日')
#elif  b = '2020-11-13':
#      print('戸塚祥太の誕生日')
#elif  b = '2020-12-10':
 #     print('塚田僚一の誕生日')
else:
    print('Nobady')