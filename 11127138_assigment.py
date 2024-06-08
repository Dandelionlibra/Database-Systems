import pandas as pd
import time
import os # judge file exist or not

# print(os.getcwd())
# pd.options.display.max_columns = None
# pd.options.display.max_rows = None


def loadfile(my_dataframe):
    filename = input("Please enter a file name(enter quit leave): ") 
    if(filename == "quit"):
        return  pd.DataFrame(), False
    try:
        # my_dataframe = pd.read_csv("路徑"+filename+".csv")
        my_dataframe = pd.read_csv(filename+".csv", thousands=',')
        if(my_dataframe.empty):
            print("\033[93m### This file no data!! ###\033[0m\n")
            return loadfile(my_dataframe)
        
        print("\033[93mLoad .csv success!!\033[0m")
        print("\033[93mCurrent table is: "+filename+'\033[0m')

        print(my_dataframe)
        print()
        return my_dataframe, True
    except FileNotFoundError:
        print("\033[91m### Don't exist this file!! ###\033[0m\n")
    except pd.errors.EmptyDataError:
        print("\033[91m### This file no data!! ###\033[0m\n")
    except pd.errors.ParserError:
        print("\033[91m### Parse error ###\033[0m\n")
    except Exception:
        print("\033[91mSome other exception\033[0m\n")
    return loadfile(my_dataframe)

