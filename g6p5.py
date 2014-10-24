'''
Program 5
John Payerchin, John Juran, Max Conroy (Group 6)
CSC 485 Python
10-27-2014
'''
import sys

def main():
	flag = True
	Dictionary={}
	Described = []
	Referenced = []
	quit = ''
	while flag:
		try:
			print('')
			print("Menu") #Creates menu
			print("----")
			print("L: Load")
			print("S: Save")
			print("A: Add")
			print("V: View")
			print("I: Information")
			print("E: Edit")
			print("U: Update")
			print("R: Relations")
			print("U: Delete")
			print("H: Help")
			print("Q: Quit")
			response = input("Please choose an option now.\n")
			response = response.lower()
			if response == 'l':
				Dictionary,loadfile,Described,Referenced = Load(Dictionary,Described,Referenced)
			elif response == 's':
				if Dictionary == {}:
					print('Dictionary is empty. Add a person or load a file first.')
				else:
					Save(Dictionary,loadfile)
			elif response == 'a':
				Dictionary, Described, Referenced = Add(Dictionary,Described,Referenced)
			elif response == 'v':
				if Dictionary == {}:
					print('Dictionary is empty. Add a person or load a file first.')
				else:
					View(Dictionary,Described,Referenced)
			elif response == 'i':
				if Dictionary == {}:
					print('Dictionary is empty. Add a person or load a file first.')
				else:
					Info(Dictionary,Described)
			elif response == 'e':
				if Dictionary == {}:
					print('Dictionary is empty. Add a person or load a file first.')
				else:
					Edit(Described,Dictionary)
            elif response == 'u':
				if Dictionary == {}:
					print('Dictionary is empty. Add a person or load a file first.')
                else:
                    Described = Update(Dictionary,Described,Referenced)
			elif response == 'q':
				quit = input("Are you sure you'd like to quit? Respond with yes or no.\n")
				quit = quit.upper()
				if quit == "YES":
					flag = False
				else:
					continue
			else:
				print("Please choose a response from the menu.\n")
		except UnboundLocalError: #Makes sure a file is loaded first
			print("You must first load a file.")
	
	print('')
def Load(Dictionary,Described,Referenced):#loads the file

	loadflag = 'False'
	Input=''
	while Input != 'quit' and loadflag == 'False':
		Input=input("Enter the name of a valid input file or enter 'quit' to quit:\n")
		try:
			loadfile=open(Input,'r')
			loadflag = 'True'
		except:
			if Input != 'quit':
				print("File does not exist.\n")
				loadflag = 'False'
	
	prevline = ''
	Listy=['MOTHER','FATHER','DAUGHTER','SON','SPOUSE','NAME']#List to see what type to read next
	Name = []
	Father = []
	Mother = []
	Spouse = []
	Son = []
	Daughter = []
	tocheck = []
	Fflag = False
	Mflag = False
	Spflag = False
	Soflag = False
	Dflag = False
	flag1 = False
	
	for line in loadfile:
		line=line.strip()
		line = line.upper()
		if prevline in ['NAME']:
			Name=line
			flag1 = True
		elif prevline in ['FATHER'] or Fflag == True:
			if line not in Listy:
				Father.append(line)
				Fflag = True
			else:
				Fflag=False
		elif prevline == 'MOTHER' or Mflag == True:	   
			if line not in Listy:
				Mother.append(line)
				Mflag = True
			else:
				Mflag = False
		elif prevline == 'SPOUSE' or Spflag == True:	   
			if line not in Listy:
				Spouse.append(line)
				Spflag = True
			else:
				Spflag=False
		elif prevline == 'SON' or Soflag == True:		  
			if line not in Listy:
				Son.append(line)
				Soflag = True
			else:
				Soflag=False  
		elif prevline == 'DAUGHTER' or Dflag == True:		  
			if line not in Listy:
				Daughter.append(line)
				Dflag = True
			else:
				Dflag=False
		if flag1 and line == 'NAME':
			if Name != '':
				Dictionary.update({Name:{'FATHER':Father,'MOTHER':Mother,'SPOUSE':Spouse,'SON':Son,'DAUGHTER':Daughter}})
		if Name not in Described and Name != []:
			Described.append(line)
			if line in Referenced:
				Referenced.remove(line)
			tocheck=Father+Mother+Spouse+Son+Daughter
			for person in tocheck:
				if person not in Described:
					if person not in Referenced:
					   Referenced.append(person)
			#create dictionary, null lists
		prevline = line.strip()	
	print("Done Loading\n")	   
	return Dictionary,Input,Described,Referenced

