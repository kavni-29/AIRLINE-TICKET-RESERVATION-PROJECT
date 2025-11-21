import csv
import datetime
from tabulate import tabulate

#CHECK FLIGHTS
def chkflights():
    names=[]
    fr=open('AIRCRAFT.CSV')
    data=list(csv.reader(fr))
    for rec in data:
        if rec[0].isalpha()==False:
            names+=[rec[0]]
    fr.close()

    for name in names:
        alist=[]
        fr=open(f'{name}.csv','r')
        cr=csv.reader(fr)
        for rec in cr:
            alist.append(rec)
        print(tabulate(alist,headers="firstrow",tablefmt="simple_grid"))
        fr.close()


#ADD A FLIGHT
def addflight():
    #Aircraft name:
    print('AIRCRAFT NAME')
    while True:
        aircraft=input('Input aircraft name: ').upper()
        while not aircraft.isalnum():
            print('Please input a valid name.')
            aircraft=input('Input aircraft name: ').upper()

        names=[]
        fr=open('AIRCRAFT.CSV')
        data=list(csv.reader(fr))
        found=False
        for rec in data:
            if rec[0].isalpha()==False:
                if aircraft==rec[0]:
                    found=True
                    cap=rec[1]
                    break
        fr.close()
        if found==True:break
        else:print('Please input a valid aircraft name.')
        
    
    #Departure Date Details:
    print('DATE OF DEPARTURE')
    #Day:
    day=input('Day[1-31]: ')
    while not day.isdigit():
        print('Please input valid information (only digits).')
        day=input('Day[1-31]: ')
    while not 1<=int(day)<=31:
        print('Please input valid information.')
        day=input('Day[1-31]: ')
    if int(day)==1:day='1'
    if int(day)==2:day='2'
    if int(day)==3:day='3'
    if int(day)==4:day='4'
    if int(day)==5:day='5'
    if int(day)==6:day='6'
    if int(day)==7:day='7'
    if int(day)==8:day='8'
    if int(day)==9:day='9'

    #Month:
    month=input('Month[1-12]: ')
    while not month.isdigit():
        print('Please input valid information (only digits).')
        month=input('Month[1-12]: ')
    while not 1<=int(month)<=12:
        print('Please input valid information.')
        month=input('Month[1-12]: ')
    if int(month)==1:month='Jan'
    elif int(month)==2:month='Feb'
    elif int(month)==3:month='Mar'
    elif int(month)==4:month='Apr'
    elif int(month)==5:month='May'
    elif int(month)==6:month='Jun'
    elif int(month)==7:month='Jul'
    elif int(month)==8:month='Aug'
    elif int(month)==9:month='Sep'
    elif int(month)==10:month='Oct'
    elif int(month)==11:month='Nov'
    else:month='Dec'

    #Year:
    year=input('Year(yy): ')
    while not year.isdigit() and len(year)==2 and int(year)>=23:
        print('Please input valid information (only digits).')
        year=input('Year(yy): ')
    
    #Place of departure:
    print('FROM')
    From=input('Place of departure: ').title()
    while not From.isalpha():
        print('Please input a valid name.')
        From=input('Place of departure: ').title()

    #Place of arrival:
    print('TO')
    To=input('Place of arrival: ').title()
    while not To.isalpha():
        print('Please input a valid name.')
        To=input('Place of arrival: ').title()
    
    #Time of departure:
    print('DEPARTURE TIME')
    hours1=input('Input hours[24-Hour Format]: ')
    while not hours1.isdigit() and len(hours1)==2 and 0<=int(hours1)<24:
        print('Please input valid information.')
        hours1=input('Input hours[24-Hour Format]: ')
    
    mins1=input('Input minutes[24-Hour Format]: ')
    while not mins1.isdigit() and len(hours1)==2 and 0<=int(mins1)<24:
        print('Please input valid information.')
        mins1=input('Input mins[24-Hour Format]: ')
    
    dtime=hours1+':'+mins1

    #Time of arrival:
    print('ARRIVAL TIME')
    hours2=input('Input hours[24-Hour Format]: ')
    while not hours2.isdigit() and len(hours2)==2 and 0<=int(hours2)<24:
        print('Please input valid information.')
        hours2=input('Input hours[24-Hour Format]: ')
    
    mins2=input('Input minutes[24-Hour Format]: ')
    while not mins2.isdigit() and len(hours2)==2 and 0<=int(mins2)<24:
        print('Please input valid information.')
        mins2=input('Input mins[24-Hour Format]: ')
    
    atime=hours2+':'+mins2

    #Economy Class Seats:
    se='0'
    #Business Class Seats:
    sb='0'
    #First Class Seats:
    sf='0'

    print('SEAT PRICES')
    while True:
        #Economy Class Seat Prize:
        amte=input('Economy Class seat price: ')
        while not amte.isdigit():
            print('Please input valid information.')
            amte=input('Economy Class seat price: ')

        #Business Class Seat Price:
        amtb=input('Business Class seat price: ')
        while not amtb.isdigit():
            print('Please input valid information.')
            amtb=input('Business Class seat price: ')

        #First Class Seat Prize:
        amtf=input('First Class seat price: ')
        while not amtf.isdigit():
            print('Please input valid information.')
            amtf=input('First Class seat price: ')
             
        if int(amte)<int(amtb)<int(amtf):
            break
        else:print('Please input valid price details.')
    
    #Flight number:
    print('FLIGHT NUMBER')
    file=open(f'{aircraft}.csv','r')
    data=list(csv.reader(file))
    lastrec=data[-1]           #accessing the last record of the flight file
    reffno=lastrec[0]          #accessing the flight number of the last record
    refval=reffno[2::]         #storing only the numerical part of the flight number in another variable 
    file.close

    num=int(refval)+1
    Fl_No='KR'+str(num)
    print(Fl_No)
    #Final details of the record in a list:
    rec=[Fl_No,aircraft,day,month,year,From,To,dtime,atime,se,sb,sf,amte,amtb,amtf,'000A','000B','000C','000D','000E','000F','000G','000H','000I','000J','000K']

    fa=open(f'{aircraft}.csv','a',newline="")
    ca=csv.writer(fa)
    ca.writerow(rec)
    print('The flight details have been successfully added.')
    fa.close()


