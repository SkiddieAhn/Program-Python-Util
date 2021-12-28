import tkinter as tk
from tkinter import ttk 
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as msg
from threading import Thread
from PIL import ImageTk,Image
import sys 
from _ast import Try
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys         
import time
import os
import urllib.request

'''
크롤링: selenium
이미지 다운로드: urllib.request
디렉토리 관련: os
시간 관련: time
GUI 프로그래밍: tkinter
참고 자료: https://yobbicorgi.tistory.com/29?category=478264
'''
# =============================================================================
# 종료 함수 
# =============================================================================  

# 초기에 프로그램 종료
def init_close(event):
    try:
        driver.close()
    except:
        pass
    win.destroy()
    sys.exit()

# 프로그램 종료 (x버튼)
def close1():
    try:
        driver.close()
    except:
        pass
    win.destroy()
    sys.exit()
    
# 프로그램 종료 (esc)
def close2(event):
    close1()

# =============================================================================
# 웹 관련 코드 (웹 드라이버, 웹 브라우저)
# =============================================================================  

''' 웹 드라이버 옵션 조정 '''
# 옵션 설정 
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')

# 콘솔창 하이드 옵션
args = ["hide_console"]

# 웹드라이버 전역변수
driver=0
driver_made=0

'''내 프로그램'''

# 웹 드라이버 생성 및 접속
def make_driver():
    # 전역 변수 수정해서 사용 
    global driver
    global driver_made

    driver=webdriver.Chrome('chromedriver',options=options,service_args=args)
    options.add_argument('headless')

    #구글 이미지 검색 접속
    driver.get("https://www.google.co.kr/imghp?hl=ko")
    time.sleep(3)

    # 모든 전처리 완료 
    driver_made=1

# 웹 브라우저 검색
def go_google(event):
    text.delete('1.0', tk.END)
    text.insert(tk.END,'구글 이미지 검색 ({})'.format(user_input.get()))
    url='https://www.google.co.kr/search?q='
    url+=user_input.get()
    url+='&hl=ko&tbm=isch&sxsrf=AOaemvJ_TVpUtznXXlPns_tyPZsJiRmn4g%3A1640673590837&source=hp&biw=1920&bih=969&ei=NrHKYZ3vL_KVr7wPyJa0sAg&iflsig=ALs-wAMAAAAAYcq_Rmm5AN4coM34fpiyzB8TvO88o9Hg&ved=0ahUKEwid4si08YX1AhXyyosBHUgLDYYQ4dUDCAY&uact=5&oq=car&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyCAgAEIAEELEDMgQIABADMgUIABCABDIICAAQgAQQsQMyCAgAEIAEELEDMgUIABCABDIICAAQgAQQsQMyCAgAEIAEELEDMgUIABCABDoHCCMQ7wMQJ1AAWNUCYOMDaABwAHgAgAFQiAHsAZIBATOYAQCgAQGqAQtnd3Mtd2l6LWltZw&sclient=img'
    webbrowser.open_new(url)


# =============================================================================
# 디렉토리 관련 함수 
# =============================================================================

# 디렉토리 생성
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. '+ directory)
        
# 파일 이름 다시 짓기
def sortAndRename(directory,keyword):
    file_list = [f for f in os.listdir(directory) if '.jpg' in f]
    num_list = sorted([int(l.split('_')[1].split('.')[0]) for l in file_list])
    count=0
    for idx in range(len(file_list)):
          src_file = directory +'/'+ keyword +'_{}.jpg'.format(num_list[idx])
          output = directory + '/'+ keyword +'_{}.jpg'.format(idx)
          text.insert(tk.END, '\n{}: {} --> {}'.format(keyword,num_list[idx], idx))
          text.see(tk.END)
          os.rename(src_file, output)
          count+=1
          if idx+1 == len(file_list):
                text.insert(tk.END,'\n파일 정리 완료: '+str(count)+'/'+str(len(file_list)))
                text.see(tk.END)

   
# =============================================================================
# 크롤링 관련 함수 
# =============================================================================

