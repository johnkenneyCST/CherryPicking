## Cherry Picking list creation 
import math ## Math Lib 
import csv ## Import for allowing csv file manipulation  
import time ## Import for time objects
import random ## Random - Mainly for testing 
import string ## Strings 
import datetime ## Accessing datetime objects
from datetime import date ## From datetime lib, accesses date objects
import argparse ## Allows for adding script arguments, will be useful for wooey
import sys ## For iterating through script arguments 
import pandas as pd


## Debug Function print the process runtime
def processRuntime(startTime):
    ## Time right now 
    end_time = time.time()
    ##Print out the process run time by subtracting the current time from the time started. 
    print('\n+++++++++++++++++++++++++++++++++++++++++++++++++')
    print("Process Runtime: " + str(round(end_time - startTime, 5))) ## How Long the Process took
    print('+++++++++++++++++++++++++++++++++++++++++++++++++')


## Tracks the time at the start of the program 
start_time = time.time()


#Each Row in the csv file contains 5 variables, these 5 variables will be linked as a CherryPickEntry object
class CherryPickEntry:
    def __init__(self, rawData):
        self.__Key = rawData[0] 
        self.__Notes = rawData[1] 
        self.__MabPipe = rawData[2]
        self.__PlasmidNumHeavy = rawData[3]
        self.__PlasmidNumLight = rawData[4]
        self.__HeavyPlasmidWellLoc = rawData[5] 
        self.__LightPlasmidWellLoc = rawData[6] 
        self.__HeavyPlasmidFinalVol = rawData[7] 
        self.__LightPlasmidFinalVol = rawData[8] 
        self.__PlateBarcode = rawData[9]
        self.__TempPlateVal = None
        
        ## Location, specific location on rack (1 , 2, 3, 4, etc) | LocationID, the rack (Rack_1, Rack_2)
        self.__HeavyTargetLocation = "None"
        self.__HeavyTargetLocationID = "None"
        self.__LightTargetLocation = "None"
        self.__LightTargetLocationID = "None"

        ## If repeat XXXX is found within notes will discregard the other 
        self.__IncludeHeavy = True
        self.__IncludeLight = True
        ## Headers list to be at the top of the csv file. 
        self.determineUse()
    


    ## This function determines based on the notes whether or not to be included in the test
    ## The formula for deciding this is if repeat xxxx is in the notes, we disregard the accompanying plasmid entry. 
    def determineUse(self):
        if "repeat" in self.__Notes.lower():
            tmpList = self.__Notes.split('t')
            entryToTrash = tmpList[-1]
            if int(entryToTrash) == int(self.__PlasmidNumHeavy):
                self.__IncludeLight = False
            elif int(entryToTrash) == int(self.__PlasmidNumLight):
                self.__IncludeHeavy = False

    ## Getters 

    def getNumEntries(self):
        if self.__IncludeHeavy == True and self.__IncludeLight == True:
            return 2
        else:
            return 1

    def getKey(self):
        return self.__Key

    def getNotes(self):
        return self.__Notes

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

    def getHeavyPlasmidFinalVol(self):
        return self.__HeavyPlasmidFinalVol

    def getLightPlasmidFinalVol(self):
        return self.__LightPlasmidFinalVol

    def getHeavyTargetLocation(self):
        return self.__HeavyTargetLocation

    def getHeavyTargetLocationID(self):
        return self.__HeavyTargetLocationID

    def getLightTargetLocation(self):
        return self.__LightTargetLocation

    def getLightTargetLocationID(self):
        return self.__LightTargetLocationID

    def getIncludeHeavy(self):
        return self.__IncludeHeavy

    def getIncludeLight(self):
        return self.__IncludeLight

    def getPlateBarcode(self):
        return self.__PlateBarcode

    def getMetaData(self, type):

       if type.lower() == "light":
            if args.PlateMapping == "Dynamic":
                tmp = [
                    self.getPlateBarcode(), 
                    self.getLightPlasmidWellLoc(), 
                    "test_eppen_0" + str(self.getLightTargetLocationID()), 
                    str(self.getLightTargetLocation()), 
                    str(self.getLightPlasmidFinalVol())
                ]
            elif args.PlateMapping == "Static":
                tmp = [
                    str(self.__TempPlateVal), 
                    self.getLightPlasmidWellLoc(), 
                    "test_eppen_0" + str(self.getLightTargetLocationID()), 
                    str(self.getLightTargetLocation()), 
                    str(self.getLightPlasmidFinalVol())
                ]
       elif type.lower() == "heavy":
            if args.PlateMapping == "Dynamic":
                tmp = [
                    self.getPlateBarcode(), 
                    self.getHeavyPlasmidWellLoc(),
                    "test_eppen_0" + str(self.getHeavyTargetLocationID()),
                    str(self.getHeavyTargetLocation()),
                    str(self.getHeavyPlasmidFinalVol())
                ]
            elif args.PlateMapping == "Static":
                tmp = [
                    str(self.__TempPlateVal), 
                    self.getHeavyPlasmidWellLoc(),
                    "test_eppen_0" + str(self.getHeavyTargetLocationID()),
                    str(self.getHeavyTargetLocation()),
                    str(self.getHeavyPlasmidFinalVol())
                ]
       return tmp or sys.exit("ERROR WITH GETTING META DATA")

    ## This gets all the relevant data for the csv file
    def getCSVFileData(self, delimeter):
        if delimeter.lower() == "light":
            self.__light
        elif delimeter.lower() == "heavy":
            pass


    ## Setters
    def setHeavyTargetLocation(self, location, maxEntriesPerRow):
        if location == 0:
            self.__HeavyTargetLocation = maxEntriesPerRow
        else:
            self.__HeavyTargetLocation = location 

    def setHeavyTargetLocationID(self, ID, maxEntriesPerRow):
        self.__HeavyTargetLocationID = int(math.ceil(ID / maxEntriesPerRow)) 

    def setLightTargetLocation(self, location, maxEntriesPerRow):
        if location == 0: ##Passing in % based off the max entries per row 
            self.__LightTargetLocation = maxEntriesPerRow
        else:
            self.__LightTargetLocation = location

    def setLightTargetLocationID(self, ID, maxEntriesPerRow):
        self.__LightTargetLocationID = int(math.ceil(ID / maxEntriesPerRow))

    def setTempPlateVal(self, val):
        self.__TempPlateVal = "plate_" + str(val)