#DELETE A FLIGHT
def delflight():
    print('FLIGHT NUMBER')
    #Flight Number:
    Fl_No=input('Please input the flight number: ').upper()
    while not Fl_No.isalnum():
        print('Please input a valid flight number.')
        Fl_No=input('Please input the flight number ').upper()

    names=[]
    fr=open('AIRCRAFT.CSV')
    data=list(csv.reader(fr))
    for rec in data:
        if rec[0].isalpha()==False:
            names+=[rec[0]]
    fr.close()

    alist=[]
    for name in names:
        fr=open(f'{name}.csv','r')
        cr=csv.reader(fr)
        for rec in cr:
            alist.append(rec)
        fr.close()
    
    found=False
    for rec in alist:
        if rec[0]==Fl_No:
            found=True
            delrec=rec          #Record to be deleted
            delname=rec[1]      #Aircraft name (to open the corresponding file.)
            break
    if found==False:print('Flight not found.')
    else:
        fr=open(f'{delname}.csv','r')
        cr=list(csv.reader(fr))
        cr.remove(delrec)
        fr.close()
        fw=open(f'{delname}.csv','w',newline="")
        cw=csv.writer(fw)
        cw.writerows(cr)
        fw.close()
        print('Flight deleted.')

        file=open('PASSENGER DETAILS.CSV','r')
        data=list(csv.reader(file))
        found=False
        for rec in data:
            if rec[0]==Fl_No:
                found=True
                data.remove(rec)
        file.close()
        fw=open('PASSENGER DETAILS.CSV','w',newline="")
        cw=csv.writer(fw)
        cw.writerows(data)
        fw.close()
        if found==True:print('Corresponding passenger details have been successfully deleted.')
        else:print('No deletion of passenger details occurred (No passengers have booked the flight yet.).')


#CHECK PASSENGER DETAILS
def chkpassengers():
    while True:
        print('1. Filter by Flight Number.')
        print('2. Filter by PNR.')
        print('3. Filter by Name.')
        ch=input('Input choice[1-3]: ')
        if ch=='1':
            fr=open('PASSENGER DETAILS.CSV')
            data=csv.reader(fr)
            
            #Flight number:
            fno=input('Flight Number: ').upper()
            alist=[]
            found=False
            while not fno.isalnum():
                print('Please input valid information.')
                fno=input('Flight Number: ').upper()
                
            for rec in data:
                if rec[0]==fno:
                    alist.append(rec)
                    found=True
            if found==True:
                print('PASSENGER DETAILS')
                print(tabulate(alist,headers=['Fl_No','PNR','SEAT','DEPARTURE','ARRIVAL','NAME','AGE','SEX','ADDRESS','PHONE','AMT','CLASS'],tablefmt="simple_grid"))
            else:print('Record(s) not found.')
            break

        elif ch=='2':
            fr=open('PASSENGER DETAILS.CSV')
            data=csv.reader(fr)
            
            #PNR:
            pnr=input('PNR: ')
            alist=[]
            found=False
            while not pnr.isdigit():
                print('Please input valid information.')
                pnr=input('PNR: ')
                
            for rec in data:
                if rec[1]==pnr:
                    alist.append(rec)
                    found=True
            if found==True:
                print('PASSENGER DETAILS')
                print(tabulate(alist,headers=['Fl_No','PNR','SEAT','DEPARTURE','ARRIVAL','NAME','AGE','SEX','ADDRESS','PHONE','AMT','CLASS'],tablefmt="simple_grid"))
            else:print('Record(s) not found.')
            break

        elif ch=='3':
            fr=open('PASSENGER DETAILS.CSV')
            data=csv.reader(fr)
            
            #Name:
            name=input('Name: ').upper()
            alist=[]
            found=False
            while not name.isalpha():
                print('Please input valid information.')
                name=input('Name: ').upper()
                
            for rec in data:
                if rec[5]==name:
                    alist.append(rec)
                    found=True
            if found==True:
                print('PASSENGER DETAILS')
                print(tabulate(alist,headers=['Fl_No','PNR','SEAT','DEPARTURE','ARRIVAL','NAME','AGE','SEX','ADDRESS','PHONE','AMT','CLASS'],tablefmt="simple_grid"))
            else:print('Record(s) not found.')
            break
                
        else:print('Please input a valid choice.')




#CHECK SCHEDULE
def schedule():
    print('CHECK FLIGHT SCHEDULE')

    #Place of departure:
    From=input('Enter an origin: ').title()
    while not From.isalpha():
        print('Please input a valid name.')
        From=input('Enter an origin: ').title()
    
    #Place of arrival:
    To=input('Enter a destination: ').title()
    while not To.isalpha():
        print('Please input a valid name.')
        To=input('Enter a destination: ').title()

    names=[]
    fr=open('AIRCRAFT.CSV')
    data=list(csv.reader(fr))
    for rec in data:
        if rec[0].isalpha()==False:
            names+=[rec[0]]
    fr.close()

    alist=[]
    for name in names:
        fr=open(f'{name}.csv','r')
        cr=csv.reader(fr)
        for rec in cr:
            if rec[5]==From and rec[6]==To:
                alist.append(rec)

        fr.close()
    if alist!=[]:print(tabulate(alist,headers=['Fl_No','AIRCRAFT','DAY','MONTH','YEAR','FROM','TO','DEPARTURE','ARRIVAL','SEATS(E)','SEATS(B)','SEATS(F)','AMT(E)','AMT(B)','AMT(F)','A','B','C','D','E','F','G','H','I','J','K'],tablefmt="simple_grid"))
    else:print('No flights available.')


