# Cheyne Stanley Randau Burberry
# TP059946

def registerpatient():
    records = []
    for i in range(2):
        item = []
        idNum = input('Enter ID number: ')
        item.append(idNum)
        firstName = input('Enter first name: ')
        item.append(firstName)
        zone = input('Enter zone: ')
        item.append(zone)
        groupNum = input('Enter group: ')
        item.append(groupNum)
        phoneNum = input('Enter phone number: ')
        item.append(phoneNum)
        emailAdd = input('Enter email address: ')
        item.append(emailAdd)
        records.append(item)

    return records


def savePatientdetails():
    try:
        fileHandler = open('patient_file.txt','a')
    except:
        print ('Unable to locate the file:')
        exit()

    records = registerpatient()

    for item in records:
        for fs in item:
            fileHandler.write(fs)
            fileHandler.write('\t')
        fileHandler.write('\n')
    fileHandler.close()

        
def printPatientdetails():
    try:
        fileHandler = open('patient_file.txt','r')
    except:
        print ('Unable to locate the file:')
        exit()

    for line in fileHandler:
        print(line)
        
    fileHandler.close()
    
        
def searchPatientdetails():
    try:
        fileHandler = open('patient_file.txt','r')
    except:
        print ('Unable to locate the file:')
        exit()

    search_key = input('Please type in ID number: ')
    
    for line in fileHandler:
        line = line.rstrip()
        if not search_key.lower() in line.lower(): 
            continue
        print(line)
        
    fileHandler.close()

def printTestresults():
    #display menu for tests results and action taken
    print("************COVID-19 MANAGEMENT**********")
    print("************TEST MENU**************")
    print('please select your desired option:')
    print('1. Carry out TEST 1')
    print('2. Carry out TEST 2')
    print('3. Carry out TEST 3')
    print('4. Exit')
    print()
    choice = int(input('Enter selection: '))

    if choice==1:
        test_1()
    elif choice==2:
        test_2()
    elif choice==3:
        test_3()
    elif choice==4:
        print('Thank you for using COVID-19 Management')
    else:
        print('Please enter 1-6')


