# 02-Clinical-Study-Data-Entry-Form
This project aims to create a data entry form for clinical studies using Tkinter and uses the data to create data visualisations. 

How does it work:
1) A data entry form that is split into 2 sections, demographics and study data, can be created using Tkinter when the user supplies a data template file that specifies the data entry fields for each section and the relevant options for each field. Note that all columns under demographic category should be in sequence in the data template file
![image](https://github.com/JiaRong00/02-Clinical-Study-Data-Entry-Form/assets/149306287/4fe92af9-518c-4576-b01d-5200f07440f0)
2) The user has to specify the column number of the last demographic field
3) The user may opt to add the data entries to an existing dataset. The user will have to supply the csv file containing the existing dataset which has the same data format as the data template
4) The user may add as many entries using the Tkinter window data entry form generated, until the window is closed
<img width="444" alt="image" src="https://github.com/JiaRong00/02-Clinical-Study-Data-Entry-Form/assets/149306287/c389c53d-bcd1-4d0b-8da0-b3e0574e952e">
6) The entried will be saved into a csv file

Files:
1) data_template.csv contains the sample data template
2) Clinical_data_form.py is the code file
