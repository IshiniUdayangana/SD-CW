import os

# Function to add a research data entry
def add_entry(entries):
    name = input("Enter experiment name : ")
    #while True:
    date = input("Enter date : ")
    researcher = input("Enter the researcher's name : ")
    while True:
        try:
            data = float(input("Input data points : "))
            while True:
                points = input("Do you wish to add more points(Y/N) : ")
                if (points.lower() == "n"):
                    print("rbhbhb")
                    break
                elif (points == "y"):
                    continue
                else:
                    print("Please input \"y\" or \"N\"")
        except ValueError:
            print("Please input numeric values as masurements")
        else:
            break
    another_entry = print("Do you want to add another entry(Y/N) : ")
    #if another_entry.lower() == "yes":
      #  add_entry(entries)
    

# Function to view all research data entries
def view_entries(entries):
    pass

# Function to save entries to a text file
def save_entries_to_file(entries, filename):
    pass

# Function to load entries from a text file
def load_entries_from_file(filename):
    pass

# Function to perform data analysis
def analyze_data(entries):
    pass

# Main function to interact with the user
def main():
    filename = "research_data.txt"
    entries = load_entries_from_file(filename)
    
    while True:
        print("\nMenu:")
        print("1. Add a research data entry")
        print("2. View all entries")
        print("3. Analyze data")
        print("4. Save entries to file")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_entry(entries)
        elif choice == '2':
            view_entries(entries)
        elif choice == '3':
            analyze_data(entries)
        elif choice == '4':
            save_entries_to_file(entries, filename)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
