from threading import Thread
import tkinter as tk
import random
import os 

def quit():
    win.destroy()
    
def cmd_start():
    x=win.winfo_screenwidth()/2+300
    y=win.winfo_screenheight()/2-150
    win.wm_geometry("+%d+%d"%(x,y))
    thread=Thread(target=real_start)
    thread.setDaemon(True)
    thread.start() # 타겟된 메소드를 다른 코어에서 일 시작 

def real_start():
    os.system("%windir%\system32\cmd.exe")
  
              
# 명령어(ffmpeg 파일이 있는 디렉토리로 이동) 복사
def precopy():
    win.clipboard_clear()
    win.clipboard_append("cd C:"+chr(92)+"ffmpeg conversion"+chr(92)+"ffmpeg-20200620-29ea4e1-win64-static"+chr(92)+"bin")
    entry.delete(0,tk.END)
    entry.insert(0,'precopy ok')
    
# 명령어 코드 반환
def html(event):
    
    # 파일 이름 랜덤 제작 (5철자)
    random_values=[0 for i in range(5)]
    name=''
    for i in range(5):
        random_values[i]=random.randint(97,122)
        if i==0:
            name=chr(random_values[i])
        else: 
            name=name+chr(random_values[i])
    
    # 코드 제작 및 반환 파트
    global s
    s1='ffmpeg.exe -i "'
    
    s2=id.get()
    try:
        # 크롬 플러그인 복사 링크일 때 
        # 영상 파일 링크 중 '#'를 기준으로 문자열을 나누고 두 번째 요소를 가져옴
        s2=s2.split('#')[1]
    except:
        # 크롬 플러그인 복사한 링크가 아닐 때
        pass
    
    s3='" -bsf:a aac_adtstoasc -c copy ./save/'+str(name)+'.mp4'
    s=s1+s2+s3 # 글로벌 변수 s
    text.insert('1.0',s)

# 엔트리 내용 제거, 텍스트 내용 복사 및 제거 
def delcopy():
    global s
    win.clipboard_clear()
    win.clipboard_append(s)
    win.update() # now it stays on the clipboard after the window is closed
    text.delete('1.0','end')
    entry.delete(0,tk.END)
    entry.focus()


#윈도우 생성 
win=tk.Tk()
win.title("M3u8 Command")
win.geometry("330x190")
win.protocol('WM_DELETE_WINDOW', quit)

# 변수 파트 
id=tk.StringVar() #입력 엔트리에 바인딩할 변수
global s,cmd_check # 글로벌 변수(입력값 합친거,cmd창 열렸나 체크)
s=str('0')

# 윈도우 가운데 
x=win.winfo_screenwidth()/2-150
y=win.winfo_screenheight()/2-150
win.wm_geometry("+%d+%d"%(x,y))

# 라벨
tk.Label(win,text="Entry:",foreground='red',background="#EAEAEA").grid(row=0,column=0,pady=2,padx=2)
tk.Label(win,text="Return:",foreground='red',background="#EAEAEA").grid(row=1,column=0,pady=2,padx=2)

# 엔트리 (입력)
entry=tk.Entry(win,width=40,textvariable=id)
entry.grid(row=0,column=1,pady=2,columnspan=3)
entry.bind('<Return>',html)

# 텍스트 (결과)
text=tk.Text(win,width=40,height=10)
text.grid(row=1,column=1,pady=2,columnspan=3)

# 버튼
cmd=tk.Button(win,command=cmd_start,text="cmd")
cmd.grid(row=2,column=1,pady=1)

pre=tk.Button(win,command=precopy,text="pre-copy")
pre.grid(row=2,column=2,pady=1)

delete=tk.Button(win,command=delcopy,text="Copy & Delete")
delete.grid(row=2,column=3,pady=1)

# 포커스 및 메인루프
entry.focus()
win.mainloop()
