#need account if person is always available

def cmitable():
    #calendar for cmi dates 
    print('{:^10}|{:^10}'.format('Name','CMI dates'))
    for i in range(emptyslots):
        print('{:^10}|{:^10}'.format(str(cmidates[i][0]),str(cmidates[i][1])))

def calendartable():
    #calender for ds dates
    print('{:^10}|{:^10}|{:^10}'.format('Date','Day','Name'))
    for i in range(numberofdays):
        print('{:^10}|{:^10}|{:^10}'.format(str(calendar[i][0]),str(calendar[i][1]),str(calendar[i][2])))

numberofdays = int(input('Number of days in that month: '))
calendar = [['Date','Day','-'] for i in range(numberofdays)]
firstdayofmonth = input('Enter first day of month: ').upper()

#setting up dates in month
for i in range(numberofdays):
    calendar[i][0] = i+1

#setting up days in month
weeknames = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
calendar[0][1] = firstdayofmonth
indexofday = weeknames.index(firstdayofmonth)
for i in range(1,numberofdays):
    if indexofday == 6:
        indexofday = 0
        calendar[i][1] = weeknames[0]
    else:
        indexofday+=1
        calendar[i][1] = weeknames[indexofday]

#set weekends to NA
for i in calendar:
    if i[1] == 'SATURDAY' or i[1] == 'SUNDAY':
        i[2] = 'NA'
NAweekday = []
while True:
    ans = input('Enter NA weekday dates. If there are none to begin with, just write 0. If there are, type in 1 by 1. \
If there are no more to enter, just write 0: ').strip()
    if ans == '0':
        break
    NAweekday.append(int(ans))
    #print(NAweekday)
    for i in NAweekday:
        calendar[i-1][2] = 'NA'
#print(calendar)

#dates where cmi
#if want someone do twice just input name in again

emptyslots = 0
for i in range(numberofdays):
    if calendar[i][2] == '-':
        emptyslots += 1
calendartable()
print('Number of emptyslots = ',emptyslots)
print('Since there are {0} empty slots, you are recommended to enter {0} \
people with the highest priority'.format(emptyslots))

cmidates = []
for i in range(emptyslots):
    listinput = []
    inputname = input('Enter name of person: ')
    listinput.append(inputname)
    inputdatelist = []
    while True:
        inputdate = input("If the person is always available, enter 0. Else, enter dates he can't make it 1 at a time. Once there are no \
more dates for that particular person, enter - : ").strip()
        if inputdate == '0':
            inputdatelist.append(0)
            listinput.append(inputdatelist)
            break
        elif inputdate == '-':
            break
        else:
            inputdatelist.append(int(inputdate))
        listinput.append(inputdatelist)
        
    cmidates.append(listinput)
print(cmidates)
                   
cmitable()

'''#find most common cmi date and put those ppl with most cmi other days but can make it on that day there
#account for case if got ppl got same no of cmi days then randomly select one of them
asclistofmostcmidate = []
deslistofmostcmidate = asclistofmostcmidate[::-1]'''

#make 1 calendar for cmi dates and another for ds dates for everyone
#insert those cmi dates first



def dsplanner():
    
    for i in cmidates:
        #print(i)
        dateofds = 1
        #if empty slot is found and the date fits
        if calendar[dateofds-1][2] == '-' and dateofds not in i[1]:
            calendar[dateofds-1][2] = i[0]
            #calendartable()

        #find next empty slot
        #need account if not empty slot
        
        else:
            #find next empty slot that fits
            while dateofds<=numberofdays:
                if calendar[dateofds-1][2]=='-' and dateofds not in i[1]:
                    break
                dateofds+=1

            #when go thru everday but can't find empty slot that fits
            if dateofds>numberofdays:
                hasswapped = False
                if hasswapped !=True:
                    emptyslotname = i[0]
                    #print('emptyslotname is', emptyslotname)
                    emptyslotcmidates = i[1]
                    #print('emptyslotcmidates is', emptyslotcmidates)
                    #find date of first empty slot 
                    for j in calendar:
                        if j[2] == '-':
                            emptyslotdate = j[0]
                            #print('emptyslotdate is', emptyslotdate)

                    #find date of 1st taken slot
                    #assume can swap first

                    for k in calendar:
                        #find taken slot that guy can make it
                        if hasswapped==True:
                            break
                        elif k[2] != 'NA' and k[2] != '-' and k[0] not in emptyslotcmidates:
                            takenslotdate = k[0]
                            takenslotname = k[2]
                            #check if guy in that takenslotdate can swap
                            for h in cmidates:
                                if str(h[0]) == str(takenslotname) and hasswapped != True:
                                    #list of cmi dates
                                    takenslotcmidates = h[1]
                                    #print(takenslotcmidates)
                                    for a in takenslotcmidates:
                                        #check if takenslotguy can swap
                                        if int(a) == int(emptyslotdate):
                                            hasswapped = False
                                            break
                                        #else takenslot guy can swap
                                        else:
                                            #else emptyslot guy can swap
                                            #print('swapped alr')
                                            calendar[takenslotdate-1][2] = emptyslotname
                                            calendar[emptyslotdate-1][2] = takenslotname
                                            hasswapped = True
                                            #calendartable()
                                            break
                
            #if empty and date fits
            elif calendar[dateofds-1][2] == '-' and dateofds not in i[1]:
                calendar[dateofds-1][2] = i[0]
                #calendartable()
        
dsplanner()
calendartable()
