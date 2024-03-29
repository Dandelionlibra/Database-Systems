import pandas as pd
import time
import os # judge file exist or not

# print(os.getcwd())
pd.options.display.max_columns = None
pd.options.display.max_rows = None

def loadfile(my_dataframe):
    filename = input("Please enter a file name(enter quit leave): ") 
    if(filename == "quit"):
        return  None, False
    try:
        # my_dataframe = pd.read_csv("C:\\Users\\user\\OneDrive\\桌面\\course\\Database Systems\\Database-Systems_midterm\\"+filename+".csv")
        my_dataframe = pd.read_csv(filename+".csv", thousands=',')
        print(filename+'.csv-success!!')
        print(my_dataframe)
        return my_dataframe, True
    except FileNotFoundError:
        print("### Don't exist this file!! ###\n")
    except pd.errors.EmptyDataError:
        print("### This file no data!! ###\n")
    except pd.errors.ParserError:
        print("### Parse error ###\n")
    except Exception:
        print("Some other exception")
    return loadfile(my_dataframe)

# select
def select_data(my_dataframe):
    column = my_dataframe.columns
    while True:
        index = 1
        for c in column:
            print("[",index,"]: ",c,sep="",end="\n")
            index=index+1
        try:
            select_column=int(input("Please enter a number:"))
            if (select_column <= 0 or select_column > index-1) :
                print("### Illegal input! ###\n")
            else:
                break
        except ValueError:
            print("### Illegal input! ###\n")
    
    column_name = column[select_column-1]
    print("column_name:",column_name)


    if column_name not in my_dataframe.columns:
        print("### Don't exist this column!! ###\n")
        select_data(my_dataframe)
    else:
        print("————————————————————————————————")
        print("│0.Quit                         │") # >
        print("│1.Select greater data          │") # >
        print("│2.Select greater or equal data │") # >=
        print("│3.Select equal data            │") # ==
        print("│4.Select not equal data        │") # !=
        print("│5.Select smaller or equal data │") # <=
        print("│6.Select smaller data          │") # <
        print("————————————————————————————————")
        
        while True:
            try:
                command=int(input("Please enter a number:"))
                if (command < 0 or command > 6):
                    print("###Please enter 1-6! ###\n")
                else:
                    break
            except ValueError:
                print("### Illegal input! ###\n")
        if(command == 0):
            return None
        elif(command == 1): # >
            while True:
                try:
                    value=int(input("Please enter the value(int):"))
                    if(my_dataframe[column_name].dtype != "int64"):
                        print("### Illegal input! ###")
                        print("### Make sure the datatype is correct! ###\n")
                        return select_data(my_dataframe)
                    else:
                        break
                except ValueError:
                    print("### Illegal input! ###")
                    print("### You need to input a number! ###\n")
            my_dataframe = my_dataframe[my_dataframe[column_name] > value]
            my_dataframe.reset_index(drop = True, inplace = True)
            return my_dataframe
        
        if(command == 1): # >=
            while True:
                try:
                    value=int(input("Please enter the value(int):"))
                    if(my_dataframe[column_name].dtype != "int64"):
                        print("### Illegal input! ###")
                        print("### Make sure the datatype is correct! ###\n")
                        return select_data(my_dataframe)
                    else:
                        break
                except ValueError:
                    print("### Illegal input! ###")
                    print("### You need to input a number! ###\n")
            my_dataframe = my_dataframe[my_dataframe[column_name] >= value]
            my_dataframe.reset_index(drop = True, inplace = True)
            return my_dataframe
        
        elif(command == 3): # ==
            while True:
                try:
                    value=input("Please enter the value(str):")
                    break
                except ValueError:
                    print("### Illegal input! ###")
                    print("### You need to input a string! ###\n")
            my_dataframe = my_dataframe[my_dataframe[column_name] == value]
            my_dataframe.reset_index(drop = True, inplace = True)
            return my_dataframe
        
        elif(command == 4): # !=
            while True:
                try:
                    value=input("Please enter the value(str):")
                    break
                except ValueError:
                    print("### Illegal input! ###")
                    print("### You need to input a string! ###\n")
            my_dataframe = my_dataframe[my_dataframe[column_name] != value]
            my_dataframe.reset_index(drop = True, inplace = True)
            return my_dataframe
        
        elif(command == 5): # <=
            while True:
                try:
                    value=int(input("Please enter the value(int):"))
                    if(my_dataframe[column_name].dtype != "int64"):
                        print("### Illegal input! ###")
                        print("### Make sure the datatype is correct! ###\n")
                        return select_data(my_dataframe)
                    break
                except ValueError:
                    print("### Illegal input! ###")
                    print("### You need to input a number! ###\n")
            my_dataframe = my_dataframe[my_dataframe[column_name] <= value]
            my_dataframe.reset_index(drop = True, inplace = True)
            return my_dataframe
        
        elif(command == 6): # <
            while True:
                try:
                    value=int(input("Please enter the value(int):"))
                    if(my_dataframe[column_name].dtype != "int64"):
                        print("### Illegal input! ###")
                        print("### Make sure the datatype is correct! ###\n")
                        return select_data(my_dataframe)
                    break
                except ValueError:
                    print("### Illegal input! ###")
                    print("### You need to input a number! ###\n")
            my_dataframe = my_dataframe[my_dataframe[column_name] < value]
            my_dataframe.reset_index(drop = True, inplace = True)
            return my_dataframe
            