#ADD A PASSENGER
def addpassenger():
    aircrafts=[]
    fr=open('AIRCRAFT.CSV')
    data=list(csv.reader(fr))
    for rec in data:
        if rec[0].isalpha()==False:
            aircrafts.append(rec[0])
    fr.close()

    
    #flight number:
    while True:
        Fl_No=input('Please input the flight number: ').upper()
        while not Fl_No.isalnum():
            print('Please input a valid flight number.')
            Fl_No=input('Please input the flight number ').upper()
        for name in aircrafts:
            c=0
            fr=open(f'{name}.csv','r')
            cr=csv.reader(fr)
            found=False
            for rec in cr:
                if rec[0]==Fl_No:
                    selection=rec
                    found=True
                    c+=1
                    break
            if found==True:break
        if c>0:break
        else:print('Please input valid flight number.')

    print(selection)
    aircraft=selection[1]

    fr=open('AIRCRAFT.CSV')
    data=list(csv.reader(fr))
    for rec in data:
        if rec[0]==aircraft:
            cap=rec[1]
            eco=rec[2]
            bus=rec[3]
            fc=rec[4]
    
    fr.close()

    #PNR:
    fr=open('PASSENGER DETAILS.CSV')
    data=list(csv.reader(fr))
    lastrec=data[-1]
    fr.close()
    ref=lastrec[1]
    if ref.isdigit()==False:
        pnr=10000+len(data)+1
    else:pnr=int(ref)+1
    print(pnr)

    #Place of departure:
    dep=selection[5]

    #Place of arrival:
    arr=selection[6]

    #Name:
    while True:
        name=input('Name: ').upper()
        blist=name.split()          #list of first, middle and last name
        check=''
        for ele in blist:
            check+=ele
        while not check.isalpha():
            print('Please input a valid name.')
            name=input('Name: ').upper()
            blist=name.split()          #list of first, middle and last name
            check=''
            for ele in blist:
                check+=ele
        break
    #Age:
    age=input('Age: ')
    while not age.isdigit():
        print('Please input valid information.')
        age=input('Age: ')
    while not int(age)>17:
        print('Please input valid information.')
        age=input('Age: ')
    
    #Sex:
    while True:
        print('1. Male(M)')
        print('2. Female(F)')
        print('3. Other(O)')
        ch=input('Choice[1-3]: ')
        if ch=='1':
            sex='M'
            break
        elif ch=='2':
            sex='F'
            break
        elif ch=='3':
            sex='O'
            break
        else:print('Please input a valid choice.')
                      

    
    #Address:
    address=input('Input address: ')
    
    #Phone Number:
    phone=input('Phone number: ')
    b=phone
    if phone[0]=='+':b=phone[1::]
    while not b.isdigit():
        print('Please input a valid phone number')
    
    #Class:
    while True:
        print('CLASS')
        print('1. Economy(E)')
        print('2. Business(B)')
        print('3. First Class(F)')
        ch=input('Choice[1-3]: ')
        if ch=='1':
            ch='E'
            break
        if ch=='2':
            ch='B'
            break
        if ch=='3':
            ch='F'
            break
        else:print('Please input valid Class.')
    #Seat:
    while True:
        print('CHOOSE SEAT')
        print('CHOOSE ROW')
        print('AVAILABLE ROWS:')
        if ch=='F':
            rowlist=['A','B','C',]
            print('A','B','C',sep='\t')
        if ch=='B':
            rowlist=['D','E','F']
            print('D','E','F',sep='\t')
        if ch=='E':
            rowlist=['G','H','I','J','K']
            print('G','H','I','J','K',sep='\t')
        choice=input('Input selected row:')
        while choice:
            while len(choice)!=1 or choice.isalpha()==False:
                print('Please input a valid choice.')
                choice=input('Input selected row:')
            choice=choice.upper()
            while choice not in rowlist:
                print('Please input a valid choice.')
                choice=input('Input selected row:')
            break
        
        print('CHOOSE SEAT NUMBER:')
        numlist=['1','2','3']
        print('SEATS:','1','2','3',sep='\t')
        st=input('Input selected seat:')
        while st not in numlist:
            print('Please input a valid seat number.')
            st=input('Input selected seat:')

        aircraft=selection[1]
        fr=open(f'{aircraft}.csv','r')
        cr=list(csv.reader(fr))
        fr.close()
        available=False
        for rec in cr:
            if rec[0]==Fl_No:
                rows=[list(rec[15]),list(rec[16]),list(rec[17]),list(rec[18]),list(rec[19]),list(rec[20]),list(rec[21]),list(rec[22]),list(rec[23]),list(rec[24]),list(rec[25])]
                if ch=='F':
                    if choice=='A':row=rows[0]
                    elif choice=='B':row=rows[1]
                    else:row=rows[2]
                elif ch=='B':
                    if choice=='D':row=rows[3]
                    elif choice=='E':row=rows[4]
                    else:row=rows[5]
                else:
                    if choice=='G':row=rows[6]
                    elif choice=='H':row=rows[7]
                    elif choice=='I':row=rows[8]
                    elif choice=='J':row=rows[9]
                    else:row=rows[10]
        
        if st=='1':c=row[0]
        elif st=='2':c=row[1]
        else:c=row[2]

        if c=='0':available=True

        if available==True:
            print('The chosen seat is available.')
            seat=choice+st
            data=[]
            for rec in cr:
                if rec[0]==Fl_No:
                    newrec=[]
                    for ele in rec:
                        ref=list(ele)
                        c=row==ref
                        if c==True:
                            print(ele)
                            if st=='1':row[0]='1'
                            elif st=='2':row[1]='1'
                            else:row[2]='1'
                            ele=row[0]+row[1]+row[2]+row[3]
                        newrec.append(ele)
                    rec=newrec
                data.append(rec)               
            break

        else:print("Seat not available. Please choose another seat.")
    fw=open(f'{aircraft}.csv','w',newline="")
    cw=csv.writer(fw)
    cw.writerows(data)
    fw.close()

    #Amount:
    aircraft=selection[1]
    fr=open(f'{aircraft}.csv','r')
    cr=list(csv.reader(fr))
    amount=0
    for rec in cr:
        if rec[0]==Fl_No:
            if ch=='E':amount=rec[12]
            elif ch=='B':amount=rec[13]
            else:amount=rec[14]
    details=[Fl_No,pnr,seat,dep,arr,name,age,sex,address,phone,amount,ch]
    fr.close()
    
    
    print(selection)
    #Updating the corresponding aircraft file and passenger details
    file=open(f'{aircraft}.csv','r')
    data=list(csv.reader(file))
    file.close()
    for rec in data:
        c=False                                        #Flag variable for reference
        if rec[1]==selection[1]:
            if int(rec[9])+int(rec[10])+int(rec[11])<int(cap):
                c=True
                if ch=='E' and int(rec[9])<int(eco):rec[9]=str(int(rec[9])+1)
                if ch=='B' and int(rec[10])<int(bus):rec[10]=str(int(rec[10])+1)
                if ch=='F' and int(rec[11])<int(fc):rec[11]=str(int(rec[11])+1)
                fa=open('PASSENGER DETAILS.CSV','a',newline="")
                ca=csv.writer(fa)
                ca.writerow(details)
                print('The passenger details have been successfully added.')
                fa.close()
                break
    if c==True:
        fw=open(f'{aircraft}.csv','w',newline="")
        cw=csv.writer(fw)
        cw.writerows(data)
        fw.close()
        print('The corresponding flight details have been successfully updated.')
    else:print('No seat available.')


    