def test_1():
    print("************COVID-19 MANAGEMENT**********")
    print("************TEST MENU**************")
    print('please select TEST according to Groupings:')
    print('ATO-T1 [1]')
    print('ACC T1 [2]')
    print('AEO-T1 [3]')
    print('SID-T1 [4]')
    print('AHS-T1 [5]')
    print('6.   Exit')
    print()
    choice = int(input('Enter selection: '))

    if choice==1:
        print('If positive: QHNF')
        print('If Negative - QDFR (T2 will be carried out)')
        
        print("Enter new case id(according to first ID)(00X = 000X):  ")
        id=input()
        print("Enter Test Result positive/negative:  ")
        test=input()
        print("Enter Action needed to be taken(QHNF/QDFR):  ")
        action=input()
        with open('testfile.txt','a') as testfile:
                testfile.write(id)
                testfile.write("\n")
                testfile.write(test)
                testfile.write("\n")
                testfile.write(action)
                testfile.write("\n\n")
                testfile.close()
                
        with open('patient_file.txt','a') as patient_file:
                patient_file.write(id)
                patient_file.write("\n")
                patient_file.write(test)
                patient_file.write("\n")
                patient_file.write(action)
                patient_file.write("\n\n")
                patient_file.close()
                print("Record has been written to file arcording to first ID ")
            
    
   
   
    if choice==2:
        print("If positive: QHNF ")
        print('If Negative - QDFR (T2 will be carried out)')
     
        print("Enter new case id(according to first ID)(00X = 000X):  ")
        id=input()
        print("Enter Test Result positive/negative:  ")
        test=input()
        print("Enter Action needed to be taken(QHNF/QDFR):  ")
        action=input()
        with open('testfile.txt','a') as testfile:
                testfile.write(id)
                testfile.write("\n")
                testfile.write(test)
                testfile.write("\n")
                testfile.write(action)
                testfile.write("\n\n")
                testfile.close()
                
        with open('patient_file.txt','a') as patient_file:
                patient_file.write(id)
                patient_file.write("\n")
                patient_file.write(test)
                patient_file.write("\n")
                patient_file.write(action)
                patient_file.write("\n\n")
                patient_file.close()
                print("Record has been written to file arcording to first ID ")
   
    
   
    if choice==3:
        print("if positive: QHNF ")
        print('If Negative - QDFR (T2 will be carried out)')
        
        print("Enter new case id(according to first ID)(00X = 000X):  ")
        id=input()
        print("Enter Test Result positive/negative:  ")
        test=input()
        print("Enter Action needed to be taken(QHNF/QDFR):  ")
        action=input()
        with open('testfile.txt','a') as testfile:
                testfile.write(id)
                testfile.write("\n")
                testfile.write(test)
                testfile.write("\n")
                testfile.write(action)
                testfile.write("\n\n")
                testfile.close()
                
        with open('patient_file.txt','a') as patient_file:
                patient_file.write(id)
                patient_file.write("\n")
                patient_file.write(test)
                patient_file.write("\n")
                patient_file.write(action)
                patient_file.write("\n\n")
                patient_file.close()
                print("Record has been written to file arcording to first ID ")
    
    
   
    if choice==4:
        print('If positive: QHNF')
        print('If Negative - HQFR (proceed to carry out 2nd test)')

        print("----proceed to test 2----")
        print("----In the test main menu----")
        
        print("Enter new case id(according to first ID)(00X = 000X):  ")
        id=input()
        print("Enter Test Result positive/negative:  ")
        test=input()
        print("Enter Action needed to be taken(QHNF/QDFR):  ")
        action=input()
        with open('testfile.txt','a') as testfile:
                testfile.write(id)
                testfile.write("\n")
                testfile.write(test)
                testfile.write("\n")
                testfile.write(action)
                testfile.write("\n\n")
                testfile.close()
                
        with open('patient_file.txt','a') as patient_file:
                patient_file.write(id)
                patient_file.write("\n")
                patient_file.write(test)
                patient_file.write("\n")
                patient_file.write(action)
                patient_file.write("\n\n")
                patient_file.close()
                print("Record has been written to file arcording to first ID ")

    
   
   
    if choice==5:   
        print('If positive: QHNF')
        print('If Negative - CWFR (T2 will be carried out)')

        print("Enter new case id(according to first ID)(00X = 000X):  ")
        id=input()
        print("Enter Test Result positive/negative:  ")
        test=input()
        print("Enter Action needed to be taken(QHNF/CWFR):  ")
        action=input()
        with open('testfile.txt','a') as testfile:
                testfile.write(id)
                testfile.write("\n")
                testfile.write(test)
                testfile.write("\n")
                testfile.write(action)
                testfile.write("\n\n")
                testfile.close()
                
        with open('patient_file.txt','a') as patient_file:
                patient_file.write(id)
                patient_file.write("\n")
                patient_file.write(test)
                patient_file.write("\n")
                patient_file.write(action)
                patient_file.write("\n\n")
                patient_file.close()
                print("Record has been written to file arcording to first ID ")
    
    
    if choice==6:
        print('thank you for using covid 19 management system')
    
    return menu()    
    
    
    
    