## Class for making the actual file, ability to access the cherry pick entry list
class CreateCherryPickList:
    def __init__(self, sortedData):
        self.__sortedData = sortedData
        ## When using 384 -> tubes protocol, a max of 32 tubes per row on the deck 
        self.__maxEntriesPerRow = 32
        ## Can only fit 10 racks on the deck for one test
        self.__maxPlatesPerTest = 10
        
        # Sorting the entries by their Pipeline 
        self.__XMT = []
        self.__SCPD = []
        self.__HeadersList = ["SourceLabID" , "SourcePosID" , "TargetLabID" , "TargetPosID", 'Volume']
        
        self.__NumEntries = self.findTotalEntries()
        self.sortByPipeline()
        self.findTotalUniquePlates()
        self.dynamicPlateMapping()
        self.determineDestination()
        self.createCSVFile()

    ## Getters
    def getSortedData(self):
        return self.__sortedData()
    
    def getNumEntries(self):
        return self.__NumEntries


    ## While still maintaing the entire data list we divide into 2 seperate groups based off of pipeline 
    def sortByPipeline(self):
        for entry in self.__sortedData:
            if entry.getMabPipe() == "XMT":
                self.__XMT.append(entry) 
            elif entry.getMabPipe() == "SCPD":
                self.__SCPD.append(entry)

    ## Goes through and calculates the actual amount of entries will be included in the list
    def findTotalEntries(self):
        NumEntries = 0
        for i in self.__sortedData:
            NumEntries += i.getNumEntries()
        return NumEntries

    ## Determines the total number of unique plates used in the test
    def findTotalUniquePlates(self):
        self.__TotalUniquePlates = 0
        self.__UniqueBarcodeList = []
        for i in self.__sortedData:
            if i.getPlateBarcode() not in  self.__UniqueBarcodeList:
                self.__UniqueBarcodeList.append(i.getPlateBarcode())
                self.__TotalUniquePlates += 1
            else:
                continue 

        # print("\nTotal Entries: " + str(self.__NumEntries))
        # print("\nUnique Plates: " + str(self.__TotalUniquePlates))

        
    

    ## Dynamically determines the plates being used 
    def dynamicPlateMapping(self):
        self.__EntriesByBarcode = {}

        for barcode in self.__UniqueBarcodeList:
            self.__EntriesByBarcode[barcode] = {}
            entries = 1
            for i in self.__sortedData:
                if i.getPlateBarcode() == barcode:
                    self.__EntriesByBarcode[barcode][entries] = i
                    entries += 1
                    

        self.__TestPrepDict = {}

        ## Determines the number of seperate tests needed, calculated by dividing the number of plates being found within the file by the maximum number of plates you can have per test (Currently 10 on starlit), then rounding UP to nearest whole number
        self.__TestNeeded = int(math.ceil(self.__TotalUniquePlates / self.__maxPlatesPerTest))
        # print("Tests needed: " + str(self.__TestNeeded))
        
        ## Creates the number of test dictionaries 
        for i in range(self.__TestNeeded):
            self.__TestPrepDict["Test_" + str(i + 1)] = {}
        
        ## Sorts barcodes from least to greatest and adds the max number of barcodes to a specific test (Currently 10 per test)
        for count, UniqueBarcode in enumerate(sorted(self.__UniqueBarcodeList)):
            for k, v in self.__TestPrepDict.items():
                if len(v) < 10 and UniqueBarcode not in v:
                    v[UniqueBarcode] = []
                    break
                else:
                    continue
        
        ## This loop links specific entries in with their barcodes 
        for entry in self.__sortedData:
            for test, barcode_dict in self.__TestPrepDict.items():
                for barcode, value in barcode_dict.items():
                    if entry.getPlateBarcode() == barcode:
                        barcode_dict[barcode].append(entry)
                
        ## Goes through and calculates the number of total entries for each test
        for testKey, testDict in self.__TestPrepDict.items():
            staticPlateVal = 1
            self.__TestPrepDict[testKey]["TotalEntries"] = 0
            self.__TestPrepDict[testKey]["RowsOfTubesNeeded"] = 0
            for barcodeKeys, barcodeList in testDict.items():
                if type(barcodeList) == list:
                    for individualEntry in barcodeList:
                        self.__TestPrepDict[testKey]["TotalEntries"] += individualEntry.getNumEntries()
                        individualEntry.setTempPlateVal(staticPlateVal + 10)
                    staticPlateVal += 1
            
            ## Determines the number of rows of tubes needed for a specific test
            self.__TestPrepDict[testKey]["RowsOfTubesNeeded"] = int(math.ceil(self.__TestPrepDict[testKey]["TotalEntries"] / 32))

        



    ## Maps out the rack and specific location on the rack for each sample's destination 
    def determineDestination(self):
        ## Using the TestPrepDict we will go test by test and map sources to locations 
        currentRowLocation = 1
        self.__maxEntriesPerRow = 32
        self.__RowsRequired = int(math.ceil(self.__NumEntries / 32))

        for testNum, testNumDict in self.__TestPrepDict.items():
            for barcodeKey, barcodeList in sorted(testNumDict.items()):
                if type(barcodeList) == list:
                    for individualEntry in barcodeList:
                        if individualEntry.getIncludeHeavy():
                            individualEntry.setHeavyTargetLocation(currentRowLocation % 32,32)
                            individualEntry.setHeavyTargetLocationID(currentRowLocation, self.__maxEntriesPerRow)
                            currentRowLocation += 1
                            
                        if individualEntry.getIncludeLight():
                            individualEntry.setLightTargetLocation(currentRowLocation % 32, 32)
                            individualEntry.setLightTargetLocationID(currentRowLocation, self.__maxEntriesPerRow)
                            currentRowLocation += 1
        # print("Current Row: " + str(currentRowLocation))
        # print("Total Entries: " + str(self.__NumEntries))

        
        # DEBUG
        # for k, v in self.__TestPrepDict.items():
        #     print(k)
        #     for kk, vv in v.items():
        #         if type(vv) == list:
        #             for i in vv:
        #                 if i.getHeavyTargetLocation() != "None":
        #                     print("\t Rack:" + str(i.getHeavyTargetLocationID()) + " - " + str(i.getHeavyTargetLocation()))
        #                 if i.getLightTargetLocation() != "None": 
        #                     print("\t Rack:" + str(i.getLightTargetLocationID()) + " - " + str(i.getLightTargetLocation()))
        

    ## This will dynamically determine based on how many tests there are to be run how many csv files are needed
    def createCSVFile(self):
        TestList = []
        for i in range(self.__TestNeeded):
            tmpFileName = "CherryPickFile_" + "Test_" + str(i + 1) + "-" + str(date.today())
            csvFile = open(tmpFileName + '.csv', 'w+')
            TestList.append(csvFile)
        for count, element in enumerate(TestList):
            currentTest = count + 1
            fileWriter = csv.writer(element, delimiter=',')
            fileWriter.writerow(self.__HeadersList)
            for k, v in self.__TestPrepDict.items():
                if str(currentTest) in k:
                    ## k = Test Number print(k)
                    for kk, vv in v.items():
                        if type(vv) == list:
                            for items in vv:
                                if items.getIncludeHeavy() == True:
                                    # print(items.getMetaData("heavy"))
                                    fileWriter.writerow(items.getMetaData("heavy"))
                                if items.getIncludeLight() == True:
                                    # print(items.getMetaData("light"))
                                    fileWriter.writerow(items.getMetaData("light"))
            # fileWriter = csv.writer(csvFile, delimiter=',')
            # fileWriter.writerow(self.__HeadersList)


        


        

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
        fileWriter.writerow(elements.mergeData(), format("left-align"))
    ## Close the File
    csvFile.close()



