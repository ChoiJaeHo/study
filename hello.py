print ('hello python world')
print ('hello git world')

#v1 = int(input('첫번째 숫자를 입력하세요: '))
#v2 = int(input('두번째 숫자를 입력하세요: '))

#if v1 == 0:
#    print('첫번째 숫자값이 0 입니다.')
#print (v1, '곱하기', v2, '는', v1*v2, '입니다.')


# 문자열 = """테스트용 줄바꿈 문자열 입니다.
# 여러줄의 문자열이 하나의 변수에 입력됩니다.
# 잘 되고 있나요"""

# print(문자열, end = '$')
# print('')

# lst = []
# for i in range(1, 101) :
#     lst.append(i)
# print(lst)

# def 더하기(a, b) :
#     global sum
#     sum = (a + b)

# 더하기(10, 20)
# print(sum)

# lam = lambda a,b : a+b

# sum = lam(10, 20)
# print(sum)

# i = int(input('숫자를 입력해주세요 : '))

# def isEven(x):
#     return (x%2 == 0)

# #lst = list(filter(lambda x: (x%2==0), range(i+1)))
# lst = list(filter(isEven, range(i+1)))
# print(lst)

# multiply4 = list(map(lambda x: x*4, range(1, i+1)))
# print(multiply4)

# from functools import reduce

# def sum2(x,y):
#     return x+y

# #print(reduce(lambda x,y:x+y, range(1,5)))
# print(reduce(sum2, range(1,5)))
# print(list(range(1,5)))

# #  reduce() 함수를 이용하여 문자열의 방향을 반대로 바꾸는함수를 만드시오.
# # 예) 기러기는 '거꿀로해도 기러기' -> '기러기 도해로꿀거 는기러기'

# comment = '기러기 도해로꿀거 는기러기'
# print(comment)
# reverse = reduce(lambda x,y: y+x, comment)
# print(reverse)

# dictionary = {'일':'숫자1', '이':'숫자2', '삼':'숫자3', '사':'숫자4', 5:'숫자5'}
# dictionary[6] = '숫자6'

# print(dictionary)
# del dictionary['이']
# print(dictionary)
# dictionary[2] = '숫자2'

# for key in dictionary.keys():
#     print(key, end=' ')
#     print(dictionary[key])

# for k,v in dictionary.items():
#     print(k, v)

# import json

# strTest = '{"AA":"1"}'
# testJson = json.loads(strTest)
# print(testJson)
# print(str(type(testJson)))
# testDump = json.dumps(testJson)
# print(testDump)
# print(str(type(testDump)))


# def myTest():
#     try:
#         raise ValueError('Test Error')
#     except:
#         raise IndexError('Test Error2')

# myTest()

# dicTest = {'severity' : 'Test'}
# print(dicTest.get('severity'))
# print(dicTest['severity'])

# allowedClientIPs = ['127.0.0.1','90.90.127.231']
# clientIp = '90.90.127.231   '
# clientIp = clientIp.strip()
# print(clientIp)

# for allowedIp in allowedClientIPs:
#     if '*' in allowedIp:
#         loc = allowedIp.find('*')
#         print(clientIp[:loc])
#         print(allowedIp[:loc])
#         if clientIp[:loc] == allowedIp[:loc]:
#             print("OK!!!")
#     elif clientIp == allowedIp:
#         print("OK!!!!!!!")

# def printTopic(*topics):
#     if topics:
#         _printTopic(topics)

# def _printTopic(topics):
#     if isinstance(topics, str):
#         print('input topic is string type')
#         topics = [topics]
#     elif isinstance(topics, list):
#         print('input topic is list type')
#     elif isinstance(topics, tuple):
#         print('input topic is tuple type')
#     else:
#         print(type(topics))
    
#     for topic in topics:
#         print('topic: ', topic)

# from datetime import datetime
# now = datetime.now().strftime('%Y%m%d%H%M%S')
# print(now)

# key = 'ABCDE'
# authKey = 'Basic %s'%(key)
# print(authKey)

# printTopic("MY_TOPIC", "SEC_TOPIC", 'THRD_TOPIC')

# str2 = 'TEST0123-TEST'
# print(str2[0:8])
# if str2[0:8] == 'TEST0123':
#     print(str2)
# else :
#     print('NOT FOUND')

# from pprint import pprint
# a = [[10,20],[30,430],[50,60,]]
# pprint(a, indent=2, width=20)


import json

str_json = '{ "headers": { "Authorization": "Basic Test" } }'
#str_json = '{}'
jsonObj = json.loads(str_json)

if not jsonObj.get('headers') or not jsonObj.get('headers').get('Authorization'):
    print('headers.Authorization key is not exist.')

if jsonObj.get('headers'):
    for key in jsonObj.get('headers').keys():
        print(f'{key}: ')
        print(f'- {jsonObj.get("headers").get(key)}')


#enb = ['MACRO', '10', '20', '30']
enb = []
if enb:
    strEnb = '%s(%s)' %('-'.join(enb[1:4]), enb[0])
else :
    strEnb = ''
print(strEnb)