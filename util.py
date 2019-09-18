# -*- coding: utf-8 -*-
# @File     : util.py.py
# @Author   : tomlirui
# @Email    : tomlirui@didiglobal.com
# @Date     : 2019-09-18
# @Desc     :

import time
from datetime import datetime


def get_timestamp(date_time_str):
    dt = datetime.strptime(date_time_str, "%Y.%j.%H.%M")
    return long(time.mktime(dt.timetuple()))


def get_date_time_str(timestamp):
    date_time_str = datetime.fromtimestamp(timestamp).strftime("%Y.%j.%H.%M")
    return date_time_str
