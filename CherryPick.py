## Cherry Picking list creation 
## Scope: Currently the cherry picking list is a manually done process, possibly using JIRA's API and other components 
## We can automate this processs entirely 

## Possible Structure: Each row in the cherry picking list reps a single entry 
## Class for each entry 
    # 1.) Plate Barcode 
    # 2.) Well number
    # 3.) Target Plate Barcode
    # 4.) Target Plate Position
    # 5.) Volume 

    ## Private Fields 
    ## Getters 
    ## Setters 
    ## Putting each entry all together 

## IMPORT STATEMENTS ## 

import csv ## Import for allowing csv file manipulation  
import time ## Import for time objects
import random ## Random - Mainly for testing 
import string ## Strings 
import datetime ## Accessing datetime objects
from datetime import date ## From datetime lib, accesses date objects
import argparse ## Allows for adding script arguments, will be useful for wooey
import sys ## For iterating through script arguments 
import pandas as pd
dataframe_1 = pd.read_excel('~/Downloads/testExcel.xls')
newDF = dataframe_1.fillna("EMPTY")
# print(newDF)
# print(newDF.loc[2])

## Counter tells how many rows there are in the file, we subtract 1 because the index starts at 0
size = newDF.__len__() - 1
## Create the headers list 
headers_list = newDF.loc[2].values.flatten().tolist()

## Appends all the entries 
testEntries = []
tmpList = []
for i in range(3, size):
    testEntries.append(newDF.loc[i])
    tmpList.append(list(newDF.loc[i].array))
    
## END OF SCRIPT IMPORTS ##


## Script Arguments, potentially a raw data file, or JIRA Task Arguments ?
## 1.) Define the 
#   parser = argparse.ArgumentParser()
# parser.add_argument("-file", "--fi", required=True)

# args = parser.parse_args()
# print(args.fi)



# print(sys.argv[1:])

## Tracks the time at the start of the program 
start_time = time.time()


#Each Row in the csv file contains 5 variables, these 5 variables will be linked as a CherryPickEntry object
class CherryPickEntry:
    def __init__(self, rawData):
        self.__Key = rawData[0] 
        self.__Status = rawData[1]
        self.__FastLane = rawData[2]
        self.__Notes = rawData[3] # Needed for comparison 
        self.__BatchKey = rawData[4]
        self.__MonoPNL = rawData[5]
        self.__CloneUID = rawData[6]
        self.__Cycle = rawData[7]
        self.__Host = rawData[8]
        self.__Iso = rawData[9]
        self.__MabPipe = rawData[10]
        self.__PlasmidNumHeavy = rawData[11]
        self.__PlasmidNumLight = rawData[12]
        self.__HeavyPlasmidWellLoc = rawData[13] # Needed 
        self.__LightPlasmidWellLoc = rawData[14] # Needed 
        self.__HeavyChainSeqFileName = rawData[15]
        self.__LightChainSeqFileName = rawData[16]
        self.__HeavyPlasmidFinalVol = rawData[17] # Needed 
        self.__LightPlasmidFinalVol = rawData[18] # Needed 
        self.__isBeingUsed = False 
    
    ## Getters 
    def getKey(self):
        return self.__Key

    def getStatus(self):
        return self.__Status
    
    def getFastLane(self):
        return self.__FastLane

    def getNotes(self):
        return self.__Notes
    
    def getBatchKey(self):
        return self.__BatchKey

    def getMonoPNL(self):
        return self.__MonoPNL

    def getCloneUID(self):
        return self.__CloneUID

    def getCycle(self):
        return self.__Cycle

    def getHost(self):
        return self.__Host

    def getIso(self):
        return self.__Iso

    def getMabPipe(self):
        return self.__MabPipe

    def getPlasmidNumHeavy(self):
        return self.__PlasmidNumHeavy

    def getPlasmidNumLight(self):
        return self.__PlasmidNumLight

    def getHeavyPlasmidWellLoc(self):
        return self.__HeavyPlasmidWellLoc

    def getLightPlasmidWellLoc(self):
        return self.__LightPlasmidWellLoc

    def getHeavyChainSeqFileName(self):
        return self.__HeavyChainSeqFileName

    def getLightChainSeqFileName(self):
        return self.__LightChainSeqFileName

    def getHeavyPlasmidFinalVol(self):
        return self.__HeavyPlasmidFinalVol

    def getLightPlasmidFinalVol(self):
        return self.__LightPlasmidFinalVol

    

    

## Method for making the actual csv file, contains the headers for the file along with creating a csv file, for now the file is created locally as we are using test data right now. 
## @params: 
    # EntriesList: The list containing all the Class Objects where each entry in the list is the entire row for a given set of data. 
def makeCSVFile(EntriesList):
    AllEntries = EntriesList
    ## The Headers of the Cherry Picking File 
    headers = ["SourceLabID" , "SourcePosID" , "TargetLabID" , "TargetPosID", 'Volume']
    ## Create a new csv File 
    csvFile = open('../Downloads/testFile' + str(date.today()) + '.csv', 'w')
    ## Create a file writer object
    fileWriter = csv.writer(csvFile, delimiter=',')
    ## Iterate over all our entries and write the file 
    fileWriter.writerow(headers)
    for elements in AllEntries:
        fileWriter.writerow(elements.mergeData())
    ## Close the File
    csvFile.close()

## END OF CHERRY PICKING CLASS ##

## Creating a list to hold all class objects 
EntriesList = []
for i in tmpList:
    EntriesList.append(CherryPickEntry(i))
for i in EntriesList:
    print(i.getKey())

## Function call to make the csv file. 
# makeCSVFile(AllEntries)

## Time right now 
end_time = time.time()

##Print out the process run time by subtracting the current time from the time started. 
print('\n+++++++++++++++++++++++++++++++++++++++++++++++++')
print("Process Runtime: " + str(round(end_time - start_time, 5))) ## How Long the Process took
print('+++++++++++++++++++++++++++++++++++++++++++++++++')

    