m=datetime.datetime.now()                         #global variable for storing the date and time of booking
#BOOK A TICKET
def bookticket():
    print('BOOK A TICKET')
    while True:
        print('1. BOOK A RESERVED TICKET.')
        print('2. BOOK A TICKET.')
        print('0. EXIT.')

        book=input('Input choice[1-2]: ')
        if book=='0':break
        elif book=='1':
            bookreserve()
            getticket()
        elif book=='2':
            #Place of departure:
            From=input('Place of departure: ').title()
            while not From.isalpha():
                print('Please input a valid name.')
                From=input('Place of departure: ').title()

            #Place of arrival:
            while True:
                To=input('Place of arrival: ').title()
                blist=To.split()
                for ele in blist:
                    c=0
                    while not ele.isalpha():
                        c+=1
                if c>0:
                    print('Please input a valid name.')
                else:break
                
            #Date:
            print('Date of Departure')
            
            while True:
                #Day:
                day=input('Day[1-31]: ')
                while not day.isdigit():
                    print('Please input valid information (only digits).')
                    day=input('Day[1-31]: ')
                while not 1<=int(day)<=31:
                    print('Please input valid information.')
                    day=input('Day[1-31]: ')
                if int(day)==1:day='1'
                if int(day)==2:day='2'
                if int(day)==3:day='3'
                if int(day)==4:day='4'
                if int(day)==5:day='5'
                if int(day)==6:day='6'
                if int(day)==7:day='7'
                if int(day)==8:day='8'
                if int(day)==9:day='9'
                #Month:
                month=input('Month[1-12]: ')
                while not month.isdigit():
                    print('Please input valid information (only digits).')
                    month=input('Month[1-12]: ')
                while not 1<=int(month)<=12:
                    print('Please input valid information.')
                    month=input('Month[1-12]: ')
                if int(month)==1:month='Jan'
                elif int(month)==2:month='Feb'
                elif int(month)==3:month='Mar'
                elif int(month)==4:month='Apr'
                elif int(month)==5:month='May'
                elif int(month)==6:month='Jun'
                elif int(month)==7:month='Jul'
                elif int(month)==8:month='Aug'
                elif int(month)==9:month='Sep'
                elif int(month)==10:month='Oct'
                elif int(month)==11:month='Nov'
                else:month='Dec'

                #Year:
                year=input('Year(yy): ')
                while not year.isdigit() and len(year)==2 and int(year)>=23:
                    print('Please input valid information (only digits).')
                    year=input('Year(yy): ')
                
                date=[day,month,year]
                break
            
            #Displaying flights available(if any):
            aircrafts=[]
            fr=open('AIRCRAFT.CSV')
            data=list(csv.reader(fr))
            for rec in data:
                if rec[0].isalpha()==False:
                    aircrafts.append(rec[0])
            fr.close()

            alist=[]
            for name in aircrafts:
                fr=open(f'{name}.csv','r')
                cr=list(csv.reader(fr))
                for rec in cr:
                    if rec[5]==From and rec[6]==To:alist.append(rec)
            if alist==[]:print('No flights available.')
            else:print(tabulate(alist,headers=['Fl_No','AIRCRAFT','DAY','MONTH','YEAR','FROM','TO','DEPARTURE','ARRIVAL','SEATS(E)','SEATS(B)','SEATS(F)','AMT(E)','AMT(B)','AMT(F)','A','B','C','D','E','F','G','H','I','J','K'],tablefmt="simple_grid"))

            while True:
                print('BOOK A TICKET?')
                print('1. YES')
                print('2. NO')
                ch=input('Choice[1-2]: ')
                if ch=='1':
                    #DATE AND TIME OF BOOKING THE TICKET:
                    global m
                    n=datetime.datetime.now()
                    m=n
                    addpassenger()
                    getticket()
                    break
                elif ch=='2':break
                else:print('Please input valid choice (digits only).')

        else:print('Please input a valid choice.')


print(m.strftime("%d/%m/%y %H:%M:%S"))