# select
def select_data(my_dataframe):
    column = my_dataframe.columns
    while True:
        index = 1
        print("[0]: Quit",end="\n")
        for c in column:
            print("[",index,"]: ",c,sep="",end="\n")
            index=index+1
        try:
            select_column=int(input("Please enter a number: "))
            if(select_column == 0):
                return pd.DataFrame()
            if (select_column <= 0 or select_column > index-1) :
                print("\033[91m### Illegal input! ###\033[0m\n")
            else:
                break
        except ValueError:
            print("\033[91m### Illegal input! ###\033[0m\n")
    
    column_name = column[select_column-1]
    print("\033[93mcolumn_name:",column_name,", datatype:",my_dataframe[column_name].dtype,"\033[0m")


    if column_name not in my_dataframe.columns:
        print("\033[91m### Don't exist this column!! ###\033[0m\n")
        return select_data(my_dataframe)
    else:
        commandnum = 0
        if(my_dataframe[column_name].dtype == "int64" or my_dataframe[column_name].dtype == "float64"): # the datatype is int so that can use >, >=, <=, < to compare
            print("————————————————————————————————")
            print("│0.Quit                         │") # >
            print("│1.Select greater data          │") # >
            print("│2.Select greater or equal data │") # >=
            print("│3.Select equal data            │") # ==
            print("│4.Select not equal data        │") # !=
            print("│5.Select smaller or equal data │") # <=
            print("│6.Select smaller data          │") # <
            print("│7.Compare with other column    │") 
            print("————————————————————————————————")
            commandnum = 7
        else:
            print("————————————————————————————————")
            print("│0.Quit                         │") # >
            print("│1.Select equal data            │") # ==
            print("│2.Select not equal data        │") # !=
            print("│3.Compare with other column    │") 
            print("————————————————————————————————")
            commandnum = 3
    
        while True:
            try:
                command=int(input("Please enter a number: "))
                if (command < 0 or command > commandnum):
                    print("\033[93m###Please enter 1-",commandnum,"! ###\033[0m\n")
                else:
                    if(commandnum == 3):
                        if(command == 1):
                            command = 3
                        elif(command == 2):
                            command = 4
                        elif(command == 3):
                            command = 7
                    break
            except ValueError:
                print("\033[91m### Illegal input! ###\033[0m\n")
        if(command == 0):
            return pd.DataFrame()
        elif(command == 1): # >
            while True:
                try:
                    value=int(input("Please enter the value(int): "))
                    break
                except ValueError:
                    print("\033[91m### Illegal input! ###\033[0m")
                    print("\033[91m### You need to input a number! ###\033[0m\n")
            my_dataframe = my_dataframe[my_dataframe[column_name] > value]
            my_dataframe.reset_index(drop = True, inplace = True)
            return my_dataframe
        
        elif(command == 2): # >=
            while True:
                try:
                    value=int(input("Please enter the value(int): "))
                    break
                except ValueError:
                    print("\033[91m### Illegal input! ###\033[0m")
                    print("\033[91m### You need to input a number! ###\033[0m\n")
            my_dataframe = my_dataframe[my_dataframe[column_name] >= value]
            my_dataframe.reset_index(drop = True, inplace = True)
            return my_dataframe
        
        elif(command == 3): # ==
            while True:
                try:
                    value=input("Please enter the value(str): ")
                    break
                except ValueError:
                    print("\033[91m### Illegal input! ###\033[0m")
                    print("\033[91m### You need to input a string! ###\033[0m\n")
            my_dataframe = my_dataframe[my_dataframe[column_name].apply(str) == value]
            my_dataframe.reset_index(drop = True, inplace = True)
            return my_dataframe
        
        elif(command == 4): # !=
            while True:
                try:
                    value=input("Please enter the value(str): ")
                    break
                except ValueError:
                    print("\033[91m### Illegal input! ###\033[0m")
                    print("\033[91m### You need to input a string! ###\033[0m\n")
            my_dataframe = my_dataframe[my_dataframe[column_name].apply(str) != value]
            my_dataframe.reset_index(drop = True, inplace = True)
            return my_dataframe
        
        elif(command == 5): # <=
            while True:
                try:
                    value=int(input("Please enter the value(int): "))
                    break
                except ValueError:
                    print("\033[91m### Illegal input! ###\033[0m")
                    print("\033[91m### You need to input a number! ###\033[0m\n")
            my_dataframe = my_dataframe[my_dataframe[column_name] <= value]
            my_dataframe.reset_index(drop = True, inplace = True)
            return my_dataframe
        
        elif(command == 6): # <
            while True:
                try:
                    value=int(input("Please enter the value(int): "))
                    break
                except ValueError:
                    print("\033[91m### Illegal input! ###\033[0m")
                    print("\033[91m### You need to input a number! ###\033[0m\n")
            my_dataframe = my_dataframe[my_dataframe[column_name] < value]
            my_dataframe.reset_index(drop = True, inplace = True)
            return my_dataframe
        
        elif(command == 7): # compare column
            last_column_index = select_column-1
            while True:
                index = 1
                print("[0]: Quit",end="\n")
                for c in column: # choose another column
                    if(c == column_name): # skip the same column
                        continue
                    print("[",index,"]: ",c,sep="",end="\n")
                    index=index+1
                try:
                    select_column=int(input("Please choose a column: "))
                    if(select_column == 0):
                        return pd.DataFrame()
                    if (select_column <= 0 or select_column > index-1) :
                        print("\033[91m### Illegal input! ###\033[0m\n")
                    else:
                        break
                except ValueError:
                    print("\033[91m### Illegal input! ###\033[0m\n")

            if(last_column_index+1 <= select_column): # set compare column, differ from the first column
                compare_column_name = column[select_column]
            else:
                compare_column_name = column[select_column-1]
            print("\033[93mcolumn_name:",compare_column_name,", datatype:",my_dataframe[compare_column_name].dtype,"\033[0m")

            new_df = pd.DataFrame(columns=my_dataframe.columns) # create a new dataframe, same columns as my_dataframe
            # print(new_df.dtypes)
            for i, dtype in my_dataframe.dtypes.items(): # set the same datatype as my_dataframe
                new_df[i] = new_df[i].astype(dtype)
            # print(new_df.dtypes)

            commandnum = 0
            if((my_dataframe[column_name].dtype == "int64" or my_dataframe[column_name].dtype == "float64") and (my_dataframe[compare_column_name].dtype == "int64" or my_dataframe[compare_column_name].dtype == "float64")):
                print("————————————————————————————————")
                print("│0.Quit                         │") # >
                print("│1.Select greater data          │") # >
                print("│2.Select greater or equal data │") # >=
                print("│3.Select equal data            │") # ==
                print("│4.Select not equal data        │") # !=
                print("│5.Select smaller or equal data │") # <=
                print("│6.Select smaller data          │") # <
                print("————————————————————————————————")
                commandnum = 6
            else:
                print("————————————————————————————————")
                print("│0.Quit                         │") # >
                print("│1.Select equal data            │") # ==
                print("│2.Select not equal data        │") # !=
                print("————————————————————————————————")
                commandnum = 2
        
            while True:
                try:
                    command=int(input("Please enter a number: "))
                    if (command < 0 or command > commandnum):
                        print("\033[93m###Please enter 1-",commandnum,"! ###\033[0m\n")
                    else:
                        if(commandnum == 2):
                            if(command == 1):
                                command = 3
                            elif(command == 2):
                                command = 4
                        break
                except ValueError:
                    print("\033[91m### Illegal input! ###\033[0m\n")

            if(command == 0):
                return pd.DataFrame()
            elif(command == 1): # >
                for index, row in my_dataframe.iterrows():
                    a_value = row[column_name]
                    b_value = row[compare_column_name]
                    
                    # check A > B or not
                    if a_value > b_value:
                        # if A > B, add this row to new dataframe
                        new_df = pd.concat([new_df, pd.DataFrame([row], columns=my_dataframe.columns)], ignore_index=True)
                return new_df
            
            elif(command == 2): # >=
                for index, row in my_dataframe.iterrows():
                    a_value = row[column_name]
                    b_value = row[compare_column_name]
                    
                    # check A >= B or not
                    if a_value >= b_value:
                        # if A >= B, add this row to new dataframe
                        new_df = pd.concat([new_df, pd.DataFrame([row], columns=my_dataframe.columns)], ignore_index=True)
                return new_df
            elif(command == 3): # ==
                for index, row in my_dataframe.iterrows():
                    a_value = str(row[column_name])
                    b_value = str(row[compare_column_name])
                    
                    # check A == B or not
                    if a_value == b_value:
                        # if A == B, add this row to new dataframe
                        new_df = pd.concat([new_df, pd.DataFrame([row], columns=my_dataframe.columns)], ignore_index=True)
                return new_df
            
            elif(command == 4): # !=
                for index, row in my_dataframe.iterrows():
                    a_value = str(row[column_name])
                    b_value = str(row[compare_column_name])
                    
                    # check A != B or not
                    if a_value != b_value:
                        # if A != B, add this row to new dataframe
                        new_df = pd.concat([new_df, pd.DataFrame([row], columns=my_dataframe.columns)], ignore_index=True)
                return new_df
            
            elif(command == 5): # <=
                for index, row in my_dataframe.iterrows():
                    a_value = row[column_name]
                    b_value = row[compare_column_name]
                    
                    # check A <= B or not
                    if a_value <= b_value:
                        # if A <= B, add this row to new dataframe
                        new_df = pd.concat([new_df, pd.DataFrame([row], columns=my_dataframe.columns)], ignore_index=True)
                return new_df
            elif(command == 6): # <
                for index, row in my_dataframe.iterrows():
                    a_value = row[column_name]
                    b_value = row[compare_column_name]
                    
                    # check A < B or not
                    if a_value < b_value:
                        # if A < B, add this row to new dataframe
                        new_df = pd.concat([new_df, pd.DataFrame([row], columns=my_dataframe.columns)], ignore_index=True)
                return new_df
        