def test_2():
    #display menu for test results and action taken for selection 2 (carry out TEST 2)  
    print("************COVID-19 MANAGEMENT**********")
    print("************TEST 2 MENU**************")
    print('please select TEST according to Groupings:')
    print('ATO-T1 [1]')
    print('ACC T1 [2]')
    print('AEO-T1 [3]')
    print('SID-T1 [4]')
    print('AHS-T1 [5]')
    print('6.   Exit')
    print()
    choice = int(input('Enter selection: '))

    if choice==1:
        print('If positive: QHNF')
        print('If Negative - QDFR (T3 will be carried out)')
        
        print("Enter previous case ID (followed by T2)(00X = 000X T2):  ")
        id=input()
        print("Enter Test Result positive/negative:  ")
        test=input()
        print("Enter Action needed to be taken(QHNF/QDFR):  ")
        action=input()
        with open('testfile2.txt','a') as testfile2:
                testfile2.write(id)
                testfile2.write("\n")
                testfile2.write(test)
                testfile2.write("\n")
                testfile2.write(action)
                testfile2.write("\n\n")
                testfile2.close()
                
        with open('patient_file.txt','a') as patient_file:
                patient_file.write(id)
                patient_file.write("\n")
                patient_file.write(test)
                patient_file.write("\n")
                patient_file.write(action)
                patient_file.write("\n\n")
                patient_file.close()
                print("Record has been written to file arcording to first ID ")

    
    if choice==2:
        print("If positive: QHNF ")
        print('If Negative - QDFR (T3 will be carried out)')
     
        print("Enter previous case ID (followed by T2)(00X = 000X T2):  ")
        id=input()
        print("Enter Test Result positive/negative:  ")
        test=input()
        print("Enter Action needed to be taken(QHNF/QDFR):  ")
        action=input()
        with open('testfile2.txt','a') as testfile2:
                testfile2.write(id)
                testfile2.write("\n")
                testfile2.write(test)
                testfile2.write("\n")
                testfile2.write(action)
                testfile2.write("\n\n")
                testfile2.close()
                
        with open('patient_file.txt','a') as patient_file:
                patient_file.write(id)
                patient_file.write("\n")
                patient_file.write(test)
                patient_file.write("\n")
                patient_file.write(action)
                patient_file.write("\n\n")
                patient_file.close()
                print("Record has been written to file arcording to first ID ")
   
    if choice==3:
        print("if positive: QHNF ")
        print('If Negative - QDFR (T3 will be carried out)')
        
        print("Enter previous case ID (followed by T2)(00X = 000X T2):  ")
        id=input()
        print("Enter Test Result positive/negative:  ")
        test=input()
        print("Enter Action needed to be taken(QHNF/QDFR):  ")
        action=input()
        with open('testfile2.txt','a') as testfile2:
                testfile2.write(id)
                testfile2.write("\n")
                testfile2.write(test)
                testfile2.write("\n")
                testfile2.write(action)
                testfile2.write("\n\n")
                testfile2.close()
                
        with open('patient_file.txt','a') as patient_file:
                patient_file.write(id)
                patient_file.write("\n")
                patient_file.write(test)
                patient_file.write("\n")
                patient_file.write(action)
                patient_file.write("\n\n")
                patient_file.close()
                print("Record has been written to file arcording to first ID ")

    if choice==4:
        print('If positive: QHNF')
        print('If Negative - HQFR (proceed to carry out 3rd test)')

        print("----proceed to test 3----")
        print("----In the test main menu----")
        
        print("Enter previous case ID (followed by T2)(00X = 000X T2):  ")
        id=input()
        print("Enter Test Result positive/negative:  ")
        test=input()
        print("Enter Action needed to be taken(QHNF/QDFR):  ")
        action=input()
        with open('testfile2.txt','a') as testfile2:
                testfile2.write(id)
                testfile2.write("\n")
                testfile2.write(test)
                testfile2.write("\n")
                testfile2.write(action)
                testfile2.write("\n\n")
                testfile2.close()
                
        with open('patient_file.txt','a') as patient_file:
                patient_file.write(id)
                patient_file.write("\n")
                patient_file.write(test)
                patient_file.write("\n")
                patient_file.write(action)
                patient_file.write("\n\n")
                patient_file.close()
                print("Record has been written to file arcording to first ID ")

    
    if choice==5:  
        print('If positive: QHNF')
        print('If Negative - CWFR (T3 will be carried out)')

        print("Enter previous case ID (followed by T2)(00X = 000X T2):  ")
        id=input()
        print("Enter Test Result positive/negative:  ")
        test=input()
        print("Enter Action needed to be taken(QHNF/CWFR):  ")
        action=input()
        with open('testfile.txt2','a') as testfile2:
                testfile2.write(id)
                testfile2.write("\n")
                testfile2.write(test)
                testfile2.write("\n")
                testfile2.write(action)
                testfile2.write("\n\n")
                testfile2.close()
                
        with open('patient_file.txt','a') as patient_file:
                patient_file.write(id)
                patient_file.write("\n")
                patient_file.write(test)
                patient_file.write("\n")
                patient_file.write(action)
                patient_file.write("\n\n")
                patient_file.close()
                print("Record has been written to file arcording to first ID ")

    if choice==6:
         print('thank you for using covid 19 management system')
    
    return menu()


