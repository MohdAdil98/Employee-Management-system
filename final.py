import streamlit as st
import mysql.connector
import pandas as pd
st.title("Employee Management System")
a=st.sidebar.selectbox("My Menu",("Home","Employer","Employee","Pdf related to EMS"))
if(a=="Home"):
    st.header("WELCOME")
    st.write("Hello this is a Employee Management System Application ")
    st.image("https://akriviahcm.com/blog/wp-content/uploads/2024/01/features-of-employee-management-system.png")
    st.video("https://videos.pexels.com/video-files/3129671/3129671-sd_640_360_30fps.mp4")
elif(a=="Employee"):     
    if "login" not in st.session_state:
        st.session_state["login"]=False
    emp_id=st.text_input("enter employee id")
    nam=st.text_input("enter the name")
    btn=st.button("login")
    if btn:
        mydb=mysql.connector.connect(host="127.0.0.1",user="root",password="root",database="employee")
        c=mydb.cursor()
        c.execute("select * from employee")
        for i in c:
            if(emp_id==i[0] and nam==i[1]):
                st.session_state["login"]=True
                break
        if(st.session_state["login"]==False):
            st.subheader("login unsucessfull")
    if(st.session_state["login"]==True):
        st.subheader("login sucessfull")
        ch=st.selectbox("features",("none","vacation day","going on leave"))
        if(ch=="vacation day"):
        
            mydb=mysql.connector.connect(host="127.0.0.1",user="root",password="root",database="employee")
            c=mydb.cursor()
            c.execute("select * from leav_e")   
            l=[]
            for r in c:
                l.append(r)
            df=pd.DataFrame(data=l,columns=["leave_id","salary_id","days"])
            st.dataframe(df)
        elif(ch=="going on leave"):
            leave_id=st.text_input("enter the leave_id") 
            salary_id=st.text_input("enter the no of  salary_id")
            days=st.text_input("enter the number of leave_day")
            btn2=st.button("Grant leave")
            if(btn2):
                mydb=mysql.connector.connect(host="127.0.0.1",user="root",password="root",database="employee")
                c=mydb.cursor()
                c.execute("insert into leav_e values(%s,%s,%s)",(leave_id,salary_id,days))
                mydb.commit()
                st.header("leave granted sucessfully")                
elif(a=="Employer"):
    if "loginn" not in st.session_state:
        st.session_state["loginn"]=False
    empr_id=st.text_input("enter employer_id")
    nam=st.text_input("enter the name")
    btn3=st.button("login")
    if btn3:
        mydb=mysql.connector.connect(host="127.0.0.1",user="root",password="root",database="employee")
        c=mydb.cursor()
        c.execute("select * from employer")
        for i in c:
            if(empr_id==i[0] and nam==i[1]):
                st.session_state["loginn"]=True
                break
        if(st.session_state["loginn"]==False):
            st.subheader("login unsucessfull")
    if(st.session_state["loginn"]==True):
        st.subheader("login sucessfull")
        x=st.selectbox("features",("none","job_dept","salary"))
        if(x=="job_dept"):
        
            mydb=mysql.connector.connect(host="127.0.0.1",user="root",password="root",database="employee")
            c=mydb.cursor()
            c.execute("select * from job_dept")   
            l=[]
            for r in c:
                l.append(r)
            df=pd.DataFrame(data=l,columns=["job_id","job_dept","Employee_id"])
            st.dataframe(df)
        elif(x=="salary"):
            salary_id=st.text_input("enter the salary_id") 
            amount=st.text_input("enter the no of  amount")
            job_id=st.text_input("enter the number of job_id")
            btn4=st.button("amount")
            if(btn4):
                mydb=mysql.connector.connect(host="127.0.0.1",user="root",password="root",database="employee")
                c=mydb.cursor()
                c.execute("insert into salary values(%s,%s,%s)",(salary_id,amount,job_id))
                mydb.commit()
                st.header("salary updated")   
       
elif(a=="Pdf related to EMS"):
    st.markdown("<h1>HELLO THIS EMPLOYEE MANAGEMENT APPLICATION</h2>",unsafe_allow_html=True)
    st.markdown('<iframe src="https://ymerdigital.com/uploads/YMER2205U2.pdf"></iframe>',unsafe_allow_html=True)
    
    