from pickle import load,dump
import time
import random
import os
import tickets
import train

def menu():
    tr=train() tick=tickets() print
    print ("WELCOME TO DIVESH AGENCY".center(80))
    while True:
        print("")
        print("=”*80)
        print(" \t\t\t\t RAILWAY”)
        print("")
        print("=*80")
        print("\t\t\t1. * *UPDATE TRAIN DETAILS.")
        print("")
        print("\t\t\t2. TRAIN DETAILS. ")
        print("")
        print("\t\t\t3. RESERVATION OF TICKETS.")
        print("")
        print("\t\t\t4. CANCELLATION OF TICKETS. ")
        print("")
        print("\t\t\t5. DISPLAY PNR STATUS.")
        print("")
        print("\t\t\t6. QUIT.")
        print("* * - office use.	")
        ch=int(input("\t\t\t ENTER YOUR CHOICE : ")) os.system('cls')
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t  LOADING. .",time.sleep(1))
        print(".",time.sleep(0 5))
        print(".",time.sleep(2))
        os.system('cls')

        if ch==1:
              j = "password"
              r = input("\n\n\n\n\n\n\n\n\n\n\n\t\t\t\tENTER THE PASSWORD:")
              os.system('cls')

              if (j==r):
              x = 'y'
              while(x.lower()=='y'):
                  fout = open("trdetails.dat","ab")
                  tr.getinput()
                  dump(tr.fout)
                  fout.close()
                  print("\n\n\n\n\n\n\n\n\n\n\n\t\t\t UPDATING TRAIN LIST PLEASE WAIT . .",time.sleep( 1))
                  print(("."),time.sleep(0.5))
                  print(("."),time.sleep(2)) os.system('cls')
                  print("\n\n\n\n\n\n\n\n\n\n\n")
                  x=input(”\t\t DO YOU  WANT TO ADD ANY MORE TRAINS DETAILS ? ")
                  os.system('cls')
                continue
            elif(j !=r):
                print("\n\n\n\n\n")
                print("WRONG PASSWORD".center(80))

     elif ch==2:
         fin = open("trdetails.dat",'rb')
         if not fin:
             print("ERROR")
         else:
             try:
                 while True:
                     print("*"*80)
                     print("\t\t\t\tTRAIN DETAILS")
                     print("*"*80)
                     print("")
                     tr = load(fin)
                     tr.output()
                     input("PRESS ENTER TO VIEW NEXT TRAIN DETAILS”)
                     os.system('cls')
            except:
                pass

    elif ch==3:
        print('='*80)
        print("\t\t\t\tRESERVATION OF TICKETS")
        print('='*80)
        print("")
        tick.reservation()

    elif ch==4:
        print("="*80)
        print("\t\t\t\tCANCELLATION OF TICKETS")
        print("")
        print("="*80)
        print("")
        tick.cancellation()
    

        

                  
        
