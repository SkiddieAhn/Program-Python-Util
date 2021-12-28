from math import exp

class Tabtwo(object):
    def __init__(self):
        return None   
    
    def file2(self,filere):
        
            f=open("tab2.txt")
            for line in f:
                (a,b,c,d,e)=line.split(" ")
                num=float(a)
                type1=str(b)
                type2=str(d)
                
            if(type1=="bit"):
                if(type2=="bit"):
                    return num
                elif(type2=="kilobit"):
                    return num/1024
                elif(type2=="megabit"):
                    return num/1048576
                elif(type2=="gigabit"):
                    return num/1000000000
                elif(type2=="byte"):
                    return num/8
                elif(type2=="kilobyte"):
                    return num/8/1024
                elif(type2=="megabyte"):
                    return num/8/1048576
                elif(type2=="gigabyte"):
                    return num/8/1000000000
                
            elif(type1=="kilobit"):
                if(type2=="bit"):
                    return num*1024
                elif(type2=="kilobit"):
                    return num
                elif(type2=="megabit"):
                    return num/1024
                elif(type2=="gigabit"):
                    return num/1048576
                elif(type2=="byte"):
                    return num/8*1024
                elif(type2=="kilobyte"):
                    return num/8
                elif(type2=="megabyte"):
                    return num/8/1024
                elif(type2=="gigabyte"):
                    return num/8/1048576
                
            elif(type1=="megabit"):
                if(type2=="bit"):
                    return num*1048576
                elif(type2=="kilobit"):
                    return num*1024
                elif(type2=="megabit"):
                    return num
                elif(type2=="gigabit"):
                    return num/1024
                elif(type2=="byte"):
                    return num*1048576/8
                elif(type2=="kilobyte"):
                    return num/8*1024
                elif(type2=="megabyte"):
                    return num/8
                elif(type2=="gigabyte"):
                    return num/8/1024
                
            elif(type1=="gigabit"):
                if(type2=="bit"):
                    return num*1000000000
                elif(type2=="kilobit"):
                    return num*1048576
                elif(type2=="megabit"):
                    return num*1024
                elif(type2=="gigabit"):
                    return num
                elif(type2=="byte"):
                    return num/8*1000000000
                elif(type2=="kilobyte"):
                    return num/8*1048576
                elif(type2=="megabyte"):
                    return num/8*1024
                elif(type2=="gigabyte"):
                    return num/8
                    
            elif(type1=="byte"):
                if(type2=="bit"):
                    return num*8
                elif(type2=="kilobit"):
                    return num*8/1024
                elif(type2=="megabit"):
                    return num*8/1048576
                elif(type2=="gigabit"):
                    return num*8/1000000000
                elif(type2=="byte"):
                    return num
                elif(type2=="kilobyte"):
                    return num*0.000977
                elif(type2=="megabyte"):
                    return num*9.5367*1/10000000
                elif(type2=="gigabyte"):
                    return num*9.3132*1/10000000000
                
            elif(type1=="kilobyte"):
                if(type2=="bit"):
                    return num*8*1024
                elif(type2=="kilobit"):
                    return num*8
                elif(type2=="megabit"):
                    return num*8/1024
                elif(type2=="gigabit"):
                    return num*8/1048576
                elif(type2=="byte"):
                    return num*1024
                elif(type2=="kilobyte"):
                    return num
                elif(type2=="megabyte"):
                    return num/1024
                elif(type2=="gigabyte"):
                    return num/1048576
                
            elif(type1=="megabyte"):
                if(type2=="bit"):
                    return num*8*1048576
                elif(type2=="kilobit"):
                    return num*8*1024
                elif(type2=="megabit"):
                    return num*8
                elif(type2=="gigabit"):
                    return num*8/1024
                elif(type2=="byte"):
                    return num*1048576
                elif(type2=="kilobyte"):
                    return num*1024
                elif(type2=="megabyte"):
                    return num
                elif(type2=="gigabyte"):
                    return num/1024
                
            elif(type1=="gigabyte"):
                if(type2=="bit"):
                    return num*8*1000000000
                elif(type2=="kilobit"):
                    return num*8*1048576
                elif(type2=="megabit"):
                    return num*8*1024
                elif(type2=="gigabit"):
                    return num*8
                elif(type2=="byte"):
                    return num*1000000000
                elif(type2=="kilobyte"):
                    return num*1048576
                elif(type2=="megabyte"):
                    return num*1024
                elif(type2=="gigabyte"):
                    return num
                
            return 0
