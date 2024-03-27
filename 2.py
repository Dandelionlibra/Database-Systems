import pandas as pd
import os
print(os.getcwd())

def loadfile(my_dataframe):
    filename = input("Please enter a file name(enter exist leave):") 
    if(filename == "exist"):
        return  my_dataframe, False
    try:
        # my_dataframe = pd.read_csv("C:\\Users\\user\\OneDrive\\桌面\\course\\Database Systems\\Database-Systems_midterm\\"+filename+".csv")
        my_dataframe = pd.read_csv(filename+".csv")
        print(filename+'.csv-success!!')
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
    # print(my_dataframe)
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
    print("column_name:",column_name)


    if column_name not in my_dataframe.columns:
        print("### Don't exist this column!! ###\n")
        select_data(my_dataframe)
    else:
        print("————————————————————————")
        print("│1.Select bigger data  │")
        print("│2.Select equal data   │")
        print("│3.Select smaller data │")
        print("————————————————————————")
        
        while True:
            try:
                command=int(input("Please enter a number:"))
                if command < 1 or command > 3:
                    print("###Please enter 1-3! ###\n")
                else:
                    break
            except ValueError:
                print("### Illegal input! ###\n")
        if(command == 1): # error input string
            while True:
                try:
                    
                    value=int(input("Please enter the value(int):"))
                    if(my_dataframe[column_name].dtype != "int64"):
                        print("### Illegal input! ###")
                        print("### Make sure the datatype is correct! ###")
                        select_data(my_dataframe)
                    else:
                        break
                except ValueError:
                    print("### Illegal input! ###\n")
                    
            # try:
            #     int(my_dataframe[column_name])
            # except ValueError:  
            #     print("### Illegal input! ###\n")
            return my_dataframe[my_dataframe[column_name] > value]
        elif(command == 2):
            while True:
                try:
                    value=input("Please enter the value:")
                    break
                except ValueError:
                    print("### Illegal input! ###")
                    print("### Illegal input! ###\n")
            return my_dataframe[my_dataframe[column_name] == value]
        elif(command == 3):
            while True:
                try:
                    value=int(input("Please enter the value(int):"))
                    break
                except ValueError:
                    print("### Illegal input! ###")
                    print("### Illegal input! ###\n")
            # try:
            #     int(my_dataframe[column_name])
            # except ValueError:  
            #     print("### Illegal input! ###\n")
            return my_dataframe[my_dataframe[column_name] < value]
    

# Project

# Rename

# Cartesian Product

# Set Union(聯集)

# Set Difference(差集)

# Set insersection()

# Division(除法)

# Natural join(合併)


def writefile(out_dataframe):
    filename = input("Please enter a file name:")
    out_dataframe.to_csv(filename+".csv")

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
                command=int(input("Please enter the command:"))
                break
            except ValueError:
                print("### Illegal input! ###\n")

        if(command == 0):
            running = Quit()
        elif(command == 1):
                my_dataframe, file_Exist = loadfile(my_dataframe)
                print(my_dataframe)
        elif(command == 2):
            if(file_Exist):
                out_dataframe = select_data(my_dataframe)
                print("******************************************************")
                print(out_dataframe)
                print("******************************************************")
            else:
                print("### Please Load file first!! ###\n")
        elif(command == 3):
            if(file_Exist):
                # out_dataframe = select_data(my_dataframe)
            # else:
                print("### Please Load file first!! ###\n")




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