import pandas as pd

def loadfile():
    filename = input("Please enter a file name(press exist leave):") 
    if(filename == "exist"):
        return  False, False
    try:
        df = pd.read_csv(filename+".csv")
        print(filename+'.csv-success!!')
        return df, True
    except:
        print("### Don't exist this file!! ###\n")
        loadfile()

# select
def select_data(df):
    column_name = input("Please enter a column name:")
    if column_name not in df.columns:
        print("### Don't exist this column!! ###\n")
        select_data(df)
    else:
        value = input("Please enter a value:")
        df_selected = df[df[column_name] == value]
        print(df_selected)

# Project

# Rename

# Cartesian Product

# Set Union

# Set Difference

def writefile(pf):
    filename = input("Please enter a file name:")
    pf.to_csv(filename+".csv")

def operationlist():
    print("----------------------------------------")
    print("1.Enter a file")
    print("2.")
    print("3.")
    print("4.")
    print("5.Quit")
    print("----------------------------------------")

def Quit():
    print("----------------------------------------")
    print("Thank you using this program")
    print("-----------------END--------------------")
    return False