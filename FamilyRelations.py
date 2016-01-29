'''
    Group #2 - Program 4 - Family Relations Program            
    Max Conroy                                                 
    CSC 485 - Special Topics in Computer Science - Python     
'''
#People data version 1 completed on my own

import sys
import os.path

# main will serve as the command handler
def main():
    d={} #dictionary
    des=[] #people described
    ref=[] #people referenced

    flag=True
    print('\n-Family relations program-')
    print('Enter H for list of commands.\n')
    while flag==True:   #outer menu loop
        command = input('Enter command... ')   #gets command from user
        command=command.lower()
        if command == 'a':
            d,des,ref = add(d,des,ref) #call add function
        elif command == 'l':    
            d,ref = load(d,des,ref)  #call load function
        elif command == 's':
            save(d)        #call save function
        elif command == 'v':
            view(d,des,ref)#call view function
        elif command == 'i':
            info(d,des,ref)#call info function
        elif command == 'h':
            printHelp()
        elif command == 'quit':
            flag=False
            print("Program Terminated.\n")  
            sys.exit()
        else:
            print('Invalid command.\n')
       
def printHelp():
    print("=================================================")
    print("     Welcome to the Family Relations Program     ")
    print("=================================================")
    print("- Enter command from the following list:         ")
    print("- A adds a person to the program. L loads people ")
    print("- from a file. S saves people to a file. V views ")
    print("- the people described and referenced. I displays")
    print("- information about a person. Quit will terminate")
    print("- the program.                                   ")
    print("=================================================")
    return

def add(d,des,ref):
        #\/family info storage
    father=[]
    mother=[]
    spouse=[]
    son=[]
    daughter=[]

    oflag=True
    while oflag==True:
        iflag=True
        person=input('Enter name of person (enter to continue):\n')
        if person=='':
            oflag=False
        elif person in d:#person already exists in dict, block gives user option to change
            yn=input('Person is already in the list. Change information for person? (y/n)\n')
            yn.lower()
            if yn == 'n':
                print('Returning to menu\n')
                oflag=False
            elif yn == 'y':
                print('Current family information for '+person+':')
                print(d[person])
                print('')
                while iflag==True:
                    f=input('Enter father(s) of '+person+' (enter to continue):\n')
                    if f=='':
                        iflag=False
                    elif iflag==True: 
                        father.append(f)
                while iflag==False:
                    f=input('Enter mother(s of '+person+' (enter to continue):\n')
                    if f=='':
                        iflag=True
                    elif iflag==False:
                        mother.append(f)
                while iflag==True:
                    f=input('Enter spouse(s) of '+person+' (enter to continue):\n')
                    if f=='':
                        iflag=False
                    elif iflag==True:
                        spouse.append(f)
                while iflag==False:
                    f=input('Enter son(s) of '+person+' (enter to continue):\n')
                    if f=='':
                        iflag=True
                    elif iflag==False:
                        son.append(f)
                while iflag==True:
                    f=input('Enter daughter(s) of '+person+' (enter to continue):\n')
                    if f=='':
                        iflag=False
                    elif iflag==True:
                        daughter.append(f)
                print('New family information for '+person+':')
                print('Father(s): ')
                print(father)
                print('Mother(s): ')
                print(mother)
                print('Spouse(s): ')
                print(spouse)
                print('Son(s): ')
                print(son)
                print('Daughter(s): ')
                print(daughter)
                accept=input('Enter C to confirm the add or R to reject the add...')
                if accept == 'C' or accept == 'c':
                    for i in d[person]:
                        ref.remove(i)   #clears ref of previous data

                    for i in father:        ####block adds new data to ref
                        if i not in ref:
                            ref.append(i)   
                    for i in mother:
                        if i not in ref:
                            ref.append(i)
                    for i in spouse:
                        if i not in ref:
                            ref.append(i)
                    for i in son:
                        if i not in ref:
                            ref.append(i)
                    for i in daughter:
                        if i not in ref:
                            ref.append(i)    ####
                    d.update({person:{'Father(s)':father,'Mother(s)':mother,'Spouse(s)':spouse,'Son(s)':son,'Daughter(s)':daughter}})
                    print('Add complete, returning to menu.\n') 
                elif accept == 'R' or accept =='r':
                    father=[]
                    mother=[]
                    spouse=[]
                    son=[]
                    daughter=[]
                    continue
                else:
                    print('Invalid input\n')
        
            else:
                print('Invalid input. Returning to menu.\n')
                oflag=False
        else:
            des.append(person)  #add person to described
            while iflag==True:
                f=input('Enter father(s) of '+person+' (enter to continue):\n')
                if f=='':
                    iflag=False
                elif iflag==True:
                    father.append(f)
            while iflag==False:
                f=input('Enter mother(s of '+person+' (enter to continue):\n')
                if f=='':
                    iflag=True
                elif iflag==False:
                    mother.append(f)
            while iflag==True:
                f=input('Enter spouse(s) of '+person+' (enter to continue):\n')
                if f=='':
                    iflag=False
                elif iflag==True:
                    spouse.append(f)
            while iflag==False:
                f=input('Enter son(s) of '+person+' (enter to continue):\n')
                if f=='':
                    iflag=True
                elif iflag==False:
                    son.append(f)
            while iflag==True:
                f=input('Enter daughter(s) of '+person+' (enter to continue):\n')
                if f=='':
                    iflag=False
                elif iflag==True:
                    daughter.append(f)
            print('Family information for '+person+':')
            print('Father(s): ')
            print(father)
            print('Mother(s): ')
            print(mother)
            print('Spouse(s): ')
            print(spouse)
            print('Son(s): ')
            print(son)
            print('Daughter(s): ')
            print(daughter)
            accept=input('Enter C to confirm the add or R to reject the add...')
            if accept == 'C' or accept == 'c':
                for i in d[person]:
                    ref.remove(i)   #clears ref of previous data

                for i in father:        ####block adds new data to ref
                    if i not in ref:
                        ref.append(i)   
                for i in mother:
                    if i not in ref:
                        ref.append(i)
                for i in spouse:
                    if i not in ref:
                        ref.append(i)
                for i in son:
                    if i not in ref:
                        ref.append(i)
                for i in daughter:
                    if i not in ref:
                        ref.append(i)    ####
                d.update({person:{'Father(s)':father,'Mother(s)':mother,'Spouse(s)':spouse,'Son(s)':son,'Daughter(s)':daughter}})
                print('Add complete, returning to menu.\n') 
            elif accept == 'R' or accept =='r':
                father=[]
                mother=[]
                spouse=[]
                son=[]
                daughter=[]
                continue
            else:
                print('Invalid input\n')
        
    return d,des,ref

