import tkinter
from tkinter import ttk
import pandas as pd
import numpy as np    


#Template for data entry form
file=input("Enter name of data template file Eg. data_template.csv\n")
df = pd.read_csv(file)
data_category=list(df.columns)
column=int(input("Indicate the last column number for demographics\n"))
data_dictionary={}
for column_name in data_category:
    column_values=df[column_name].tolist()
    column_values = [x for x in column_values if str(x) != 'nan'] #remove nan values
    if len(column_values)>0:
        data_dictionary[column_name] = column_values

demographic_columns=data_category[:column]
study_data_columns=data_category[column:]

#Existing dataset/create new dataframe if no existing dataset
while True:
    existing_data=input("Are you adding data to an existing file? Enter Yes or No\n").lower().strip()
    if existing_data=="yes":
        new_df=pd.read_csv(input("Enter CSV filename\n"))
        if new_df.columns[0] != data_category[0]:
         new_df=new_df.iloc[:,1:]
        break
    elif existing_data=="no":
        new_df= pd.DataFrame(columns=data_category)
        break

#Create Tkinter window for data entry
window = tkinter.Tk()
window.title("Research Study Subject Data Entry Form")
frame = tkinter.Frame(window)
frame.pack()
Entries=[]

# Saving subject basic demographic data
row_number=0
column_number=0
id_number=0
demographic_frame =tkinter.LabelFrame(frame, text="Subject Demographics") #new section within frame
demographic_frame.grid(row= 0, column=0, sticky="news", padx=20, pady=10) #position of section
for column in demographic_columns:
    data=tkinter.Label(demographic_frame, text=column)
    data.grid(row=row_number, column=column_number)
    if column in data_dictionary:
        data_entry= ttk.Combobox(demographic_frame, values=data_dictionary[column])
    else:
        data_entry=tkinter.Entry(demographic_frame)
    data_entry.grid(row=row_number+1, column=column_number)
    Entries.append(data_entry.get())
    column_number+=1
    if column_number == 3:
        column_number=0
        row_number+=2

for widget in demographic_frame.winfo_children(): #Spacing between each category
    widget.grid_configure(padx=10, pady=5)

# Saving study data
data_frame =tkinter.LabelFrame(frame, text="Study Data") #new section within frame
data_frame.grid(row= 1, column=0, sticky="news", padx=20, pady=10) #position of section

for column in study_data_columns:
    data=tkinter.Label(data_frame, text=column)
    data.grid(row=row_number, column=column_number)
    if column in data_dictionary:
        data_entry= ttk.Combobox(data_frame, values=data_dictionary[column])
    else:
        data_entry=tkinter.Entry(data_frame)
    data_entry.grid(row=row_number+1, column=column_number)
    Entries.append(data_entry.get())
    column_number+=1
    if column_number == 3:
        column_number=0
        row_number+=2

for widget in data_frame.winfo_children(): #Spacing between each category
    widget.grid_configure(padx=10, pady=5)


def enter_data():
    global new_df
    subject_dictionary={}
    subject_data=[]
    def get_all_entry_widgets_text_content(parent_widget):
        children_widgets = parent_widget.winfo_children()
        for child_widget in children_widgets:
            if child_widget.winfo_class() == 'Entry' or child_widget.winfo_class() =='TCombobox':
                if child_widget.get() == "":
                    subject_data.append("")
                else:
                    subject_data.append(child_widget.get())
    get_all_entry_widgets_text_content(demographic_frame)
    get_all_entry_widgets_text_content(data_frame)
    for i in range(len(data_category)):
        subject_dictionary[data_category[i]]=[subject_data[i]]
    subject_df=pd.DataFrame(subject_dictionary)
    new_df=pd.concat([new_df,subject_df])


#Submit button to append new data
Submit = tkinter.Button(frame, text="Submit", command= enter_data)
Submit.grid(row=2, column=0, sticky="news", padx=20, pady=10)
window.mainloop()

#Save to csv file
new_df = new_df.reset_index(drop=True)
new_df.index = new_df.index+1
new_df.to_csv("Updated Study Data.csv")

