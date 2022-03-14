from pykiwoom.kiwoom import *
import time
import pandas as pd

# 로그인
kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

# 종목 코드 KOSDAQ ROE 5개년
codes = ['058470', '005290', '064760', '213420', '166090', '131970', '183300', 
        '036810', '101160', '036200', '083450', '089890', '241790']

dfs = []
df = kiwoom.block_request("opt10081",
                          종목코드="241790",
                          기준일자="20220314",
                          수정주가구분=1,
                          output="주식일봉차트조회",
                          next=0)
print(df.head())
dfs.append(df)

while kiwoom.tr_remained:
    df = kiwoom.block_request("opt10081",
                              종목코드="241790",
                              기준일자="20220314",
                              수정주가구분=1,
                              output="주식일봉차트조회",
                              next=2)
    dfs.append(df)
    time.sleep(1)

df = pd.concat(dfs)
df.to_excel("241790.xlsx")