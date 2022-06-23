import time, datetime, pytz

result = '2022-06-23T05:16:56+00:00'

# time.strptime(result, "%Y-%m-%dT%H:%M:%S.%f%z", time.)
a = datetime.datetime.fromisoformat(result)
b = datetime.datetime.now()
# print(type(a), type(b))
# print(a, b)
# a = a.replace(tzinfo=pytz.timezone('UTC'))
# b = b.replace(tzinfo=pytz.timezone('Asia/Shanghai'))
# print(pytz.timezone('China Standard Time'))
# print(a, b)
# print(b - a)

print(a.timestamp(), b.timestamp())
