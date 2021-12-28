import tkinter as tk
from tkinter.scrolledtext import ScrolledText

# 복사 항목 카운팅 변수/ 누적 사이즈 변수
count=0
nsize=0
''' 누적 사이즈로 표시하는 이유:

    만일 (처리 개수/리스트 크기)라고 가정.
    3개 중 한 개가 빠져서 1/3이라고 표시했는데 2개가 더 들어오면 list.size()가 4가 되니 1/4가 됨
    이 때, 리스트 요소 개수도 4고 크기도 4인데 1개가 빠져 나갔다고 하면 혼동이 될 수 있음
    고로, 1/3에서 2개가 더 들어와 1/5가 됐다라고 표현하면 혼동이 안 됨
    그러므로 (처리 개수/누적 사이즈)로 표현함
    
    P.s. 처리 개수와 누적 사이즈는 리스트가 텅 비게 되면 0으로 변경됨 
'''

# text데이터 제거
def delete():
    text.delete(1.0,'end')
    text.focus()

# text데이터를 리스트로 만듬 (데이터가 널값이면 리스트에 추가 x)
def flist(event):
    global nsize # 함수에서 전역변수 nsize를 사용
    
    win.geometry("740x370") # 윈도우 사이즈부터 재조정 
    s=text.get(1.0,'end')
    sarray=s.split('\n')
    for i in sarray:
        if(i!=''):
            list.insert(tk.END,i)
            nsize+=1
    
    cl.configure(text="복사 완료: "+str(count)+"/"+str(nsize)) # 리스트가 있는 도중에 엔터를 누르면 nsize가 변하므로 라벨도 다시 보임
        
# 첫 번째 항목을 복사 / 이후 삭제 
def html():
    global count # 함수에서 전역변수 count를 사용
    global nsize # 함수에서 전역변수 nsize를 사용 
    
    # 리스트 크기가 1이상일 때만 진행 
    if(list.size()!=0):
        # 리스트 인덱스 0을 반환 (튜플로 반환됨) 이후 스트링형으로 저장
        tp=list.get(0,0)
        s=tp[0]
        
        # 복사/ 라벨로 알림 / 삭제 
        win.clipboard_clear()
        win.clipboard_append(s)
        win.update() # now it stays on the clipboard after the window is closed
        list.delete(0)
        # 삭제했는데 리스트에 남은게 없을 때 / 아닐 때 
        if(list.size()==0):
            count=0
            nsize=0
        else: count=count+1
        cl.configure(text="복사 완료: "+str(count)+"/"+str(nsize))
    else:
        print("리스트가 비었음")        

#윈도우 생성 
win=tk.Tk()
win.title("Return String")
win.geometry("710x370") 

# 윈도우 가운데 
x=win.winfo_screenwidth()/2-300
y=win.winfo_screenheight()/2-160
win.wm_geometry("+%d+%d"%(x,y))

# 라벨
tk.Label(win,text="입력:",foreground='red',background="#EAEAEA").grid(row=0,column=0,padx=2)
tk.Label(win,text="리스트:",foreground='red',background="#EAEAEA").grid(row=0,column=2,padx=2)
cl=tk.Label(win,text="",foreground='blue',background="#EAEAEA") # 복사 완료 개수 알리는 라벨 
cl.grid(row=1,column=2,padx=2)

# 텍스트
text=ScrolledText(win,width=40)
text.grid(row=0,column=1,padx=2)
text.bind('<Return>',flist)

# 스크롤 적용된 리스트 박스 
scrollbar = tk.Scrollbar(win, orient="vertical")
scrollbar.grid(row=0,column=4,sticky=tk.N+tk.S)

list=tk.Listbox(win,width=40,height=20,yscrollcommand=scrollbar.set)
list.grid(row=0,column=3,padx=2)
scrollbar.config(command=list.yview) #스크롤바 리스트박스에 연결 

# 버튼
delete=tk.Button(win,command=delete,text="텍스트 제거")
delete.grid(row=1,column=1,pady=10)

firstcopy=tk.Button(win,command=html,text="첫 번째 항목 복사")
firstcopy.grid(row=1,column=3,pady=10)

# 포커스 및 메인룹
text.focus()
win.mainloop()