def getticket():
    print('GET TICKET')
    pnr=input('Please input the PNR: ')
    while not pnr.isdigit():
        print('Please input valid information.')
        pnr=input('Please input the PNR')
    file=open('PASSENGER DETAILS.CSV','r')
    data=list(csv.reader(file))
    found=False
    for rec in data:
        if rec[1]==pnr:
            found=True
            Fl_No=rec[0]
            seat=rec[2]
            From=rec[3]
            To=rec[4]
            name=rec[5]
            amt=rec[-2]
            cl=rec[11]
            tno='TN'+pnr
            aircrafts=[]
            fr=open('AIRCRAFT.CSV')
            data=list(csv.reader(fr))
            for rec in data:
                if rec[0].isalpha()==False:
                    aircrafts+=[rec[0]]
            fr.close()
            print(aircrafts)
            c=False                               #Flag variable for reference
            for aircraft in aircrafts:
                fr=open(f'{aircraft}.csv','r')
                cr=csv.reader(fr)
                for rec in cr:
                    if rec[0]==Fl_No:
                        deptime=rec[7]
                        arrtime=rec[8]
                        date=rec[2]+'-'+rec[3]+'-'+rec[4]


    #Printing the ticket:
    if found==True:
        print('-'*100)
        global m
        print('Booked on ',m.strftime("%d/%m/%y %H:%M:%S"))
        print('Fly Air Airlines')
        print('PASSENGER TICKET')
        finalticket=[[f"Ticket no.: {tno}",f"Flight no.: {Fl_No}"],[f"Seat: {seat}",f"Name: {name}"],[f"Date: {date}", 'Status: Confirmed'],[f"From: {From}",f"To: {To}"],[f"Departure: {deptime}",f"Arrival: {arrtime}"],[f"Class: {cl}",f"Fare: {amt}"]]
        print(tabulate(finalticket))
        print('-'*100)
    else:print('Passenger details not found. Please recheck the data inputted.')


#CANCEL FLIGHT BY USER
maindata=[]                     #Creating a global variable for reference
def cancelflight():
    print('CANCEL YOUR FLIGHT')
    pnr=input('Please input your pnr number: ')
    while not pnr.isdigit():
        print('Please input a valid pnr number.')
        pnr=input('Please input your pnr number: ')
    
    file=open('PASSENGER DETAILS.CSV','r')
    data=list(csv.reader(file))
    file.close()
    found=False
    for rec in data:
        if rec[1]==pnr:
            Fl_No=rec[0]
            cl=rec[-1]
            seat=rec[2]
            seatlist=list(seat)
            rowseat=seatlist[0]
            numseat=seatlist[1]
            data.remove(rec)
            found=True
    if found==True:
        fw=open('PASSENGER DETAILS.CSV','w',newline="")
        cw=csv.writer(fw)
        cw.writerows(data)
        fw.close()
        print('Passenger details have been updated successfully.')

        names=[]
        fr=open('AIRCRAFT.CSV')
        data=list(csv.reader(fr))
        for rec in data:
            if rec[0].isalpha()==False:
                names+=[rec[0]]
        fr.close()
        print(names)
        b=False                               #Flag variable for reference
        for name in names:
            fr=open(f'{name}.csv','r')
            cr=list(csv.reader(fr))
            for rec in cr:
                if rec[0]==Fl_No:
                    b=True
                    aircraft=name
                    chosendata=cr
                    if cl=='E':
                        rec[9]=str(int(rec[9])-1)
                    elif cl=='B':
                        rec[10]=str(int(rec[10])-1)
                    elif cl=='F':
                        rec[11]=str(int(rec[11])-1)
                    rows=[list(rec[15]),list(rec[16]),list(rec[17]),list(rec[18]),list(rec[19]),list(rec[20]),list(rec[21]),list(rec[22]),list(rec[23]),list(rec[24]),list(rec[25])]
                    if cl=='F':
                        if rowseat=='A':row=rows[0]
                        elif rowseat=='B':row=rows[1]
                        else:row=rows[2]
                    elif cl=='B':
                        if rowseat=='D':row=rows[3]
                        elif rowseat=='E':row=rows[4]
                        else:row=rows[5]
                    else:
                        if rowseat=='G':row=rows[6]
                        elif rowseat=='H':row=rows[7]
                        elif rowseat=='I':row=rows[8]
                        elif rowseat=='J':row=rows[9]
                        else:row=rows[10]
                    break   
            fr.close()
        if numseat=='1':c=row[0]
        elif numseat=='2':c=row[1]
        else:numseat=row[2]
        available=False
        if c=='1':available=True       
        if available==True:
            finaldata=[]
            print(Fl_No)
            for rec in chosendata:
                if rec[0]==Fl_No:
                    newrec=[]
                    for ele in rec:
                        ref=list(ele)
                        c=row==ref
                        if c==True:
                            if numseat=='1':row[0]='0'
                            elif numseat=='2':row[1]='0'
                            else:row[2]='0'
                            ele=row[0]+row[1]+row[2]+row[3]
                        newrec.append(ele)
                    rec=newrec
                finaldata.append(rec)
        

        fw=open(f'{aircraft}.csv','w',newline="")
        cw=csv.writer(fw)
        cw.writerows(finaldata)
        fw.close()
        print('The corresponding flight details have been successfully updated.')
        print('Flight has been successfully cancelled.') 
    else:print('Record not found.')

