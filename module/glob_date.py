import glob
import datetime
import os
import csv

import pandas as pd
import numpy as np


def get_sent_date_in_moshi(moshi: str, active: bool) -> list[str]:
    """

    同一模試期間のメール送信日付を取得
    if active glob
    else cacheから取得

    Args:
        moshi (str): （例）2022年度第3回東大本番レベル模試
        active (bool): 該当模試がアクティブかどうか

    Returns:
        list[str]: 該当模試期間のメール送信日
    """
    date = []

    if active:
        date_path = glob.glob(f"../../{moshi}/open/*")
        date = [date[-6:] for date in date_path]    
        date.sort()
        with open(f"cache/{moshi}_date.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(date)
    else:
        print("date file exists!")
        with open(f"cache/{moshi}_date.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                date = row

    print(f"sent date: {date}")

    return date

def get_sent_date_in_n(n: int):
    """
    回数指定で送信日を取得する
    if file exists cacheから日付を取得

    Args:
        n (int): _description_
    """
    today = int(datetime.date.today().strftime("%y%m%d"))
    sent_date_lst = []

    if os.path.isfile(f"cache/{today}_{n}_date.csv"):
        print("date file exists!")
        with open(f"cache/{today}_{n}_date.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                sent_date_lst = row
    else:
        sent_date = today
        for i in range(today):
            if glob.glob(f"../../2022年度*/open/*{sent_date}*/*.csv") == []:
                sent_date -= 1
            else:
                break
        
        sent_date_lst = []

        open_path = glob.glob(f"../../2022年度*/open/*")
        for date in open_path:
            date = date.split("/")[4]
            # if date <= sent_date:
            sent_date_lst.append(date)
        
        sent_date_lst.sort()
        sent_date_lst = sent_date_lst[-n:]
        sent_date_lst = [str(date) for date in sent_date_lst]

        with open(f"cache/{today}_{n}_date.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(sent_date_lst)

    print(f"sent date: {sent_date_lst}")

    return sent_date_lst

