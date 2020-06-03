# Cheyne Stanley Randau Burberry
# TP059946

def registerpatient():
    records = []
    for i in range(1):
        item = []
        idNum = input('Enter ID number: ')
        item.append(idNum)
        firstName = input('Enter first name: ')
        item.append(firstName)
        zone = input('Enter zone: ')
        item.append(zone)
        groupNum = input('Enter group: ')
        item.append(groupNum)
        phoneNum = input('Enter phone number(+60): ')
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

    return menu()    

def printPatientdetails():
    print("**********************************Patient Details************************************")
    try:
        fileHandler = open('patient_file.txt','r')
    except:
        print ('Unable to locate the file:')
        exit()

    for line in fileHandler:
        print(line)
        
    fileHandler.close()
    
    print("")
    print("")
    return menu()
        
def searchPatientdetails():
    try:
        fileHandler = open('patient_file.txt','r')
    except:
        print ('Unable to locate the file:')
        exit()

    search_key = input('Please type in ID number: ')
    print("**********************************Searched Patient Details************************************")

    for line in fileHandler:
        line = line.rstrip()
        if not search_key.lower() in line.lower(): 
            continue
        print(line)
        
    fileHandler.close()
    print("")
    print("")
    return menu()
    
def printTestresults():
    #display menu for tests results and action taken
    print("************COVID-19 MANAGEMENT**********")
    print("************TEST MENU**************")
    print('please select your desired option:')
    print('1. Carry out TEST 1(required for every patient)')
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
    #MAIN TEST MENU - when user prompts for choice 4 in the MAIN MANAGEMENT MENU
    print("************COVID-19 MANAGEMENT**********")
    print("************TEST 1 MENU**************")
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
        #prompts user for test results in a new sub menu
        print("************COVID-19 MANAGEMENT**********")
        print("************TEST 1 MENU**************")
        print('please select TEST RESULTS')
        print('1. POSITIVE')
        print('2. NEGATIVE')
        print()
        choice = int(input('Enter selection: '))

        if choice==1:
            #prompt user for information (case ID, test result and NW/ICU)
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Enter NW or ICU:")
            ward=input()
            action="QHNF"
            print("Action taken:"+action)
            status="ACTIVE"
            print(status)
            #open file - then saves the input above (appending)
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(ward)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\t")
                    testfile.write(status)
                    testfile.write("\n")
                    testfile.close()
            #open file - then saves the same input above (appending) to a different file (patient_file.txt)   
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(ward)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\t")
                    patient_file.write(status)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
            
            return menu()  
        
        elif choice==2:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Test 2 Required")
            action="QDFR"
            print("Action taken:"+action)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
   
            return menu()
    
    elif choice==2:
        #prompts user for test results in a new sub menu
        print("************COVID-19 MANAGEMENT**********")
        print("************TEST 1 MENU**************")
        print('please select TEST RESULTS')
        print('1. POSITIVE')
        print('2. NEGATIVE')
        print()
        choice = int(input('Enter selection: '))

        if choice==1:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Enter NW or ICU:")
            ward=input()
            action="QHNF"
            print("Action taken:"+action)
            status="ACTIVE"
            print(status)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(ward)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\t")
                    testfile.write(status)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(ward)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\t")
                    patient_file.write(status)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
   
            return menu()
        
        elif choice==2:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Test 2 Required")
            action="QDFR"
            print("Action taken:"+action)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
   
        return menu()
 
    elif choice==3:
        #prompts user for test results in a new sub menu
        print("************COVID-19 MANAGEMENT**********")
        print("************TEST 1 MENU**************")
        print('please select TEST RESULTS')
        print('1. POSITIVE')
        print('2. NEGATIVE')
        print()
        choice = int(input('Enter selection: '))

        if choice==1:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Enter NW or ICU:")
            ward=input()
            action="QHNF"
            print("Action taken:"+action)
            status="ACTIVE"
            print(status)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(ward)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\t")
                    testfile.write(status)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(ward)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\t")
                    patient_file.write(status)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
            return menu()   
        
        elif choice==2:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Test 2 Required")
            action="QDFR"
            print("Action taken:"+action)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\t")
                    patient_file.write(status)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
   
            return menu()
    
    
   
    elif choice==4:
        #prompts user for test results in a new sub menu
        print("************COVID-19 MANAGEMENT**********")
        print("************TEST 1 MENU**************")
        print('please select TEST RESULTS')
        print('1. POSITIVE')
        print('2. NEGATIVE')
        print()
        choice = int(input('Enter selection: '))

        if choice==1:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Enter NW or ICU:")
            ward=input()
            action="QHNF"
            print("Action taken:"+action)
            status="ACTIVE"
            print(status)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\nt")
                    testfile.write(ward)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\t")
                    testfile.write(status)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(ward)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\t")
                    patient_file.write(status)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
            
            return menu()   
        
        elif choice==2:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Test 2 Required")
            action="HQFR"
            print("Action taken:"+action)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
   
            return menu()
    
   
   
    elif choice==5:   
        #prompts user for test results in a new sub menu
        print("************COVID-19 MANAGEMENT**********")
        print("************TEST 1 MENU**************")
        print('please select TEST RESULTS')
        print('1. POSITIVE')
        print('2. NEGATIVE')
        print()
        choice = int(input('Enter selection: '))

        if choice==1:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Enter NW or ICU:")
            ward=input()
            action="HQNF"
            print("Action taken:"+action)
            status="ACTIVE"
            print(status)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(ward)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\t")
                    testfile.write(status)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(ward)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\t")
                    patient_file.write(status)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
            
            return menu()   
        
        elif choice==2:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Test 2 Required")
            action="CWFR"
            print("Action taken:"+action)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
   
            return menu()
    
    elif choice==6:
        print('thank you for using covid 19 management system')
    
    return menu()  
    
    
    
    
