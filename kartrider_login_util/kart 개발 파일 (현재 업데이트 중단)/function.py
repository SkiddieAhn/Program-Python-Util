from selenium import webdriver
from time import sleep
import os
from tkinter import messagebox as msg
import tkinter as tk
import sys
from tkinter import ttk
from tkinter import Menu
import webbrowser

#------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------윈도우------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#

class func(object):
    def __init__(self,window,tab1,id,pw): # kartauto로부터 변수 받음 
        global ps #윈도우
        ps=window
        global win #탭1
        win=tab1 
        global id1 #id
        id1=id
        global pw1 #pw
        pw1=pw
        return None

    #--------------------------------------------------------------------------#
    # WebBrowser Function #
    #--------------------------------------------------------------------------#

    # 링크 이동 버튼들 
    def portal(self,n):
        def realcall():
            if (j%2)!=0 or (j%2)==0:
                if n==0: # 옵션0 카트라이더 (제로)
                    return None
                elif n==0.1: # 옵션1 카트라이더 (로그인)
                    webbrowser.open_new("https://nxlogin.nexon.com/common/login.aspx?redirect=http%3a%2f%2fkart.nexon.com%2fmain%2findex.aspx")
                elif n==0.5: # 옵션2 카트라이더 (홈피)
                    webbrowser.open_new("http://kart.nexon.com/main/index.aspx")            
                elif n==1: # 옵션3 카트라이더 (패치)
                    webbrowser.open_new("http://kart.nexon.com/Kart/News/Patch/List.aspx")  
                elif n==2: # 담톨 유튜브
                    webbrowser.open_new("https://www.youtube.com/user/fkdls00375")            
                elif n==3: # 씨익
                    webbrowser.open_new("http://bj.afreecatv.com/gmn105")            
                elif n==4: # 은렌
                    webbrowser.open_new("http://bj.afreecatv.com/dahwa4103")            
                elif n==5: # 제티
                    webbrowser.open_new("http://bj.afreecatv.com/spa7274")            
                elif n==6: # 경떨
                    webbrowser.open_new("http://bj.afreecatv.com/xxxxxx41")            
                elif n==7: # 랭커
                    webbrowser.open_new("http://bj.afreecatv.com/sgwoo9112")            
                elif n==8: # sl길드    
                    webbrowser.open_new("https://cafe.naver.com/slkartringa")            
            if (j%2)!=0:
                ps.quit()
                ps.destroy()
        return realcall
    
    def patch(self,event):
        webbrowser.open_new("http://kart.nexon.com/Kart/News/Patch/List.aspx")  
            
    #--------------------------------------------------------------------------#
    # Selenium 자동화 파트들  #
    #--------------------------------------------------------------------------#

    def finish(self,special):
        if demon2.get()==0 or special>0: # 홈페이지까지 이동이거나 오른 쪽 마우스 클릭 
            os.system("taskkill /im MicrosoftWebDriver.exe")
        elif demon2.get()==1: # 게임까지 이동(+) 왼쪽 마우스 클릭) 
            driver.find_element_by_xpath("//*[@class='btn_gamestart']/img").click()
            sleep(1)
            driver.close()
            os.system("taskkill /im MicrosoftWebDriver.exe")

    def callback(self,n,special): # special => 오른쪽 마우스 클릭하면 홈피까지만 이동
        def realcall():
            if (n==1 or special==1) and (notechk%2!=0): # 자동 계정1 
                idfull=noteid
                pwfull=notepw
            elif (n==1 or special==1) and (notechk%2)==0:
                return None
            
            elif (n==2 or special==2) and (notechk2%2!=0): # 자동 계정2
                idfull=noteid2
                pwfull=notepw2
            elif (n==2 or special==2) and (notechk2%2)==0:
                return None
            
            elif (n==3 or special==3) and (notechk3%2!=0): # 자동 계정3
                idfull=noteid3
                pwfull=notepw3
            elif (n==3 or special==3) and (notechk3%2)==0:
                return None       
                 
            else: # 수동 입력 
                if not id1.get() or not pw1.get():
                    msg.showerror('SL에디션','아이디 혹은 비밀번호가 입력되지 않았습니다')
                    return None
                idfull=id1.get()
                pwfull=pw1.get()
            
            global driver
            driver = webdriver.Edge('MicrosoftWebDriver')
            dfurl="https://nxlogin.nexon.com/common/login.aspx?redirect=http%3a%2f%2fkart.nexon.com%2fmain%2findex.aspx"
            erurl="https://nxlogin.nexon.com/common/login.aspx?redirect=http%3a%2f%2fkart.nexon.com%2fmain%2findex.aspx&n4errorcode=1"
            
            driver.get(dfurl)
            driver.implicitly_wait(10)
            
            a=driver.find_element_by_id("txtNexonID")
            b=driver.find_element_by_id("txtPWD")

            a.clear()
            driver.find_element_by_id("txtNexonID").send_keys(idfull)
    
            #----------자동 입력 시스템일 때 clear가 안 먹히므로 이렇게 세팅--------------
            b.send_keys("x")
            b.clear()
            #-----------------------------------------------------------
        
            driver.find_element_by_id("txtPWD").send_keys(pwfull)
                
            driver.find_element_by_id("btnLogin").click()
            sleep(1)
            
            if driver.current_url==erurl: # 오류 생겼을 때
                driver.close()
                os.system("taskkill /im MicrosoftWebDriver.exe")
                msg.showerror('SL에디션','아이디 혹은 비밀번호가 잘못되었습니다')
                    
            else:
                try:
                    self.finish(special)
                except:
                    driver.find_element_by_xpath("//*[@class='gnbFullBannerBtToday']").click()
                    self.finish(special)
                if (j%2)!=0: # 오프 설정 상태 
                    if demon2.get()==0 or (demon2.get()==1 and special>0): # 게임까지 이동(오른쪽,왼쪽 마우스 암거나) or (홈페이지까지 이동)이면서 (오른 쪽 마우스 클릭) 
                        os.system("taskkill /im MicrosoftWebDriver.exe")
                    ps.quit()
                    ps.destroy()

        return realcall

    def callback1(self,event): # 엔터와 연동됨 
        self.callback(0,0)()
    def callback2(self): # 버튼과 연동됨
        self.callback(0,0)()
    def callback3(self,event): # 수동 시작 오른쪽 마우스 홈페이지로 가게
        self.callback(0,0.5)() 
    def callback3_1(self,event):  # 자동 시작-계정1 오른쪽 클릭 홈페이지로 가게
        self.callback(0,1)()
    def callback3_2(self,event):  # 자동 시작-계정2 오른쪽 클릭 홈페이지로 가게
        self.callback(0,2)()
    def callback3_3(self,event):  # 자동 시작-계정3 오른쪽 클릭 홈페이지로 가게
        self.callback(0,3)()


