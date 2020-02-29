import os
import csv
import operator
#Read in csv file
filepath = os.path.join(".","Resources","budget_data.csv")
with open(filepath,newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #remove header
    next(csvreader)

    total_month = 0
    net_total = 0
    last_month_value = 0
    total_change = 0
    Change_dictionary = {}
    for row in csvreader:
        #The total number of months included in the dataset
        total_month = total_month + 1

        #The net total amount of "Profit/Losses" over the entire period
        net_total = net_total + float(row[1])
        
        #The average of the changes in "Profit/Losses" over the entire period - variable preparation
        monthly_change = float(row[1]) - last_month_value
        total_change = total_change + monthly_change
        last_month_value = float(row[1])
        # create a dictionary for month and monthly change - 1st month to be removed below
        Change_dictionary.update({row[0]: monthly_change})

    # create a dictionary for month and monthly change - 1st month removed
    del Change_dictionary[next(iter(Change_dictionary))]
    
    #Create a list with monthly change
    monthly_change_list = list(Change_dictionary.values()) 
       
    #The average of the changes in "Profit/Losses" over the entire period - final formula
    total_change = sum(monthly_change_list)
    average_change = total_change/(total_month-1)
    #max & min monthly change value        
    greatest_increase = max(monthly_change_list)
    greatest_decrease = min(monthly_change_list)
    #find the key of max & min monthly change in dictionary
    key_list = list(Change_dictionary.keys())
    greatest_increase_month = key_list[monthly_change_list.index(greatest_increase)]
    greatest_decrease_month = key_list[monthly_change_list.index(greatest_decrease)]

    print("Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {total_month}")
    print(f"Total: ${int(net_total)}")
    print(f"Average Change: ${round(average_change,2)}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${int(greatest_increase)})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${int(greatest_decrease)})")

text_file = open("Main_Result.txt","w+")
print("Financial Analysis",file = text_file)
print("------------------------------",file = text_file)
print(f"Total Months: {total_month}",file = text_file)
print(f"Total: ${int(net_total)}",file = text_file)
print(f"Average Change: ${round(average_change,2)}",file = text_file)
print(f"Greatest Increase in Profits: {greatest_increase_month} (${int(greatest_increase)})",file = text_file)
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${int(greatest_decrease)})",file = text_file)
text_file.close()