def Add(Dictionary,Described,Referenced):
	Father=[]
	Mother=[]
	Spouse=[]
	Son=[]
	Daughter=[]
	exists = True
	while exists == True:	   
		Name = input("Enter the name of the person you wish to add.\n")
		Name = Name.upper()
		if Name in Dictionary:
			duplicateresp = input("The person already exists. Would you like to add them anyway? Answer 'Yes' or 'No'.")
			duplicateresp = duplicateresp.upper()
			if duplicateresp == 'no':
				exists = False
			else:
				continue
		else:
			resp = 'j'
			while resp !='':
				resp = input("Enter a father's name. Enter to continue to mothers.\n")
				if resp !='':
					Father.append(resp)
                    if resp in Described:
                        if name in Dictionary[resp]:
                            continue
                        else:
                            print('''The father's description of child needs updated''')
                            
			resp = 'j'
			while resp !='':
				resp = input("Enter a mother's name. Enter to continue to spouses.\n")
				if resp !='':
					Mother.append(resp)
                    if resp in Described:
                        if name in Dictionary[resp]:
                            continue
                        else:
                            print('''The mother's description of child needs updated''')
			resp = 'j'
			while resp !='':
				resp = input("Enter a spouse's name. Enter nothing to continue to sons.\n")
				if resp !='':
						Spouse.append(resp)
                        if resp in Described:
                            if name in Dictionary[resp]
                                continue
                            else:
                                print('''The spouse's description of spouse needs updated''')
			resp = 'j'
			while resp !='':
				resp = input("Enter a son's name. Enter nothing to continue to daughters.\n")
				if resp !='':
					Son.append(resp)
                        if resp in Described:
                            if name in Dictionary[resp]
                                continue
                            else:
                                print('''The Son's description of parent needs updated''')
			resp = 'j'
			while resp !='':
				resp = input("Enter a daughter's name. Enter nothing to finish.\n")
				if resp !='':
					Daughter.append(resp)
                        if resp in Described:
                            if name in Dictionary[resp]
                                continue
                            else:
                                print('''The daughter's description of  needs updated''')
			exists = False
			Dictionary.update({Name:{'FATHER':Father,'MOTHER':Mother,'SPOUSE':Spouse,'SON':Son,'DAUGHTER':Daughter}})
			if Name not in Described:
				Described.append(Name)
				if Name in Referenced:
					Referenced.remove(Name)
			tocheck = Father+Mother+Spouse+Son+Daughter
			for person in tocheck:
				if person not in Described:
					if person not in Referenced:
						Referenced.append(person)
	print("The person has successfully been added.")
	
	return Dictionary,Described,Referenced
	
	
def Save(Dictionary,loadfile):
	Res=input("Would you like to over write the file? 'y' for yes 'n' for no\n")
	Res=Res.lower()
	if Res in ['n']:
		loadfile=input("Enter the name of the file to write to\n")
	f=open(loadfile,'w')
	for key in Dictionary:
		f.write("NAME\n")
		f.write(key+"\n")
		for key2 in Dictionary[key]:
			f.write (key2+"\n")
			for key3 in Dictionary[key][key2]:
				f.write(key3+"\n") 
	f.write("NAME")
	f.close()
	print("The File has saved.\n")