# 클로저 함수 사용 
def closure(event):
    def crawling():
        # 텍스트 초기화 
        text.delete('1.0', tk.END)
        pb['value']=0
        
        # 사용자가 입력한 수치가 있을 때 -> 수치만큼 다운로드
        user_input_num=user_input2.get()
        if user_input_num.isdigit():
            if int(user_input_num)>0:
                user_input_num=int(user_input_num)
            else:
                user_input_num=-1
        else:
            user_input_num=-1
        
        # ---------------------
        # 디렉토리 경로 설정
        # ---------------------
        search=str(user_input.get())
        entry.insert(tk.END,' (작업 중.....)')
        text.insert(tk.END,'경로 설정.....')
        keyword=search
        createFolder('./'+keyword+'_img_download')
        
        # ---------------------
        # 구글 이미지 검색
        # ---------------------
        text.insert(tk.END,'\n검색 ({}).....'.format(search))
        driver.get('https://www.google.co.kr/imghp?hl=ko')
        google_entry=driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
        google_entry.send_keys(keyword)
        driver.find_element_by_xpath('//*[@id="sbtc"]/button').click()
        
        # ---------------------
        # 스크롤링
        # ---------------------
        if user_input_num > 20 or user_input_num==-1:
            text.insert(tk.END,'\n더 많은 이미지 검색.....')
            elem=driver.find_element_by_tag_name('body')
            for i in range(60):
                elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(0.1)
            
            try:
                driver.find_element_by_class_name('mye4qd').click() # '결과 더 보기' 클릭
                for i in range(60):
                    elem.send_keys(Keys.PAGE_DOWN)
                    time.sleep(0.1)
            except:
                pass
        
        # ---------------------
        # 이미지 선택 및 개수 세기
        # ---------------------
        text.insert(tk.END,'\n다운로드 준비 중.....')
        links=[]
        images=driver.find_elements_by_css_selector('img.rg_i.Q4LuWd') # 페이지 요소 다중 선택 (클래스명 기준)
        for image in images:
            if image.get_attribute('src')!=None:
                links.append(image.get_attribute('src'))
        
        text.insert(tk.END,'\n찾은 이미지 개수: '+str(len(links)))
        time.sleep(2)
        pb['maximum']=len(links)
        
        # ---------------------
        # 다룬로드
        # ---------------------
        
        # 다운로드할 때마다 카운트 증가
        count=0
        for k,i in enumerate(links):
            url=i
            start=time.time()
            try:
                urllib.request.urlretrieve(url,'./'+keyword+'_img_download/'+keyword+'_'+str(k)+'.jpg')
                down_status='\n'+str(k+1)+'/'+str(len(links))+' '+keyword+' 다운로드 중...... Download time : '+str(time.time()-start)[:5]+'초'
                text.insert(tk.END,down_status)
                text.see(tk.END)
                count+=1
            except:
                fail='\n'+str(k+1)+'/'+str(len(links))+' '+keyword+' 다운로드 실패......'
                text.see(tk.END)
                text.insert(tk.END,fail)
                pass
            pb['value']=k
            pb.update()
            if k+1 == user_input_num or k+1 == len(links):
                # 프로그레스바 수정
                pb['value']=len(links)
                pb.update()
                # scrolledtext 수정
                text.insert(tk.END,'\n이미지 크롤링 완료: '+str(count)+'/'+str(len(links)))
                text.see(tk.END)
                # 디렉토리 열어서 확인
                path='./'+search+'_img_download'
                path = os.path.realpath(path)
                os.startfile(path)
                break
        
        # entry 원래대로
        entry.delete(0, tk.END)
        entry.insert(tk.END,search)

    return crawling


# =============================================================================
# 스레드 처리
# =============================================================================  

# (임시 윈도우) 스레드에서 메소드 실행
def init_threading():
    thread=Thread(target=make_driver)
    thread.setDaemon(True)
    thread.start() # 타겟된 메소드를 다른 코어에서 일 시작 
    
# (윈도우) 스레드에서 메소드 실행
def create_threading(event):
    crawling=closure(event)
    thread3=Thread(target=crawling)
    thread3.setDaemon(True)
    thread3.start() # 타겟된 메소드를 다른 코어에서 일 시작 


# =============================================================================
# 버튼 커맨드 함수 
# =============================================================================  

# (Go to Directory) 버튼 클릭
def opendir():
    text.delete('1.0', tk.END)
    path='./'+str(user_input.get())+'_img_download'
    path = os.path.realpath(path)
    try:
        text.insert(tk.END, '이동:'+path)
        os.startfile(path) 
    except:
        text.insert(tk.END, '\n지정된 파일을 찾을 수 없습니다:\n'+path)
          
# (raname) 버튼 클릭          
def rename():
    ret =msg.askyesno("Warning!!", str(user_input.get())+' 디렉토리를 정리하겠습니까?')
    if ret == True:
        text.delete('1.0', tk.END)
        path='./'+str(user_input.get())+'_img_download'
        text.insert(tk.END, '정리:'+path)
        try:
            sortAndRename(path,str(user_input.get()))
        except:
            text.insert(tk.END, '\n해당 디렉토리에서 작업을 처리할 수 없습니다!:\n'+path)
            
