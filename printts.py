import pytz
from datetime import datetime

def tsprint(*args):
    # Edit this line to change timezone
    tz = pytz.timezone('Asia/Bangkok')
    datetime_Tz = datetime.now(tz)
    CTime = datetime_Tz.strftime("[%d-%m-%Y|%H:%M:%S]")
    print(CTime, ' '.join(map(str, args)))

if __name__ == "__main__":
    tsprint('test', 'time', 'stamp'+'xx')

    # for i in range(len(pytz.common_timezones)):
    #     print(pytz.common_timezones[i])