# Project
def project(my_dataframe):
    column = my_dataframe.columns
    remain=[]
    while True:
        index = 1
        if len(remain)!=0:
            print("***************** Current keep column: *****************")
            print("Current keep column: ")
            for tmp in remain:
                print(tmp)
            print("********************************************************\n")

        print("[0]: Finish")
        for c in column: # show colume
            print("[",index,"]: ",c,sep="",end="\n")
            index=index+1
        try:
            select_column=int(input("Please enter a number: "))
            if select_column == 0: # quit
                break
            elif (select_column <= 0 or select_column > index-1) :
                print("### Illegal input! ###\n")
            else: # append remain column
                same_Column = False
                for tmp in remain:
                    if column[select_column-1] == tmp:
                        same_Column = True
                        break
                if same_Column == False :
                    remain.append(column[select_column-1])
                        
        except ValueError:
            print("### Illegal input! ###\n")
    
    # if len(remain)==0:
    #     return None
    # add specific columns
    # df = my_dataframe.loc[:, remain]

    # delete all, except remain
    my_dataframe = my_dataframe.drop(my_dataframe.columns.difference(remain), axis=1)

    # delete repeat data
    my_dataframe = my_dataframe.drop_duplicates(subset=None, keep='first', inplace=False) # keep first appear otherwise all of the duplicate data will be delete
    my_dataframe.reset_index(drop = True, inplace = True)

    return my_dataframe

# Rename
def Rename(my_dataframe):
    df = pd.DataFrame()


# Cartesian Product
def Cartesian_Product(my_dataframe):
    df = pd.DataFrame()
    df, success= loadfile(df)
    if success:
        # df = pd.concat([my_dataframe, df])
        my_dataframe = my_dataframe.merge(df, how = 'cross')
        # print("********************DF********************")
        # print(my_dataframe)
        return my_dataframe
    else:
        print("### Fail to add a new file! ###")
        return my_dataframe
    

# Set Union(聯集)
def union(my_dataframe):
    df = pd.DataFrame()
    df, success= loadfile(df)
    if success:
        # df = pd.concat([my_dataframe, df])
        df = my_dataframe.merge(df)
        print("********************DF********************")
        print(df)
        return df
    else:
        print("### Fail to add a new file! ###")
        return my_dataframe


# Set Difference(差集)
def difference_data(my_dataframe):
    df = pd.DataFrame()
    df, success= loadfile(df)
    if success:
        # df = pd.concat([my_dataframe, df])
        df = pd.concat([my_dataframe, df, df]).drop_duplicates(keep = False)
        # df = pd.concat([my_dataframe, df]).drop_duplicates(keep = False) # get exclusive

        return df
    else:
        print("### Fail to add a new file! ###")
        return my_dataframe
    
# Set insersection(交集)
def insersection(my_dataframe):
    df = pd.DataFrame()
    df, success= loadfile(df)
    if success:
        # df = pd.concat([my_dataframe, df])
        df = my_dataframe.merge(df)
        
        return df
    else:
        print("### Fail to add a new file! ###")
        return my_dataframe
    
# Division(除法)

# Natural join(合併)


def writefile(out_dataframe):
    while(True):
        filename = input("Please enter a file name(Enter quit to leave):")
        if(filename == 'quit'):
            return
        fileName_Exist = os.path.isfile(filename+'.csv')
        # print(fileName_Exist)
        while(fileName_Exist):
            command = input("Already have this filename, do you want to continue?(Y/N): ")
            if(command == 'Y' or command == 'y' or command == 'YES' or command == 'yes'):
                fileName_Exist = False
            elif(command == 'N' or command == 'n' or command == 'NO' or command == 'no'):
                print("### Go back to the previous step ###\n")
                break
            else:
                print("### Illegal input! ###\n")
        
        if(fileName_Exist == False):
            try:
                out_dataframe.to_csv(filename+".csv", index =  False)
                print('success created '+filename+'.csv-!!\n', sep='')
                return
            except FileExistsError:
                print("### FileExists Error! ###\n")
            except:
                print("### Unexcepted Error! ###\n")

