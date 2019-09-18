# -*- coding: utf-8 -*-
# @File     : pipeline.py.py
# @Author   : tomlirui
# @Email    : tomlirui@didiglobal.com
# @Date     : 2019-09-18
# @Desc     : 下载任务

import wget
import sys
import util

def download(from_date_time, to_date_time):
    from_timestamp = util.get_timestamp(from_date_time)
    to_timestamp = util.get_timestamp(to_date_time)

    for timestamp in range(from_timestamp, to_timestamp+1, 3600):
        date_time_str = util.get_date_time_str(timestamp)
        file_name = 'SUOh_' + date_time_str + '.PWV'
        url = 'https://www.suominet.ucar.edu/data/pwvConusHourly/' + file_name
        wget.download(url, out=file_name)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('[usage] pipeline.py [from_date_time] [to_date_time]')
        exit(-1)

    from_date_time = sys.argv[1]
    to_date_time = sys.argv[2]
    download(from_date_time, to_date_time)