#RESERVE A TICKET:
def reserve():
    status='Waiting'
    aircrafts=[]
    fr=open('AIRCRAFT.CSV')
    data=list(csv.reader(fr))
    for rec in data:
        if rec[0].isalpha()==False:
            aircrafts.append(rec[0])
    fr.close()

    
    #flight number:
    while True:
        Fl_No=input('Please input the flight number: ').upper()
        while not Fl_No.isalnum():
            print('Please input a valid flight number.')
            Fl_No=input('Please input the flight number ').upper()
        for name in aircrafts:
            c=0
            fr=open(f'{name}.csv','r')
            cr=csv.reader(fr)
            found=False
            for rec in cr:
                if rec[0]==Fl_No:
                    selection=rec
                    date=rec[2]+'-'+rec[3]+'-'+rec[4]
                    found=True
                    c+=1
                    break
            if found==True:break
        if c>0:break
        else:print('Please input valid flight number.')

    print(selection)
    aircraft=selection[1]

    fr=open('AIRCRAFT.CSV')
    data=list(csv.reader(fr))
    for rec in data:
        if rec[0]==aircraft:
            cap=rec[1]
            eco=rec[2]
            bus=rec[3]
            fc=rec[4]
    
    fr.close()

    #PNR:
    fr=open('PASSENGER DETAILS.CSV')
    data=list(csv.reader(fr))
    lastrec=data[-1]
    fr.close()
    ref=lastrec[1]
    if ref.isdigit()==False:
        pnr=10000+len(data)+1
    else:pnr=int(ref)+1
    print(pnr)

    #Place of departure:
    dep=selection[5]

    #Place of arrival:
    arr=selection[6]

    #Name:
    name=input('Name: ').upper()
    blist=name.split()          #list of first, middle and last name
    check=''
    for ele in blist:
        check+=ele
    while not check.isalpha():
        print('Please input a valid name.')
        name=input('Name: ').upper()
    
    #Age:
    age=input('Age: ')
    while not age.isdigit():
        print('Please input valid information.')
        age=input('Age: ')
    while not int(age)>17:
        print('Please input valid information.')
        age=input('Age: ')
        
    #Phone Number:
    phone=input('Phone number: ')
    b=phone
    if phone[0]=='+':b=phone[1::]
    while not b.isdigit():
        print('Please input a valid phone number')
    #Sex:
    while True:
        print('1. Male(M)')
        print('2. Female(F)')
        print('3. Other(O)')
        ch=input('Choice[1-3]: ')
        if ch=='1':
            sex='M'
            break
        elif ch=='2':
            sex='F'
            break
        elif ch=='3':
            sex='O'
            break
        else:print('Please input a valid choice.')
                      
    #Address:
    address=input('Input address: ')

    #Class:
    while True:
        print('CLASS')
        print('1. Economy(E)')
        print('2. Business(B)')
        print('3. First Class(F)')
        ch=input('Choice[1-3]: ')
        if ch=='1':
            ch='E'
            break
        if ch=='2':
            ch='B'
            break
        if ch=='3':
            ch='F'
            break
        else:print('Please input valid Class.')
    #Seat:
    while True:
        print('CHOOSE SEAT')
        print('CHOOSE ROW')
        print('AVAILABLE ROWS:')
        if ch=='F':
            rowlist=['A','B','C',]
            print('A','B','C',sep='\t')
        if ch=='B':
            rowlist=['D','E','F']
            print('D','E','F',sep='\t')
        if ch=='E':
            rowlist=['G','H','I','J','K']
            print('G','H','I','J','K',sep='\t')
        choice=input('Input selected row:')
        while choice:
            while len(choice)!=1 or choice.isalpha()==False:
                print('Please input a valid choice.')
                choice=input('Input selected row:')
            choice=choice.upper()
            while choice not in rowlist:
                print('Please input a valid choice.')
                choice=input('Input selected row:')
            break
        
        print('CHOOSE SEAT NUMBER:')
        numlist=['1','2','3']
        print('SEATS:','1','2','3',sep='\t')
        st=input('Input selected seat:')
        while st not in numlist:
            print('Please input a valid seat number.')
            st=input('Input selected seat:')

        aircraft=selection[1]
        fr=open(f'{aircraft}.csv','r')
        cr=list(csv.reader(fr))
        fr.close()
        available=False
        for rec in cr:
            if rec[0]==Fl_No:
                rows=[list(rec[15]),list(rec[16]),list(rec[17]),list(rec[18]),list(rec[19]),list(rec[20]),list(rec[21]),list(rec[22]),list(rec[23]),list(rec[24]),list(rec[25])]
                if ch=='F':
                    if choice=='A':row=rows[0]
                    elif choice=='B':row=rows[1]
                    else:row=rows[2]
                elif ch=='B':
                    if choice=='D':row=rows[3]
                    elif choice=='E':row=rows[4]
                    else:row=rows[5]
                else:
                    if choice=='G':row=rows[6]
                    elif choice=='H':row=rows[7]
                    elif choice=='I':row=rows[8]
                    elif choice=='J':row=rows[9]
                    else:row=rows[10]
        
        if st=='1':c=row[0]
        elif st=='2':c=row[1]
        else:c=row[2]

        if c=='0':available=True

        if available==True:
            print('The chosen seat is available.')
            seat=choice+st
            data=[]
            for rec in cr:
                if rec[0]==Fl_No:
                    newrec=[]
                    for ele in rec:
                        ref=list(ele)
                        c=row==ref
                        if c==True:
                            if st=='1':row[0]='R'
                            elif st=='2':row[1]='R'
                            else:row[2]='R'
                            ele=row[0]+row[1]+row[2]+row[3]
                        newrec.append(ele)
                    rec=newrec
                data.append(rec)              
            break

        else:
            if c=='R':
                print('Seat is already reserved.')
            elif c=='1':
                print("Seat not available. Please choose another seat.")

    fw=open(f'{aircraft}.csv','w',newline="")
    cw=csv.writer(fw)
    cw.writerows(data)
    fw.close()
    
    #Amount:
    aircraft=selection[1]
    fr=open(f'{aircraft}.csv','r')
    cr=list(csv.reader(fr))
    amount=0
    for rec in cr:
        if rec[0]==Fl_No:
            if ch=='E':amount=rec[12]
            elif ch=='B':amount=rec[13]
            else:amount=rec[14]   
    
    fr.close()

    details=[Fl_No,pnr,aircraft,date,dep,arr,seat,name,age,phone,ch,amount,status]
    print(details)
    fa=open('RESERVATION.CSV','a',newline="")
    ca=csv.writer(fa)
    ca.writerow(details)
    print('The passenger reservation details have been successfully added.')
    fa.close()

    passengerrec=[Fl_No,pnr,seat,dep,arr,name,age,sex,address,phone,amount,ch]
    file=open('PASSENGER DETAILS.CSV','a',newline="")
    cf=csv.writer(file)
    cf.writerow(passengerrec)
    print('The passenger details have been successfully added.')
    file.close()