def load(d,des,ref):
    inputFlag = False   #flag for checking file validity
    state = 0           #initial state of loading file
    fcheck = False      #checks that file is open when moving to load
    icheck = False      #flag checks for new name token in file
        #\/family info storage
    father=[]
    mother=[]
    spouse=[]
    son=[]
    daughter=[]
    name=''

    while inputFlag == False:                                              
        inputFile = input("Enter file name to load (Enter to continue): ")         #prompt for input file
        if inputFile == '':                                                 #return to menu        
            print('Returning to menu.\n')
            inputFlag = True
        else:                                               #try to open file
            if os.path.exists(inputFile) == True:          
                if os.path.isfile(inputFile) == True:       
                    ifile = open(inputFile,"r")             
                    print("Input File Opened.\n")
                    inputFlag = True                        #Exit the loop
                    fcheck = True
                else:                                       #is not a file
                    print("The input file is not a file.\n")
            else:                                           #doesn't exist         
                print("The input file doesn't exist.\n")
    if fcheck == True:
        for i in ifile:
            i=i.lower().rstrip()
            try:
                if state == 0:                               #state waits for name token
                    if i == 'name':
                        state=1
                elif state == 1:                    #state waits for name for name token
                    if i == 'name':
                        print('Name was followed by duplicate name.') 
                    if i.strip() == '':
                        print('No entry for name')
                    if icheck == True:           #checks if new name token in file
                        for i in d[name]:
                            ref.remove(i)   #clears ref of previous data

                        for i in father:        ####block adds new data to ref
                            if i not in ref:
                                ref.append(i)   
                        for i in mother:
                            if i not in ref:
                                ref.append(i)
                        for i in spouse:
                            if i not in ref:
                                ref.append(i)
                        for i in son:
                            if i not in ref:
                                ref.append(i)
                        for i in daughter:
                            if i not in ref:
                                ref.append(i)    ####
                        #block sets data into dictionary and resets list and name for new name token          
                        d.update({name:{'Father(s)':father,'Mother(s)':mother,'Spouse(s)':spouse,'Son(s)':son,'Daughter(s)':daughter}})
                        father=[]
                        mother=[]
                        spouse=[]
                        son=[]
                        daughter=[]
                        name=i
                        state=2
                        icheck = False
                    else:
                        if i in des:
                            print(i+' is already being described, data will be overwritten')
                        elif i not in des:
                            des.append(i)
                        name=i
                        state=2

                elif state == 2:                    #state waits for family token
                    if i == 'name':
                        print('Name token followed by name token. A name is expected.')
                    elif i == 'father':
                        state=3
                    elif i == 'mother':
                        state=4
                    elif i == 'spouse':
                        state=5
                    elif i == 'son':
                        state=6
                    elif i == 'daughter':
                        state=7
                    elif i == '':
                        print('No entry for name')
                    elif i == 'name':
                        state=1
                elif state == 3:                        #state for father token
                    if i == 'father':
                        print('Father token followed by father token. A name is expected')
                    elif i == 'mother':
                        state=4
                    elif i == 'spouse':
                        state=5
                    elif i == 'son':
                        state=6
                    elif i == 'daughter':
                        state=7
                    elif i.strip() == '':
                        print('No entry for name')
                    elif i == 'name':
                        state=1
                        icheck = True
                    else:
                        father.append(i)
                        
                elif state == 4:                        #state for mother token
                    if i == 'mother':
                        print('Mother token followed by mother token. A name is expected')
                    elif i == 'father':
                        print('Father token was already entered. Mother, spouse, son or daughter is expected')
                    elif i == 'spouse':
                        state=5
                    elif i == 'son':
                        state=6
                    elif i == 'daughter':
                        state=7
                    elif i.strip() == '':
                        print('No entry for name')
                    elif i == 'name':
                        state=1
                        icheck = True
                    else:
                        mother.append(i)
                elif state == 5:                        #state for spouse token
                    if i == 'spouse':
                        print('Spouse token followed by spouse token. A name is expected')
                    elif i == 'father':
                        print('Father token was already entered. Mother, spouse, son or daughter is expected')
                    elif i == 'mother':
                        print('Mother token was already entered. Spouse, son or daughter is expected')
                    elif i == 'son':
                        state=6
                    elif i == 'daughter':
                        state=7
                    elif i.strip() == '':
                        print('No entry for name')
                    elif i == 'name':
                        state=1
                        icheck = True
                    else:
                        spouse.append(i)
                elif state == 6:                        #state for son token
                    if i == 'son':
                        print('Son token followed by son token. A name is expected')
                    elif i == 'father':
                        print('Father token was already entered. Mother, spouse, son or daughter is expected')
                    elif i == 'mother':
                        print('Mother token was already entered. Spouse, son or daughter is expected')
                    elif i == 'spouse':
                        print('Spouse token was already entered. Son or daughter is expected')
                    elif i == 'daughter':
                        state=7
                    elif i.strip() == '':
                        print('No entry for name')
                    elif i == 'name':
                        state=1
                        icheck = True
                    else:
                        son.append(i)
                elif state == 7:                        #state for daughter token
                    if i == 'daughter':
                        print('Daughter token followed by daughter token. A name is expected')
                    elif i == 'father':
                        print('Father token was already entered. Mother, spouse, son or daughter is expected')
                    elif i == 'mother':
                        print('Mother token was already entered. Spouse, son or daughter is expected')
                    elif i == 'spouse':
                        print('Spouse token was already entered. Son or daughter is expected')

                    elif i.strip() == '':
                        print('No entry for name')
                    elif i == 'name':
                        state=1
                        icheck = True
                    else:
                        daughter.append(i)
                else:
                    print('Error detected')
                    break
                                        
            except Exception:
                print('Exception error')
                pass

        for i in father:        ####block adds new data to ref
            if i not in ref:
                ref.append(i)   
        for i in mother:
            if i not in ref:
                ref.append(i)
        for i in spouse:
            if i not in ref:
                ref.append(i)
        for i in son:
            if i not in ref:
                ref.append(i)
        for i in daughter:
            if i not in ref:
                ref.append(i)    ####
        d.update({name:{'Father(s)':father,'Mother(s)':mother,'Spouse(s)':spouse,'Son(s)':son,'Daughter(s)':daughter}})
        print('File load complete, returning to menu.\n')
        ifile.close()
    return d,ref