## MAIN METHOD ##
def main():
    print("\n+++++++++++++++++++++++++++++++\n\tProcess Start\n+++++++++++++++++++++++++++++++\n")
    print("\nReading Raw Data File...\n")
    try: 
        dataframe_1 = pd.read_html(args.file.name)
    except Exception as error:
        sys.exit(error)
    else:
        newDF = dataframe_1[1]
        for i in newDF.columns:
            newDF.rename(columns={i : i.replace(" ", "").lower()}, inplace=True,)
        print("\nReconfiguring Columns...\n")
        EntriesList = []
        for i in range(len(newDF)):
            tmpList = [
                str(newDF["key"][i]), 
               str(newDF['notes'][i]),
                str(newDF['mabpipelinetype'][i]), 
                str(newDF['plasmidnumberheavy'][i]),
                str(newDF['plasmidnumberlight'][i]),
                str(newDF["heavyplasmidwelllocation"][i]),
                str(newDF['lightplasmidwelllocation'][i]), 
                str(newDF['heavyplasmidfinalvolume(μl)'][i]),
                str(newDF['lightplasmidfinalvolume(μl)'][i]),
                str(newDF['platebarcode'][i])
            ]
            EntriesList.append(CherryPickEntry(tmpList))
        print("\nInstantiating Cherry Pick Entries...\n")
        
        # barcodeCount = []
        # for i in EntriesList:
        #     print(i.getPlateBarcode())
        #     if i.getPlateBarcode() not in barcodeCount:
        #         barcodeCount.append(i.getPlateBarcode())
        
        print("\nCollected Data...Initializing Cherry Picking File...\n")
        ## Instantiate Cherry Pick List Class -> Being passed in all individual cherry pick entries 
        CreateCherryPickList(EntriesList)

            
    
    
    
    
    

    ## Appends all the entries 
    # testEntries = []
    # tmpList = []
    # for i in range(3, size):
    #     testEntries.append(newDF.loc[i])
    #     tmpList.append(list(newDF.loc[i].array))

    # EntriesList = []
    # for i in tmpList:
    #     EntriesList.append(CherryPickEntry(i))
    # CreateCherryPickList(EntriesList)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog="CherryPick.py", 
                    description="This Script automates the cherry picking list creation process")
    parser.add_argument('--file', type=argparse.FileType('r'), required=True,help="The xls file exported from JIRA containing the Raw Data of all the grouped issues. This file will be converted into a new csv file to be inserted into the hamilton." )
    parser.add_argument('--Plate_Mapping', type=str, required=True, help="Whether the sources in the csv file will be the plate barcodes (Dynamic) or the static hard coded values such as 'plate_11' (Static).", choices=["Dynamic", "Static"], default="Dynamic")
    args = parser.parse_args()

    ## MAIN METHOD CALL ##
    main()
    sys.exit(processRuntime(start_time))

    
