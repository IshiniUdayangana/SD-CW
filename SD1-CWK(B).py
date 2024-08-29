import os
import datetime
import math
import statistics

class ResearchDataManager:
    def __init__(self):
        self.entries = []
        self.filename = "research_data.txt"
    
    def add_entry(self):
    
        while True:
        
            length = len(self.entries)
            exist_index = 0
            another_entry = None
        
            if length != 0:
                while True:
                    name_found = False
                    name = input("\nEnter experiment name : ")

                    while exist_index < length:
                        if self.entries[exist_index]["name"] == name:
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
                            self.entries.append({"name": name,"date": date,"researcher": researcher, "data": points_list})
                            
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
            

    
    def view_entries(self):
        entry_count = len(self.entries)
        if entry_count != 0:
            index = 0
            while index < entry_count:
                print("\n" + str(index+1) + ". " + "name : " + self.entries[index]["name"] + "\tdate : " + self.entries[index]["date"] + "\tresearcher : " + self.entries[index]["researcher"] + "\tdata : " + str(self.entries[index]["data"]))
                index += 1
        else:
            print("\nAny entry does not input yet")
    
    
    def save_entries_to_file(self):
        if len(self.entries) == 0:
            print("\nAny entry does not found to save!")
        else:
            with open(self.filename, "w") as file:
                index = 0
                for entry in self.entries:
                    file.write(str(index+1) + ". " + "name : " + self.entries[index]["name"] + "\tdate : " + self.entries[index]["date"] + "\tresearcher : " + self.entries[index]["researcher"] + "\tdata : " + str(self.entries[index]["data"]) + "\n")
                    index += 1
                print("\nEntries saved to the file")

    
    def load_entries_from_file(self):
        self.entries = []
        try:
            with open(self.filename,"r") as file:
                for line in file:
                    self.entries.append(eval(line.strip()))
        except FileNotFoundError:
            return []
        return self.entries

    
    def analyze_data(self):
        
        while True:
        
            length = len(self.entries)
            
            if length != 0:
                while True:
                    exist_index = 0
                    name_found = False

                    name = input("\nEnter experiment name to analyze : ")

                    while exist_index < length:
                        
                        if self.entries[exist_index]["name"] == name:
                            name_found = True
                            data_found = exist_index
                            tot = 0.0
                            no_points = 0
                            print(self.entries[data_found]["data"])
                            
                            for points in self.entries[data_found]["data"]:
                                tot += points
                                no_points += 1
                                avg = tot / length
                            print("\nAverage : " + str(avg))
                            variance = 0.0
                            
                            for points in self.entries[data_found]["data"]:
                                
                                variance += (points - avg) ** 2 /  no_points
                                
                            standard_deviation = math.sqrt(variance)
                            print("\nStandard Deviation : " + str(standard_deviation))

                            median = statistics.median(self.entries[data_found]["data"])

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


    def update_entry(self):

        while True:
        
            length = len(self.entries)
        
            if length != 0:
                while True:
                    exist_index = 0
                    name_found = False
                    name = input("\nEnter experiment name to update : ")

                    while exist_index < length:
                        if self.entries[exist_index]["name"] == name:
                            name_found = True
                            print("1. Name")
                            print("2. Researcher")
                            print("3. Data")
                
                            try:
                                update_option = int(input("Input category you want to update : "))

                                if update_option == 1:
                                    while True:
        
                                        length = len(self.entries)
        
                                        if length != 0:
                                            while True:
                                                avai_index = 0
                                                old_name_found = False
                                                new_name = input("\nEnter new experiment name : ")

                                             

                                                while avai_index < length:
                                                    if self.entries[avai_index]["name"] == new_name:
                                                        old_name_found = True
                                                        print("Name has been exist! Please enter a unique name")
                                                        break
                                                    else:
                                                        avai_index += 1
                                                    
        
                                                if old_name_found == False:
                                                    self.entries[exist_index]["name"] = new_name
                                                    print("Name updated")
                                                    break
                                                
                                            if old_name_found == False:
                                                    return
                                elif update_option == 2:
                                    new_researcher = input("Enter new researchser name : ")
                                    self.entries[exist_index]["researcher"] = new_researcher
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
                                                    self.entries[exist_index]["data"] = new_points_list
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
    

    

    def delete_entry(self):
        while True:
        
            length = len(self.entries)
            exist_index = 0
            name_found = False
        
            if length != 0:
                while True:
                    name = input("\nEnter experiment name to delete : ")

                    while exist_index < length:
                        if self.entries[exist_index]["name"] == name:
                            name_found = True
                            del self.entries[exist_index]
                            print("Entry deleted successfully")
                            break
                        else:
                            exist_index += 1
        
                    if name_found == False:
                        print("name does not match, Please check and re-enter the name of entry to delete")
                        break
                    
                    else:
                        break
                    
            else:
                print("\nNo any entry to delete")
                break
        
            if name_found == True:
                break

def main():
    manager = ResearchDataManager()
    manager.load_entries_from_file()
    
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
            manager.add_entry()
        elif choice == '2':
            manager.view_entries()
        elif choice == '3':
            manager.analyze_data()
        elif choice == '4':
            manager.save_entries_to_file()
        elif choice == '5':
            manager.update_entry()
            pass
        elif choice == '6':
            manager.delete_entry()
        elif choice == '7':
            break
        else:
            print("\nInvalid choice, please try again.")

if __name__ == "__main__":
    main()
