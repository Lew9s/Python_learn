stu_list = []
def wel():
    #目录1
    print("欢迎")
    print('1.增加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.查询单个学生信息')
    print('5.查询全部学生信息')
    print('6.退出学生信息系统')
    order = input("请输入要执行操作的序号：")
    return order

def add_stu_info():
    #增加学生信息
    stu_num = input('请输入学号:')
    name = input('请输入姓名:')
    sex = input('请输入性别:')
    math = input('请输入高数成绩:')
    english = input('请输入英语成绩:')
    python = input('请输入Python成绩:')
    pe = input('请输入体育成绩:')
    moral = input('请输入德育成绩:')
    stu_info = {"学号":stu_num,"姓名":name, "性别":sex, "高数":math, "英语":english, "Python":python, "体育":pe, "德育":moral}
    stu_list.append(stu_info)
    print("添加成功")
        
def get_all_info():
    #查询全部
    for stu_info in stu_list:
        print(stu_info)
    
def del_stu_info():
    #删除信息
    name = input("请输入要删除的学生的名字:")
    #判断是否存在
    exist = False
    for stu in stu_list:
        if stu["姓名"] == name:
            exist = True
            stu_list.remove(stu)
            print("{}的信息删除成功".format(stu["姓名"]))
            
    if not exist:
        print("{}的信息不存在".format(name))  
        
def event():
    #目录2
    print("1.修改学号")
    print("2.修改性别")
    print("3.修改高数成绩")
    print("4.修改英语成绩")
    print("5.修改Python成绩")
    print("6.修改体育成绩")
    print("7.修改德育成绩")
    input_num = input("请输入对应序号：")
    return input_num
    
def modify_stu_info():
    #修改信息
    name = input("请输入要修改的学生的名字:")
    #判断是否存在
    exist = False
    for stu in stu_list:
        if stu["姓名"] == name:
            exist = True
            input_num = event()
            if input_num == "1":
               stu["学号"] = input("请输入修改后的学号：")
                   
            elif input_num == "2":
                stu["性别"] = input('请输入修改性别:')
                
            elif input_num == "3":
                stu["高数"] = input('请输入修改高数成绩:')
                
            elif input_num == "4":
                stu["英语"] = input('请输入修改英语成绩:')
                
            elif input_num == "5":
                stu["Python"] = input('请输入修改Python成绩:')
                
            elif input_num == "6":
                stu["体育"] = input('请输入修改体育成绩:')
                
            elif input_num == "7":
                stu["德育"] = input('请输入修改德育成绩:')
                
            print("{}的信息修改成功".format(stu["姓名"]))
            
    if not exist:
        print("{}的信息不存在".format(name))

def get_single_info():
    #查询单个
    name = input("请输入要查询的学生的姓名：")
    exist = False
    for stu in stu_list:
        if stu["姓名"] == name:
            exist = True
            print(stu)
            
    if not exist:
        print("{}的信息不存在".format(name))

def cal_gpa():
    #计算学分绩点
    for stu in stu_list:
        math = stu["高数"]
        if math < 60:
            a = 0
        else:
            a = (math - 60)/10 +1
            
        english = stu["英语"]
        if english <60:
            b = 0
        else:
            b = (english -60)/10 +1
            
        python = stu["Ptyhon"]
        if python < 60:
            c = 0
        else:
            c = (python - 60)/10 +1
            
        pe = stu["体育"]
        if pe <60:
            d = 0
        else:
            d = (pe - 60)/10 +1
            
        #GPA = (每门课的绩点*每门课的学分)/总学分
        gpa = (a*6 + b*3 + c*4.5)/(6+3+4.5)
        

def scholarship():
    


def main():
    #主要逻辑
    while True:
        order = wel()
        if order == "1":
            #增加信息
            add_stu_info()
            
        elif order == "2":
            #删除信息
            del_stu_info()
            
        elif order == "3":
            #修改信息
            modify_stu_info()
            
        elif order == "4":
            #查询单个
            get_single_info()
        elif order == "5":
            #查询全部
            get_all_info()
            
        elif order == "6":
            #退出
            print("已退出学生信息系统")
            break
 main()