#------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------설정창--------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#

class setfunc(object):
    def __init__(self,jreceive,dem,dem2,fr):
        global j #j (온/오프 변수)
        j=jreceive
        global demon #메뉴1 항목
        demon=dem 
        global demon2 #메뉴2 항목
        demon2=dem2
        global f #f인스턴스
        f=fr
        return None
    
    def opsreceive(self,opwindow):
        global ops #ops (설정창 윈도우)
        ops=opwindow

    
    def close(self,event):
        ops.destroy()
        ops.quit()
        
    #--------------------------------------------------------------------------#
    # 프로그램 설정 메뉴 (메인 버튼 및 시작옵션) #
    #--------------------------------------------------------------------------#

    def kartstart(self,n): # 메인 버튼 눌렀을 때 함수 호출:1, 초기 게임 시작 옵션 변수 설정:2
        def realstart(): # 프로그램이 처으 켜지고 실행
            global demon
            global demon2
            try:
                note=open("c://sledition/kart.txt")
                for line in note:
                    (num,num2)=line.split("/")
                demon.set(num)
                demon2.set(num2)
                note.close()
            except:
                if n==1:
                        demon.set(0)
                elif n==2:
                        demon2.set(1) # 메뉴2 초기 값 1
            if n==1:
                list=[0,0.1,0.5,1]
                f.portal(list[demon.get()])()
        return realstart
    
    def change(self): # 라디오버튼 눌렀을 때 노트 만들고 데이터 저장
        os.makedirs('c://sledition',exist_ok=True)
        note=open("c://sledition/kart.txt","w")
        note.write(str(demon.get()))
        note.write("/")
        note.write(str(demon2.get()))
        note.close()
    
    def setnum(self,n): # 저장된 데이터 가지고  메뉴 들어갔을 때 라디오버튼 세팅
        global demon
        global demon2
        note=open("c://sledition/kart.txt")
        for line in note:
            (num,num2)=line.split("/")
        demon.get(num)
        demon2.get(num2)
        note.close()
        if n==1:
            return demon
        elif n==2:
            return demon2

    #--------------------------------------------------------------------------#
    # 프로그램 설정 화면 파트 (프로그램 자동 종료) #
    #--------------------------------------------------------------------------#

    def memorize(self): # 프로그램 시작할 때 노트가 있는지 얻는지 확인하고 있다면 j값 가져와야 함 
        global j
        try:
            note2=open("c://sledition/op.txt")
            for i in note2:
                j=int(i)
            note2.close()
        except:
            note2=open("c://sledition/op.txt","w")
            note2.write(str(j))
            note2.close()
        return j
        
            
    def opnote(self,check): # j값 변경 후 체크버튼 상태 바꿈 
            global j
            j+=1
            note2=open("c://sledition/op.txt","w")
            note2.write(str(j))
            note2.close()
            self.memorize()
            if (j%2)==0: # command에 의해서 무조건 label 텍스트가 바뀜!!!
                check.deselect()
                opstext=ttk.Label(ops,text="( 현재  OFF )",background="#EAEAEA").grid(row=2)
            else:
                check.select()
                opstext=ttk.Label(ops,text="( 현재  ON )",background="#EAEAEA").grid(row=2)
            return j
    
                    
    #--------------------------------------------------------------------------#
    # 프로그램 설정 메뉴 (첫 번째 계정) #
    #--------------------------------------------------------------------------#
    
    def fwrite(self,noteida,notepwa): # 노트에 암호화하여 작성 
        test=open("c://sledition/first.txt","w")  # test= 암호화 테스트 파일 담을 변수
        test.write(notenic)
        test.write("/")
        # 암호화 시작
        for i in noteida:
            test.write(chr(ord(i)+6)) # 아스키코드에 6더한 것을 다시 바꾼 후 노트에 저장: ID
        test.write("/")
        for i in notepwa:
            test.write(chr(ord(i)+6)) # 아스키코드에 6더한 것을 다시 바꾼 후 노트에 저장: pw
        test.write("/")
        test.write(str(notechk))
        test.close()
    
    def fnotef(self): # 노트에서 값 불러오기 
        global notenic
        global noteid
        global notepw
        global notechk
        try:
            testb=open("c://sledition/first.txt") # testb= 복호화 테스트 파일 담을 변수
            for i in testb:
                (notenic,noteidb,notepwb,notechk1)=i.split("/") #noteidb = note id 복호화 필요 변수   
            notechk=int(notechk1)
            testb.close()            
            
            testb=open("c://sledition/first.txt","w") 

            # 복호화 시작
            for i in noteidb:
                testb.write(chr(ord(i)-6)) # 아스키코드에 6뺀 것을 다시 바꾼 후 노트에 저장: ID
            testb.write("/")
            for i in notepwb:
                testb.write(chr(ord(i)-6)) # 아스키코드에 6뺀 것을 다시 바꾼 후 노트에 저장: pw
            testb.close()
            
            # 복호화한거 변수로 저장
            testbcheck=open("c://sledition/first.txt")
            for i in testbcheck:
                (noteid,notepw)=i.split("/")
            testbcheck.close()
            
            self.fwrite(noteid,notepw) # 복호화했지만 파일은 암호화된 상태여야 하므로
                
        except:
            notenic="<< 첫 번째 계정 >>"
            noteid="default" 
            notepw="default"
            notechk=0
            self.fwrite(noteid,notepw) # 암호화 저장하기 위해 fwrite로 보냄

        return notenic # 닉네임만 건너줘 / 나머지 gui는 이 모듈에서 담당할테니 
            
            
    def fossetting(self,fn,fi,fp,fchkr,fopsr): # 첫 번째 계정 윈도우 세팅 
        global fchk # 체크버튼 
        global fops # 윈도우
        fops=fopsr
        
        fchk=fchkr
        fn.delete(0, 'end')
        fn.insert(tk.END,notenic)
        fi.delete(0, 'end')
        fi.insert(tk.END,noteid)
        fp.delete(0, 'end')
        fp.insert(tk.END,notepw)
        
        if (notechk%2)==0: 
            fchk.deselect()
            tk.Label(fops,text="(비활성화)").grid(row=2,column=2,pady=2,padx=2)
        else:
            fchk.select()
            tk.Label(fops,text="(활성화)").grid(row=2,column=2,pady=2,padx=2)
    
    def fosclick(self): #체크버튼 클릭했을 때!!
        global notechk
        notechk+=1
        self.fwrite(noteid,notepw)
        if (notechk%2)==0: 
            fchk.deselect()
            tk.Label(fops,text="(비활성화)").grid(row=2,column=2,pady=2,padx=2)
        else:
            fchk.select()
            tk.Label(fops,text="(활성화)").grid(row=2,column=2,pady=2,padx=2)
        return notechk
     
    
    def fossave(self,tar1r,tar2r,tar3r,fl): # 저장 버튼 클릭했을 때!!
        def realsave():
            global notenic
            notenic=str(tar1r.get())
            global noteid
            noteid=str(tar2r.get())
            global notepw
            notepw=str(tar3r.get())
            self.fwrite(noteid,notepw) # 엔트리에 입력한 아디,비번을 암호화 저장하기 위해 fwrite로 보냄 
            
            fl.configure(text=notenic)
        return realsave
    
    #--------------------------------------------------------------------------#
    # 프로그램 설정 메뉴 (두 번째 계정) #
    #--------------------------------------------------------------------------#
    
    def swrite(self,noteida2,notepwa2): # 노트에 암호화하여 작성 
        test2=open("c://sledition/second.txt","w")  # test2= 암호화 테스트 파일 담을 변수
        test2.write(notenic2)
        test2.write("/")
        # 암호화 시작
        for i in noteida2:
            test2.write(chr(ord(i)+6)) # 아스키코드에 6더한 것을 다시 바꾼 후 노트에 저장: ID
        test2.write("/")
        for i in notepwa2:
            test2.write(chr(ord(i)+6)) # 아스키코드에 6더한 것을 다시 바꾼 후 노트에 저장: pw
        test2.write("/")
        test2.write(str(notechk2))
        test2.close()
    
    def snotef(self): # 노트에서 값 불러오기 
        global notenic2
        global noteid2
        global notepw2
        global notechk2
        try:
            testb2=open("c://sledition/second.txt") # testb2= 복호화 테스트 파일 담을 변수
            for i in testb2:
                (notenic2,noteidb2,notepwb2,notechk1)=i.split("/") #noteidb2 = note2 id 복호화 필요 변수   
            notechk2=int(notechk1)
            testb2.close()            
            
            testb2=open("c://sledition/second.txt","w") 

            # 복호화 시작
            for i in noteidb2:
                testb2.write(chr(ord(i)-6)) # 아스키코드에 6뺀 것을 다시 바꾼 후 노트에 저장: ID
            testb2.write("/")
            for i in notepwb2:
                testb2.write(chr(ord(i)-6)) # 아스키코드에 6뺀 것을 다시 바꾼 후 노트에 저장: pw
            testb2.close()
            
            # 복호화한거 변수로 저장
            testbcheck2=open("c://sledition/second.txt")
            for i in testbcheck2:
                (noteid2,notepw2)=i.split("/")
            testbcheck2.close()
            
            self.swrite(noteid2,notepw2) # 복호화했지만 파일은 암호화된 상태여야 하므로
                
        except:
            notenic2="<< 두 번째 계정 >>"
            noteid2="default" 
            notepw2="default"
            notechk2=0
            self.swrite(noteid2,notepw2) # 암호화 저장하기 위해 swrite로 보냄

        return notenic2 # 닉네임만 건너줘 / 나머지 gui는 이 모듈에서 담당할테니 
            
            
    def sossetting(self,sn,si,sp,schkr,sopsr): # 첫 번째 계정 윈도우 세팅 
        global schk # 체크버튼 
        global sops # 윈도우
        sops=sopsr
        
        schk=schkr
        sn.delete(0, 'end')
        sn.insert(tk.END,notenic2)
        si.delete(0, 'end')
        si.insert(tk.END,noteid2)
        sp.delete(0, 'end')
        sp.insert(tk.END,notepw2)
        
        if (notechk2%2)==0: 
            schk.deselect()
            tk.Label(sops,text="(비활성화)").grid(row=2,column=2,pady=2,padx=2)
        else:
            schk.select()
            tk.Label(sops,text="(활성화)").grid(row=2,column=2,pady=2,padx=2)
    
    def sosclick(self): #체크버튼 클릭했을 때!!
        global notechk2
        notechk2+=1
        self.swrite(noteid2,notepw2)
        if (notechk2%2)==0: 
            schk.deselect()
            tk.Label(sops,text="(비활성화)").grid(row=2,column=2,pady=2,padx=2)
        else:
            schk.select()
            tk.Label(sops,text="(활성화)").grid(row=2,column=2,pady=2,padx=2)
        return notechk2
     
    
    def sossave(self,sar1r,sar2r,sar3r,sl): # 저장 버튼 클릭했을 때!!
        def realsave2():
            global notenic2
            notenic2=str(sar1r.get())
            global noteid2
            noteid2=str(sar2r.get())
            global notepw2
            notepw2=str(sar3r.get())
            self.swrite(noteid2,notepw2) # 엔트리에 입력한 아디,비번을 암호화 저장하기 위해 swrite로 보냄 
            
            sl.configure(text=notenic2)

        return realsave2
    
    #--------------------------------------------------------------------------#
    # 프로그램 설정 메뉴 (세 번째 계정) #
    #--------------------------------------------------------------------------#
    
    def twrite(self,noteida3,notepwa3): # 노트에 암호화하여 작성 
        test3=open("c://sledition/third.txt","w")  # test3= 암호화 테스트 파일 담을 변수
        test3.write(notenic3)
        test3.write("/")
        # 암호화 시작
        for i in noteida3:
            test3.write(chr(ord(i)+6)) # 아스키코드에 6더한 것을 다시 바꾼 후 노트에 저장: ID
        test3.write("/")
        for i in notepwa3:
            test3.write(chr(ord(i)+6)) # 아스키코드에 6더한 것을 다시 바꾼 후 노트에 저장: pw
        test3.write("/")
        test3.write(str(notechk3))
        test3.close()
    
    def tnotef(self): # 노트에서 값 불러오기 
        global notenic3
        global noteid3
        global notepw3
        global notechk3
        try:
            testb3=open("c://sledition/third.txt") # testb3= 복호화 테스트 파일 담을 변수
            for i in testb3:
                (notenic3,noteidb3,notepwb3,notechk1)=i.split("/") #noteidb3 = note3 id 복호화 필요 변수   
            notechk3=int(notechk1)
            testb3.close()            
            
            testb3=open("c://sledition/third.txt","w") 

            # 복호화 시작
            for i in noteidb3:
                testb3.write(chr(ord(i)-6)) # 아스키코드에 6뺀 것을 다시 바꾼 후 노트에 저장: ID
            testb3.write("/")
            for i in notepwb3:
                testb3.write(chr(ord(i)-6)) # 아스키코드에 6뺀 것을 다시 바꾼 후 노트에 저장: pw
            testb3.close()
            
            # 복호화한거 변수로 저장
            testbcheck3=open("c://sledition/third.txt")
            for i in testbcheck3:
                (noteid3,notepw3)=i.split("/")
            testbcheck3.close()
            
            self.twrite(noteid3,notepw3) # 복호화했지만 파일은 암호화된 상태여야 하므로
                
        except:
            notenic3="<< 세 번째 계정 >>"
            noteid3="default" 
            notepw3="default"
            notechk3=0
            self.twrite(noteid3,notepw3) # 암호화 저장하기 위해 fwrite로 보냄

        return notenic3 # 닉네임만 건너줘 / 나머지 gui는 이 모듈에서 담당할테니 
            
            
    def tossetting(self,tn,ti,tp,tchkr,topsr): # 첫 번째 계정 윈도우 세팅 
        global tchk # 체크버튼 
        global tops # 윈도우
        tops=topsr
        
        tchk=tchkr
        tn.delete(0, 'end')
        tn.insert(tk.END,notenic3)
        ti.delete(0, 'end')
        ti.insert(tk.END,noteid3)
        tp.delete(0, 'end')
        tp.insert(tk.END,notepw3)
        
        if (notechk3%2)==0: 
            tchk.deselect()
            tk.Label(tops,text="(비활성화)").grid(row=2,column=2,pady=2,padx=2)
        else:
            tchk.select()
            tk.Label(tops,text="(활성화)").grid(row=2,column=2,pady=2,padx=2)
    
    def tosclick(self): #체크버튼 클릭했을 때!!
        global notechk3
        notechk3+=1
        self.twrite(noteid3,notepw3)
        if (notechk3%2)==0: 
            tchk.deselect()
            tk.Label(tops,text="(비활성화)").grid(row=2,column=2,pady=2,padx=2)
        else:
            tchk.select()
            tk.Label(tops,text="(활성화)").grid(row=2,column=2,pady=2,padx=2)
        return notechk3
     
    
    def tossave(self,ttar1r,ttar2r,ttar3r,tl): # 저장 버튼 클릭했을 때!!
        def realsave3():
            global notenic3
            notenic3=str(ttar1r.get())
            global noteid3
            noteid3=str(ttar2r.get())
            global notepw3
            notepw3=str(ttar3r.get())
            self.twrite(noteid3,notepw3) # 엔트리에 입력한 아디,비번을 암호화 저장하기 위해 twrite로 보냄 
            
            tl.configure(text=notenic3)
        return realsave3
        