# Project
def project(my_dataframe):
    column = my_dataframe.columns
    remain=[]
    while True:
        index = 1
        if len(remain)!=0:
            print("\n\033[94m***************** Current keep column: *****************\033[0m")
            for tmp in remain:
                print(tmp)
            print("\033[94m********************************************************\033[0m\n")

        print("[0]: Finish")
        for c in column: # show colume
            print("[",index,"]: ",c,sep="",end="\n")
            index=index+1
        try:
            select_column=int(input("Please enter a number, select the column need to project: "))
            if select_column == 0: # finish
                break
            elif (select_column <= 0 or select_column > index-1) :
                print("### Illegal input! ###\n")
            else: # append remain column
                same_Column = False
                for tmp in remain:
                    if column[select_column-1] == tmp:
                        same_Column = True
                        print("\033[93m### This column is already in the list! ###\033[0m\n")
                        break
                if same_Column == False :
                    remain.append(column[select_column-1])
                        
        except ValueError:
            print("\033[91m## Illegal input! ###\033[0m\n")

    # delete all, except remain
    my_dataframe = my_dataframe.drop(my_dataframe.columns.difference(remain), axis=1)

    while(True):
        command = input("Do you want to make a multset?(Y/N): ")
        if(command == 'Y' or command == 'y' or command == 'YES' or command == 'yes'):
            break
        elif(command == 'N' or command == 'n' or command == 'NO' or command == 'no'):
            # delete repeat data
            my_dataframe = my_dataframe.drop_duplicates(subset=None, keep='first', inplace=False) # keep first appear otherwise all of the duplicate data will be delete
            break
        else:
            print("\033[91m### Illegal input! ###\033[0m\n")

    my_dataframe.reset_index(drop=True, inplace=True)
    return my_dataframe