def operationlist():
    print("————————————————————————————————————————")
    print("│0.Quit                                │")
    print("│1.Load file                           │")
    print("│2.Implement select                    │")
    print("│3.Implement project                   │")
    print("│4.Implement rename                    │")
    print("│5.Implement cartesian Product         │")
    print("│6.Implement set Union                 │")
    print("│7.Implement set Difference            │")
    print("│8.Implement set insersection          │")
    print("│9.Implement division                  │")
    print("│10.Implement natural join             │")
    print("│11.Export the archive                 │")
    print("————————————————————————————————————————")

def Quit():
    print("————————————————————————————————————————")
    print("|    Thank you using this program      |")
    print("——————————————————END———————————————————\n")
    time.sleep(5)
    return False

def Test(my_dataframe):
    # column = my_dataframe.columns
    column = my_dataframe.columns
    
    index = 1
    for c in column:
        print("[",index,"]: ",c,sep="",end="\n")
        index=index+1
    select_column=int(input("Please enter a number:"))
    
    
    column_name = column[select_column-1]
    print(column_name)



"""my_dataframe = pd.DataFrame()
my_dataframe = pd.read_csv("c.csv")

index = 1
column = my_dataframe.columns
for c in column:
    print("[",index,"]: ",c,sep="",end="\n")
    index=index+1
# select_column=input("Please enter a number:")
while True:
    try:
        select_column=int(input("Please enter a number:"))
        break
    except ValueError:
        print("### Illegal input! ###\n")

column_name = column[select_column-1]
print("\ncolumn_name:",column_name)
print(my_dataframe[column_name].dtype)"""



def main():
    running = True
    file_Exist = False
    my_dataframe = pd.DataFrame()
    out_dataframe = pd.DataFrame()
    print("Wellcome to this program")
    while(running):
        operationlist() # operation menu
        while True: # Enter the command
            try:
                command=int(input("Please enter the command: "))
                break
            except ValueError:
                print("### Illegal input! ###\n")

        if(command == 0):
            running = Quit()
        elif(command == 1):
                my_dataframe, file_Exist = loadfile(my_dataframe)
                # print(my_dataframe)

        elif(command == 2):
            if(file_Exist):
                out_dataframe = select_data(my_dataframe)
                print("—————————————————————————————————— END Select ———————————————————————————————————")
                print(out_dataframe)
                print("—————————————————————————————————————————————————————————————————————————————————")
            else:
                print("### Please Load file first!! ###\n")
        elif(command == 3):
            if(file_Exist):
                out_dataframe = project(my_dataframe)
                print("————————————————————————————————— END Project ———————————————————————————————————")
                print(out_dataframe)
                print("—————————————————————————————————————————————————————————————————————————————————")
            else:
                print("### Please Load file first!! ###\n")

        elif(command == 4):
            if(file_Exist):
                # out_dataframe = select_data(my_dataframe)
            # else:
                print("### Please Load file first!! ###\n")
        elif(command == 5):
            if(file_Exist):
                out_dataframe = Cartesian_Product(my_dataframe)
                print("———————————————————————————————— End Difference —————————————————————————————————")
                print(out_dataframe)
                print("—————————————————————————————————————————————————————————————————————————————————")
            else:
                print("### Please Load file first!! ###\n")

        elif(command == 6):
            if(file_Exist):
                out_dataframe = union(my_dataframe)
            else:
                print("### Please Load file first!! ###\n")
        elif(command == 7):
            if(file_Exist):
                out_dataframe = difference_data(my_dataframe)
                print("————————————————————————————— END Cartesian_Product —————————————————————————————")
                print(out_dataframe)
                print("—————————————————————————————————————————————————————————————————————————————————")
            else:
                print("### Please Load file first!! ###\n")
        elif(command == 8):
            if(file_Exist):
                out_dataframe = insersection(my_dataframe)
                print("——————————————————————————————— END insersection ————————————————————————————————")
                print(out_dataframe)
                print("—————————————————————————————————————————————————————————————————————————————————")
            else:
                print("### Please Load file first!! ###\n")
            '''elif(command == 9):
            if(file_Exist):
                # out_dataframe = select_data(my_dataframe)
            else:
                print("### Please Load file first!! ###\n")
        elif(command == 10):
            if(file_Exist):
                # out_dataframe = select_data(my_dataframe)
            # else:
                print("### Please Load file first!! ###\n")'''

        elif(command == 11):
            if(file_Exist):
                writefile(out_dataframe)
            else:
                print("### Please Load file first!! ###\n")
        elif(command == 12):
            if(file_Exist):
                Test(my_dataframe)
            else:
                print("### Please Load file first!! ###\n")
        else:
            print("### The command doesn't exist !! ###\n")
        
        print()


main()