def View(Dictionary,Described,Referenced):	 
	
	print('People who have been described:')
	for i in Described:
		print(i)
	print('')
	print('People who have been referenced, but not described:')
	for item in Referenced:
		print(item)
	
def Info(Dictionary,Described):
	Fathers = []
	Mothers = []
	Spouses = []
	Sons = []
	Daughters = []
	Name = ''
	flag = True
	print('People who have been described:')	
	for person in Described:
		print(person)
	print('')
	while flag == True:
		resp = input('Which person would you like more information on?\n')
		resp = resp.upper()
		if resp in Described:
			Name = Dictionary[resp]
			Fathers.append(Dictionary[resp]['FATHER'])
			Mothers.append(Dictionary[resp]['MOTHER'])	  
			Spouses.append(Dictionary[resp]['SPOUSE'])
			Sons.append(Dictionary[resp]['SON'])
			Daughters.append(Dictionary[resp]['DAUGHTER'])
			print('')
			print("Father(s):")
			for i in Fathers:
				print(i)
			print('')
			print("Mother(s):")
			for i in Mothers:
				print(i)
			print('')
			print("Spouse(s):")
			for i in Spouses:
				print(i)
			print('')
			print("Son(s):")
			for i in Sons:
				print(i)
			print('')
			print("Daughter(s):")
			for i in Daughters:
				print(i)
			flag = False
					  
		else:
			print("Please select a name from the list.")
			 
def Edit(Described,Dictionary):
	Fathers = []
	Mothers = []
	Spouses = []
	Sons = []
	Daughters = []
	ufathers = Fathers
	umothers = Mothers
	uspouses = Spouses
	usons = Sons
	udaughters = Daughters
	flag = True
	editresp = ''
	editflag = True
	print('People who have been described:')	
	for person in Described:
		print(person)
	print('')
	while flag == True:
		resp = input('Which person would you like to edit?\n')
		resp = resp.upper()
		if resp in Described:
			print('Now editing ',resp,".")
			print("Original Information:")
			Fathers.append(Dictionary[resp]['FATHER'][0])
			Mothers.append(Dictionary[resp]['MOTHER'][0])	  
			Spouses.append(Dictionary[resp]['SPOUSE'][0])
			Sons.append(Dictionary[resp]['SON'][0])
			Daughters.append(Dictionary[resp]['DAUGHTER'][0])
			print('')
			print("Father(s):")
			for i in Fathers:
				print(i)
			print('')
			print("Mother(s):")
			for i in Mothers:
				print(i)
			print('')
			print("Spouse(s):")
			for i in Spouses:
				print(i)
			print('')
			print("Son(s):")
			for i in Sons:
				print(i)
			print('')
			print("Daughter(s):")
			for i in Daughters:
				print(i)
			flag = False
			while editflag == True: #loops the edit until quit is entered
				editresp = input("Would you like to add a relative, delete a relative, or quit?\n")
				editresp = editresp.lower()
				if editresp == 'add':
					ufathers,umothers,uspouses,usons,udaughters = addrelative(ufathers,umothers,uspouses,usons,udaughters)
					print("The person has successfully been added.")
					resp,flag= printupdatedperson(resp,ufathers,umothers,uspouses,usons,udaughters)
				elif editresp == 'delete':
					ufathers,umothers,uspouses,usons,udaughters = deleterelative(ufathers,umothers,uspouses,usons,udaughters)
					print("The person has successfully been deleted.")
					resp,flag= printupdatedperson(resp,ufathers,umothers,uspouses,usons,udaughters)
				elif editresp == 'quit':
					quitresp = input('Would you like to save your changes? Answer yes or no.').lower()
					if quitresp == 'yes':
						Dictionary.update({resp:{'FATHER':ufathers,'MOTHER':umothers,'SPOUSE':uspouses,'SON':usons,'DAUGHTER':udaughters}})
						print('Your changes have been saved.')
						editflag == False
					elif quitresp == 'no':
						quitresp2 = input("Are you sure? You will lose all changes. Answer yes or no.\n")
						if quitresp2 == "yes":
							print("Your changes have not been saved.")
							editflag = False
						elif quitresp2 == 'no':
							continue
						else:
							print("Enter a valid response.")
				else: 
					print("Please choose an appropriate response.")
		else:
			print("Please select a name from the list.")


