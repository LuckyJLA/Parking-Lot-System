import pandas as pd
import numpy as np
import datetime as dt


#checks credentials for log in
def login(username, password):
    up = pd.read_csv(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\Frames\CSV files\Users.csv")
    users = np.array(up['username'])
    ps = np.array(up['password'])

    for i in range(2):
        if (users[i] == username and ps[i] == password):
            #returns true if the credentials are correct
            return True
    #returns false if the credentials are wrong
    return False


#initializes variable that will be used for parking lot checking
def init_monitor_csv():
    global csv_file, lot, stat
    csv_file = pd.read_csv(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\Frames\CSV files\ParkMonitor.csv")
    lot = np.array(csv_file['lot_num']); stat = np.array(csv_file['available'])


def lotcheck(lot_num, whatop):
    init_monitor_csv()

    #if the function was called from park
    if whatop == "Park":
        for i in range(15):
            if lot[i]==lot_num:
                if stat[i] == True:
                    return True

    #if the function was called from Unpark
    if whatop == "Unpark":
        for i in range(15):
            if lot[i]==lot_num:
                if stat[i] == False:
                    return False


#gives color to the parking lot buttons
def button_color(lot_num):
    init_monitor_csv()
    
    for i in range(15):
        if lot[i]==lot_num:
            #if it's available
            if stat[i] == True: 
                return '#00DC16' 
            
            # False means someone already parked    
            elif stat[i] == False: 
                return '#FF0000'



#initializes global variable for park and unpark
def init_Logs_csv():
    global logs, timenow, nowcount, monitor, lotnum
    
    logs = pd.read_csv(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\Frames\CSV files\ParkingLog.csv")
    timenow = np.array(logs['timestamp']); nowcount = np.array(logs['parked_counter'])

    monitor = pd.read_csv(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\Frames\CSV files\ParkMonitor.csv")
    lotnum = np.array(monitor['lot_num']) 


def go_park(newlotnum, newtime):
    init_Logs_csv()
    
    #converts string into int
    thisnum = int(newlotnum)
    print('======PARKING======')
    for i in range(15):
        #finds the parking lot number clicked
        if lotnum[i]==thisnum:
        
            #updates the Logs and Monitor
            newCount = nowcount[-1]+1
            monitor.iloc[i,1] = False
            newLog = pd.DataFrame({'timestamp':[newtime],
                                   'lot_num':[thisnum],
                                   'in_out':[True],
                                   'parked_counter':[newCount]})
            
            monitor.to_csv(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\Frames\CSV files\ParkMonitor.csv", index=False)
            newLog.to_csv(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\Frames\CSV files\ParkingLog.csv", mode='a', index=False, header=False)
            dailycount(newtime)
            print('done')

            return True
    return False


def go_unpark(newlotnum, newtime):
    init_Logs_csv()
    
    #converts string into int
    thisnum = int(newlotnum)
    for i in range(15):
        #finds the parking lot number clicked
        if lotnum[i]==thisnum:
        
            #updates the Logs and Monitor
            newCount = nowcount[-1]-1
            monitor.iloc[i,1] = True
            newLog = pd.DataFrame({'timestamp':[newtime],
                                   'lot_num':[thisnum],
                                   'in_out':[False],
                                   'parked_counter':[newCount]})
            
            monitor.to_csv(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\Frames\CSV files\ParkMonitor.csv", index=False)
            newLog.to_csv(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\Frames\CSV files\ParkingLog.csv", mode='a', index=False, header=False)
            print('done')
            return True
    return False


#Used for updating the csv file that contains how many cars parked in a day
def dailycount(newtime):
    
    file = pd.read_csv(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\Frames\CSV files\DailyCount.csv")
    filedate = np.array(file["Date"]); filecount = np.array(file["Number"])
    
    #converts string into time and time to string in an specific format
    new_date = dt.datetime.strptime(newtime, "%m/%d/%Y %I:%M %p")
    nd_string = dt.datetime.strftime(new_date, "%m/%d/%Y")

    
    newdatecount = 1

    #if the date already exists in the file
    for i in range(filedate.size):
        if filedate[i] == nd_string:
            #adds 1 car that parked in that date
            file.iloc[i,1] = filecount[i] + 1
            newdatecount = 0
            #updates the file
            file.to_csv(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\Frames\CSV files\DailyCount.csv", index=False)
       
    #if its a new date
    if newdatecount == 1:

        #finds the difference between that latest date in the file and given date
        file_date =  dt.datetime.strptime(filedate[-1], "%m/%d/%Y")
        diff_days = new_date - file_date
        loop = diff_days.days

        if loop > 1:
            #fills the days that has no car parked
            for i in range(loop-1):
                file_date = file_date + dt.timedelta(days=1)
                date_count = pd.DataFrame( {'Date':[file_date.strftime("%m/%d/%Y")], 'Number':[0]})
                date_count.to_csv(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\Frames\CSV files\DailyCount.csv", mode='a', index=False, header=False)

        #adds the new log
        date_count = pd.DataFrame( {'Date':[nd_string], 'Number':[1]})
        date_count.to_csv(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\Frames\CSV files\DailyCount.csv", mode='a', index=False, header=False)