def test_2():
   #MAIN TEST MENU - when user prompts for choice 4 in the MAIN MANAGEMENT MENU
    print("************COVID-19 MANAGEMENT**********")
    print("************TEST 2 MENU**************")
    print('please select TEST according to Groupings:')
    print('ATO-T2 [1]')
    print('ACC T2 [2]')
    print('AEO-T2 [3]')
    print('SID-T2 [4]')
    print('AHS-T2 [5]')
    print('6.   Exit')
    print()
    choice = int(input('Enter selection: '))

    if choice==1:
        #prompts user for test results in a new sub menu
        print("************COVID-19 MANAGEMENT**********")
        print("************TEST MENU**************")
        print('please select TEST RESULTS')
        print('1. POSITIVE')
        print('2. NEGATIVE')
        print()
        choice = int(input('Enter selection: '))

        if choice==1:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Enter NW or ICU:")
            ward=input()
            action="QHNF"
            print("Action taken:"+action)
            status="ACTIVE"
            print(status)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(ward)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\t")
                    testfile.write(status)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("tn")
                    patient_file.write(test)
                    patient_file.write("\nt")
                    patient_file.write(ward)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\t")
                    patient_file.write(status)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
            
            return menu()  
        
        elif choice==2:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Test 3 Required")
            action="QDFR"
            print("Action taken:"+action)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
   
            return menu()   
    
    elif choice==2:
        #prompts user for test results in a new sub menu
        print("************COVID-19 MANAGEMENT**********")
        print("************TEST 2 MENU**************")
        print('please select TEST RESULTS')
        print('1. POSITIVE')
        print('2. NEGATIVE')
        print()
        choice = int(input('Enter selection: '))

        if choice==1:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Enter NW or ICU:")
            ward=input()
            action="QHNF"
            print("Action taken:"+action)
            status="ACTIVE"
            print(status)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(ward)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\t")
                    testfile.write(status)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(ward)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\t")
                    patient_file.write(status)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
   
            return menu()
        
        elif choice==2:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Test 3 Required")
            action="QDFR"
            print("Action taken:"+action)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
   
        return menu()
 
    if choice==3:
        #prompts user for test results in a new sub menu
        print("************COVID-19 MANAGEMENT**********")
        print("************TEST 2 MENU**************")
        print('please select TEST RESULTS')
        print('1. POSITIVE')
        print('2. NEGATIVE')
        print()
        choice = int(input('Enter selection: '))

        if choice==1:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Enter NW or ICU:")
            ward=input()
            action="QHNF"
            print("Action taken:"+action)
            status="ACTIVE"
            print(status)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(ward)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\t")
                    testfile.write(status)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(ward)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\t")
                    patient_file.write(status)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
            
            return menu()    
        
        elif choice==2:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Test 3 Required")
            action="QDFR"
            print("Action taken:"+action)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
   
            return menu()
    
    
   
    if choice==4:
        #prompts user for test results in a new sub menu
        print("************COVID-19 MANAGEMENT**********")
        print("************TEST 2 MENU**************")
        print('please select TEST RESULTS')
        print('1. POSITIVE')
        print('2. NEGATIVE')
        print()
        choice = int(input('Enter selection: '))

        if choice==1:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Enter NW or ICU:")
            ward=input()
            action="QHNF"
            print("Action taken:"+action)
            status="ACTIVE"
            print(status)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\nt")
                    testfile.write(ward)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\t")
                    testfile.write(status)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(ward)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\t")
                    patient_file.write(status)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
            return menu()    
        
        elif choice==2:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Test 3 Required")
            action="HQFR"
            print("Action taken:"+action)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
   
            return menu()
    
   
   
    if choice==5:   
        #prompts user for test results in a new sub menu
        print("************COVID-19 MANAGEMENT**********")
        print("************TEST 2 MENU**************")
        print('please select TEST RESULTS')
        print('1. POSITIVE')
        print('2. NEGATIVE')
        print()
        choice = int(input('Enter selection: '))

        if choice==1:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Enter NW or ICU:")
            ward=input()
            action="HQNF"
            print("Action taken:"+action)
            status="ACTIVE"
            print(status)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(ward)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\t")
                    testfile.write(status)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(ward)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\t")
                    patient_file.write(status)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
           
            return menu()   
        
        elif choice==2:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Test 3 Required")
            action="CWFR"
            print("Action taken:"+action)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
   
            return menu()
    
    if choice==6:
        print('thank you for using covid 19 management system')
    
    return menu()    
    


