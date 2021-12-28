import tkinter as tk

class ToolTip(object):
    def __init__(self,widget):
         self.widget=widget
         self.tip_window=None

    def show_tip(self,tip_text):
        if self.tip_window or not tip_text:
            return
        x,y,_cx,cy=self.widget.bbox("insert") # 바운딩 박스,cx,cy는 폭과 높이, 문자를 표시하지 않으면 none을 반환
        x=x+self.widget.winfo_rootx()+130 # 부모 윈도우를 기준으로 해서 왼쪽의 x좌표와 윗면의  y좌표를 반환한다. 
        y=y+cy+self.widget.winfo_rooty()+150
        self.tip_window=tw=tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1) #데코레이션을 해주냐, 안해주냐  예를 들어 확채,축소,x그런게 다 데코레이션이다.
        tw.wm_geometry("+%d+%d"%(x,y)) #윈도우가 놓일 위치를 제어한다. 
        label=tk.Label(tw,text=tip_text,justify=tk.LEFT,background="#ffffe0",relief=tk.GROOVE,borderwidth=1,font=("tahomg","8","normal"))
        label.pack(ipadx=1)
            
    def hide_tip(self):
        tw=self.tip_window
        self.tip_window=None
        if tw:
            tw.destroy()
