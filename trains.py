def init():
    trainno=0
    no_ofac1stclass=0
    no_ofac2ndclass=0
    no_ofac3rdclass=0
    no_ofsleeper=0
    totalseats=0
    trainname=''
    startingpt=''
    destination=''
def getinput():
    print("="*80)
    print("\t\t\t ENTER THE TRAIN DETAILS")
    print('')
    trainname=input("ENTER THE TRAIN NAME:").upper()
    print('')
    no_ofac1stclass=int(input("ENTER NO_OF AC FIRST CLASS SEATS TO BE RESERVED:"))
    print('')
    no_of2ndclass=int(input("ENTER NO_OF AC SECOND CLASS SEATS TO BE RESERVED:"))
    print('')
    no_ofac3rdclass=int(input("ENTER NO_OF AC THIRD CLASS SEATS TO BE RESERVED:"))
    print('')
    no_ofsleeper=int(input("ENTER NO_OF SLEEPER CLASS SEATS TO BE RESERVED:"))
    print('')
    startingpt=input("ENTER THE STARTING POINT:")
    print('')
    destination=input("ENTER THE DESTINATION POINT")
    os.system('cls')
def output():
    print("="*80)
    print('')
    print("THE ENTERED TRAINNAME IS:",trainname)
    print("THE ENTERED TRAIN NUMBER IS:",trainno)
    print("STARTING POINT ENTERED IS:",startingpt)
    print("DESTINATION POINT ENTERED IS:",destination)
    print("NO_OF AC FIRST CLASS SEATS RESERVED ARE:",no_ofac1stclass)
    print("NO_OF AC SECOND CLASS SEATS RESERVED ARE:",no_ofac2ndclass)
    print("NO_OF AC THIRD CLASS SEATS RESERVED ARE:",no_ofac3rdstclass)
    print("NO_OF SLEEPER CLASS SEATS RESERVED ARE:",no_ofsleeper)
    print('')
    print("="*80)
def gettrainname():
    return trainname
def gettrainno():
    return trainno
def getno_ofac1stclass():
    return getno_ofac1stclass
def getno_ofac2ndclass():
    return getno_ofac2ndclass
def getno_ofac3rdclass():
    return getno_ofac3rdclass
def getno_ofsleeper():
    return no_ofsleeper
def getstartinpt():
    return startingpt
def getdestination():
    return destination

    
