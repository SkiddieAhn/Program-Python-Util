from matplotlib.figure import Figure
import tkinter as tk
from pylab import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def save(receive):
    Save=open("save.txt","a")
    Save.write(receive)
    Save.close()
    
class trifunc(object):
    def __init__(self,axe,receive,series):
        self.root=tk.Tk()
        self.root.title("Trigonometrical Function")
        self.root.withdraw()
        if(receive=="x" or receive=="1/2x" or receive=="2x" or receive=="sinX" or receive=="cosX" or receive=="tanX"):
           self.trimake(axe,receive,series)
        else:
            self.receivezero=receive
            receive=float(receive)/180*pi
            self.trimake(axe,receive,series)
        
    def drawfunction(self,receive,answer,code):
        self.fig=Figure()
        self.axis=self.fig.add_subplot(111)
        if(code==0):
            self.axis.plot(self.x, self.y, color='blue')
            self.axis.grid() 
            self.represent()
        else:
            self.axis.plot(self.x, self.y, color='blue')
            self.axis.scatter(receive,answer,30, color='red')
            self.axis.annotate('The Answer='+str(answer),xy=(receive,answer),xytext=(+10, +30), textcoords='offset points', fontsize=16,arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2",color='red'),color='red')
            self.axis.grid() 
            self.represent()
            
    def decidey(self,receive,series):   
        if(series=="sin"):
            if(receive=="x"):
                self.y=sin(self.x)
                self.drawfunction(receive,0,0)
            elif(receive=="1/2x"):
                self.y=sin(1/2*self.x)
                self.drawfunction(receive,0,0)
            elif(receive=="2x"):
                self.y=sin(2*self.x)
                self.drawfunction(receive,0,0)
            elif(receive=="sinX"):
                self.y=sin(self.x)*sin(self.x)
                self.drawfunction(receive,0,0)
            else:
                self.y=sin(self.x)
                answer=round(sin(receive),2)
                self.drawfunction(receive,answer,1)
                save("sin("+str(self.receivezero)+"°)= "+str(answer)+"\n")
                
        elif(series=="cos"):
            if(receive=="x"):
                self.y=cos(self.x)
                self.drawfunction(receive,0,0)
            elif(receive=="1/2x"):
                self.y=cos(1/2*self.x)
                self.drawfunction(receive,0,0)
            elif(receive=="2x"):
                self.y=cos(2*self.x)
                self.drawfunction(receive,0,0)
            elif(receive=="cosX"):
                self.y=cos(self.x)*cos(self.x)
                self.drawfunction(receive,0,0)
            else:
                self.y=cos(self.x)
                answer=round(cos(receive),2)
                self.drawfunction(receive,answer,1)
                save("cos("+str(self.receivezero)+"°)= "+str(answer)+"\n")
                
        elif(series=="tan"):
            if(receive=="x"):
                self.y=tan(self.x)
                self.drawfunction(receive,0,0)
            elif(receive=="1/2x"):
                self.y=tan(1/2*self.x)
                self.drawfunction(receive,0,0)
            elif(receive=="2x"):
                self.y=tan(2*self.x)
                self.drawfunction(receive,0,0)
            elif(receive=="tanX"):
                self.y=tan(self.x)*tan(self.x)
                self.drawfunction(receive,0,0)
            else:
                self.y=tan(self.x)
                answer=round(tan(receive),2)
                self.drawfunction(receive,answer,1)
                save("tan("+str(self.receivezero)+"°)= "+str(answer)+"\n")
                
    def trimake(self,axe,receive,series):
        
        # x,y variable
        if(axe=="0~2pi"):
            self.x=arange(0,2*pi,0.1)
            self.decidey(receive,series)
        elif(axe=="-2pi~2pi"):
            self.x=arange(-2*pi,2*pi,0.1)
            self.decidey(receive,series)
        elif(axe=="-4pi~4pi"):
            self.x=arange(-4*pi,4*pi,0.1)
            self.decidey(receive,series)
        elif(axe=="-6pi~6pi"):
            self.x=arange(-6*pi,6*pi,0.1)
            self.decidey(receive,series)
        
        
        # Create figure and subplot
        
        #-----------------------------------------------------------------------------------#
        #-----------------------------------------------------------------------------------#
        
    def represent(self): 
        canvas=FigureCanvasTkAgg(self.fig,master=self.root)
        canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
        
        self.root.update()
        self.root.deiconify()
        




