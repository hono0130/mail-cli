import glob

import pandas as pd
import numpy as np


def get_sent_file(date: str) -> pd.DataFrame:
    """
    各日付の送信リストを一つのデータフレームに結合

    Args:
        date (str): 送信日

    Returns:
        pd.DataFrame: 送信者リストを結合したもの
    """

    print(f"sent 探索中のsent_date: {date}")

    sent_path = f"../../2022年度*/sent/*{date}*/*.csv"
    sent_file = glob.glob(sent_path)

    df_sent = pd.DataFrame()

    for file in sent_file:
        print(f"該当するファイル名：{file}")
        df_tmp = pd.read_csv(file)
        df_tmp = df_tmp.fillna(df_tmp["学年"].mode().iloc[0])
        df_sent = pd.concat([df_sent, df_tmp])

    return df_sent


def get_open_file(date: str) -> pd.DataFrame:
    """
    各日付の送信リストを一つのデータフレームに結合

    Args:
        date (str): 送信日

    Returns:
        pd.DataFrame: 開封者リストを結合したもの
    """    

    print(f"open 探索中のsent_date: {date}")

    open_path = f"../../2022年度*/open/*{date}*/*.csv"
    open_file = glob.glob(open_path)

    df_open = pd.DataFrame()

    for file in open_file:
        print(f"該当するファイル名：{file}")
        df_tmp = pd.read_csv(file)
        df_tmp = df_tmp.fillna(df_tmp["学年"].mode().iloc[0])
        df_open = pd.concat([df_open, df_tmp])

    return df_open


def get_click_file(date):

    print(f"click 探索中のsent_date: {date}")

    click_path = f"../../2022年度*/click/*{date}*/*"
    click_file = glob.glob(click_path)

    df_click = pd.DataFrame()

    for file in click_file:
        print(f"該当するファイル名：{file}")
        df_tmp = pd.read_csv(file)
        if len(df_tmp) != 0:
            df_tmp = df_tmp.fillna(df_tmp["学年"].mode().iloc[0])
        df_click = pd.concat([df_click, df_tmp])

    return df_click

