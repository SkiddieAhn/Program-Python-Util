import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sys
import Tooltip as tt
import function
from tkinter import Menu
from tkinter import messagebox as msg
import os

def close(event):
    win.quit()
    win.destroy() # 하위 윈도우도 한 번에 닫힘!!

def tool(widget, text):
    toolTip=tt.ToolTip(widget)
    def enter(event):
        toolTip.show_tip(text)
    def leave(event):
        toolTip.hide_tip()
    widget.bind("<Enter>",enter)
    widget.bind("<Leave>",leave)

def active(widget,widget2):
    def enter(event):
        widget.configure(state="active")
    def leave(event):
        widget.configure(state="normal")
    if widget=="all":
        def enter2(event):
            fl.configure(state="active")
            sl.configure(state="active")
            tl.configure(state="active")
        def leave2(event):
            fl.configure(state="normal")
            sl.configure(state="normal")
            tl.configure(state="normal")       
        widget2.bind("<Enter>",enter2)
        widget2.bind("<Leave>",leave2)
        return None
    widget.bind("<Enter>",enter)
    widget.bind("<Leave>",leave)
    widget2.bind("<Enter>",enter)
    widget2.bind("<Leave>",leave)

def message(event):
    msg.askokcancel("도움말", "SL방송국과 카트라이더를 쉽게 넘나들 수 있는 프로그램!  'SL에디션'입니다.\n\n * 버튼 한 번으로 사이트 접속이 가능합니다! \n * 사용자 편한대로 설정이 가능합니다! \n * 자동 로그인 기능을 제공합니다! (계정 최대 3개) \n\n  [ 단축키 =>  Enter: 게임 시작, Esc: 프로그램 종료, F1: 도움말 \nF2: 프로그램 설정 , F3: 패치 안내, 오른쪽 클릭: 홈페이지까지만 이동 ] \n\n << 본 페이지를 다시 띄우려면  F1을 누르면 됩니다!! >> \n\n << 본 프로그램은 Microsoft Edge 환경을 요구합니다. >> \n\n << 본 프로그램은  대중화되기에 부적절하므로 일체 공유하지 마시기 바랍니다. >> \n\n << 계정에 대한 책임은 모두 본인에게 있습니다. >> \n\n Copyrightⓒ 2019. SHA All Rights Reserved")

# 시작 
win=tk.Tk()
win.configure(background="white")
win.wm_iconbitmap("picture/kart.ico")
win.wm_overrideredirect(1)


# 윈도우 가운데 
x=win.winfo_screenwidth()/2-150
y=win.winfo_screenheight()/2-150
win.wm_geometry("+%d+%d"%(x,y))

# 프로그램 처음 실행 시 나타나는 메시지 창
try:
    slmsg=open("c://sledition/slmsg.txt")
    slmsg.close()
except:
    msgv=msg.askokcancel("도움말", "SL방송국과 카트라이더를 쉽게 넘나들 수 있는 프로그램!  'SL에디션'입니다.\n\n * 버튼 한 번으로 사이트 접속이 가능합니다! \n * 사용자 편한대로 설정이 가능합니다! \n * 자동 로그인 기능을 제공합니다! (계정 최대 3개) \n\n  [ 단축키 =>  Enter: 게임 시작, Esc: 프로그램 종료, F1: 도움말\nF2: 프로그램 설정 , F3: 패치 안내, 오른쪽 클릭: 홈페이지까지만 이동 ] \n\n << 본 페이지를 다시 띄우려면  F1을 누르면 됩니다!! >> \n\n << 본 프로그램은 Microsoft Edge 환경을 요구합니다. >> \n\n << 본 프로그램은  대중화되기에 부적절하므로 일체 공유하지 마시기 바랍니다. >> \n\n << 계정에 대한 책임은 모두 본인에게 있습니다. >> \n\n Copyrightⓒ 2019. SHA All Rights Reserved")
    if msgv >0: 
        os.makedirs('c://sledition',exist_ok=True)
        slmsg=open("c://sledition/slmsg.txt","w")
        slmsg.write("stop")
        slmsg.close()
    else:
        sys.exit()

# 탭 컨트롤 생성
tabControl=ttk.Notebook(win)
tabControl.pack(expand=False,fill="y") 
        
        
# 새로운 탭(탭1) 추가
tab1=tk.Frame(tabControl,bg="#F6F6F6")
tabControl.add(tab1, text="게임시작")

# 디자인 오픈소스
mygreen = "#d2ffd2"
myred = "#dd0202"

