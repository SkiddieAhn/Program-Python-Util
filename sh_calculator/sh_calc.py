import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
import Tooltip as tt
from math import *
from pylab import *
import trifunction as tri
from time import sleep
import daycalc as dc
import tabtwo 
                
def create_ToolTip(widget, text):
    toolTip=tt.ToolTip(widget)
    def enter(event):
        toolTip.show_tip(text)
    def leave(event):
        toolTip.hide_tip()
    widget.bind("<Enter>",enter)
    widget.bind("<Leave>",leave)

def save(receive):
    Save=open("save.txt","a")
    Save.write(receive)
    Save.close()


class main():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("SH Calculator")
        self.A=1
        self.start=0
        self.create_widgets()
    
    # 클로저 함수 이용    
    def falsetext(self,n):
        def Text():
            text=[self.text0,self.text1,self.text2,self.text3,self.text4,self.text5,self.text6,self.text7,self.text8,self.text9] # 탭1 숫자 리스트
            textequal=self.texta # 탭1 등호 변수 
            textpoint=self.textg # 탭1 점 변수
            textrute=self.textf # 탭1 루트 변수
            textABC=[self.textb,self.textc,self.textd,self.texte] # 탭1 계산  리스트
            texttwo=[self.text20,self.text21,self.text22,self.text23,self.text24,self.text25,self.text26,self.text27,self.text28,self.text29] # 탭2 숫자 리스트
            textABC2=[self.text2a,self.text2b] # 탭2 계산  리스트
            
                
            if(n<10): # 탭1 숫자 버튼
                    tabstart=1
                    receive=self.scrinsert(text[n])
                    self.f=open("tab1.txt","a")
                    self.f.write(str(text[n]))
            elif(n==10): # 탭1 = 버튼
                    tabstart=1
                    receive=self.scrinsert(" "+textequal+" ")
                    self.equal()
            elif(n==15): # 탭1 루트 버튼
                    tabstart=1
                    receive=self.scrinsert(textrute)
                    self.file(textrute)

            elif(n==16): # 탭1 . 버튼
                    tabstart=1
                    receive=self.scrinsert(textpoint)
                    self.f=open("tab1.txt","a")
                    self.f.write(textpoint)
            elif(10<n<20): # 탭1 계산 버튼
                    tabstart=1
                    receive=self.scrinsert(textABC[n-11])
                    self.file(textABC[n-11])
                    
            elif(20<=n<30): # 탭2 숫자 버튼
                    receive=self.scrinsert2(texttwo[n-20])
                    tabstart=2
                    self.f2=open("tab2.txt","a")
                    self.f2.write(str(texttwo[n-20]))
            elif(30<=n<40): # 탭2 계산 버튼
                    receive=self.scrinsert2(str(textABC2[n-30])+" ")
                    if(textABC2[n-30]=="CHANGE"):
                        tabstart=2
                        self.f2=open("tab2.txt","a")
                        self.f2.write(str(textABC2[n-30]))
                    elif(textABC2[n-30]=="="):
                        tabstart=2
                        Tw=tabtwo.Tabtwo()
                        tab2final=Tw.file2(textABC2[n-30])
                        self.scrinsert2(" "+str(tab2final)+"\n")
                    
            if(tabstart==1):
                self.f.close()
            elif(tabstart==2):
                self.f2.close()
            
        return Text
    
    
    def file(self,filere):
        if(self.A==1):
            self.f=open("tab1.txt","a")
            if(filere=="-"):
                self.f.write(" + -")
            elif(filere=="^(1/2)"):
                self.f.close()
                self.f=open("tab1.txt")
                for line in self.f:
                    (self.a)=line.split(" ")
                self.scrinsert(" = "+str(sqrt(float(self.a[0])))+"\n")
                self.f.close()
                return 0
            else:
                self.f.write(" "+filere+" ")
            self.f.close()
            self.A+=1
            return 0
        
        elif(self.A>=2):
            self.f=open("tab1.txt")
            for line in self.f:
                (self.a,self.b,self.c)=line.split(" ")
            self.f.close()
            self.f=open("tab1.txt","a")
            if(filere=="-"):
                self.f.write("\n"+self.c+" + -")
            else:
                self.f.write("\n"+self.c+" "+filere+" ")
            self.f.close()
            self.A+=1
            return 0
        
    def equal(self):
        self.ap=0
        self.value=0
        self.sachik=0
        
        self.f=open("tab1.txt")
        for line in self.f:
                (self.a,self.b,self.c)=line.split(" ")
                
                if(self.b=="+"):

                    if(self.value==0): # 일반연산 파트
                        self.value=float(self.a)+float(self.c)
                    else:
                        self.value=self.value+float(self.c)
                        
                    if(self.ap==0): # 더하기가 먼저 나오는 사칙 연산 준비
                        self.ap=float(self.a)
                        self.sachik=1
                    else:
                        self.ap=self.ap+float(self.a)
                       
                        
                        
                elif(self.b=="x"):
                    
                    if(self.value==0): # 일반연산 파트
                        self.value=float(self.a)*float(self.c)            
                    else:
                        self.value*=float(self.c)
                                       
                    if(self.sachik==1): # 더하기가 먼저 나오는 사칙 연산 파트
                        self.value=self.ap+float(self.a)*float(self.c)
                        self.values=float(self.a)*float(self.c)
                        self.sachik+=1
                    elif(self.sachik>=2):
                        self.value=self.ap+self.values*float(self.c)
                        self.values*=float(self.c)
                        self.sachik+=1
                        
                                                
                elif(self.b=="/"):
                    if(self.value==0):
                        self.value=float(self.a)/float(self.c)
                    else:
                        self.value=self.value/float(self.c)
                        
                    if(self.sachik==1):
                        self.values=float(self.a)/float(self.c)
                        self.value=self.ap+float(self.a)/float(self.c)
                        self.sachik+=1
                    elif(self.sachik>=2):
                        self.value=self.ap+self.values/float(self.c)
                        self.values=self.values/float(self.c)
                        self.sachik+=1
                   
        self.scrinsert(str(self.value)+"\n")   
        self.f.close()
        return 0
        
    def scrinsert(self,receive):
        self.scr.insert(tk.INSERT,receive)
        save(str(receive))
    def scrinsert2(self,receive):
        self.scr2.insert(tk.INSERT,receive)
        save(str(receive))
        
    def msgBox(self):
        ret=msg.askokcancel("저작자","20184060 컴퓨터공학과 안성현")
        
    def scrcombobox(self,event):
        number=self.number.get()
        self.f2=open("tab2.txt","a")
        self.f2.write(" "+number+" ")
        self.f2.close()
        self.scr2.insert(tk.INSERT," "+number+" ")
        save(" "+number+" ")
        
    def scrcombobox2(self,event):
        number2=self.number2.get()
        self.f2=open("tab2.txt","a")
        self.f2.write(" "+number2+" ")
        self.f2.close()
        self.scr2.insert(tk.INSERT," "+number2+" ")
        save(" "+number2+" ")
        
    def destroyWindow(self):
        self.win.quit()
        self.win.destroy()
        self.f=open("tab1.txt","w")
        self.f.close()
        self.f=open("tab2.txt","w")
        self.f.close()
        
    def scrdelete(self):
        self.scr.delete(1.0,tk.END)
        self.A=1
        self.f=open("tab1.txt","w")
        self.f.close()
        
    def scrnumber(self):
        self.scrnum+=1
        if(self.scrnum%2==1):
            self.scr.configure(state="disabled")
        else:
            self.scr.configure(state="normal")
            
    #----------------------------------------------------#
    def scrnumber2(self):
        self.scrnum2+=1
        if(self.scrnum2 %2==1):
            self.scr2.configure(state="disabled")
        else:
            self.scr2.configure(state="normal")  
        
    def scrdelete2(self):
        self.scr2.delete(1.0,tk.END)
        self.f=open("tab2.txt","w")
        self.f.close()
        

    def false_graph(self,num):
        def make_graph():
            sin="sin"
            cos="cos"
            tan="tan"
            
            if(num==1):
                Tri=tri.trifunc(self.scvn.get(),float(self.sinname.get()),sin)
            elif(num==2):
                Tri=tri.trifunc(self.scvn.get(),float(self.cosname.get()),cos)
            elif(num==3):
                Tri=tri.trifunc(self.scvn.get(),float(self.tanname.get()),tan)
            elif(num==4):
                if(self.sinname2.get()=="x"):
                    Tri=tri.trifunc(self.scvn.get(),"x",sin)
                elif(self.sinname2.get()=="1/2x"):
                    Tri=tri.trifunc(self.scvn.get(),"1/2x",sin)
                elif(self.sinname2.get()=="2x"):
                    Tri=tri.trifunc(self.scvn.get(),"2x",sin)
                elif(self.sinname2.get()=="sinX"):
                    Tri=tri.trifunc(self.scvn.get(),"sinX",sin)
            elif(num==5):
                if(self.cosname2.get()=="x"):
                    Tri=tri.trifunc(self.scvn.get(),"x",cos)
                elif(self.cosname2.get()=="1/2x"):
                    Tri=tri.trifunc(self.scvn.get(),"1/2x",cos)
                elif(self.cosname2.get()=="2x"):
                    Tri=tri.trifunc(self.scvn.get(),"2x",cos)
                elif(self.cosname2.get()=="cosX"):
                    Tri=tri.trifunc(self.scvn.get(),"cosX",cos)
            elif(num==6):
                if(self.tanname2.get()=="x"):
                    Tri=tri.trifunc(self.scvn.get(),"x",tan)
                elif(self.tanname2.get()=="1/2x"):
                    Tri=tri.trifunc(self.scvn.get(),"1/2x",tan)
                elif(self.tanname2.get()=="2x"):
                    Tri=tri.trifunc(self.scvn.get(),"2x",tan)
                elif(self.tanname2.get()=="tanX"):
                    Tri=tri.trifunc(self.scvn.get(),"tanX",tan)
        return make_graph
    
    def change_day(self,event):
            month=self.monthname.get()
            if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
                self.day['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
            elif(month==4 or month==6 or month==9 or month==11):
                self.day['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
            elif(month==2):
                self.day['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28)
    
    def military(self,label,tab):
        def start():
            year=self.yearname.get()
            month=self.monthname.get()
            day=self.dayname.get()
            
            self.start+=1
            ttk.Label(label,text="Deciding your Military Life").grid(column=0,row=6,columnspan=4)
            self.progress_bar['value']=0
            self.progress_bar['maximum']=100
            for i in range(101):
                sleep(0.05)
                self.progress_bar['value']=i
                self.progress_bar.update()
            ttk.Label(label,text="               Success                    ").grid(column=0,row=6,columnspan=4)
            
            for i in range(6):
                if(i==0):
                    Dc1=str(year)+"/"+str(month)+"/"+str(day)
                    save("enlist:"+Dc1+"\n")
                elif(i==1):
                    Dc2=dc.Daycalc()
                    Dc2=Dc2.private(year,month,day)
                    save("private"+Dc2+"\n")
                elif(i==2):
                    Dc3=dc.Daycalc()
                    Dc3=Dc3.privatefirst(year,month,day)
                    save("privatefirst"+Dc3+"\n")
                elif(i==3):
                    Dc4=dc.Daycalc()
                    Dc4=Dc4.Corporal(year,month,day)
                    save("Corporal"+Dc4+"\n")
                elif(i==4):
                    Dc5=dc.Daycalc()
                    Dc5=Dc5.Sergeant(year,month,day)
                    save("sergeant"+Dc5+"\n")
                elif(i==5):
                    Dc6=dc.Daycalc()
                    Dc6=Dc6.discharge(year,month,day)
                    save("discharge"+Dc6+"\n")
                    
            # tab4 라벨 생성  
            self.ranklabel3=ttk.LabelFrame(tab,text='Consequence')
            self.ranklabel3.grid(column=0,row=7)
            
            # (tab4-라벨프레임 내) 라벨         
            ttk.Label(self.ranklabel3,text="Military enlist: "+Dc1).grid(column=0,row=8)
            ttk.Label(self.ranklabel3,text="Private(-): "+Dc2).grid(column=0,row=9)
            ttk.Label(self.ranklabel3,text="Private First(=):"+Dc3).grid(column=1,row=9)
            ttk.Label(self.ranklabel3,text="Corporal(=-): "+Dc4).grid(column=0,row=10)
            ttk.Label(self.ranklabel3,text="Sergeant(==): "+Dc5).grid(column=1,row=10)
            ttk.Label(self.ranklabel3,text="Military discharge: "+Dc6).grid(column=0,row=11)
            create_ToolTip(self.ranklabel3,'진급과 전역 날짜를 어림잡아 계산합니다. (입대/이병/일병/상병/병장/전역 순)')
        return start
    
    
    def saverepre(self):
        name=self.radioname.get()
        if(name==0):
            self.txt.delete(1.0,tk.END)
            savea=open("save.txt")
            saveb=savea.read()
            self.txt.insert('1.0',saveb)
            savea.close()
            
            s = ttk.Style()                     
            s.configure('Wild.TRadiobutton',foreground='red') 
            
            title=["Browse Note","Disappear Text","","Cover Note"]
            for ver in range(3):
                if(ver==2):
                    ver=3
            if(ver==3):
                radio=ttk.Radiobutton(self.notelabel2,text=title[ver], variable=self.radioname,value=ver,command=self.saverepre,style='Wild.TRadiobutton')
                radio.grid(column=ver-1, row=6)
            else:
                radio=ttk.Radiobutton(self.notelabel2,text=title[ver], variable=self.radioname,value=ver,command=self.saverepre)
                radio.grid(column=ver, row=6)
            ttk.Label(self.notelabel2,text="PLEASE READ USER TIP!!!").grid(column=1,row=7)
            
        elif(name==1):
            self.txt.delete(1.0,tk.END)
        elif(name==2):
            savea=open("save.txt","a")
            savec=self.txt.get(1.0,tk.END)
            savea.write(savec)
            savea.close()
        elif(name==3):
            savea=open("save.txt","w")
            savec=self.txt.get(1.0,tk.END)
            savea.write(savec)
            savea.close()
    
    def deletenote(self):
        savea=open("save.txt","w")
        savea.close()
        self.txt.delete(1.0,tk.END)
            
    def create_widgets(self):
        
        self.win.protocol("WM_DELETE_WINDOW",self.destroyWindow) # x창 치면 콜백함수를 실행하라 

        # 메뉴바 생성
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar) 
        
        # 메뉴 생성 및 아이템 생성
        file_menu = Menu(menu_bar,tearoff=0) # 메뉴안에 메뉴를 생성=>(메뉴 안) 빈 항목 생성
        menu_bar.add_cascade(label="Add",menu=file_menu)
        file_menu.add_command(label="Delete Note",command=self.deletenote) # 항목 추가
        file_menu.add_command(label="Exit",command=self.destroyWindow) # 항목 추가
        file_menu.add_command(label="Dev.",command=self.msgBox) # 항목 추가
            
        # 탬 컨트롤 생성
        tabControl=ttk.Notebook(self.win)
        tabControl.pack(expand=False,fill="x") 
        
        
        # 새로운 탭(탭1) 추가
        tab1=ttk.Frame(tabControl)
        tabControl.add(tab1, text="calculator")
        
        # 탭1안에 있는 위젯을 담는 프레임이자 라벨 위젯 (1행)
        frame = ttk.Label(tab1, text='')
        frame.grid(column=0, row=0)
        
        
        # 탭1- 체크버튼 (2행)
        self.scrnum=0
        check1 = tk.Checkbutton(frame, text="Lock Num",command=self.scrnumber)
        check1.deselect()
        check1.grid(column=3, row=1,sticky="E",pady=2)
        
        check2 = tk.Checkbutton(frame, text="Delete All",command=self.scrdelete)
        check2.deselect()
        check2.grid(column=4, row=1, sticky="E",pady=2)
        
        # 탭1- 스크롤드 텍스트 (3행)
        scrol_w = 50
        scrol_h =8
        self.scr = scrolledtext.ScrolledText(frame, width=scrol_w, height=scrol_h, wrap=tk.WORD,font=("Helvetica", 9))
        self.scr.grid(column=0, columnspan=5,sticky="WE")
        create_ToolTip(self.scr,'계산 진행 및 결과 창입니다.')
        
        # 탭1- 버튼 (4행 부분)
        bt1=ttk.Button(frame,text=1,width=10,command=self.falsetext(1))
        bt1.grid(column=0, row=3,sticky='W',pady=7,ipady=5)
        self.text1=bt1.cget("text") # 버튼1 객체에 있는 텍스트 속성 값 가져옴
        
        bt2=ttk.Button(frame,text=2, width=10,command=self.falsetext(2))
        bt2.grid(column=1, row=3,sticky='W',pady=7,ipady=5)
        self.text2=bt2.cget("text") 
        
        bt3=ttk.Button(frame,text=3, width=10,command=self.falsetext(3))
        bt3.grid(column=2, row=3,sticky='W',pady=7,ipady=5)
        self.text3=bt3.cget("text")
        
        bta=ttk.Button(frame,text="=", width=20,command=self.falsetext(10))
        bta.grid(column=3, row=3,pady=7,columnspan=2,sticky="WE",ipady=5)
        self.texta=bta.cget("text")
        create_ToolTip(bta,'계산 후에는 Delete ALL을 해주세요!!')

        
        # 탭1- 버튼(5행 부분)
        bt4=ttk.Button(frame,text="4", width=10,command=self.falsetext(4))
        bt4.grid(column=0, row=4,sticky='W',ipady=5)
        self.text4=bt4.cget("text")
        
        
        bt5=ttk.Button(frame,text="5", width=10,command=self.falsetext(5))
        bt5.grid(column=1, row=4,sticky='W',ipady=5)
        self.text5=bt5.cget("text")
        
        
        bt6=ttk.Button(frame,text="6", width=10,command=self.falsetext(6))
        bt6.grid(column=2, row=4,sticky='W',ipady=5)
        self.text6=bt6.cget("text")
        
        
        btb=ttk.Button(frame,text="+", width=10,command=self.falsetext(11))
        btb.grid(column=3, row=4,pady=7,sticky="WE",ipady=5) 
        self.textb=btb.cget("text")
        
        
        btc=ttk.Button(frame,text="-", width=10,command=self.falsetext(12))
        btc.grid(column=4, row=4,pady=7,sticky="WE",ipady=5)
        self.textc=btc.cget("text")
        
         
        
        # 탭1- 버튼(6행 부분)
        bt7=ttk.Button(frame,text="7", width=10,command=self.falsetext(7))
        bt7.grid(column=0, row=5,sticky='W',pady=7,ipady=5) 
        self.text7=bt7.cget("text")
        
        
        bt8=ttk.Button(frame,text="8", width=10,command=self.falsetext(8))
        bt8.grid(column=1, row=5,sticky='W',pady=7,ipady=5)
        self.text8=bt8.cget("text")
        
        
        bt9=ttk.Button(frame,text="9", width=10,command=self.falsetext(9))
        bt9.grid(column=2, row=5,sticky='W',pady=7,ipady=5)
        self.text9=bt9.cget("text")
        
        
        btd=ttk.Button(frame,text="x", width=10,command=self.falsetext(13))
        btd.grid(column=3, row=5,pady=7,sticky="WE",ipady=5)
        self.textd=btd.cget("text")
        
        bte=ttk.Button(frame,text="/", width=10,command=self.falsetext(14))
        bte.grid(column=4, row=5,pady=7,sticky="WE",ipady=5)
        self.texte=bte.cget("text")
        
        
        bt0=ttk.Button(frame,text="0", width=30,command=self.falsetext(0))
        bt0.grid(column=0, row=6,pady=7,sticky="WE",ipady=5,columnspan=3)
        self.text0=bt0.cget("text") 
        
        
        btf=ttk.Button(frame,text="^(1/2)", width=10,command=self.falsetext(15))
        btf.grid(column=3, row=6,pady=7,sticky="WE",ipady=5)
        self.textf=btf.cget("text")
        create_ToolTip(btf,'제곱근은 단일 계산만 가능합니다. ( ex)9^(1/2)=3 )')
        
        
        btg=ttk.Button(frame,text=".", width=10,command=self.falsetext(16))
        btg.grid(column=4, row=6,pady=7,sticky="WE",ipady=5)
        self.textg=btg.cget("text")
        
        
        
        # 새로운 탭(탭2) 추가
        tab2=ttk.Frame(tabControl)
        tabControl.add(tab2, text="bit unit")

        
        # 탭1- 체크버튼 (2행)
        self.scrnum2=0
        self.check21 = tk.Checkbutton(tab2, text="Lock All",command=self.scrnumber2)
        self.check21.deselect()
        self.check21.grid(column=2, row=0)
        
        self.check22 = tk.Checkbutton(tab2, text="Delete All Unit",command=self.scrdelete2)
        self.check22.deselect()
        self.check22.grid(column=3, row=0)
        
        # 탭2- 스크롤드 텍스트 (3행)
        scrol_w = 50
        scrol_h =9
        self.scr2 = scrolledtext.ScrolledText(tab2, width=scrol_w, height=scrol_h, wrap=tk.WORD,font=("Helvetica", 9))
        self.scr2.grid(column=0, columnspan=5,sticky="WE")
        create_ToolTip(self.scr2,'계산 진행 및 결과 창입니다.')
        
        
        # 탭2- 버튼 (4행 부분)
        bbt1=ttk.Button(tab2,text="1", width=10,command=self.falsetext(21))
        bbt1.grid(column=0, row=3,sticky='W',pady=7,ipady=5)
        self.text21=bbt1.cget('text')
        
        bbt2=ttk.Button(tab2,text="2", width=10,command=self.falsetext(22)) 
        bbt2.grid(column=1, row=3,sticky='W',pady=7,ipady=5)
        self.text22=bbt2.cget('text')
        
        
        bbt3=ttk.Button(tab2,text="3", width=10,command=self.falsetext(23))
        bbt3.grid(column=2, row=3,sticky='W',pady=7,ipady=5)
        self.text23=bbt3.cget('text')
        
        bbta=ttk.Button(tab2,text="=", width=20,command=self.falsetext(30))
        bbta.grid(column=3, row=3,pady=7,sticky="WE",ipady=5)
        self.text2a=bbta.cget('text')
        create_ToolTip(bbta,'계산 후에는 Delete ALL을 해주세요!!')
        
        # 탬2- 버튼(5행 부분)
        bbt4=ttk.Button(tab2,text="4", width=10,command=self.falsetext(24))
        bbt4.grid(column=0, row=4,sticky='W',ipady=5)
        self.text24=bbt4.cget('text')
        
        bbt5=ttk.Button(tab2,text="5", width=10,command=self.falsetext(25))
        bbt5.grid(column=1, row=4,sticky='W',ipady=5)
        self.text25=bbt5.cget('text')
        
        bbt6=ttk.Button(tab2,text="6", width=10,command=self.falsetext(26))
        bbt6.grid(column=2, row=4,sticky='W',ipady=5)
        self.text26=bbt6.cget('text')
                
        # 탭2- 콤보박스 위젯(5행)
        self.number=tk.StringVar()
        self.number_chosen=ttk.Combobox(tab2,width=20,textvariable=self.number,state= 'readonly')
        self.number_chosen['values']=('bit',"kilobit","megabit","gigabit")
        self.number_chosen.grid(column=3,row=4,ipady=5)
        self.number_chosen.current(0)
        self.number_chosen.bind("<<ComboboxSelected>>",self.scrcombobox)
        
        # 탭2- 버튼 (6행 부분)
        bbt7=ttk.Button(tab2,text="7", width=10,command=self.falsetext(27))
        bbt7.grid(column=0, row=5,sticky='W',pady=7,ipady=5) 
        self.text27=bbt7.cget('text')
        
        bbt8=ttk.Button(tab2,text="8", width=10,command=self.falsetext(28))
        bbt8.grid(column=1, row=5,sticky='W',pady=7,ipady=5)
        self.text28=bbt8.cget('text')
        
        bbt9=ttk.Button(tab2,text="9", width=10,command=self.falsetext(29))
        bbt9.grid(column=2, row=5,sticky='W',pady=7,ipady=5)
        self.text29=bbt9.cget('text')
        
        # 탭2- 콤보박스 위젯(6행)
        self.number2=tk.StringVar()
        self.number_chosen2=ttk.Combobox(tab2,width=20,textvariable=self.number2,state= 'readonly')
        self.number_chosen2['values']=("byte","kilobyte","megabyte","gigabyte")
        self.number_chosen2.grid(column=3,row=5,ipady=5)
        self.number_chosen2.current(0)
        self.number_chosen2.bind("<<ComboboxSelected>>",self.scrcombobox2)
        
        
        
        # 탭2- 버튼 위젯(7행) 
        bbt0=ttk.Button(tab2,text="0", width=30,command=self.falsetext(20))
        bbt0.grid(column=0, row=6,pady=7,sticky="WE",ipady=5,columnspan=3)
        self.text20=bbt0.cget('text')
        
        bbtb=ttk.Button(tab2,text="CHANGE", width=20,command=self.falsetext(31))
        bbtb.grid(column=3, row=6,pady=7,sticky="WE",ipady=5)
        self.text2b=bbtb.cget('text')
        create_ToolTip(bbtb,'(수+단위+change+단위) or (수+단위+단위+change)로 입력!!')
        
         # 새로운 탭(탭3) 추가
        tab3=ttk.Frame(tabControl)
        tabControl.add(tab3, text="Tri Function")
        
        ttk.Label(tab3,text="").grid(row=1)
        
        ques0=ttk.LabelFrame(tab3,text='Scope Setting')
        ques0.grid()
        
        ttk.Label(ques0,text="Scope: ",font=("TkDefaultFont", 20)).grid(column=0,row=1)
        self.scvn= tk.StringVar()    
        self.scv = ttk.Combobox(ques0, width=12,textvariable=self.scvn)
        self.scv['values']=("0~2pi","-2pi~2pi","-4pi~4pi","-6pi~6pi")
        self.scv.current(0)
        self.scv.grid(column=1, row=1) 
        create_ToolTip(self.scv,'삼각함수 범위를 지정해주세요')
        ttk.Label(tab3,text="").grid()

        
        ques=ttk.LabelFrame(tab3,text='Trigonometrical Function')
        ques.grid()
        
        # (tab3-라벨프레임 내) 라벨 + 엔트리 위젯+ 버튼
        
        self.sinname= tk.StringVar()    
        ttk.Label(ques,text="Sin(",font=("TkDefaultFont", 20)).grid(column=0,row=2)
        
        self.sinentry = ttk.Entry(ques, width=12,textvariable=self.sinname)
        self.sinentry.grid(column=1, row=2) 
        
        ttk.Label(ques,text="°)= ",font=("TkDefaultFont", 20)).grid(column=2,row=2)
        sinbt=ttk.Button(ques,text="Answer?",command=self.false_graph(1))
        sinbt.grid(column=3,row=2)
        create_ToolTip(sinbt,'삼각함수를 그리고 표시합니다.')
        
         # (tab3-라벨프레임 내) 라벨 + 엔트리 위젯
        ttk.Label(ques,text="cos(",font=("TkDefaultFont", 20)).grid(column=0,row=3)
    
        self.cosname= tk.StringVar()
        self.cosentry = ttk.Entry(ques, width=12, textvariable=self.cosname)
        self.cosentry.grid(column=1, row=3) 
        
        ttk.Label(ques,text="°)= ",font=("TkDefaultFont", 20)).grid(column=2,row=3)
        
        cosbt=ttk.Button(ques,text="Answer?",command=self.false_graph(2))
        cosbt.grid(column=3,row=3)
        create_ToolTip(cosbt,'삼각함수를 그리고 표시합니다.')

        
         # (tab3-라벨프레임 내) 라벨 + 엔트리 위젯
        ttk.Label(ques,text="tan(",font=("TkDefaultFont", 20)).grid(column=0,row=4)
        
        self.tanname= tk.StringVar()
        self.tanentry = ttk.Entry(ques, width=12, textvariable=self.tanname)
        self.tanentry.grid(column=1, row=4) 
        
        ttk.Label(ques,text="°)= ",font=("TkDefaultFont", 20)).grid(column=2,row=4)
        
        tanbt=ttk.Button(ques,text="Answer?",command=self.false_graph(3))
        tanbt.grid(column=3,row=4)
        
        ttk.Label(tab3,text="").grid(row=1)
        create_ToolTip(tanbt,'삼각함수를 그리고 표시합니다.')
        
        ques=ttk.LabelFrame(tab3,text='Trigonometrical Function')
        ques.grid()
        
        #----------------------------------------------------------------------------------#
        ttk.Label(tab3,text="").grid()

        #----------------------------------------------------------------------------------#
     
        ques2=ttk.LabelFrame(tab3,text='Making Function')
        ques2.grid(row=5)
        
        # (tab3-라벨프레임 내) 라벨 + 엔트리 위젯+ 버튼
        ttk.Label(ques2,text="Sin(",font=("TkDefaultFont", 20)).grid(column=0,row=6)
        
        self.sinname2= tk.StringVar()
        self.sincb = ttk.Combobox(ques2, width=12, textvariable=self.sinname2,state='readonly')
        self.sincb['values']=("x","1/2x","2x","sinX")
        self.sincb.current(0)
        self.sincb.grid(column=1, row=6) 
        ttk.Label(ques2,text=")= ",font=("TkDefaultFont", 20)).grid(column=2,row=6)
        
        sinbt2=ttk.Button(ques2,text="Draw",command=self.false_graph(4))
        sinbt2.grid(column=3,row=6)
        create_ToolTip(sinbt2,'선택한 삼각함수를 그립니다')

         # (tab3-라벨프레임 내) 라벨 + 엔트리 위젯
        ttk.Label(ques2,text="cos(",font=("TkDefaultFont", 20)).grid(column=0,row=7)
    
        self.cosname2= tk.StringVar()
        self.coscb = ttk.Combobox(ques2, width=12, textvariable=self.cosname2,state='readonly')
        self.coscb['values']=("x","1/2x","2x","cosX")
        self.coscb.current(0)
        self.coscb.grid(column=1, row=7) 
        
        ttk.Label(ques2,text=")= ",font=("TkDefaultFont", 20)).grid(column=2,row=7)
        
        cosbt2=ttk.Button(ques2,text="Draw",command=self.false_graph(5))
        cosbt2.grid(column=3,row=7)
        create_ToolTip(cosbt2,'선택한 삼각함수를 그립니다')

        
         # (tab3-라벨프레임 내) 라벨 + 엔트리 위젯
        ttk.Label(ques2,text="tan(",font=("TkDefaultFont", 20)).grid(column=0,row=8)
        
        self.tanname2= tk.StringVar()
        self.tancb = ttk.Combobox(ques2, width=12, textvariable=self.tanname2,state='readonly')
        self.tancb['values']=("x","1/2x","2x","tanX")
        self.tancb.current(0)
        self.tancb.grid(column=1, row=8) 
        
        ttk.Label(ques2,text=")= ",font=("TkDefaultFont", 20)).grid(column=2,row=8)
        
        tanbt2=ttk.Button(ques2,text="Draw",command=self.false_graph(6))
        tanbt2.grid(column=3,row=8)
        create_ToolTip(tanbt2,'선택한 삼각함수를 그립니다')
             
        # 새로운 탭(탭4) 추가
        tab4=ttk.Frame(tabControl)
        tabControl.add(tab4, text="RANK")
        
        # (tab4) 라벨 프레임
        ranklabel=ttk.LabelFrame(tab4,text='Description')
        ranklabel.grid()
        
        # (tab4-라벨프레임 내) 라벨
        ttk.Label(ranklabel,text="Military Calc",font=("TkDefaultFont", 20)).grid(column=1,row=1)
        ttk.Label(ranklabel,text="                  Represent your military rank and discharge dates.               ").grid(column=1,row=2)
        ttk.Label(ranklabel,text="   Please enter the date of military enlistment.").grid(column=1,row=3)
        create_ToolTip(ranklabel,'당신의  진급과 군전역 날짜를 나타냅니다. 군입대일을 입력하세요.')
        
        ttk.Label(tab4,text="").grid(row=1)
        
        # (tab4) 라벨 프레임
        ranklabel2=ttk.LabelFrame(tab4,text='Calculation')
        ranklabel2.grid(row=2)
        
        # (tab4-라벨프레임 내) 스핀박스 및 콤보박스
        ttk.Label(ranklabel2,text="[ Year ]").grid(column=0,row=3)
        
        self.yearname=tk.IntVar()
        self.year=tk.Spinbox(ranklabel2,from_=2015, to=2025,width=10,bd=2,textvariable=self.yearname)
        self.year.grid(column=0,row=4,padx=3)
        self.yearname.set("2018")
        
        ttk.Label(ranklabel2,text="[ Month ]").grid(column=1,row=3)

        self.monthname=tk.IntVar()
        month=ttk.Combobox(ranklabel2,width=7,textvariable=self.monthname)
        month['values']=(1,2,3,4,5,6,7,8,9,10,11,12)
        month.current(0)
        month.bind("<<ComboboxSelected>>",self.change_day)
        month.grid(column=1,row=4,padx=3)
        
        ttk.Label(ranklabel2,text="[ Day ]").grid(column=2,row=3)

        self.dayname=tk.IntVar()
        self.day=ttk.Combobox(ranklabel2,width=7,textvariable=self.dayname)
        self.day['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
        self.day.current(0)
        self.day.grid(column=2,row=4)
        
        rankbt=ttk.Button(ranklabel2,text="Start",command=self.military(ranklabel2,tab4))
        rankbt.grid(column=3,row=4,padx=5)
        
        # (tab4-라벨프레임 내) 프로그래스바 
        self.progress_bar=ttk.Progressbar(ranklabel2,orient='horizontal',length="330",mode='determinate')
        self.progress_bar.grid(column=0,row=5,columnspan=4,pady=4)
        
           # 새로운 탭(탭5) 추가
        tab5=ttk.Frame(tabControl)
        tabControl.add(tab5, text="Note")
        
        # (tab5) 라벨 프레임
        notelabel=ttk.LabelFrame(tab5,text='Description')
        notelabel.grid()
        
        # (tab5-라벨프레임 내) 라벨
        ttk.Label(notelabel,text="N.O.T.E",font=("TkDefaultFont", 20)).grid(column=1,row=1)
        ttk.Label(notelabel,text="                  Indicates the formula you have calcuclate so far.               ").grid(column=1,row=2)
        ttk.Label(notelabel,text="   Also you are free to write.").grid(column=1,row=3)
        create_ToolTip(notelabel,'계산한 수식들을 불러옵니다. 또한 자유롭게 작성할 수 있습니다.')
        
        self.txt = scrolledtext.ScrolledText(tab5, width=scrol_w, height=scrol_h+5, wrap=tk.WORD,font=("Verdana", 8))
        self.txt.grid(sticky="WE",column=0,row=2)
        
        self.notelabel2=ttk.LabelFrame(tab5,text="")
        self.notelabel2.grid(column=0,row=3)
        
        self.radioname=tk.IntVar()
        self.radioname.set(99)
        
        title=["Browse Note","Disappear Text","Add Note"]
        
        for ver in range(3):
            radio=ttk.Radiobutton(self.notelabel2,text=title[ver], variable=self.radioname,value=ver,command=self.saverepre)
            radio.grid(column=ver, row=6)
        
        
        ttk.Label(self.notelabel2,text="                                                      ").grid(column=1,row=7)
        create_ToolTip(self.notelabel2,'* USER TIP * \n\n= Browse Note: 노트(수식,내용)를 불러옵니다.\n  (화면의 내용을 지우고 불러옴!!)\n= Disappear Text: 화면의 내용을 지웁니다.\n= Add Note: 입력한 내용을 노트에 추가합니다. \n= Cover Note: 화면의 내용을 노트에 덮어쓰기합니다.\n  (기존에 중요한 내용이 있다면 지우지 마세요!!)\n= Delete Note: 노트 를 삭제합니다.[ Add메뉴에 위치 ]\n  (새 노트를  원하시면  Delete및 작성 후 cover를 누르세요!!)')

        self.scr.focus()
        self.scr2.focus()
        month.focus()

Main=main()
# 이벤트순환문 생성
Main.win.mainloop()