# Rename column
def Rename(my_dataframe):
    column = my_dataframe.columns
    while True:
        index = 1
        print("[0]: Quit")
        for c in column:
            print("[",index,"]: ",c,sep="",end="\n")
            index=index+1
        try:
            select_column=int(input("Please enter a number: "))
            if(select_column == 0):
                return pd.DataFrame()
            if (select_column <= 0 or select_column > index-1) :
                print("\033[91m### Illegal input! ###\033[0m\n")
            else:
                break
        except ValueError:
            print("\033[91m### Illegal input! ###\033[0m\n")
    
    old_column = column[select_column-1]
    if old_column not in my_dataframe.columns:
        print("\033[93m### Don't exist this column!! ###\033[0m\n")
        return Rename(my_dataframe)
    else:
        # rename the column
        new_column = input("Please enter the new name for the column: ")
        my_dataframe.rename(columns={old_column: new_column}, inplace=True)
        print("\033[95m"+old_column+"  ->  "+new_column+"\033[0m")
        print("\033[95mColumn renamed successfully!\033[0m")
        return my_dataframe

'''
merge(left, right, on, left_on, right_on, how)

## how = (inner, outer, left, right, cross)
## inner: keep only the common key
## outer: keep all keys, if no data, fill NaN
## left: keep all keys from left
## right: keep all keys from right
## cross: Cartesian Product

'''

'''
concat(objs, axis, join, join_axes, ignore_index, keys, levels, names, verify_integrity, sort, copy)

## axis = 0: row, 1: column
## join = (inner, outer)
## ignore_index = True, clear index and reset it
## keys = ['x', 'y'], create a new column, x and y
## sort = True, sort the data
## copy = True, copy the data
'''
# Cartesian Product
def Cartesian_Product(my_dataframe):
    df = pd.DataFrame()
    df, success= loadfile(df)
    if success:
        my_dataframe = my_dataframe.merge(df, how = 'cross') # how = 'cross' is Cartesian Product
        df = df.reset_index(drop = True, inplace = True)
        return my_dataframe
    else:
        print("\033[91m### Fail to add a new file! ###\033[0m")
        return pd.DataFrame()
    
# Set Union(聯集)
def union(my_dataframe):
    df = pd.DataFrame()
    df, success= loadfile(df)
    if success:
        df = my_dataframe.merge(df, how = 'outer') # how = 'outer' is Union
        return df
    else:
        print("\033[91m### Fail to add a new file! ###\033[0m")
        return pd.DataFrame()

"""
drop_duplicates(subset, keep, inplace, ignore_index)

## subset = None, all columns
## keep = (first, last, False)
## first: keep the first appear, last: keep the last appear, False: drop all duplicates
## inplace = True, modify the data
## ignore_index = True, clear index and reset it
"""