def save(d):
    outputFlag = False 
    fcheck = False      #checks if file was opened                                                          
    while outputFlag == False:                                                   #Loops for output until output file satisfies
        outputFile = input("Enter file name to save to. (Enter to continue): ")       
        if outputFile == '':                                                
            print('Returning to menu.')
            outputFlag=True                                                         
        else:                                                #try to open file
            if os.path.exists(outputFile) == True:          
                if os.path.isfile(outputFile) == True:       
                    print("The output file exists! Do you want to overwrite it?")
                    overwriter = input("Enter Y to overwrite or anything else to enter a new file name: ")     
                    if overwriter == "Y" or overwriter == "y":      #Overwrite the output file
                        ofile = open(outputFile,"w")                
                        print("Output File Opened!\n")
                        outputFlag = True                           #Exit the loop
                        fcheck=True
                    else:                                    #user doesn't want to overwrite
                        print("The output file has not been overwritten, please input a new output file!\n")
                else:                                        #is not a file
                    print("The output file is not a file!\n")
            else:                                            #doesn't exist         
                print("The output file doesn't exist!\n")
    if fcheck == True:
        for i in d:
            try:
                ofile.write('Name: '+i+'\n')
            except Exception:
                pass
            for o in d[i]:
                try:
                    ofile.write(o+'\n')
                except Exception:
                    pass
                for p in d[i][o]:
                    try:
                        ofile.write(p+'\n')
                    except Exception:
                        pass
        print('Data has been saved, returning to menu.\n')
        ofile.close()
    return

def view(d,des,ref):
    print('People who are being described by family relations:')
    for i in des:
        print(i+'\n')
    print('People who are being referenced by the people described:')
    for i in ref:
        print(i+'\n')
    return

def info(d,des,ref):
    flag=False
    while flag == False:
        print('People being described: ')
        for i in des:
            print(i)
        f=input('Enter name of person described to view their family information (Enter to continue)')
        f=f.rstrip().lower()
        if f == '':
            flag=True
        elif f not in des:
            print('Person is not being described. Try again.\n')
        elif f in des:
            print('People who are referenced by '+f)
            for i in d[f]:
                print(i)
                for v in d[f][i]:
                    print(v)
    return                                                            

main()

