import csv
from csv import reader
import os.path
from csv import DictReader
from csv import DictWriter
import random
import os
import shutil
from os import path



def add_column_in_csv(input_file, output_file, transform_row, tansform_column_names):

                                                            # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
    open(output_file, 'w', newline='') as write_obj:
                                                            # Create a DictReader object from the input file object
        dict_reader = DictReader(read_obj)
                                                            # Get a list of column names from the csv
        field_names = dict_reader.fieldnames
                                                            # Call the callback function to modify column name list
        tansform_column_names(field_names)
                                                            # Create a DictWriter object from the output file object by passing column / field names
        dict_writer = DictWriter(write_obj, field_names)
                                                            # Write the column names in output csv file
        dict_writer.writeheader()
                                                            # Read each row of the input csv file as dictionary
        for row in dict_reader:
                                                            # Modify the dictionary / row by passing it to the transform function (the callback)
            transform_row(row, dict_reader.line_num)
                                                            # Write the updated dictionary or row to the output file
            dict_writer.writerow(row)



final_final = [] # a kone su tr
final = {}
data = [] #dictionary u poat
count=1
header = []
new_header = []
j = 0


Input = []

header_of_new_col = []
default_text = ''

        

#check whether file exits or not

if os.path.isfile('student.csv'):
    print ("File exists")
    with open('student.csv', 'r') as a:
        A = reader(a)
        header = next(A)
        print("The already added headers are\n",header)
    ans = input("Waana add more?\n Y/N: ")
    
    #htet htae yin
    
    if ans == 'Y':
        while True:
            B = input("Enter the header %d: "%count)
            count+=1
            if (B == 's'):
                print("New headers are:\n",new_header)
                break
            else:
                new_header.append(B)
        count = 1


        for i in range(len(new_header)):
            output = str(random.randint(1,10000))
            Input.append(output)

        print(Input)
        decide = input("Enter the file name to update: ")                                                                    
        add_column_in_csv(decide+'.csv', Input[0] + '.csv',
                            lambda row, line_num: row.update({new_header[0]: default_text}),
                            lambda field_names: field_names.append(new_header[0]))

        for i in range(len(new_header)-1):
            add_column_in_csv(Input[i] +'.csv', Input[i+1] + '.csv',
                            lambda row, line_num: row.update({new_header[i+1]: default_text}),
                            lambda field_names: field_names.append(new_header[i+1]))
            
        
        while j < len(Input)-1:
            os.remove(Input[j]+'.csv')
            print(j)
            j+=1


            ############ Header New ################
            
        with open(Input[-1]+'.csv', 'r') as f:
            F = reader(f)
            Header = next(F)
            print(Header)

        while True:
            for i in range(len(Header)):
                C = input("Enter the %s for student: "%(Header[i]))
                if C == 'n':
                    break
                else:
                    data.append(C)
            if C == 'n':
                break
            
            final = dict(zip(Header , data))
            data = []
            final_final.append(final)
                   
            if C == 'n':
                break
           
        FINAL = len(final_final)
         
        with open (Input[-1]+'.csv', 'a+', newline = '') as a:
            writer = csv.DictWriter(a, fieldnames = Header)
            for i in range(FINAL):
                writer.writerow(final_final[i])

        desired = input("Enter the name for your updated file: ")

        if path.exists(Input[-1]+".csv"):
                # get the path to the file in the current directory
                src = path.realpath(Input[-1]+".csv");
                        
                # rename the original file
                os.rename(Input[-1]+".csv",desired+".csv") 
                
               ##################################################################################

                
    elif ans == 'N':
        
        with open('student.csv', 'r') as f:
            F = reader(f)
            header = next(F)
            print(header)
        while True:
            for i in range(len(header)):
                C = input("Enter the %s for student: "%(header[i]))
                if C == 'n':
                    break
                else:
                    data.append(C)
            if C == 'n':
                break
            
            final = dict(zip(header , data))
            data = []
            final_final.append(final)
                   
            if C == 'n':
                break
           
        FINAL = len(final_final)
             
        with open ('student.csv', 'a+', newline = '') as a:
            writer = csv.DictWriter(a, fieldnames = header)

            for i in range(FINAL):
                writer.writerow(final_final[i])
                

        
            
        
                
     
            
               

#if not exit
        
else:
    print ("File does not exist")
    print("Let's create a file\nEnter s to stop adding header")
    while True:
        B = input("Enter the header %d: "%count)
        count+=1
        if (B == 's'):
            print(header)
            break
        else:
            header.append(B)
    count = 1
    while True:
        for i in range(len(header)):
            C = input("Enter the %s for student: "%(header[i]))
            if C == 'n':
                break
            else:
                data.append(C)
        if C == 'n':
            break
        
        final = dict(zip(header , data))
        data = []
        final_final.append(final)
               
        if C == 'n':
            break
       
    FINAL = len(final_final)
         
    with open ('student.csv', 'w', newline = '') as a:
        writer = csv.DictWriter(a, fieldnames = header)
        writer.writeheader()
        for i in range(FINAL):
            writer.writerow(final_final[i])
    




##    # Check file as empty
##    if header != None:
##        # Iterate over each row after the header in the csv
##        for row in A:
##            # row variable is a list that represents a row in csv
##            print(row)
##
##print('Header was: ')
##print(header)
    

        
