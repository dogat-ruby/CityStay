# coding: utf-8
import re
import datetime

global list_of_dict

global dict_Matter_Type
dict_Matter_Type = dict()

##################################################          Subroutines         ###########################################
def getMatterIntroDate():
    MatterIntroDate = [d['MatterIntroDate']    for d in list_of_dict     if d['MatterIntroDate']]
    #print("MatterIntroDate = ", MatterIntroDate)  
    for index in range (len(MatterIntroDate)):
        date = re.split('T', MatterIntroDate[index])
        MatterIntroDate[index] = date[0]
    #print("New MatterIntroDate = ", MatterIntroDate)
    print('length of MatterIntroDate = ',len(MatterIntroDate))
    return (MatterIntroDate)

def getMatterAgendaDate():
    MatterAgendaDate = [d['MatterAgendaDate']    for d in list_of_dict     if d['MatterAgendaDate']]
    #print("MatterAgendaDate = ",MatterAgendaDate)
    for index in range (len(MatterAgendaDate)):
        date = re.split('T', MatterAgendaDate[index])
        MatterAgendaDate[index] = date[0]
    #print("New MatterIntroDate = ", MatterAgendaDate)
    print('length of MatterAgendaDate = ',len(MatterAgendaDate))
    return(MatterAgendaDate)	

def getMatterLastModifiedDate():
    MatterLastModifiedDate = [d['MatterLastModifiedUtc']    for d in list_of_dict     if d['MatterLastModifiedUtc']]
    #print("MatterLastModifiedDate = ",MatterLastModifiedDate)
    for index in range (len(MatterLastModifiedDate)):
        date = re.split('T', MatterLastModifiedDate[index])
        MatterLastModifiedDate[index] = date[0]
    #print("New MatterLastModifiedDate = ", MatterLastModifiedDate)
    print('length of MatterLastModifiedDate = ',len(MatterLastModifiedDate))
    return(MatterLastModifiedDate)	
	
def diffInDates(dateList1, dateList2):
    array_len = len(dateList1)
    diffDates = list()
    for index in range (array_len):
        try:
            date1 = dateList1[index]
        except IndexError:
            print("element not present dateList1 at index = ",index)
        try:
            date1 = dateList2[index]
        except IndexError:
            print("element not present dateList2 at index = ",index)
        date = dateList2[index]
        if(re.search(r'null',date)):
            continue	
        (y1, m1, d1) = date.split('-')
        date = dateList1[index]
        #print('date2 = ',date)
        if(re.search(r'null',date)):
            continue
        (y2, m2, d2) = date.split('-')
        (y1, m1, d1, y2, m2, d2) = int(y1), int(m1), int(d1), int(y2), int(m2), int(d2)
        d1 = datetime.date(y1, m1, d1)
        d2 = datetime.date(y2, m2, d2)
        diffDates.append((d1-d2).days)
        #print('Diff between Matter Intro date and Matter Agenda date = ',delta.days)
    #print(diffDates)		
    return(diffDates) #diffDates

def get_Matter_Type_Name():
    for d in list_of_dict :
        if d['MatterTypeName']:
            if d['MatterTypeName'] in dict_Matter_Type:
                dict_Matter_Type[d['MatterTypeName']] += 1
            else:
                dict_Matter_Type[d['MatterTypeName']] = 1		
 
    #print(dict_Matter_Type)
    #return (dict_Matter_Type)	

def averageMatterTime():
    ##Obtain MatterIntroDate	
    MatterIntroDate = getMatterIntroDate()	
    ##Obtain MatterAgendaDate
    MatterAgendaDate = getMatterAgendaDate()
    ##Obtain Difference between MatterIntroDate and MatterAgendaDate
    differenceInDates = diffInDates(MatterIntroDate, MatterAgendaDate)
    ##Obtain Total of differences
    total = 0
    for date in differenceInDates:
        total = total + date
    #print (total)
    
    total_days = total / len(MatterAgendaDate)
    total_days_int = int(total / len(MatterAgendaDate))
    total_hours = ((total_days - total_days_int) * 24)
    total_hours_int = int((total_days - total_days_int) * 24)
    total_min_int = int((total_days - total_days_int - total_hours_int / 24) * 1440)
    result = str(total_days_int) + ' days, ' + str(total_hours_int) + ' hours and ' + str(total_min_int) + ' minutes'
    #print(result)
    return result

##################################################          Main_Program         ###########################################
if __name__ == "__main__":
    ##Obtain MatterIntroDate	
    MatterIntroDate = getMatterIntroDate()	
    ##Obtain MatterAgendaDate
    MatterAgendaDate = getMatterAgendaDate()
    #print("New MatterAgendaDate = ", MatterAgendaDate)
    #1...Obtain Difference between MatterIntroDate and MatterAgendaDate
    differenceInDates = diffInDates(MatterIntroDate, MatterAgendaDate)
    print ("Difference between MatterIntroDate and MatterAgendaDate is :")
    print(differenceInDates)

    ##Obtain MatterLastModDate
    MatterLastModDate = getMatterLastModifiedDate()
    #print("New MatterLastModDate = ", MatterLastModDate)
    differenceInDates = diffInDates(MatterIntroDate, MatterAgendaDate)
    print ("Difference between MatterIntroDate and MatterLastModifiedDate is :")
    print(differenceInDates)		

    get_Matter_Type_Name()
    print('The type and number of of Matter Types are :')
    print(dict_Matter_Type)		
    #MatterStatusName: how many counts ofhow many types
    # MatterTypeName: how many counts ofhow many types
    #MatterEnactmentDate
    #MatterPassedDate
    #MatterRequester
    #MatterLastModifiedUtc 