# Set Difference(差集)
def difference_data(my_dataframe):
    df = pd.DataFrame()
    df, success= loadfile(df)
    if success:
        # check the columns which is in df also in my_dataframe
        common_columns=[]
        for column1 in my_dataframe.columns:
            for column2 in df.columns:
                if column1 == column2:
                    if column1 not in common_columns:
                        common_columns.append(column1)
                        break
        if(len(common_columns) < df.columns.size or len(common_columns) < my_dataframe.columns.size):
            return pd.DataFrame()
                    
        # set the same datatype as my_dataframe
        output = pd.DataFrame(columns=my_dataframe.columns)
        for i, dtype in my_dataframe.dtypes.items():
            output[i] = output[i].astype(dtype)

        # check the data is exist in df or not
        for idx1, row1 in my_dataframe.iterrows():
            Same = False
            for idx2, row2 in df.iterrows():
                if row1.equals(row2):
                    Same = True
                    break
            if Same == False:
                # if the data doesn't exist in df, add this row to output
                output = pd.concat([output, my_dataframe.iloc[[idx1]]], ignore_index=True)
                # print(output)

        return output
    else:
        print("\033[91m### Fail to add a new file! ###\033[0m")
        return pd.DataFrame()
    
# Set insersection(交集)
def insersection(my_dataframe):
    df = pd.DataFrame()
    df, success= loadfile(df) # inner
    if success:
        df = my_dataframe.merge(df)
        return df
    else:
        print("\033[91m### Fail to add a new file! ###\033[0m")
        return pd.DataFrame()
    
# Division(除法)   
def division(my_dataframe):
    df = pd.DataFrame()
    df, success = loadfile(df)
    if success:
        # check the columns which is in df also in my_dataframe
        common_columns=[]
        for column1 in my_dataframe.columns:
            for column2 in df.columns:
                if column1 == column2:
                    if column1 not in common_columns:
                        common_columns.append(column1)
                        break
        if(len(common_columns) < df.columns.size):
            print("\033[91m### Column format errpr! ###\033[0m")
            return pd.DataFrame()
        
        # find the columns which is not in df.columns
        remain_columns=[]
        for column in my_dataframe.columns:
            if column not in common_columns:
                remain_columns.append(column)

        # create new dataframe, same columns as my_dataframe
        tmp = pd.DataFrame(columns=my_dataframe.columns)
        output = pd.DataFrame(columns=my_dataframe.columns)
        # set the same datatype as my_dataframe
        for i, dtype in my_dataframe.dtypes.items():
            output[i] = output[i].astype(dtype)
            tmp[i] = tmp[i].astype(dtype)
        copydata1 = my_dataframe # copy the data


        index_to_drop = [] # record the index which is already checked
        for idx1, row1 in my_dataframe.iterrows():
            for idx2, row2 in copydata1.iterrows():
                Same = True
                for column in remain_columns:
                    if row1[column] != row2[column]:
                        Same = False
                        break
                if Same:
                    index_to_drop.append(idx2)
                    tmp = pd.concat([tmp, pd.DataFrame([row2], columns=my_dataframe.columns)], ignore_index=True)

            if tmp.size > my_dataframe.shape[1] : # shape[1] = number of columns
                # check if the data as same as df or not, renew the output
                output = compare(tmp, df, output)

            # drop the data which is already checked
            copydata1.drop(index_to_drop, inplace=True)
            index_to_drop.clear()
            tmp.drop(tmp.index, inplace=True)

        # drop the columns which is df.columns
        output = output.drop(df.columns, axis=1)
        return output

    else:
        print("\033[91m### Fail to add a new file! ###\033[0m")
        return my_dataframe
    
def compare(tmp, df, output):
    count = 0 # shape[0] = number of rows
    for idx1, row1 in df.iterrows():
        for idx2, row2 in tmp.iterrows():
            Same = True
            for column in df.columns:
                if row1[column] != row2[column]:
                    Same = False
                    break
            if Same:
                break
        if Same:
            count += 1 # count the number of same data

    # if the data as same as df, renew the output
    if count == df.shape[0]: # shape[0] = number of rows
        output = pd.concat([output, tmp.iloc[[0]]], ignore_index=True)
    return output


# Natural join(合併)
def natural_join(my_dataframe):
    df = pd.DataFrame()
    df, success = loadfile(df)
    if success:
        common_columns=[] # record the common columns
        for column1 in my_dataframe.columns:
            for column2 in df.columns:
                if column1 == column2:
                    if column1 not in common_columns:
                        common_columns.append(column1)
                        break

        # check the common columns is empty or not
        if len(common_columns) == 0:
            print("\033[93m### No common columns found for natural join! ###\033[0m")
            return pd.DataFrame()
        else:
            my_dataframe = my_dataframe.merge(df, on=common_columns, how='inner')
            return my_dataframe
    else:
        print("\033[91m### Fail to add a new file! ###\033[0m")
        return pd.DataFrame()

