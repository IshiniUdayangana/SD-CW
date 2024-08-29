import os
import avro.schema
import avro.io
import io
import datetime
import math
import statistics
import avro.datafile

class ResearchDataManager:
    def __init__(self):
        self.entries = []
        self.filename = "research_data.avro"
        self.schema = avro.schema.Parse(open("research_data_schema.avsc", "r").read())

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
                        if self.entries[exist_index]["experiment_name"] == name:
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
                            self.entries.append({"experiment_name": name,"date": date,"researcher": researcher, "data_points": points_list})
                            
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
                print("\n" + str(index+1) + ". " + "name : " + self.entries[index]["experiment_name"] + "\tdate : " + self.entries[index]["date"] + "\tresearcher : " + self.entries[index]["researcher"] + "\tdata : " + str(self.entries[index]["data_points"]))
                index += 1
        else:
            print("\nAny entry does not input yet")
    
    
    def save_entries_to_file(self):
        
        if len(self.entries) != 0:
            with open(self.filename, "wb") as file:
                writer = avro.datafile.DataFileWriter(file, avro.io.DatumWriter(), self.schema)
                for entry in self.entries:
                    writer.append(entry)
                print("Entries saved successfully!")
                writer.close()
        else:
            print("\nNo any entries found to save")
    
    def load_entries_from_file(self):
        
        try:
            with open(self.filename,"rb") as file:
                reader = avro.datafile.DataFileReader(file, avro.io.DatumReader())
                self.entries = [entry for entry in reader]
                reader.close()
        except FileNotFoundError:
            return []

    def readable_avro(self):
        if len(self.entries) != 0:
            with open(self.filename, "rb") as file:
                reader = avro.datafile.DataFileReader(file, avro.io.DatumReader())
                for record in reader:
                    print("name : ", record["experiment_name"])
                    print("date : ", record["date"])
                    print("researcher : ", record["researcher"])
                    print("data points : ", record["data_points"])
                    print("\n\n")
                reader.close()
        else:
            print("\nNo any data to convert to readable mode")

    
    def analyze_data(self):
        while True:
        
            length = len(self.entries)
            
            if length != 0:
                while True:
                    exist_index = 0
                    name_found = False

                    name = input("\nEnter experiment name to analyze : ")

                    while exist_index < length:
                        
                        if self.entries[exist_index]["experiment_name"] == name:
                            name_found = True
                            data_found = exist_index
                            tot = 0.0
                            no_points = 0
                            
                            for points in self.entries[data_found]["data_points"]:
                                tot += points
                                no_points += 1
                                avg = tot / length
                            print("\nAverage : " + str(avg))
                            variance = 0.0
                            
                            for points in self.entries[data_found]["data_points"]:
                                
                                variance += (points - avg) ** 2 /  no_points
                                
                            standard_deviation = math.sqrt(variance)
                            print("\nStandard Deviation : " + str(standard_deviation))

                            median = statistics.median(self.entries[data_found]["data_points"])

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
                        if self.entries[exist_index]["experiment_name"] == name:
                            name_found = True
                            print("1. Name")
                            print("2. Researcher")
                            print("3. Data")
                
                            try:
                                update_option = int(input("\nInput category you want to update : "))

                                if update_option == 1:
                                    while True:
        
                                        length = len(self.entries)
        
                                        if length != 0:
                                            while True:
                                                avai_index = 0
                                                old_name_found = False
                                                new_name = input("\nEnter new experiment name : ")

                                             

                                                while avai_index < length:
                                                    if self.entries[avai_index]["experiment_name"] == new_name:
                                                        old_name_found = True
                                                        print("Name has been exist! Please enter a unique name")
                                                        break
                                                    else:
                                                        avai_index += 1
                                                    
        
                                                if old_name_found == False:
                                                    self.entries[exist_index]["experiment_name"] = new_name
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
                                                    self.entries[exist_index]["data_points"] = new_points_list
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
                        if self.entries[exist_index]["experiment_name"] == name:
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
        print("\nMenu:")
        print("1. Add a research data entry")
        print("2. View all entries")
        print("3. Analyze data")
        print("4. Save entries to file")
        print("5. Update a entry")
        print("6. Delete a entry")
        print("7. View entries in readable mode")
        print("8. Exit")
        
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
        elif choice == '6':
            manager.delete_entry()
        elif choice == '7':
            manager.readable_avro()
        elif choice == '8':
            break
        else:
            print("\nInvalid choice, please try again.")

if __name__ == "__main__":
    main()
