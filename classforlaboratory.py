#CPRG-16
##Student name: Kerish Do
#Student ID: 000885324

def printMenu(): 
    # menu 
    print('\n Laboratories Menu:\n')
    print('1 - Display laboratories list')
    print('2 - Add laboratory')
    print('3 - Back to the Main Menu')
    
###
def writeListOfLabsToFile(): 
    contentfile = ['Facility_Cost', 'Facility1_800', 'Facility2_1200', 'Facility3_500', 'Facility4_50']
    createFile = open('laboratories.txt', 'w+')
    for item in contentfile:
        createFile.write(item + '\n')

class laboratory:
    
    def __init__ (self,labname,costlab, labinfo): 
        self.labname = labname
        self.costlab = costlab
        self.labinfo = labinfo

    def readLaboratoriesFile(): 
        labList = open('laboratories.txt', 'r')
        dataList = labList.read()
        dataList = dataList.replace('Facility', 'Lab')
        dataList = dataList.replace('_','\t')
        return dataList

    def displayLabsList(): # Display the lab list
        list = laboratory.readLaboratoriesFile()
        print('\n')
        print(list)
    
    def enterLaboratoryInfo(): #input labname and cost
        labname = input('\nEnter Laboratory Name: ')
        cost = int(input('\nEnter Laboratory cost: '))
        labinfo = str(labname)+'_'+str(cost)
        return labinfo

    def formatLabInfo(): 
        ## format 
        formatLabInfo = laboratory.enterLaboratoryInfo()
        outputLabInfo = formatLabInfo.replace("Lab", "Facility")
        return outputLabInfo

    def addLabToFile(): 
        file_object = open('laboratories.txt', "a+")
        file_object.seek(0)
        file_object.write(laboratory.formatLabInfo())
        file_object.write("\n")

writeListOfLabsToFile() 
while(True):
    printMenu()
    labchoice = int(input('\nPlease select your options:\n'))
    if labchoice == 1:
        laboratory.displayLabsList()
    elif labchoice == 2:
        laboratory.addLabToFile()
    elif labchoice == 3:
        loop = 0
    else:
        print('\nInvalid option. Please enter a number between 1 and 3.')
        