def bookreserve():
    status='Confirmed'
    pnr=input('Please input your pnr number: ')
    while not pnr.isdigit():
        print('Please input a valid pnr number.')
        pnr=input('Please input your pnr number: ')
    
    file=open('PASSENGER DETAILS.CSV','r')
    data=list(csv.reader(file))
    file.close()
    found=False
    for rec in data:
        if rec[1]==pnr:
            Fl_No=rec[0]
            cl=rec[-1]
            seat=rec[2]
            seatlist=list(seat)
            rowseat=seatlist[0]
            numseat=seatlist[1]
            reqrow=rec
            found=True

    if found==True:

        file=open('RESERVATION.CSV','r')
        data=list(csv.reader(file))
        file.close()
        c=False
        for rec in data:
            if rec[1]==pnr:
                data.remove(rec)
                c=True
        
        if c==True:
            fw=open('RESERVATION.CSV','w',newline="")
            cw=csv.writer(fw)
            cw.writerows(data)
            fw.close()
            print('Passenger reservation details have been updated successfully.')

            #Updating the corresponding aircraft file details
            names=[]
            fr=open('AIRCRAFT.CSV')
            data=list(csv.reader(fr))
            for rec in data:
                if rec[0].isalpha()==False:
                    names+=[rec[0]]
            fr.close()
            for name in names:
                file=open(f'{name}.csv','r')
                data=list(csv.reader(file))
                file.close()
                for rec in data:
                    if rec[0]==Fl_No:
                        chosendata=data
                        aircraft=name
                        fr=open('AIRCRAFT.CSV')
                        cr=list(csv.reader(fr))
                        for k in cr:
                            if k[0]==aircraft:
                                cap=k[1]
                                eco=k[2]
                                bus=k[3]
                                fc=k[4]
                        fr.close()
                        b=False 
                        if int(rec[9])+int(rec[10])+int(rec[11])<int(cap):
                            b=True
                            if cl=='E' and int(rec[9])<int(eco):rec[9]=str(int(rec[9])+1)
                            elif cl=='B' and int(rec[10])<int(bus):rec[10]=str(int(rec[10])+1)
                            elif cl=='F' and int(rec[11])<int(fc):rec[11]=str(int(rec[11])+1)
                            rows=[list(rec[15]),list(rec[16]),list(rec[17]),list(rec[18]),list(rec[19]),list(rec[20]),list(rec[21]),list(rec[22]),list(rec[23]),list(rec[24]),list(rec[25])]
                            if cl=='F':
                                if rowseat=='A':row=rows[0]
                                elif rowseat=='B':row=rows[1]
                                else:row=rows[2]
                            elif cl=='B':
                                if rowseat=='D':row=rows[3]
                                elif rowseat=='E':row=rows[4]
                                else:row=rows[5]
                            else:
                                if rowseat=='G':row=rows[6]
                                elif rowseat=='H':row=rows[7]
                                elif rowseat=='I':row=rows[8]
                                elif rowseat=='J':row=rows[9]
                                else:row=rows[10]
                        break        
            if numseat=='1':c=row[0]
            elif numseat=='2':c=row[1]
            else:numseat=row[2]
            available=False
            if c=='R':available=True

            if available==True:
                finaldata=[]
                print(Fl_No)
                for rec in chosendata:
                    if rec[0]==Fl_No:
                        newrec=[]
                        for ele in rec:
                            ref=list(ele)
                            c=row==ref
                            if c==True:
                                if numseat=='1':row[0]='1'
                                elif numseat=='2':row[1]='1'
                                else:row[2]='1'
                                ele=row[0]+row[1]+row[2]+row[3]
                            newrec.append(ele)
                        rec=newrec
                    finaldata.append(rec)
            

            fw=open(f'{aircraft}.csv','w',newline="")
            cw=csv.writer(fw)
            cw.writerows(finaldata)
            fw.close()
            print('The corresponding flight details have been successfully updated.')

        else:print('Reservation details not found.')
                           
    else:print('Passenger details not found.')     
                

#CHECK RESERVATION DETAILS
def chkreservation():
    while True:
        print('1. Filter by Flight Number.')
        print('2. Filter by PNR.')
        print('3. Filter by Name.')
        ch=input('Input choice[1-3]: ')
        if ch=='1':
            fr=open('RESERVATION.CSV')
            data=csv.reader(fr)
            
            #Flight number:
            fno=input('Flight Number: ').upper()
            alist=[]
            found=False
            while not fno.isalnum():
                print('Please input valid information.')
                fno=input('Flight Number: ').upper()
                
            for rec in data:
                if rec[0]==fno:
                    alist.append(rec)
                    found=True
            if found==True:
                print('RESERVATION DETAILS')
                print(tabulate(alist,headers=['Fl_No','PNR','AIRCRAFT','DATE','FROM','TO','SEAT','NAME','AGE','PHONE','CLASS','FARE','STATUS'],tablefmt="simple_grid"))
            else:print('Record(s) not found.')
            break

        elif ch=='2':
            fr=open('RESERVATION.CSV')
            data=csv.reader(fr)
            
            #PNR:
            pnr=input('PNR: ')
            alist=[]
            found=False
            while not pnr.isdigit():
                print('Please input valid information.')
                pnr=input('PNR: ')
                
            for rec in data:
                if rec[1]==pnr:
                    alist.append(rec)
                    found=True
            if found==True:
                print('RESERVATION DETAILS')
                print(tabulate(alist,headers=['Fl_No','PNR','AIRCRAFT','DATE','FROM','TO','SEAT','NAME','AGE','PHONE','CLASS','FARE','STATUS'],tablefmt="simple_grid"))
            else:print('Record(s) not found.')
            break

        elif ch=='3':
            fr=open('RESERVATION.CSV')
            data=csv.reader(fr)
            
            #Name:
            name=input('Name: ').upper()
            alist=[]
            found=False
            while not name.isalpha():
                print('Please input valid information.')
                name=input('Name: ').upper()
                
            for rec in data:
                if rec[7]==name:
                    alist.append(rec)
                    found=True
            if found==True:
                print('RESERVATION DETAILS')
                print(tabulate(alist,headers=['Fl_No','PNR','AIRCRAFT','DATE','FROM','TO','SEAT','NAME','AGE','PHONE','CLASS','FARE','STATUS'],tablefmt="simple_grid"))
            else:print('Record(s) not found.')
            break
                
        else:print('Please input a valid choice.')