style = ttk.Style()

style.theme_create( "sl", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": mygreen },
            "map":       {"background": [("selected", myred)],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )

style.theme_use("sl")


# 이미지 세팅
    
def imgresize(image,a,b): # 버튼 이미지 사이즈 설정 
    image = image.resize((a, b), Image.ANTIALIAS)
    return image

image=Image.open("picture/start.jpg")
image=imgresize(image,300,180)
start=ImageTk.PhotoImage(image)

image=Image.open("playbutton/play.png")
image=imgresize(image,85,40)
play=ImageTk.PhotoImage(image)

image=Image.open("picture/pretty.jpg")
image=imgresize(image,143,230)
pimg=ImageTk.PhotoImage(image)

image=Image.open("playbutton/yellow.png")
image=imgresize(image,152,44)
yellow=ImageTk.PhotoImage(image)

image=Image.open("playbutton/orange.png")
image=imgresize(image,152,44)
orange=ImageTk.PhotoImage(image)

image=Image.open("playbutton/red.png")
image=imgresize(image,152,44)
red=ImageTk.PhotoImage(image)

image=Image.open("stream/damtol.png")
image=imgresize(image,73,73)
damtol=ImageTk.PhotoImage(image)

image=Image.open("stream/ssieic.png")
image=imgresize(image,73,73)
ssieic=ImageTk.PhotoImage(image)

image=Image.open("stream/eunlen.png")
image=imgresize(image,73,73)
eunlen=ImageTk.PhotoImage(image)

image=Image.open("stream/jetty.png")
image=imgresize(image,73,73)
jetty=ImageTk.PhotoImage(image)

image=Image.open("stream/kyung.png")
image=imgresize(image,73,73)
kyung=ImageTk.PhotoImage(image)

image=Image.open("stream/ranker.png")
image=imgresize(image,73,73)
ranker=ImageTk.PhotoImage(image)

#--------------------------------------------------------------------------#
# 변수 정리 /인스턴스화 및 노트 정리  #
#--------------------------------------------------------------------------#

j=0 # 온/오프 변수

id1=tk.StringVar()
pw1=tk.StringVar()

demon=tk.IntVar() # 메인 버튼 메뉴 라디오 버튼 밸류와 바인딩될 변수 
demon2=tk.IntVar() # 시작 버튼 메뉴 라디오 버튼 밸류와 바인딩될 변수 

var1=tk.IntVar() # 메뉴 계정 파트 체크 버튼 밸류와 바인딩될 변수 
var2=tk.IntVar()
var3=tk.IntVar()

tar1=tk.StringVar() # 첫번째 계정 엔트리 밸류와 바인딩될 변수 
tar2=tk.StringVar()
tar3=tk.StringVar()

sar1=tk.StringVar() # 두번째 계정 엔트리 밸류와 바인딩될 변수 
sar2=tk.StringVar()
sar3=tk.StringVar()

ttar1=tk.StringVar() # 세번째 계정 엔트리 밸류와 바인딩될 변수 
ttar2=tk.StringVar()
ttar3=tk.StringVar()

f=function.func(win,tab1,id1,pw1)
s=function.setfunc(j,demon,demon2,f)

j=s.memorize() # 버튼 누르면 프로그램 꺼질지 안 꺼질지 세팅
s.kartstart(2)() # 초기 게임 시작 옵션 변수 설정
nic=s.fnotef()  
nic2=s.snotef()
nic3=s.tnotef()  


#--------------------------------------------------------------------------#
# 탭1(게임시작) GUI #
#--------------------------------------------------------------------------#


# 메인 버튼
main=tk.Button(tab1,image=start,relief=tk.FLAT,bg="white",command=s.kartstart(1)) 
main.grid(row=0,column=0,columnspan=3)
tool(main,"ESC:종료,F1:도움말,F2:설정")

# 라벨
tk.Label(tab1,text="ID:",foreground='red',background="#EAEAEA").grid(row=1,column=0,pady=2,padx=2)
tk.Label(tab1,text="PW:",foreground='red',background="#EAEAEA").grid(row=2,column=0,pady=2,padx=2)

# 엔트리
idbt=ttk.Entry(tab1,width=20,textvariable=id1)
idbt.grid(row=1,column=1,pady=2)
ttk.Entry(tab1,width=20,textvariable=pw1,show="*").grid(row=2,column=1,pady=2)

# 시작 버튼 
playbt=tk.Button(tab1,image=play,relief=tk.FLAT,command=f.callback2,bg="#F6F6F6")
playbt.grid(row=1,column=2,rowspan=2,pady=2)

#--------------------------------------------------------------------------#
# 탭2(자동시작) GUI #
#--------------------------------------------------------------------------#

# 새로운 탭(탭2) 추가
tab2=tk.Frame(tabControl,bg="#F6F6F6")
tabControl.add(tab2, text="자동시작")

"""1"""

first=tk.Button(tab2,relief=tk.FLAT,image=red,bg="#F6F6F6",command=f.callback(1,0)) 
first.grid(row=0,column=0)

fl=tk.Label(tab2,text=nic,bg="#F6F6F6", font='Helvetica 11 bold',foreground="red",activebackground="#EAEAEA",activeforeground="red")
fl.grid(row=1,column=0,pady=2,padx=2)


active(fl,first)

"""2"""

second=tk.Button(tab2,relief=tk.FLAT,image=orange,bg="#F6F6F6",command=f.callback(2,0)) 
second.grid(row=2,column=0)

sl=tk.Label(tab2,text=nic2,bg="#F6F6F6", font='Helvetica 11 bold',foreground="orange",activebackground="#EAEAEA",activeforeground="orange")
sl.grid(row=3,column=0,pady=2,padx=2)


active(sl,second)


"""3"""

third=tk.Button(tab2,relief=tk.FLAT,image=yellow,bg="#F6F6F6",command=f.callback(3,0)) 
third.grid(row=4,column=0)

tl=tk.Label(tab2,text=nic3,bg="#F6F6F6", font='Helvetica 11 bold',foreground="#FFE400",activebackground="#EAEAEA",activeforeground="yellow")
tl.grid(row=5,column=0,pady=2,padx=2)


active(tl,third)

pbt=tk.Button(tab2,relief=tk.FLAT,image=pimg,bg="#F6F6F6") 
pbt.grid(row=0,column=1,rowspan=6)
active("all",pbt)

#--------------------------------------------------------------------------#
# 탭3(SL방송국) GUI #
#--------------------------------------------------------------------------#

# 새로운 탭(탭3) 추가
tab3=ttk.Frame(tabControl)
tabControl.add(tab3, text="SL방송국")

tk.Button(tab3,relief=tk.FLAT,image=damtol,command=f.portal(2)).grid(row=0,column=0)
tk.Button(tab3,relief=tk.FLAT,image=ssieic,command=f.portal(3)).grid(row=0,column=1)
tk.Button(tab3,relief=tk.FLAT,image=eunlen,command=f.portal(4)).grid(row=1,column=0)
tk.Button(tab3,relief=tk.FLAT,image=jetty,command=f.portal(5)).grid(row=1,column=1)
tk.Button(tab3,relief=tk.FLAT,image=kyung,command=f.portal(6)).grid(row=2,column=0)
tk.Button(tab3,relief=tk.FLAT,image=ranker,command=f.portal(7)).grid(row=2,column=1)

slbt=tk.Button(tab3,relief=tk.FLAT,image=pimg,command=f.portal(8))
slbt.grid(row=0,column=2,rowspan=3)
tool(slbt,"SL카페로 이동~~!!")

#--------------------------------------------------------------------------#
# 설정 메뉴 계정 관리 GUI #
#--------------------------------------------------------------------------#

    
def fos(): # 1계정 윈도우
    
    def fosclose(event):
        fops.destroy()
        fops.quit()
        
    fops=tk.Toplevel(bg="#F6F6F6")
    fops.wm_iconbitmap("picture/kart.ico")
    fops.wm_geometry("+%d+%d"%(x+300,y))
    fops.title("첫 번째 계정")
    
    ttk.Label(fops,text="닉네임과  ID,PW를 입력하고  저장해주세요!!").grid(columnspan=3,pady=3)
    # 라벨
    tk.Label(fops,text="닉네임:").grid(row=1,column=0,pady=2,padx=2)
    tk.Label(fops,text="ID:").grid(row=2,column=0,pady=2,padx=2)
    tk.Label(fops,text="PW:").grid(row=3,column=0,pady=2,padx=2)

    # 엔트리
    fn=ttk.Entry(fops,width=20,textvariable=tar1)
    fn.grid(row=1,column=1,pady=3)
    fi=ttk.Entry(fops,width=20,textvariable=tar2)
    fi.grid(row=2,column=1,pady=2)
    fp=ttk.Entry(fops,width=20,show="*",textvariable=tar3)
    fp.grid(row=3,column=1,pady=3)
    
    # 체크 버튼 
    fchk=tk.Checkbutton(fops,text="활성화/비활성화",bg="#EAEAEA",variable=var1,command=s.fosclick) 
    fchk.grid(row=1,column=2,padx=3)
    
    # 저장버튼
    fbt=tk.Button(fops,text="저장",bg="#BDBDBD",command=s.fossave(tar1,tar2,tar3,fl))
    fbt.grid(row=3,column=2,padx=3,pady=3)
    # 함수 호출할 자리!!! 
    s.fossetting(fn,fi,fp,fchk,fops)
    
    fops.bind('<Escape>',fosclose)
    
    fops.mainloop()
        
def sos(): # 2계정 윈도우
    
    def sosclose(event):
        sops.destroy()
        sops.quit()
        
    sops=tk.Toplevel(bg="#F6F6F6")
    sops.wm_iconbitmap("picture/kart.ico")
    sops.wm_geometry("+%d+%d"%(x+300,y))
    sops.title("두 번째 계정")
    
    ttk.Label(sops,text="닉네임과  ID,PW를 입력하고 저장해주세요!!").grid(columnspan=3,pady=2)
    # 라벨
    tk.Label(sops,text="닉네임:").grid(row=1,column=0,pady=2,padx=2)
    tk.Label(sops,text="ID:").grid(row=2,column=0,pady=2,padx=2)
    tk.Label(sops,text="PW:").grid(row=3,column=0,pady=2,padx=2)

    # 엔트리
    sn=ttk.Entry(sops,width=20,textvariable=sar1)
    sn.grid(row=1,column=1,pady=2)
    si=ttk.Entry(sops,width=20,textvariable=sar2)
    si.grid(row=2,column=1,pady=2)
    sp=ttk.Entry(sops,width=20,show="*",textvariable=sar3)
    sp.grid(row=3,column=1,pady=2)
    
    # 체크 버튼 
    schk=tk.Checkbutton(sops,text="활성화/비활성화",bg="#EAEAEA",variable=var2,command=s.sosclick) 
    schk.grid(row=1,column=2,padx=3)
    
    # 저장버튼
    sbt=tk.Button(sops,text="저장",bg="#BDBDBD",command=s.sossave(sar1,sar2,sar3,sl))
    sbt.grid(row=3,column=2,padx=3,pady=3)
    # 함수 호출할 자리!!! 
    s.sossetting(sn,si,sp,schk,sops)

    sops.bind('<Escape>',sosclose)

    sops.mainloop()
        
def tos(): # 3계정 윈도우 
    
    def tosclose(event):
        tops.destroy()
        tops.quit()
        
    tops=tk.Toplevel(bg="#F6F6F6")
    tops.wm_iconbitmap("picture/kart.ico")
    tops.wm_geometry("+%d+%d"%(x+300,y))
    tops.title("세 번째 계정")
    
    ttk.Label(tops,text="닉네임과  ID,PW를 입력하고 저장해주세요!!").grid(columnspan=3,pady=2)
    # 라벨
    tk.Label(tops,text="닉네임:").grid(row=1,column=0,pady=2,padx=2)
    tk.Label(tops,text="ID:").grid(row=2,column=0,pady=2,padx=2)
    tk.Label(tops,text="PW:").grid(row=3,column=0,pady=2,padx=2)

    # 엔트리
    tn=ttk.Entry(tops,width=20,textvariable=ttar1)
    tn.grid(row=1,column=1,pady=2)
    ti=ttk.Entry(tops,width=20,textvariable=ttar2)
    ti.grid(row=2,column=1,pady=2)
    tp=ttk.Entry(tops,width=20,show="*",textvariable=ttar3)
    tp.grid(row=3,column=1,pady=2)
    
    # 체크 버튼 
    tchk=tk.Checkbutton(tops,text="활성화/비활성화",bg="#EAEAEA",variable=var3,command=s.tosclick) 
    tchk.grid(row=1,column=2,padx=3)
    
    # 저장버튼
    tbt=tk.Button(tops,text="저장",bg="#BDBDBD",command=s.tossave(ttar1,ttar2,ttar3,tl))
    tbt.grid(row=3,column=2,padx=3,pady=3)
    
    # 함수 호출할 자리!!! 
    s.tossetting(tn,ti,tp,tchk,tops)

    tops.bind('<Escape>',tosclose)

    tops.mainloop()

#--------------------------------------------------------------------------#
# 설정 윈도우(ops) GUI #
#--------------------------------------------------------------------------#

def opsfunc(self): # 프로그램 옵션 누르면 ops(설정창) 뜨게 함
    ops=tk.Toplevel(bg="#F6F6F6")
    ops.title("프로그램 설정")
    ops.wm_iconbitmap("picture/kart.ico")
    ops.wm_geometry("+%d+%d"%(x+300,y+150))
    ops.resizable(width=False, height=False)
    s.opsreceive(ops) #설정 윈도우 전달 
    
    #----------------------------화면 만들기(프로그램 자동 종료)--------------------------------------------#
    
    def opnotepath(): # opnote함수로 가게 해주는 함수
        global j
        j=s.opnote(check)
    
    ttk.Label(ops,text="아래 체크 버튼을 누르면, 버튼을 누를시 자동으로 프로그램이 종료됩니다.",background="#EAEAEA").grid()
    check=tk.Checkbutton(ops,text="ON/OFF",bg="white") # 체크버튼 클릭했을 때!!
    check.configure(command=opnotepath) #체크버튼 전달 
    check.grid()
    if (j%2)==0: # 체크버튼을 클릭하지 않아도 아래 소스는 무조건 실행되어야 함!!
        check.deselect()
        opstext=ttk.Label(ops,text="( 현재  OFF )",background="#EAEAEA").grid(row=2)
    else:
        check.select()
        opstext=ttk.Label(ops,text="( 현재  ON )",background="#EAEAEA").grid(row=2)
    ops.bind('<Escape>',s.close)
    
    #----------------------------메뉴 만들기(메인 버튼 옵션)--------------------------------------------#

    # 메뉴바 생성
    menu_bar = Menu(ops)
    # 첫 번째 메뉴
    file_menu = Menu(menu_bar,tearoff=0) 
    menu_bar.add_cascade(label="메인버튼 옵션",menu=file_menu)

    try: # try문 소스가 오류가 없으면(저장된 데이터가 있으면) 실행!!
        demon.set(s.setnum(1))
    except: # try문 소스가 오류가 있으면(저장된 데이터가 없으면) 실행!!
        pass # 이미 함수에서 초기값 0으로 세팅함
        
    name=["동작안함","로그인창","홈페이지","패치안내"]
    for i in range(4):
        file_menu.add_radiobutton(label=name[i],value=i,variable=demon,command=s.change)
    
    ops.config(menu=menu_bar)
    
   #-------------------------------(시작 옵션)-----------------------------------------#
   
    try: # try문 소스가 오류가 없으면(저장된 데이터가 있으면) 실행!!
        demon2.set(s.setnum(2))
    except:
        pass # 이미 함수에서 초기값 1로 세팅함
    # 두 번째 메뉴
    file_menu2 = Menu(menu_bar,tearoff=0) 
    menu_bar.add_cascade(label="시작 옵션",menu=file_menu2)

    name2=["홈페이지까지 동작","게임실행까지 동작"]
    for i in range(2):
        file_menu2.add_radiobutton(label=name2[i],value=i,variable=demon2,command=s.change)
    
    #-------------------------------(자동 로그인 옵션)-----------------------------------------#

    # 세 번째 메뉴
    file_menu3 = Menu(menu_bar,tearoff=0) 
    menu_bar.add_cascade(label="자동시작 옵션",menu=file_menu3)
    file_menu3.add_command(label="첫 번째 계정",command=fos) # 항목 추가
    file_menu3.add_command(label="두 번째 계정",command=sos) # 항목 추가
    file_menu3.add_command(label="세 번째 계정",command=tos) # 항목 추가
    
    #-----------------------------------------------------------------------------------#

    ops.mainloop()
  
#--------------------------------------------------------------------------#
# 키보드 키와 연결 #
#--------------------------------------------------------------------------#

playbt.bind('<Button-3>',f.callback3) #수동- 오른쪽 마우스 클릭 시 홈페이지로 이동되도록
first.bind('<Button-3>',f.callback3_1) #자동_계정1- 오른쪽 마우스 클릭 시 홈페이지로 이동되도록
second.bind('<Button-3>',f.callback3_2) #지동_계정2- 오른쪽 마우스 클릭 시 홈페이지로 이동되도록
third.bind('<Button-3>',f.callback3_3) #자동_계정3- 오른쪽 마우스 클릭 시 홈페이지로 이동되도록
win.bind('<Return>',f.callback1)
win.bind('<Escape>',close)
win.bind('<F1>',message)
win.bind('<F2>',opsfunc)
win.bind('<F3>',f.patch)


#--------------------------------------------------------------------------#

idbt.focus()
win.mainloop()




    