def test_3():
    #display menu for test results and action taken for selection 3 (carry out TEST 3)
    print("************COVID-19 MANAGEMENT**********")
    print("************TEST 3 MENU**************")
    print('please select TEST according to Groupings:')
    print('ATO-T1 [1]')
    print('ACC T1 [2]')
    print('AEO-T1 [3]')
    print('SID-T1 [4]')
    print('AHS-T1 [5]')
    print('6.   Exit')
    print()
    choice = int(input('Enter selection: '))

    if choice==1:
        print('If positive: QHNF')
        print('If Negative - RU')
        
        print("Enter previous case ID (followed by T3)(00X = 000X T3):  ")
        id=input()
        print("Enter Test Result positive/negative:  ")
        test=input()
        print("Enter Action needed to be taken(QHNF/RU):  ")
        action=input()
        with open('testfile3.txt','a') as testfile3:
                testfile3.write(id)
                testfile3.write("\n")
                testfile3.write(test)
                testfile3.write("\n")
                testfile3.write(action)
                testfile3.write("\n\n")
                testfile3.close()
                
        with open('patient_file.txt','a') as patient_file:
                patient_file.write(id)
                patient_file.write("\n")
                patient_file.write(test)
                patient_file.write("\n")
                patient_file.write(action)
                patient_file.write("\n\n")
                patient_file.close()
                print("Record has been written to file arcording to first ID ")

    if choice==2:
        print("If positive: QHNF ")
        print('If Negative - RU')
     
        print("Enter previous case ID (followed by T3)(00X = 000X T3):  ")
        id=input()
        print("Enter Test Result positive/negative:  ")
        test=input()
        print("Enter Action needed to be taken(QHNF/RU):  ")
        action=input()
        with open('testfile3.txt','a') as testfile3:
                testfile3.write(id)
                testfile3.write("\n")
                testfile3.write(test)
                testfile3.write("\n")
                testfile3.write(action)
                testfile3.write("\n\n")
                testfile3.close()
                
        with open('patient_file.txt','a') as patient_file:
                patient_file.write(id)
                patient_file.write("\n")
                patient_file.write(test)
                patient_file.write("\n")
                patient_file.write(action)
                patient_file.write("\n\n")
                patient_file.close()
                print("Record has been written to file arcording to first ID ")

    if choice==3:
        print("if positive: QHNF ")
        print('If Negative - RU')
        
        print("Enter previous case ID (followed by T3)(00X = 000X T3):  ")
        id=input()
        print("Enter Test Result positive/negative:  ")
        test=input()
        print("Enter Action needed to be taken(QHNF/RU):  ")
        action=input()
        with open('testfile3.txt','a') as testfile3:
                testfile3.write(id)
                testfile3.write("\n")
                testfile3.write(test)
                testfile3.write("\n")
                testfile3.write(action)
                testfile3.write("\n\n")
                testfile3.close()
                
        with open('patient_file.txt','a') as patient_file:
                patient_file.write(id)
                patient_file.write("\n")
                patient_file.write(test)
                patient_file.write("\n")
                patient_file.write(action)
                patient_file.write("\n\n")
                patient_file.close()
                print("Record has been written to file arcording to first ID ")
    
    if choice==4:
        print("if positive: QHNF ")
        print('If Negative - RU')
        
        print("Enter previous case ID (followed by T3)(00X = 000X T3):  ")
        id=input()
        print("Enter Test Result positive/negative:  ")
        test=input()
        print("Enter Action needed to be taken(QHNF/RU):  ")
        action=input()
        with open('testfile3.txt','a') as testfile3:
                testfile3.write(id)
                testfile3.write("\n")
                testfile3.write(test)
                testfile3.write("\n")
                testfile3.write(action)
                testfile3.write("\n\n")
                testfile3.close()
                
        with open('patient_file.txt','a') as patient_file:
                patient_file.write(id)
                patient_file.write("\n")
                patient_file.write(test)
                patient_file.write("\n")
                patient_file.write(action)
                patient_file.write("\n\n")
                patient_file.close()
                print("Record has been written to file arcording to first ID ")

    if choice==5:
        print("if positive: QHNF ")
        print('If Negative - CW')
        
        print("Enter previous case ID (followed by T3)(00X = 000X T3):  ")
        id=input()
        print("Enter Test Result positive/negative:  ")
        test=input()
        print("Enter Action needed to be taken(QHNF/CW):  ")
        action=input()
        with open('testfile3.txt','a') as testfile3:
                testfile3.write(id)
                testfile3.write("\n")
                testfile3.write(test)
                testfile3.write("\n")
                testfile3.write(action)
                testfile3.write("\n\n")
                testfile3.close()
                
        with open('patient_file.txt','a') as patient_file:
                patient_file.write(id)
                patient_file.write("\n")
                patient_file.write(test)
                patient_file.write("\n")
                patient_file.write(action)
                patient_file.write("\n\n")
                patient_file.close()
                print("Record has been written to file arcording to first ID ")
    
    if choice==6:
         print('thank you for using covid 19 management system')
    
    return menu()
    
def modifyStatus():
    #modify patient status (active/revovered/deceased)
    pass


def menu():
    #This will be the Main Screen before user is asked to select an option from 1-6
    print("************COVID-19 MANAGEMENT**********")
    print("************MAIN MENU**************")
    print('please select your desired option:')
    print('1. Add New Patient(Register)')
    print('2. Print patient info')
    print('3. Search for Patient')
    print('4. Test Result for Covid-19')
    print('5. Modify the Status')
    print('6. Exit')
    print()
    choice = int(input('Enter selection: '))

    if choice==1:
        savePatientdetails()
    elif choice==2:
        printPatientdetails()
    elif choice==3:
        searchPatientdetails()
    elif choice==4:
        printTestresults()
    elif choice==5:
        modifyStatus()
    elif choice==6:
        print('Thank you for using COVID-19 Management')
    else:
        print('Please enter 1-6')

    print()
    print()

menu()

