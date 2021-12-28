import random

class Daycalc(object):
    def __init__(self):
        return None
            
    def private(self,year,month,day):
        month+=1
        day+=random.randrange(1,15)
        if(month==2):
            if(day>=28):
                month+=1
                day=day-28
        elif(day>=30):
            month+=1
            day=day-30
        elif(month>12):
            year+=1
            month-=12
        variable=str(year)+"/"+str(month)+"/"+str(day)
        return variable
    
    def privatefirst(self,year,month,day):
        month+=3
        day+=random.randrange(1,15)
        if(month==2):
            if(day>=28):
                month+=1
                day=day-28
        elif(day>=30):
            month+=1
            day=day-30
        elif(month>12):
            year+=1
            month-=12
        variable=str(year)+"/"+str(month)+"/"+str(day)
        return variable
    
    def Corporal(self,year,month,day):
        month+=10
        day+=random.randrange(1,15)
        if(month==2):
            if(day>=28):
                month+=1
                day=day-28
        elif(day>=30):
            month+=1
            day=day-30
        elif(month>12):
            year+=1
            month-=12
        variable=str(year)+"/"+str(month)+"/"+str(day)
        return variable
    
    def Sergeant(self,year,month,day): 
        month+=17
        day+=random.randrange(1,15)
        if(month==2):
            if(day>=28):
                month+=1
                day=day-28
        elif(day>=30):
            month+=1
            day=day-30
        elif(12<month<=24):
            year+=1
            month-=12  
        elif(month>24):
            year+=1
            month-=24
        variable=str(year)+"/"+str(month)+"/"+str(day)
        return variable
        
    def discharge(self,year,month,day):
        if(month==1 or month==3 or month==5 or month==6 or month==8 or month==10 or month==12):
                if(month==5 and 20<=day<=31):
                    year+=2
                    month=1
                    days=day+12
                    day=days-31
                    variable=str(year)+"/"+str(month)+"/"+str(day)
                    return variable
                    
                if(month<=5):
                    year+=1
                    month+=7
                else:
                    year+=2
                    months=month+7
                    month=months-12
                    
                if(1<=day<=19):
                    day+=12
                else:
                    days=day+12
                    day=days-31
                    month+=1
                    
                    
        elif(month==2 or month==4 or month==9 or month==11):
                if(month<=5):
                    year+=1
                    month+=7
                else:
                    year+=2
                    months=month+7
                    month=months-12
                    
                if(1<=day<=18):
                    day+=12
                else:
                    days=day+12
                    day=days-30
                    month+=1
                    
        elif(month==7):
                year+=2
                month=2
                if(1<=day<=16):
                    day+=12
                else:
                    days=day+12
                    day=days-28
                    month+=1
                    
        variable=str(year)+"/"+str(month)+"/"+str(day)
        return variable
                