# (clear) 버튼 클릭     
def clear():
    pb['value']=0
    entry.delete(0, tk.END)
    entry2.delete(0, tk.END)
    text.delete('1.0', tk.END)
    
              
# =============================================================================
# 윈도우 라인 (기본 설정)
# =============================================================================      

# 윈도우 생성 
win=tk.Tk()
win.withdraw()
win.title("Google Image Crawling")
win.geometry("340x220")
win.wm_iconbitmap("skd.ico")
win.wm_protocol('WM_DELETE_WINDOW',close1)
win.bind('<Escape>',close2)

# 윈도우 가운데 
x=win.winfo_screenwidth()/2-150
y=win.winfo_screenheight()/2-150
win.wm_geometry("+%d+%d"%(x,y))

# 변수 파트 
user_input=tk.StringVar() #입력 엔트리에 바인딩할 변수
user_input2=tk.StringVar() #입력 엔트리2에 바인딩할 변수


# =============================================================================
# 임시 윈도우 라인
# =============================================================================  

# 임시 윈도우 생성 및 위치 지정 
ops=tk.Toplevel()
ops.configure(background="white")
ops.wm_overrideredirect(1)
ops.bind('<Escape>',init_close)
ops.geometry("320x250")

ox=ops.winfo_screenwidth()/2-150
oy=ops.winfo_screenheight()/2-150
ops.wm_geometry("+%d+%d"%(ox,oy)) 

# 이미지 설정 후 배치 
image=Image.open("skd.jpg")
image2=image.resize((320,210),Image.ANTIALIAS)
img=ImageTk.PhotoImage(image2)
panel=tk.Label(ops,image=img,relief=tk.FLAT,background="white")
panel.pack()

# 라벨 및 프로그레스바 배치 
infor=tk.Label(ops,text="Preparing",background="white")
infor.pack()

pb=ttk.Progressbar(ops,orient='horizontal',mode='determinate',length=320)
pb.pack()

# 스레드에서 웹 드라이버 실행 
init_threading()

# 상태에 맞춰 프로그레스바 진행 
pb['maximum']=115
for i in range(116):
    time.sleep(0.13)
    pb['value']=i
    pb.update()
    
    if(-1<i<10):# 0~9
        infor.configure(text="Preparing")
    elif ((i-10)%30==0): # 10,40,70,100
        infor.configure(text="Preparing.")
    elif ((i-20)%30==0): #20,50,80,110
        infor.configure(text="Preparing..")
    elif ((i%30)==0): #30,60,90
        infor.configure(text="Preparing...")
        
    if(driver_made==1):
        infor.configure(text="Web Driver run complete!!")
        pb['value']=115
        pb.update()
        time.sleep(0.5)
        break

# 마무리 
ops.destroy()
win.deiconify()


# =============================================================================
# 윈도우 라인 (GUI)
# =============================================================================  

# 라벨
tk.Label(win,text="Search:",foreground='red',background="#EAEAEA").grid(row=0,column=0,pady=2,padx=2)
tk.Label(win,text="Status:",foreground='red',background="#EAEAEA").grid(row=1,column=0,pady=2,padx=2)
tk.Label(win,text="Bar:",foreground='red',background="#EAEAEA").grid(row=2,column=0,pady=2,padx=2)

# 엔트리 (입력)
entry=tk.Entry(win,width=40,textvariable=user_input)
entry.grid(row=0,column=1,pady=2,columnspan=3)
entry.bind('<F1>',create_threading)
entry.bind('<Return>',go_google)

# 엔트리 (개수 입력)
entry2=tk.Entry(win,width=5,textvariable=user_input2)
entry2.grid(row=0,column=2,pady=4,columnspan=3)
entry2.bind('<F1>',create_threading)

# 진행 상태 알림
text=ScrolledText(win,width=38,height=10)
text.grid(row=1,column=1,pady=2,columnspan=3)

# 프로그레스바
pb=ttk.Progressbar(win,orient='horizontal',mode='determinate',length=283)
pb.grid(row=2,column=1,pady=2,columnspan=3)
pb['maximum']=100
pb['value']=0
pb.update()

# 버튼
bgo=tk.Button(win,text="Go to Directory",command=opendir)
bgo.grid(row=3,column=1,pady=1)

bre=tk.Button(win,text="Arrange File",command=rename)
bre.grid(row=3,column=2,pady=1)

bcl=tk.Button(win,text="Clear",command=clear)
bcl.grid(row=3,column=3,pady=1)

# 포커스 및 메인루프
entry.focus()
win.mainloop()
