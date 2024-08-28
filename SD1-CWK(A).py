import os
import math
import statistics
import datetime


# Function to add a research data entry
'''Get a unique name(If the name equals to pre-entered name, they ask to re-enter the name)
    and get researcher's name and the data points as input.
    Then inputs saved to entries as a dictionaries. Date(date = entry entered date) will automatically saved to the dictionary'''
  

def add_entry(entries):
  
    while True:
        
        length = len(entries)
        exist_index = 0
        another_entry = None
        
        if length != 0:
            while True:
                name_found = False
                name = input("\nEnter experiment name : ")

                while exist_index < length:
                    if entries[exist_index]["name"] == name:
                        name_found = True
                        print("\nName has been exist! Please enter a unique name")
                        break
                    else:
                        exist_index += 1
        
                if name_found == False:
                    break
                    
        else:
            name = input("\nEnter experiment name : ")
                
        date = str(datetime.datetime.now().date())
    
        researcher = input("\nEnter the researcher's name : ")
    
        points_list = []
        while True:
            
            try:
                data = float(input("\nInput data points : "))
                points_list.append(data)  
                
                while True:
                    more_points = input("\nDo you wish to add more points(Y/N) : ").lower()
                    if more_points == "n":
                        entries.append({"name": name,"date": date,"researcher": researcher, "data": points_list})
                        
                        while True:
                            
                            another_entry = input("\nDo you want to add another entry(Y/N) : ").lower()
                            
                            if another_entry == "n":  
                                return
                            elif another_entry == "y":
                                break
                            else:
                                print("\nPlease input \"y\" or \"N\"")
                                
                    elif more_points == "y":
                        break
                    else:
                        print("\nPlease input \"y\" or \"N\"")
                    if another_entry == "y":
                        break
                if another_entry == "y":
                    break
            
            except ValueError:
                print("\nPlease input numeric values as masurements")
        

# Function to view all research data entries

'''Load entries from the "research_data.txt" to the system and show the all existing entries.
If the entries not found, it will show a messege'''

def view_entries(entries):
    entry_count = len(entries)
    if entry_count != 0:
        index = 0
        while index < entry_count:
            print("\n" + str(index+1) + ". " + "name : " + entries[index]["name"] + "\tdate : " + entries[index]["date"] + "\tresearcher : " + entries[index]["researcher"] + "\tdata : " + str(entries[index]["data"]))
            index += 1
    else:
        print("\nAny entry does not input yet")
        

# Function to save entries to a text file
'''This function to save entries(list of entry dictionaries) to "research_data.txt" file'''

def save_entries_to_file(entries, filename):
    if len(entries) == 0:
        print("\nAny entry does not found to save!")
    else:
        with open(filename, "w") as file:
            index = 0
            for entry in entries:
                file.write(str(index+1) + ". " + "name : " + entries[index]["name"] + "\tdate : " + entries[index]["date"] + "\tresearcher : " + entries[index]["researcher"] + "\tdata : " + str(entries[index]["data"]) + "\n")
                index += 1
            print("Entries saved to the file")

                
# Function to load entries from a text file
def load_entries_from_file(filename):
    entries = []
    try:
        with open("research_data.txt","r") as file:
            for line in file:
                entries.append(eval(line.strip()))
    except FileNotFoundError:
        #print("gtrfd")
        return []
    return entries

# Function to perform data analysis

'''This function ask to enter the name of entry to analyze, if the name exist it will show average, standard deviation and the median
if it is not print a message to re-enter the name of entry'''

def analyze_data(entries):

    while True:
        
        length = len(entries)
        
        if length != 0:
            while True:
                exist_index = 0
                name_found = False
                name = input("\nEnter experiment name to analyze : ")

                while exist_index < length:
                    
                    if entries[exist_index]["name"] == name:
                        name_found = True
                        data_found = exist_index
                        tot = 0.0
                        no_points = 0
                        
                        for points in entries[data_found]["data"]:
                            tot += points
                            no_points += 1
                            avg = tot / length
                        print("\nAverage : " + str(avg))
                        variance = 0.0
                        
                        for points in entries[data_found]["data"]:
                            variance += (points - avg) ** 2 /  no_points
                            
                        standard_deviation = math.sqrt(variance)
                        
                        print("\nStandard Deviation : " + str(standard_deviation))
                        
                        median = statistics.median(entries[data_found]["data"])
                        
                        print("\nMedian : " + str(median))
                        break
                    
                    else:
                        exist_index += 1
        
                if name_found == True:
                    break
                else:
                   print("\nname does not match, Please check and re-enter the name of entry to delete")       
        else:
            print("\nAny data not found to analyze ")
            break
        if name_found == True:
            break
       
    

