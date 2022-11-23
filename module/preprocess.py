import glob

import pandas as pd
import numpy as np

def count(df: pd.DataFrame) -> dict[str, int]:
    """
    Dataframeから各学年の人数を数え上げる

    Args:
        df (pd.DataFrame): 

    Returns:
        dict[str, int]: 学年と人数の辞書
    """
    
    print("学年がnanの人数:" + str(df["学年"].isna().sum()))

    num_dict = {}
    num_dict["H3"] = len(df[df["学年"] == "高3"])
    num_dict["H2"] = len(df[df["学年"] == "高2"])
    num_dict["H1"] = len(df[df["学年"] == "高1"])

    return num_dict

def high_prospect(df: pd.DataFrame) -> pd.DataFrame:
    """
    Dataframeから高い見込みのみをフィルタリングする

    Args:
        df (pd.DataFrame): 

    Returns:
        pd.DataFrame: 高い見込みのみのDataframe
    """
    high_grade = ["B+", "A-", "A", "A+"]
    moshi_grade = ["C", "B", "A"]

    df_target = df[(df["グレード"].isin(high_grade)) & ((df["*****"] == True) | (df["**"].isin(moshi_grade)))]

    return df_target

