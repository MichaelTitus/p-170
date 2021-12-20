from tkinter import * 

root = Tk()  
root.geometry("900x600") 
root.title("percentage calculator")
grade3=Label(root)
grade5=Label(root)
grade10=Label(root)

class grade_3():
    
    def __init__(self,Math,ELA):
        self.math=Math
        self.ela=ELA
        
        
    def percentage(self):
        total_marks=self.math+self.ela
        avg=total_marks/200
        percent=avg*100
        grade3["text"]=percent+"%"
class grade_5():
    
    def __init__(self,Math,ELA,SocialStudies):
        self.math=Math
        self.ela=ELA
        self.socialstudies=SocialStudies
        
    def percentage(self):
        total_marks=self.math+self.ela+self.socialstudies
        avg=total_marks/300
        percent=avg*100
        grade5["text"]=percent+"%"
class grade_10():
    
    def __init__(self,Math,ELA,SocialStudies,Science):
        self.math=Math
        self.ela=ELA
        self.socialstudies=SocialStudies
        self.science=Science
        
    def percentage(self):
        total_marks=self.math+self.ela+self.socialstudies+self.science
        avg=total_marks/400
        percent=avg*100
        grade10["text"]=percent+"%"        

obj_g3=grade_3(90,100)
btn3=Button(root,text="grade 3",command=obj_g3.percentage)
btn3.pack()
grade3.pack()

obj_g5=grade_5(69,72)
btn5=Button(root,text="grade 5",command=obj_g5.percentage)
btn5.pack()
grade5.pack()

obj_g10=grade_10(56,94)
btn10=Button(root,text="grade 10",command=obj_g10.percentage)
btn10.pack()
grade10.pack()


root.mainloop()