def update_entry(entries):

    while True:
        
        length = len(entries)
        
        if length != 0:
            while True:
                exist_index = 0
                name_found = False
                name = input("\nEnter experiment name to update : ")

                while exist_index < length:
                    if entries[exist_index]["name"] == name:
                        name_found = True
                        print("1. Name")
                        print("2. Researcher")
                        print("3. Data")
                        #print("4. Update All")
                        #print("5. Exit")
                        try:
                            update_option = int(input("Input category you want to update : "))

                            if update_option == 1:
                                while True:
        
                                    length = len(entries)
                                    avai_index = 0
                                    old_name_found = False
        
                                    if length != 0:
                                        while True:
                                            print(entries)
                                            #old_name_found = False
                                            new_name = input("\nEnter new experiment name : ")

                                             

                                            while avai_index < length:
                                                if entries[avai_index]["name"] == new_name:
                                                    old_name_found = True
                                                    print("Name has been exist! Please enter a unique name")
                                                    break
                                                else:
                                                    avai_index += 1
                                                    
        
                                            if old_name_found == False:
                                                entries[exist_index]["name"] = new_name
                                                print("Name updated")
                                                break
                                            
                                        if old_name_found == False:
                                                return
                            elif update_option == 2:
                                new_researcher = input("Enter new researchser name : ")
                                entries[exist_index]["researcher"] = new_researcher
                                break
                                
                            elif update_option == 3:
                                new_points_list = []
                                while True:
                                    try:
                                        new_data = float(input("Input new data points : "))
                                        new_points_list.append(new_data)  
                                        print(new_points_list)
                                        while True:
                                            more_points = input("Do you wish to add more points(Y/N) : ").lower()
                                            if more_points == "n":
                                                entries[exist_index]["data"] = new_points_list
                                                    #entries.append({"name": name,"date": date,"researcher": researcher, "data": points_list})
                                                print(entries)
                                                return
                            
                                            elif more_points == "y":
                                                break
                                            else:
                                                print("Please input \"y\" or \"N\"")
                                        
                                    except ValueError:
                                        print("Please input numeric values as masurements")
        
                    
                                
                            else:
                                print("Invalid input")
                                
                                                
                        except ValueError:
                            print("Invalid input. Please re-enter your choice")
                    
                    else:
                        exist_index += 1
                        
        
            
                if name_found == True:
                    break
                else:
                   print("name does not match, Please check and re-enter the name of entry to delete")
                   break
        else:
            print("\nAny data not found to analyze\n ")
            break
        if name_found == True:
            break
    

''' This function is for delete the entries using name. '''  
def delete_entry(entries):


    while True:
        
        length = len(entries)
        exist_index = 0
        name_found = False
        
        if length != 0:
            while True:
                name = input("\nEnter experiment name to delete : ")

                while exist_index < length:
                    if entries[exist_index]["name"] == name:
                        name_found = True
                        del entries[exist_index]
                        print("\nEntry deleted successfully!\n")
                        break
                    else:
                        exist_index += 1
        
                if name_found == False:
                    print("\nname does not match, Please check and re-enter the name of entry to delete\n")
                    break
                
                else:
                    break
                    
        else:
            print("\nNo any entry to delete\n")
            break
        
        if name_found == True:
            break
        

# Main function to interact with the user
def main():
    filename = "research_data.txt"
    entries = load_entries_from_file(filename)
    
    while True:
        print("\nMenu:\n")
        print("1. Add a research data entry")
        print("2. View all entries")
        print("3. Analyze data")
        print("4. Save entries to file")
        print("5. Update a entry")
        print("6. Delete a entry")
        print("7. Exit")
        
        choice = input("\nEnter your choice: ")
        if choice == '1':
            add_entry(entries)
        elif choice == '2':
            view_entries(entries)
        elif choice == '3':
            analyze_data(entries)
        elif choice == '4':
            save_entries_to_file(entries, filename)
        elif choice == '5':
            update_entry(entries)
        elif choice == '6':
            delete_entry(entries)
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
