# coding: utf-8
import re
import datetime


##################################################          Subroutines         ###########################################
def getMatterIntroDate(list_of_dict):
    MatterIntroDate = [d['MatterIntroDate']    for d in list_of_dict     if d['MatterIntroDate']]
    #print("MatterIntroDate = ", MatterIntroDate)  
    for index in range (len(MatterIntroDate)):
        date = re.split('T', MatterIntroDate[index])
        MatterIntroDate[index] = date[0]
    #print("New MatterIntroDate = ", MatterIntroDate)
    print('length of MatterIntroDate = ',len(MatterIntroDate))
    return (MatterIntroDate)

def getMatterAgendaDate(list_of_dict):
    MatterAgendaDate = [d['MatterAgendaDate']    for d in list_of_dict     if d['MatterAgendaDate']]
    #print("MatterAgendaDate = ",MatterAgendaDate)
    for index in range (len(MatterAgendaDate)):
        date = re.split('T', MatterAgendaDate[index])
        MatterAgendaDate[index] = date[0]
    #print("New MatterIntroDate = ", MatterAgendaDate)
    print('length of MatterAgendaDate = ',len(MatterAgendaDate))
    return(MatterAgendaDate)	

def getMatterLastModifiedDate(list_of_dict):
    MatterLastModifiedDate = [d['MatterLastModifiedUtc']    for d in list_of_dict     if d['MatterLastModifiedUtc']]
    #print("MatterLastModifiedDate = ",MatterLastModifiedDate)
    for index in range (len(MatterLastModifiedDate)):
        date = re.split('T', MatterLastModifiedDate[index])
        MatterLastModifiedDate[index] = date[0]
    #print("New MatterLastModifiedDate = ", MatterLastModifiedDate)
    print('length of MatterLastModifiedDate = ',len(MatterLastModifiedDate))
    return(MatterLastModifiedDate)	
	
def diffInDatesList(dateList1, dateList2):
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
    
def diffInDates(date1, date2):
  diffDates = 0
  #Split in two lists
  date1 = re.split('T', date1)
  date2 = re.split('T', date2)
  #Split first list
  (y1, m1, d1) = date2[0].split('-')
  (y2, m2, d2) = date1[0].split('-')
  #Convert to integers
  (y1, m1, d1, y2, m2, d2) = int(y1), int(m1), int(d1), int(y2), int(m2), int(d2)
  d1 = datetime.date(y1, m1, d1)
  d2 = datetime.date(y2, m2, d2)	
  diffDates = (d1-d2).days
  return(diffDates)

def get_Matter_Type_Name(list_of_dict):
    matterTypeName = {}
    for d in list_of_dict :
        if d['MatterTypeName']:
            if d['MatterTypeName'] in matterTypeName:
                matterTypeName[d['MatterTypeName']] += 1
            else:
                matterTypeName[d['MatterTypeName']] = 1	
    #print(dict_Matter_Type)
    return (matterTypeName)	

def get_Matter_Body_Name(list_of_dict):
    matterBodyName = {}
    for d in list_of_dict :
        if d['MatterBodyName']:
            if d['MatterBodyName'] in matterBodyName:
                matterBodyName[d['MatterBodyName']] += 1
            else:
                matterBodyName[d['MatterBodyName']] = 1	
    return (matterBodyName)	
 
def get_Matter_Status(list_of_dict):  
    matterStatus = {}
    for d in list_of_dict:
        if d['MatterTypeName']:
            #print(d['MatterStatusName'])
            if d['MatterTypeName'] in matterStatus:
                #~ print(matterStatus[d['MatterTypeName']][d['MatterStatusName']])
                if d['MatterStatusName'] in matterStatus[d['MatterTypeName']]:
                    matterStatus[d['MatterTypeName']][d['MatterStatusName']] += 1
                else:
                    matterStatus[d['MatterTypeName']][d['MatterStatusName']] = 1
            else:
                matterStatus[d['MatterTypeName']] = {}
    return matterStatus

def get_Matter_Intro_Agenda(list_of_dict):
    matterTotalDays = {}
    for d in list_of_dict:
        if d['MatterTypeName']:
            #print(d['MatterIntroDate'], d['MatterAgendaDate'])
            MatterIntroDate = d['MatterIntroDate']
            if d['MatterAgendaDate']:
                MatterAgendaDate = d['MatterAgendaDate']
            else:
                MatterAgendaDate = d['MatterPassedDate']
            try:
                diff = diffInDates(MatterIntroDate, MatterAgendaDate)
                #print(d['MatterTypeName'], ':', diff)
                if d['MatterTypeName'] in matterTotalDays:
                    matterTotalDays[d['MatterTypeName']] += diff
                else:
                    matterTotalDays[d['MatterTypeName']] = diff
            except:
                #print("Skip: Cannot get Intro or Agenda date") 
                continue
    return matterTotalDays
    
def averageMatterTime(list_of_dict):
  ##Obtain MatterIntroDate	
  MatterIntroDate = getMatterIntroDate(list_of_dict)	
  ##Obtain MatterAgendaDate
  MatterAgendaDate = getMatterAgendaDate(list_of_dict)
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

def getAverageDurationPerType(dictNumbers, dictDays):
  averageMatterDuration = {}
  for key in dictNumbers:
    try:
      averageMatterDuration[key] = round(dictDays[key] / dictNumbers[key], 2)
    except:
      #print('Error calculating average duration for', key)
      continue
  return averageMatterDuration

##################################################          Main_Program         ###########################################
if __name__ == "__main__": 
  # Item 1
  dictTypeNumber = get_Matter_Type_Name(list_of_dict)
#print('\nThe type and number of matter types are:')
  #print(dictTypeNumber)	
  dictTypeDuration = get_Matter_Intro_Agenda(list_of_dict)
  #print('\nThe total number of days per type:')
  #print(dictTypeDuration)
  dictTypeAverageDuration = getAverageDurationPerType(dictTypeNumber, dictTypeDuration)
  print('\n1) The average duration (in days) per type:')
  print(dictTypeAverageDuration)
  
  # Item 2
  dictTypeStatus = get_Matter_Status(list_of_dict)
  print('\n2) Number of similar statuses per type of matter:')
  print(dictTypeStatus)
  
  # Item 3
  dictBodyNumber = get_Matter_Body_Name(list_of_dict)
  print('\n3) Number of files per body:')
  print(dictBodyNumber)