def test_3():
    #MAIN TEST MENU - when user prompts for choice 4 in the MAIN MANAGEMENT MENU
    print("************COVID-19 MANAGEMENT**********")
    print("************ TEST 3 MENU**************")
    print('please select TEST according to Groupings:')
    print('ATO-T3 [1]')
    print('ACC T3 [2]')
    print('AEO-T3 [3]')
    print('SID-T3 [4]')
    print('AHS-T3 [5]')
    print('6.   Exit')
    print()
    choice = int(input('Enter selection: '))

    if choice==1:
        #prompts user for test results in a new sub menu
        print("************COVID-19 MANAGEMENT**********")
        print("************TEST 3 MENU**************")
        print('please select TEST RESULTS')
        print('1. POSITIVE')
        print('2. NEGATIVE')
        print()
        choice = int(input('Enter selection: '))

        if choice==1:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Enter NW or ICU:")
            ward=input()
            action="QHNF"
            print("Action taken:"+action)
            status="ACTIVE"
            print(status)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(ward)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\t")
                    testfile.write(status)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(ward)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\t")
                    patient_file.write(status)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
           
            return menu()
        
        elif choice==2:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("no more tests required")
            action="RU"
            print("Action taken:"+action)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
   
            return menu() 
    
    elif choice==2:
        #prompts user for test results in a new sub menu
        print("************COVID-19 MANAGEMENT**********")
        print("************TEST 3 MENU**************")
        print('please select TEST RESULTS')
        print('1. POSITIVE')
        print('2. NEGATIVE')
        print()
        choice = int(input('Enter selection: '))

        if choice==1:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Enter NW or ICU:")
            ward=input()
            action="QHNF"
            print("Action taken:"+action)
            status="ACTIVE"
            print(status)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(ward)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\t")
                    testfile.write(status)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(ward)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\t")
                    patient_file.write(status)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
   
            return menu()
        
        elif choice==2:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("no more tests required")
            action="RU"
            print("Action taken:"+action)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
   
        return menu()
 
    if choice==3:
        #prompts user for test results in a new sub menu
        print("************COVID-19 MANAGEMENT**********")
        print("************TEST 3 MENU**************")
        print('please select TEST RESULTS')
        print('1. POSITIVE')
        print('2. NEGATIVE')
        print()
        choice = int(input('Enter selection: '))

        if choice==1:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Enter NW or ICU:")
            ward=input()
            action="QHNF"
            print("Action taken:"+action)
            status="ACTIVE"
            print(status)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(ward)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\t")
                    testfile.write(status)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(ward)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\t")
                    patient_file.write(status)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
            
            return menu()    
        
        elif choice==2:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("no more tests required")
            action="RU"
            print("Action taken:"+action)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
   
            return menu()
    
    
   
    if choice==4:
        #prompts user for test results in a new sub menu
        print("************COVID-19 MANAGEMENT**********")
        print("************TEST 3 MENU**************")
        print('please select TEST RESULTS')
        print('1. POSITIVE')
        print('2. NEGATIVE')
        print()
        choice = int(input('Enter selection: '))

        if choice==1:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Enter NW or ICU:")
            ward=input()
            action="QHNF"
            print("Action taken:"+action)
            status="ACTIVE"
            print(status)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\nt")
                    testfile.write(ward)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\t")
                    testfile.write(status)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(ward)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\t")
                    patient_file.write(status)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
            
            return menu()    
        
        elif choice==2:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("no more tests required")
            action="RU"
            print("Action taken:"+action)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
   
            return menu()
    
   
   
    if choice==5:   
        #prompts user for test results in a new sub menu
        print("************COVID-19 MANAGEMENT**********")
        print("************TEST 3 MENU**************")
        print('please select TEST RESULTS')
        print('1. POSITIVE')
        print('2. NEGATIVE')
        print()
        choice = int(input('Enter selection: '))

        if choice==1:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("Enter NW or ICU:")
            ward=input()
            action="HQNF"
            print("Action taken:"+action)
            status="ACTIVE"
            print(status)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(ward)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\t")
                    testfile.write(status)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(ward)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\t")
                    patient_file.write(status)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
            
            return menu()   
        
        elif choice==2:
            
            print("Enter new case id(according to first ID)(00X = 000X):  ")
            id=input()
            print("Enter Test Result:")
            test=input()
            print("no more tests required")
            action="CW"
            print("Action taken:"+action)
            
            with open('testfile.txt','a') as testfile:
                    testfile.write(id)
                    testfile.write("\t")
                    testfile.write(test)
                    testfile.write("\t")
                    testfile.write(action)
                    testfile.write("\n")
                    testfile.close()
                
            with open('patient_file.txt','a') as patient_file:
                    patient_file.write(id)
                    patient_file.write("\t")
                    patient_file.write(test)
                    patient_file.write("\t")
                    patient_file.write(action)
                    patient_file.write("\n")
                    patient_file.close()
                    print("Record has been written to file arcording to case ID ")
   
            return menu()
    
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

