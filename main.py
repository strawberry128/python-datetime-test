from datetime import datetime
import time

TIME_FORMAT = '{0:04d}/{1:02d}/{2:02d} {3:02d}:{4:02d}:{5:02d}.{6:06d}'

now = datetime.now()

s = time.time()
for i in range(1000000):
    f = now.strftime('%Y/%m/%d %H:%M:%S.%f')
print('datetime.strftime  : %s' % (time.time() - s))

s = time.time()
for i in range(1000000):
    f = '{0:%Y/%m/%d %H:%M:%S.%f}'.format(now)
print('str.format1        : %s' % (time.time() - s))

s = time.time()
for i in range(1000000):
    f = '{0:04d}/{1:02d}/{2:02d} {3:02d}:{4:02d}:{5:02d}.{6:06d}'.format(
        now.year, now.month, now.day,
        now.hour, now.minute, now.second, now.microsecond
    )
print('str.format2        : %s' % (time.time() - s))

s = time.time()
for i in range(1000000):
    f = TIME_FORMAT.format(
        now.year, now.month, now.day,
        now.hour, now.minute, now.second, now.microsecond
    )
print('str.format3        : %s' % (time.time() - s))

s = time.time()
for i in range(1000000):
    f = '{year:04d}/{month:02d}/{day:02d} {hour:02d}:{minute:02d}:{second:02d}.{microsecond:06d}'.format(
        year=now.year, month=now.month, day=now.day,
        hour=now.hour, minute=now.minute, second=now.second, microsecond=now.microsecond
    )
print('str.format4        : %s' % (time.time() - s))

s = time.time()
for i in range(1000000):
    f = f'{now:%Y/%m/%d %H:%M:%S.%f}'
print('f-string1          : %s' % (time.time() - s))

s = time.time()
for i in range(1000000):
    f = f'{now.year:04d}/{now.month:02d}/{now.day:02d} {now.hour:02d}:{now.minute:02d}:{now.second:02d}.{now.microsecond:02d}'
print('f-string2          : %s' % (time.time() - s))


def format_datetime_1(dt):
    return '{0:04d}/{1:02d}/{2:02d} {3:02d}:{4:02d}:{5:02d}.{6:06d}'.format(
        dt.year, dt.month, dt.day,
        dt.hour, dt.minute, dt.second, dt.microsecond
    )


def format_datetime_2(dt):
    return TIME_FORMAT.format(
        dt.year, dt.month, dt.day,
        dt.hour, dt.minute, dt.second, dt.microsecond
    )


def format_datetime_3(dt, format=''):
    return format.format(
        dt.year, dt.month, dt.day,
        dt.hour, dt.minute, dt.second, dt.microsecond
    )


s = time.time()
for i in range(1000000):
    f = format_datetime_1(now)
print('format-function1   : %s' % (time.time() - s))

s = time.time()
for i in range(1000000):
    f = format_datetime_2(now)
print('format-function2   : %s' % (time.time() - s))

s = time.time()
for i in range(1000000):
    f = format_datetime_3(now, format='{0:04d}/{1:02d}/{2:02d} {3:02d}:{4:02d}:{5:02d}.{6:06d}')
print('format-function3-1 : %s' % (time.time() - s))

s = time.time()
for i in range(1000000):
    f = format_datetime_3(now, format=TIME_FORMAT)
print('format-function3-2 : %s' % (time.time() - s))
