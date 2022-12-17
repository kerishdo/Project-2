class Facility:
    def __init__(self, Facility_name):
        self.Facility_name = Facility_name
        
#getters
    def get_Facility_name(self):
        return self.Facility_name

#setters
    def set_Facility_name(self, Facility_name):
        self.Facility_name = Facility_name

    global facilitylist
    facilitylist = []
#Methods


    def facility_menu(self):
        global facility_choice
        facility_choice = int(input("Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n\t"))

    def readFacilityfile(self):
        facilityfile = open("facilities.txt", "r")
        for line in facilityfile:
            line_strip = line.strip()
            line_split = line_strip.split()
            facilitylist.append(line_split)
        facilityfile.close()

    def displayFacilities(self):
        my_file = open("facilities.txt", "r")
        for each_line in my_file:
            print(each_line)

    def addFacility(self):
        facilityname = (input("Enter the name of the facility:\n\t"))
        new_Facility = open("facilities.txt", "a")
        new_Facility.write("\n")
        new_Facility.write(facilityname)
        new_Facility.close()
