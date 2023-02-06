# Cherry Picking List Creation 
CherryPick.py is a python script that automates the creation of cherry picking files. 
Currently this script is only designed for 384 -> tubes protocol. 

# Usage 
The script is deployed on Wooey, an application that uses Django to give a lightweight GUI to a python script. 

### Link to wooey
https://bds.cellsignal.com/wooey/
### **Look for CherryPicking.py on main page !**

# Script Params 
The script only takes two parameters, there is a file upload where the user will upload an xls file. Specifically the xls file that is exported
straight from JIRA containing all the different Cherry Picking entries. The next parameter is choosing a source plate variable (Dynamic for Plate Barcode & Static for static placeholder ex: plate_11) **The uploaded file must be the file from JIRA and must be an xls file.** 
### Note 
There are specific fields that are essential and are needed in the script even though they will not appear in the output list. The following required data fields that are a neccessity in the document are:
- Key (Actual JIRA Issue)
- Status 
- Fast Lane (PLM)
- Notes 
- Mab Pipeline Type
- Plasmid Number Heavy 
- Plasmid Number Light 
- Heavy Plasmid Well Location 
- Light Plasmid Well Location 
- Heavy Plasmid Volume 
- Light Plasmid Volume 
- Plate Barcode 


## High Level Overview 
The script will load the contents of the passed in file and using a designed class will create entry objects that will represent a single entry within the file and within that one object will contain each of the following fields defined above.
After compiling a list which contains all of the entries to be included into the csv output file the script takes those entries and moves them to another designed class which is responsible for the following:
- Sorting by pipeline
- Determining the number of unqiue barcodes within data 
- Determining the number of singular entries within the whole data file
- Dynamically map out the position of plates and divide up entries into multiple tests if neccesary 
- Dynamically map out the destination of each sample based on which test the sample is in and its position on the rack. 
- Take the mappings and translate into csv file for the robot (Currently Starlit) compatible. 
### Note: If more than 1 test/run is required multiple csv files will be outputted.

## Documentation
The following link will take you to the documentation of this script furter explaining the design structure and data structures used in this script. 
### Link:
https://cellsignal.atlassian.net/wiki/spaces/AUT/pages/3686072323/Cherry+Picking+List+Creation+Automation+Project