def printupdatedperson(resp,Fathers,Mothers,Spouses,Sons,Daughters):
	print("Edited information for",resp,":")
	print('')
	print("Father(s):")
	for i in Fathers:
		print(i)
	print('')
	print("Mother(s):")
	for i in Mothers:
		print(i)
	print('')
	print("Spouse(s):")
	for i in Spouses:
		print(i)
	print('')
	print("Son(s):")
	for i in Sons:
		print(i)
	print('')
	print("Daughter(s):")
	for i in Daughters:
		print(i)
	flag = False
	return resp,flag

def deleterelative(f,m,sp,so,d):
	delresp = 'aaa'
	while delresp.lower() != '':
		print('Would you like to delete a father, mother, spouse, son, or daughter?')
		delresp = input('Enter nothing when finished deleting.\n')
		if delresp =='father':
			personname = input('Enter the father you wish to delete.\n').upper()
			if personname in f:
				f.remove(personname)
				print('The person has been deleted.')
			else:
				print("The person is not a father.")
		elif delresp =='mother':
			personname = input('Enter the mother you wish to delete.\n').upper()
			if personname in m:
				m.remove(personname)
				print('The person has been deleted.')
			else:
				print("The person is not a father.")
		elif delresp =='spouse':
			personname = input('Enter the spouse you wish to delete.\n').upper()
			if personname in sp:
				sp.remove(personname)
				print('The person has been deleted.')
			else:
				print("The person is not a spouse.")
		elif delresp =='son':
			personname = input('Enter the son you wish to delete.\n').upper()
			if personname in so:
				so.remove(personname)
				print('The person has been deleted.')
			else:
				print("The person is not a son.")
		elif delresp =='daughter':
			personname = input('Enter the daughter you wish to delete.\n').upper()
			if personname in d:
				d.remove(personname)
				print('The person has been deleted.')
			else:
				print("The person is not a daughter.")
		else:
			print("Please choose an appropriate response.")
	return f,m,sp,so,d					

def addrelative(f,m,sp,so,d):
	addresp = 'aaaa'
	while addresp.lower() != '':
		print("Would you like to add a father, mother, spouse, son, or daughter?")
		addresp = input("Enter nothing when finished adding.\n")	
		if addresp == 'father':
			personname = input("Enter the father you wish to add.\n").upper()
			if personname not in f:
				f.append(personname)
				print("The person has been added.")
			else:
				print("He was not added. He already exists.")
		elif addresp == 'mother':
			personname = input("Enter the mother you wish to add.\n").upper()
			if personname not in m:
				m.append(personname)
				print("The person was added.")
			else:
				print("She was not added. She already exists.")
		elif addresp == 'spouse':
			personname = input("Enter the spouse you wish to add.\n").upper()
			if personname not in sp:
				sp.append(personname)
				print("The person was added.")
			else:
				print("They were not added. They already exist.")
		elif addresp == 'son':
			personname = input("Enter the son you wish to add.\n").upper()
			if personname not in so:
				so.append(personname)
				print("The person was added.")
			else:
				print('He was not added. He already exists.')
		elif addresp == 'daughter':
			personname = input("Enter the daughter you wish to add.\n").upper()
			if personname not in d:
				d.append(personname)
				print("The person was added.")
			else:
				print('She was not added. She already exists.')
		elif addresp != '':
			print("Please choose an appropriate relative type.")
	return f,m,sp,so,d
    def Update(Dictionary, Described, Referenced):
        for key in Dictionary.keys():
            for key2 in Dictionary[key].values():
                if  key2 not in Referenced:
                    Referenced.append()
            if key not in Described:
                Described.append()
    return Described
main()
