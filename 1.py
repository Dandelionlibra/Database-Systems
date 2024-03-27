import pandas as pd
import sqlite3
my_dataframe = pd.DataFrame

def loadfile():
    filename = input("Please enter a file name:")  
    try:
        #df = pd.read_csv(filename+".csv")
        df = pd.read_csv("C:\\Users\\user\\OneDrive\\桌面\\course\\Database Systems\\Database-Systems_midterm\\p.csv")
        print(filename+'.csv-success!!')
        return df
    except:
        print("Don't exist this file!")

    
    '''
    # df = pd.read_csv('./course/Database Systems/Billionaire.csv')

    # https://data.gov.tw/dataset/54819
    url_MiddleEast = 'https://www.trade.gov.tw/OpenData/getOpenData.aspx?oid=82402BD808E00D99'
    # https://data.gov.tw/dataset/45203
    url_Asia = 'https://www.trade.gov.tw/OpenData/getOpenData.aspx?oid=3B791EACC1B5C579'
    # https://data.gov.tw/dataset/54821
    url_America = 'https://www.trade.gov.tw/OpenData/getOpenData.aspx?oid=F1217FC01AA4A3EF'
    # https://data.gov.tw/dataset/54822
    url_Africa = 'https://www.trade.gov.tw/OpenData/getOpenData.aspx?oid=3F9699D734EEE154'
    # https://data.gov.tw/dataset/54820
    url_Europe = 'https://www.trade.gov.tw/OpenData/getOpenData.aspx?oid=7087F3F01D20F112'
    '''
def writefile():
    my_dataframe.to_csv("midterm.csv")


df = loadfile()
print(df)


# df = pd.read_csv('C:\Users\user\OneDrive\桌面\course\Database Systems\Billionaire.csv')

'''
url_MiddleEast = 'https://www.trade.gov.tw/OpenData/getOpenData.aspx?oid=82402BD808E00D99'

df_MiddleEast = pd.read_csv(url_MiddleEast, thousands=',') # thousands 去除千位符號


print(df_MiddleEast.index)
print(df_MiddleEast.columns)
print(df_MiddleEast)
'''
# table_1 = pd.read_csv('covid19_global_cases_and_deaths.csv')
# # table_2 = pd.read_csv('檔案名稱')

# print(table_1)


