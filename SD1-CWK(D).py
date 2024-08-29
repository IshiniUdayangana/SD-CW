import tkinter as tk
from tkinter import ttk
import datetime
import datetime
import avro.schema
import avro.io
import avro.datafile
from tkinter import messagebox

class ResearchDataManager:
    def __init__(self):
        self.entries = []
        self.filename = "research_data.avro"
        self.schema = avro.schema.Parse(open("research_data_schema.avsc", "r").read())
    
    def add_entry(self, experiment_name, date, researcher, data_points):
        self.entries.append({"experiment_name" : experiment_name, "date" : date, "researcher" : researcher, "data_points" : data_points})
    
    def get_entries(self):
        return self.entries
    
    def save_entries_to_file(self):
        if self.entries:
            with open(self.filename, "wb") as file:
                writer = avro.datafile.DataFileWriter(file, avro.io.DatumWriter(), self.schema)
                
                for entry in self.entries:
                    writer.append(entry)
                writer.close()
                
            messagebox.showinfo("Success", "Entries saved successfully!")
            
        else:
            messagebox.showwarning("Warning", "No entries to save.")
    
    def load_entries(self):
        try:
            with open(self.filename, "rb") as file:
                reader = avro.datafile.DataFileReader(file, avro.io.DatumReader())
                self.entries = [entry for entry in reader]
                reader.close()
                
            messagebox.showinfo("Success", "Entries loaded successfully")
            
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")
            
        except Exception as e:
            messagebox.showerror("Error", "An error occured")

def add_entry(manager, tree):
    def save_entry():
        
       experiment_name = name_entry.get()
       
       researcher = researcher_entry.get()
       
       data_points = list(map(float, data_entry.get().split(",")))
       
       date = str(datetime.datetime.now().date())
       
       manager.add_entry(experiment_name, date, researcher, data_points)
       refresh_table(manager, tree)
       add_window.destroy()

    add_window = tk.Toplevel()
    add_window.title("Add Entry")
    
    tk.Label(add_window, text="Experiment Name").pack()
    name_entry = tk.Entry(add_window)
    name_entry.pack()

    tk.Label(add_window, text="Researcher").pack()
    researcher_entry=tk.Entry(add_window)
    researcher_entry.pack()
    
    tk.Label(add_window, text="Data points").pack()
    data_entry = tk.Entry(add_window)
    data_entry.pack()
    
    tk.Button(add_window, text="Save", command = save_entry).pack()
    

def refresh_table(manager, tree):
    for item in tree.get_children():
        tree.delete(item)
    for entry in manager.get_entries():
        tree.insert('', 'end', values=(entry["experiment_name"], entry["date"], entry["researcher"], entry["data_points"]))
    

def sort_by_column(tree, col, descending):
    data = [(tree.set(child, col), child) for child in tree.get_children('')]
    data.sort(reverse=descending)

    for index, item in enumerate(data):
        tree.move(item[1], '', index)
        
    tree.heading(col, command=lambda: sort_by_column(tree, col, not desending))

def main():
    manager = ResearchDataManager()
    
    root = tk.Tk()
    # add code as necessary

    root.title("Research Data Manager")

    

    tk.Label(root, text="Search:").pack(side="top", anchor="w", padx=10, pady=5)
    search_entry=tk.Entry(root)
    search_entry.pack(side="top", anchor = "w", fill = "x", padx = 10, pady = 5)
    
    columns = ("experiment_name", "date", "researcher", "data_points")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    
    for col in columns:
        tree.heading(col, text=col.replace("_", " ").title(), command=lambda c = col: sort_by_column(tree, c, False))
        tree.column(col, width=100)
    tree.pack(expand=True, fill="both")

    
    add_btn = tk.Button(root, text = "Add Entry", command=lambda: add_entry(manager, tree))
    add_btn.pack(side="left", padx=10, pady=10)

    refresh_btn = tk.Button(root, text = "Refresh Table", command=lambda: refresh_table(manager, tree))
    refresh_btn.pack(side="left", padx=10, pady=10)

    save_btn = tk.Button(root, text = "Save Entries", command=lambda: manager.save_entries_to_file())
    save_btn.pack(side="left", padx = 10, pady= 10)

    load_btn = tk.Button(root, text = "Load Entreis", command = lambda: [manager.load_entries(), refresh_table(manager, tree)])
    load_btn.pack(side="left", padx=10, pady = 10)

    search_entry.bind("<KeyRelease>", lambda event: refresh_table(manager, tree, search_entry.get()))
    
    
    root.mainloop()

if __name__ == "__main__":
    main()

#if you are paid to do this coursework please do not remove this line 