def writefile(my_dataframe):
    while(True):
        filename = input("Please enter a file name(Enter quit to leave): ")
        if(filename == 'quit'):
            return
        fileName_Exist = os.path.isfile(filename+'.csv')
        
        # check the file is exist or not
        while(fileName_Exist):
            command = input("\033[93mAlready have this filename, do you want to continue?(Y/N): \033[0m")
            if(command == 'Y' or command == 'y' or command == 'YES' or command == 'yes'):
                fileName_Exist = False
            elif(command == 'N' or command == 'n' or command == 'NO' or command == 'no'):
                print("\033[92m### Go back to the previous step ###\033[0m\n")
                break
            else:
                print("\033[91m### Illegal input! ###\033[0m\n")
        
        # create the file
        if(fileName_Exist == False):
            try:
                my_dataframe.to_csv(filename+".csv", index =  False)
                print('\033[93msuccess created '+filename+'.csv-!!\033[0m\n', sep='')
                return
            except FileExistsError:
                print("\033[91m### FileExists Error! ###\033[0m\n")
            except:
                print("\033[91m### Unexcepted Error! ###\033[0m\n")

def operationlist():
    print("—————————————————————————————————————————————————")
    print("│0.Quit                                         │")
    print("│1.Load file                                    │")
    print("│2.Implement select                             │")
    print("│3.Implement project                            │")
    print("│4.Implement rename                             │")
    print("│5.Implement cartesian Product                  │")
    print("│6.Implement set Union                          │")
    print("│7.Implement set Difference                     │")
    print("│8.Implement set insersection                   │")
    print("│9.Implement division                           │")
    print("│10.Implement natural join                      │")
    print("│11.Export the archive                          │")
    print("│12.Show current data                           │")
    print("│13.Update current data to last calculation     │")
    print("—————————————————————————————————————————————————")

def Quit():
    print("\n————————————————————————————————————————")
    print("|    Thank you using this program      |")
    print("——————————————————END———————————————————\n")
    # time.sleep(5)
    return False



