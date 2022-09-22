def __init__():
    no_ofac1stclass=0
    totaf=0
    no_ofac2ndclass=0
    no_ofac3rdclass=0
    no_ofsleeper=0
    no_oftickets=0
    name=''
    age=''
    resno=0
    status=''
def ret():
    return resno
def retname():
    return name
def display():
    f=0
    fin1=open("Tickets.dat", 'rb')
    if not fin1:
        print("ERROR")
    else:
        print('')
        n=int(input("Enter PNR Number:"))
        print("\n\n")
        print("Fetching data...", center(80))
        time.sleep(1)
        os.system('cls')
        try:
            while True:
                tick=load(fin1)
            if(n==tick.ret()):
                f=1
                print("="*80)
                print("PNR Status".center(80))
                print("="*80)
                print('')
                print("Passenger's Name:", tick.name)
                print("")
                print("Passenger's Age:", tick.age)
                print("")
                print("PNR No:", tick.resno)
                print("")
                print("Status:", tick.status)
                print("")
                print("No. of Seats Booked:", tick.no_oftickets)
                print("")
        except:
            pass
            fin1.close()
            if(f==0):
                print("")
                print("Wrong PNR Number")
                print("")
def pending():
    status="WAITING LIST"
    print("PNR Number: ", resno)
    print("")
    time.sleep(1.2)
    print("Status = ", status)
    print("")
    print("No. of Seats Booked: ", no_oftickets)
    print("")
def confirmation():
    status="CONFIRMED"
    print("PNR Number: ", resno)
    print("")
    time.sleep(1.5)
    print("Status = ", status)
    print("")
def cancellation():
    z=0
    f=0
    fin=open("tickets.dat", 'rb')
    fout=pen("temp.dat", 'ab')
    print("")
    r = int(input("Enter PNR No: "))
    try:
        while True:
            tick=load(fin)
            z=tick.ret()
        if(z!=r):
            dump(tick,fout)
        elif(z==r):
            f=1
        else:
            pass
    except:
        pass
    fin.close()
    fout.close()
    os.remove("tickets.dat")
    os.rename("temp.dat", "tickets.dat")
    if (f==0):
        print("")
        print("NO SUCH RESERVATION NUMBER FOUND")
        print("")
        time.sleep(2)
        os.system('cls')
    else:
        print("")
        print("TICKET CANCELLED")
        print("")
def reservation():
    trainno=int(input("Enter the Train No: "))
    z=0
    f=0
    fin2=open("trdetails.dat", 'rb+')
    fin2.seek(0)
    if not fin2:
        print("ERROR")
    else:
        try:
            while True:
                tr = load(fin2)
                z=tr.gettrainno()
                n=tr.gettrainname()
                if (trainno==z):
                    print("")
                    print("Train Name: ", n)
                    f=1
                    print("")
                    print("-"*80)
                    no_ofac1st=tr.getno_ofac1stclass()
                    no_ofac2nd=tr.getno_ofac2ndclass()
                    no_ofac3rd=tr.getno_ofac3rdclass()
                    no_ofsleeper=tr.getno_ofsleeper()
                    if (f==1):
                        fout=opem("tickets.dat", "ab")
                        print("")
                        name = input("Enter Passenger's Name: ")
                        print("")
                        age = int(input("Enter Passenger's Age: "))
                        print("")
                        print("\t\t Select a class you would like to travel in:")
                        print("1. AC FIRST CLASS")
                        print("")
                        print("2. AC SECOND CLASS")
                        print("")
                        print("3. AC THIRD CLASS")
                        print("")
                        print("4. SLEEPER CLASS")
                        print("")
                        c= int(input("\t\t Enter your choice: "))
                        os.system('cls')
                        amt1=0
                        if(c==1):
                            no_oftickets = int(input("Enter number of AC FIRST CLASS seats to be booked:"))
                            i = 1
                            while i<=no_oftickets:
                                totaf=totaf+1
                                amt1=1000*no_oftickets
                                i=i+1
                                print("")
                                print("PROCESSING...", time. sleep(0.5))
                                print(".", time.sleep(0.3))
                                print(".", time.sleep(2))
                                os.system('cls')
                                print("Total Amount to be Paid: ", amt1)
                                resno=random.ranint(1000,2546)
                                x=no_ofac3rd-totaf
                                print("")
                                if(x>0):
                                    confirmation()
                                    dump(fout1)
                                    break
                                else:
                                    pending()
                                    dump(tick,fout1)
                                    break
                        elif(c==2):
                            no_oftickets = int(input("Enter number of AC SECOND CLASS seats to be booked:"))
                            i=1
                            while (i<=no_oftickets):
                                totaf=totaf+1
                                amt1=900*no_oftickets
                                i=i+1
                                print("")
                                print("PROCESSING...", time.sleep(0.5))
                                print(".", time.sleep(0.3))
                                print(".". time.sleep(2))
                                os.system('cls')
                                print("Total Amount to be Paid: ", amt1)
                                resno = random.randint(1000,2456)
                                x=no_ofac2nd-totaf
                                print("")
                                if(x>0):
                                    confirmation()
                                    dump(fout1)
                                    break
                                else:
                                    pending()
                                    dump(tick, fout1)
                                    break
                        elif(c==3):
                            no_oftickets = int(input("Enter number of AC THIRD CLASS seats to be booked:"))
                            i=1
                            while (i<=no_oftickets):
                                totaf=totaf+1
                                amt1=800*no_oftickets
                                i=i+1
                                print("")
                                print("PROCESSING...", time.sleep(0.5))
                                print(".", time.sleep(0.3))
                                print(".". time.sleep(2))
                                print(".")
                                time.sleep(2)
                                os.system('cls')
                                print("Total Amount to be Paid: ", amt1)
                                resno = random.randint(1000,2456)
                                x=no_ofac3rd-totaf
                                print("")
                                if(x>0):
                                    confirmation()
                                    dump(fout1)
                                    break
                                else:
                                    pending()
                                    dump(tick, fout1)
                                    break
                        elif(c==4):
                            no_oftickets = int(input("Enter number of SLEEPER CLASS seats to be booked:"))
                            i=1
                            while (i<=no_oftickets):
                                totaf=totaf+1
                                amt1=550*no_oftickets
                                i=i+1
                                print("")
                                print("PROCESSING...", time.sleep(0.5))
                                print(".", time.sleep(0.3))
                                print(".". time.sleep(2))
                                print(".")
                                time.sleep(2)
                                os.system('cls')
                                print("Total Amount to be Paid: ", amt1)
                                resno = random.randint(1000,2456)
                                x=no_ofac3rd-totaf
                                print("")
                                if(x>0):
                                    confirmation()
                                    dump(fout1)
                                    break
                                else:
                                    pending()
                                    dump(tick, fout1)
                                    break
        except:
            pass
        if(f==0):
            time.sleep(2)
            print("\n\n\n\n\n\n\t\t\t\t No such train found")
            time.sleep(2)
            print("")
            print("")
            print("")
        
