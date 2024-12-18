positionDs = input("What position you're applying for? ")
date = input("Date today: ")
yourName = input("Enter your full name: ")
presentAdd = input("Enter your present address: ")
permanentAdd = input("Enter your permanent address: ")
mobileNo = input("Enter your mobile number: ")
homeNo = input("Enter home number: ")
dateBirth = input("Enter your birthday: ")
placeBirth = input("Enter the place of your birth: ")
citizenship = input("Enter your nationality: ")
religion = input("Enter your religion: ")
yAge = input("Enter your age: ")
ySex = input("Enter your sex: ")
civilStat = input("Enter your civil status: ")
yHeight = input("Enter your height: ")
yWeight = input("Enter your weight: ")
spouseN = input("Enter the name of your spouse: ")
occup = input("Enter your occupation: ")
noChild = input("Enter the number of your children: ")
namesAbirth = input("Enter their names and birthday: ")
fatherN = input("Enter the name of your father: ")
fOccup = input("Enter your father's occupation: ")
fAdd = input("Enter the adress of your father: ")
motherN = input("Enter the name of your mother: ")
mOccup = input("Enter your mother's occupation: ")
mAdd = input("Enter the address of your mother: ")
language = input("Enter the langauges or dialects you can speak: ")
pEmergency = input("Who's the person to be contacted in case of emergency? ")
relation = input("What is your relationship with him or her?" )
pAdd= input("His/her address: ")
pTel = input("His/her telephone number: ")
elem = input("Name of your elementary school: ")
deg = input("What degree you received? ")
year = input("What year you graduated? ")
highscl = input("Name of your high school: ")
dEg = input("What degree you received? ")
yEar = input("What year you graduated? ")
collg = input("Name of your college school: ")
deG = input("What degree you received? ")
yeAr = input("What year you graduated? ")
Voc = input("Name of your vocational school: ")
degr = input("What degree you received? ")
yeaR = input("What year you graduated? ")
spSkills = input("Enter your skills: ")
companyN = input("Enter the company name: ")
yOCCU = input("Your occupation in that company: ")
salary = input("Your salary range: ")
Cname = input("Enter the name of your character reference: ")
Coccu = input("What is her/his occupation? ")
Cadd = input("What is her/his address? ")
Ctel = input("His/her telephone number: ")
cName = input("Enter the name of your character reference: ")
cOccu = input("What is her/his occupation? ")
cAdd = input("What is her/his address? ")
cTel = input("His/her telephone number: ")

print ("\033[1m--------------------------------------------------------BIO-DATA-------------------------------------------------------------\033[0m " +
"\n|		    			              \33[4mPERSONAL DATA\33[m	    		    	                            \n" + "| POSITION DESIRED:\33[4m " + positionDs + "\33[m                                                                DATE: \33[4m" + date + "\33[m                      \b\n" +
"| NAME:\33[4m " + yourName + "          \33[m \n" + "| PRESENT ADDRESS:\33[4m " + presentAdd + "\33[m                         MOBILE NO: \33[4m " + mobileNo + "\33[m                     \n" +
"| PERMANENT ADDRESS:\33[4m " + permanentAdd + "\33[m                                 HOME NO:\33[4m " + homeNo + "\33[m                      \n" +
"| DATE OF BIRTH:\33[4m " + dateBirth + "\33[m     " + "PLACE OF BIRTH:\33[4m " + placeBirth + "\33[m     " + "CITIZENSHIP:\33[4m " + citizenship + "\33[m        " + "RELIGION:\33[4m " + religion + "\33[m   \n" + 
"| AGE:\33[4m " + yAge +   "\33[m      " + "SEX:\33[4m " + ySex + "\33[m             " + "CIVIL STATUS:\33[4m "+ civilStat + "\33[m               " + "HEIGHT:\33[4m " + yHeight + "\33[m                " + "WEIGHT:\33[4m " + yWeight + "\33[m   \n" +
"| NAME OF SPOUSE:\33[4m " + spouseN + "\33[m                                                                                " + "OCCUPATION:\33[4m " + occup + "\33[m     \n" + 
"| NO. OF CHILDREN:\33[4m " + noChild + "\33[m                     THEIR NAMES AND DATE OF BIRTH:\33[4m " + namesAbirth + "\33[m                       \n" + 
"| FATHER'S NAME:\33[4m " + fatherN + "\33[m       " + "OCCUPATION:\33[4m " + fOccup + "\33[m          " + "ADDRESS:\33[4m " + fAdd + "\33[m  \n" + 
"| MOTHER'S NAME:\33[4m " + motherN + "\33[m     " + "OCCUPATION:\33[4m " + mOccup + "\33[m      " + "ADDRESS:\33[4m " + mAdd + "\33[m  \n" + 
"| LANGUAGES/DIALECTS YOU CAN SPEAK OR WRITE:\33[4m " + language + "\33[m \n" + 
"| PERSON TO BE NOTIFIED IN CASE OF EMERGENCY:\33[4m " + pEmergency + "\33[m                                      " + "RELATIONSHIP:\33[4m" + relation + "\33[m \n" + 
"| ADDRESS:\33[4m " + pAdd + "\33[m                               " + "TEL NO:\33[4m " + pTel + "\33[m \n" + 
"|=================================================\33[4mEDUCATIONAL BACKGROUND\33[m=======================================================\n" + 
"|               NAME OF SCHOOL                            DEGREE RECEIVED             YEAR GRADUATED\n" +
"| ELEMENTARY:\33[4m " + elem + "\33[m                      \33[4m" + deg + "\33[m                      \33[4m" + year + "\33[m \n" + 
"| HIGH SCHOOL:\33[4m " + highscl + "\33[m               \33[4m" + dEg + "\33[m                 \33[4m" + yEar + "\33[m \n" + 
"| COLLEGE:\33[4m " + collg + "\33[m                     \33[4m" + deG + "\33[m                        \33[4m" + yeAr + "\33[m \n" + 
"| VOCATIONAL:\33[4m " + Voc + "\33[m                                               \33[4m" + degr + "\33[m                        \33[4m" + yeaR + "\33[m \n" + 
"| SPECIAL SKILLS:\33[4m " + spSkills + "\33[m \n" + 
"|===================================================\33[4mEMPLOYMENT HISTORY\33[m=========================================================\n" + 
"|      NAME OF THE COMPANY                    OCCUPATION                 SALARY \n" + 
"|             \33[4m" + companyN + "\33[m                                " + "\33[4m" + yOCCU + "\33[m                      " + "\33[4m"+ salary + "\33[m \n" + 
"| -------------------------             " + "---------------------          " + "-------------\n" + 
"| -------------------------             " + "---------------------          " + "-------------\n" + 
"|==================================================\33[4mCHARACTER REFERENCES\33[m========================================================\n" + 
"|           NAME                  OCCUPATION                        ADDRESS                                         TEL NO.\n" + ""
"|    " + "\33[4m " + Cname + "\33[m              \33[4m" + Coccu + "\33[m       \33[4m" + Cadd + "\33[m    " + "\33[4m " + Ctel + "\33[m \n" +
"|    " + "\33[4m " + cName + "\33[m              \33[4m" + cOccu + "\33[m       \33[4m" + cAdd + "\33[m    " + "\33[4m " + cTel + "\33[m \n") 