def main():
    running = True
    file_Exist = False
    my_dataframe = pd.DataFrame()
    out_dataframe = pd.DataFrame()
    print("\nWellcome to this program")
    while(running):
        operationlist() # operation menu
        while True: # Enter the command
            try:
                command=int(input("Please enter the command: "))
                break
            except ValueError:
                print("\033[91m### Illegal input! ###\033[0m\n")
                operationlist()

        if(command == 0):
            running = Quit()
        elif(command == 1):
                my_dataframe, file_Exist = loadfile(my_dataframe)
                # print(my_dataframe)

        elif(command == 2):
            if(file_Exist):
                out_dataframe = select_data(my_dataframe)
                print("\033[92m—————————————————————————————————— END Select ———————————————————————————————————\033[0m")
                if(out_dataframe.empty):
                    print("### This file no data!! ###")
                else:
                    print(out_dataframe)
                print("\033[92m—————————————————————————————————————————————————————————————————————————————————\033[0m")
            else:
                print("\033[93m### Please Load file first!! ###\033[0m\n")
        elif(command == 3):
            if(file_Exist):
                out_dataframe = project(my_dataframe)
                print("\033[92m————————————————————————————————— END Project ———————————————————————————————————\033[0m")
                if(out_dataframe.empty):
                    print("### This file no data!! ###")
                else:
                    print(out_dataframe)
                print("\033[92m—————————————————————————————————————————————————————————————————————————————————\033[0m")
            else:
                print("\033[93m### Please Load file first!! ###\033[0m\n")

        elif(command == 4):
            if(file_Exist):
                out_dataframe = Rename(my_dataframe)
                print("\033[92m—————————————————————————————————— END Rename ———————————————————————————————————\033[0m")
                if(out_dataframe.empty):
                    print("### This file no data!! ###")
                else:
                    print(out_dataframe)
                print("\033[92m—————————————————————————————————————————————————————————————————————————————————\033[0m")
            else:
                print("\033[93m### Please Load file first!! ###\033[0m\n")

        elif(command == 5):
            if(file_Exist):
                out_dataframe = Cartesian_Product(my_dataframe)
                print("\033[92m————————————————————————————— END Cartesian_Product —————————————————————————————\033[0m")
                if(out_dataframe.empty):
                    print("### This file no data!! ###")
                else:
                    print(out_dataframe)
                print("\033[92m—————————————————————————————————————————————————————————————————————————————————\033[0m")
            else:
                print("\033[93m### Please Load file first!! ###\033[0m\n")

        elif(command == 6):
            if(file_Exist):
                out_dataframe = union(my_dataframe)
                print("\033[92m——————————————————————————————————— End Union ———————————————————————————————————\033[0m")
                if(out_dataframe.empty):
                    print("### This file no data!! ###")
                else:
                    print(out_dataframe)
                print("\033[92m—————————————————————————————————————————————————————————————————————————————————\033[0m")
            else:
                print("\033[93m### Please Load file first!! ###\033[0m\n")

        elif(command == 7):
            if(file_Exist):
                out_dataframe = difference_data(my_dataframe)
                print("\033[92m———————————————————————————————— End Difference —————————————————————————————————\033[0m")
                if(out_dataframe.empty):
                    print("### This file no data!! ###")
                else:
                    print(out_dataframe)
                print("\033[92m—————————————————————————————————————————————————————————————————————————————————\033[0m")
            else:
                print("\033[93m### Please Load file first!! ###\033[0m\n")

        elif(command == 8):
            if(file_Exist):
                out_dataframe = insersection(my_dataframe)
                print("\033[92m——————————————————————————————— END Insersection ————————————————————————————————\033[0m")
                if(out_dataframe.empty):
                    print("### This file no data!! ###")
                else:
                    print(out_dataframe)
                print("\033[92m—————————————————————————————————————————————————————————————————————————————————\033[0m")
            else:
                print("\033[93m### Please Load file first!! ###\033[0m\n")

        elif(command == 9):
            if(file_Exist):
                out_dataframe = division(my_dataframe)
                print("\033[92m————————————————————————————————— END Division ——————————————————————————————————\033[0m")
                if(out_dataframe.empty):
                    print("### This file no data!! ###")
                else:
                    print(out_dataframe)
                print("\033[92m—————————————————————————————————————————————————————————————————————————————————\033[0m")
            else:
                print("\033[93m### Please Load file first!! ###\033[0m\n")

        elif(command == 10):
            if(file_Exist):
                out_dataframe = natural_join(my_dataframe)
                print("\033[92m——————————————————————————————— END Natural Join ————————————————————————————————\033[0m")
                if(out_dataframe.empty):
                    print("### This file no data!! ###")
                else:
                    print(out_dataframe)
                print("\033[92m—————————————————————————————————————————————————————————————————————————————————\033[0m")
            else:
                print("\033[93m### Please Load file first!! ###\033[0m\n")

        elif(command == 11):
            if(file_Exist):
                writefile(my_dataframe)
            else:
                print("\033[93m### Please Load file first!! ###\033[0m\n")

        elif(command == 12):
            if(file_Exist):
                print("\033[92m——————————————————————————————— Show current data ———————————————————————————————\033[0m")
                print(my_dataframe)
                print("\033[92m—————————————————————————————————————————————————————————————————————————————————\033[0m")
            else:
                print("\033[93m### Please Load file first!! ###\033[0m\n")

        elif(command == 13):
            if(file_Exist):
                print("\033[92m——————————————————————————————— Reset current data ——————————————————————————————\033[0m")
                if(out_dataframe.empty):
                    print("\033[93m### Last file is empty!! ###\033[0m")
                else:
                    my_dataframe = out_dataframe
                    print("### Update success!! ###")
                    print(my_dataframe)
                print("\033[92m—————————————————————————————————————————————————————————————————————————————————\033[0m")
            else:
                print("\033[93m### Please Load file first!! ###\033[0m\n")
        else:
            print("\033[91m### The command doesn't exist !! ###\033[0m\n")
        
        print()


main()