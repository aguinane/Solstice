#!/usr/bin/python3
import database
import datetime
import time
import os

SETTINGS_FILENAME = os.path.abspath('settings/dbExample.json')
    
def main():
    get_voltage_chart_data(1)
    
    
def get_voltage_chart_data(meterId):
    """ Return json object for flot chart
    """
    query_filename = os.path.abspath('sql/Last50VoltReadings.sql')
    params_dict = {'METERID': meterId}
    h, d = database.run_query(SETTINGS_FILENAME, query_filename, params_dict)
    
    chartdata = {}
    chartdata['label'] = 'Voltage Profile'
    chartdata['a'] = []
    chartdata['b'] = []
    chartdata['c'] = []    
    
    for row in d:
        dTime = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        ts = int(time.mktime(dTime.timetuple()) * 1000)
        chartdata['a'].append([ts,row[1]])
        chartdata['b'].append([ts,row[2]])
        chartdata['c'].append([ts,row[3]])                
        
    return chartdata
    
def get_thd_chart_data(meterId):
    """ Return json object for flot chart
    """
    query_filename = os.path.abspath('sql/Last50THDReadings.sql')
    params_dict = {'METERID': meterId}
    h, d = database.run_query(SETTINGS_FILENAME, query_filename, params_dict)
    
    chartdata = {}
    chartdata['label'] = 'THD Profile'
    chartdata['a'] = []
    chartdata['b'] = []
    chartdata['c'] = []    
    
    for row in d:
        dTime = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        ts = int(time.mktime(dTime.timetuple()) * 1000)
        chartdata['a'].append([ts,row[1]])
        chartdata['b'].append([ts,row[2]])
        chartdata['c'].append([ts,row[3]])                
        
    return chartdata
    
    
def get_unbal_chart_data(meterId):
    """ Return json object for flot chart
    """
    query_filename = os.path.abspath('sql/Last50UnbalReadings.sql')
    params_dict = {'METERID': meterId}
    h, d = database.run_query(SETTINGS_FILENAME, query_filename, params_dict)
    
    chartdata = {}
    chartdata['label'] = 'Unbalance Profile'
    chartdata['a'] = [] 
    
    for row in d:
        dTime = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        ts = int(time.mktime(dTime.timetuple()) * 1000)
        chartdata['a'].append([ts,row[1]])             
        
    return chartdata  
    
def get_events_chart_data(meterId):
    """ Return json object for flot chart
    """
    query_filename = os.path.abspath('sql/EventsByMonth.sql')
    params_dict = {'METERID': meterId}
    h, d = database.run_query(SETTINGS_FILENAME, query_filename, params_dict)
    
    chartdata = {}
    chartdata['label'] = 'Unbalance Profile'
    chartdata['sag'] = [] 
    chartdata['swl'] = []     
    
    for row in d:
        dTime = datetime.datetime.strptime(row[0], '%Y-%m-%d')
        ts = int(time.mktime(dTime.timetuple()) * 1000)
        chartdata['sag'].append([ts,row[1]])
        chartdata['swl'].append([ts,row[2]])
        
    return chartdata          
    
    
if __name__ == '__main__':
    main()    