#CANCEL RESERVATION:
def cancelreservation():
    pnr=input('Please input your pnr number: ')
    while not pnr.isdigit():
        print('Please input a valid pnr number.')
        pnr=input('Please input your pnr number: ')
    
    file=open('PASSENGER DETAILS.CSV','r')
    data=list(csv.reader(file))
    file.close()
    found=False
    for rec in data:
        if rec[1]==pnr:
            Fl_No=rec[0]
            cl=rec[-1]
            seat=rec[2]
            seatlist=list(seat)
            rowseat=seatlist[0]
            numseat=seatlist[1]
            found=True
            data.remove(rec)
        

    if found==True:
        fw=open('PASSENGER DETAILS.CSV','w',newline="")
        cw=csv.writer(fw)
        cw.writerows(data)
        fw.close()

        file=open('RESERVATION.CSV','r')
        data=list(csv.reader(file))
        file.close()
        c=False
        for rec in data:
            if rec[1]==pnr:
                data.remove(rec)
                c=True
        
        if c==True:
            fw=open('RESERVATION.CSV','w',newline="")
            cw=csv.writer(fw)
            cw.writerows(data)
            fw.close()
            print('Passenger reservation details have been updated successfully.')

            #Updating the corresponding aircraft file details
            names=[]
            fr=open('AIRCRAFT.CSV')
            data=list(csv.reader(fr))
            for rec in data:
                if rec[0].isalpha()==False:
                    names+=[rec[0]]
            fr.close()
            for name in names:
                file=open(f'{name}.csv','r')
                data=list(csv.reader(file))
                file.close()
                for rec in data:
                    if rec[0]==Fl_No:
                        aircraft=name
                        chosendata=data
                        if cl=='E':rec[9]=str(int(rec[9])-1)
                        elif cl=='B':rec[10]=str(int(rec[10])-1)
                        elif cl=='F':rec[11]=str(int(rec[11])-1)
                        rows=[list(rec[15]),list(rec[16]),list(rec[17]),list(rec[18]),list(rec[19]),list(rec[20]),list(rec[21]),list(rec[22]),list(rec[23]),list(rec[24]),list(rec[25])]
                        if cl=='F':
                            if rowseat=='A':row=rows[0]
                            elif rowseat=='B':row=rows[1]
                            else:row=rows[2]
                        elif cl=='B':
                            if rowseat=='D':row=rows[3]
                            elif rowseat=='E':row=rows[4]
                            else:row=rows[5]
                        else:
                            if rowseat=='G':row=rows[6]
                            elif rowseat=='H':row=rows[7]
                            elif rowseat=='I':row=rows[8]
                            elif rowseat=='J':row=rows[9]
                            else:row=rows[10]
                        break        
            if numseat=='1':c=row[0]
            elif numseat=='2':c=row[1]
            else:numseat=row[2]
            available=False
            if c=='R':available=True

            if available==True:
                finaldata=[]
                print(Fl_No)
                for rec in chosendata:
                    if rec[0]==Fl_No:
                        newrec=[]
                        for ele in rec:
                            ref=list(ele)
                            c=row==ref
                            if c==True:
                                if numseat=='1':row[0]='0'
                                elif numseat=='2':row[1]='0'
                                else:row[2]='0'
                                ele=row[0]+row[1]+row[2]+row[3]
                            newrec.append(ele)
                        rec=newrec
                    finaldata.append(rec)
            

            fw=open(f'{aircraft}.csv','w',newline="")
            cw=csv.writer(fw)
            cw.writerows(finaldata)
            fw.close()
            print('The corresponding flight details have been successfully updated.')
            print('Reservation has been successfully cancelled.')

        else:print('Reservation details not found.')
                           
    else:print('Passenger details not found.')     
             




while True:
    print('1. ADMIN')
    print('2. USER')
    print('0. EXIT')

    ch=int(input('Choice[0-2]: '))
    if ch==1:
        while True:
            print('1. CHECK FLIGHTS')
            print('2. ADD A FLIGHT')
            print('3. DELETE A FLIGHT')
            print('4. PASSENGER DETAILS')
            print('5. RESERVATION DETAILS')
            print('0. EXIT')

            a=int(input('Choice[0-5]: '))
            if a==1:chkflights()
            elif a==2:addflight()
            elif a==3:delflight()
            elif a==4:chkpassengers()
            elif a==5:chkreservation()
            else:break
            
    elif ch==2:
        while True:
            print('1. FLIGHT SCHEDULE')
            print('2. BOOK FLIGHT')
            print('3. PRINT TICKET')
            print('4. CANCEL FLIGHT')
            print('5. MAKE A RESERVATION')
            print('6. CANCEL A RESERVATION')
            print('0. EXIT')
            
            b=int(input('Choice[0-6]: '))
            if b==1:schedule()
            elif b==2:bookticket()
            elif b==3:getticket()
            elif b==4:cancelflight()
            elif b==5:reserve()
            elif b==6:cancelreservation()
            else:break
    else:break





























    




















    
