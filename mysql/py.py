#import requests
import mysql.connector
import streamlit as st



st.set_page_config(page_title="my web",page_icon=":🤖",layout="wide")
def local_css(file_name):#هذا الفنقشن مشان اجيب التصميم من ملف السي اس اس الي مخزنو في البرنامج
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")



#---connection بدي اعمل اتصال للبيانات واعطي الاتصال لمتغير
mydb=mysql.connector.connect(

  host="localhost",
  user="root",
  password="***********",
  database="crud_new1"

)

mycursor= mydb.cursor()
print("connection established")


#---------------بناء الموقع



def main():

 st.header("Data Base Mysql:wave:")
 "---"

 option = st.sidebar.selectbox("select",("Create","Read","Update","Delete"))
  

 if option =="Create":
    st.subheader("Create a Record")
    name=st.text_input("Enter Name",placeholder="name")
    email=st.text_input("Enter Email",placeholder="email")
    #submitted = st.form_submit_button("Save Data")
    #if submitted:
    if st.button("Create:"):
      sql= "insert into users(name,email) values(%s,%s)"
      val = (name,email)
      mycursor.execute(sql,val)
      mydb.commit()
      st.success("Done:✅")

 elif option =="Read":
   st.subheader("Read a Record")
   mycursor.execute("select * from users")
   result = mycursor.fetchall()#بتعطي او بتطبع الي جبتو من الداتا
   for row in result:
     st.write(row)
     #st.write(f"{row}")
 elif option =="Update":
   st.subheader("Update a Record")
   id = st.number_input("Enter ID",min_value=1)
   name = st.text_input("New Name")
   email = st.text_input("Enter Email")

   if st.button("Update"):
     sql = "update users set name=%s, email=%s where id =%s"
     val = (name,email,id)
     mycursor.execute(sql,val)
     mydb.commit()
     st.success("done ☑")
     


 elif option =="Delete":
   st.subheader("Delet a Record ❌")
   id = st.number_input("Enter ID",min_value=1)
   
   if st.button("Delete",type="primary"):
     sql = "delete from users where id =%s"
     val = (id,)
     mycursor.execute(sql,val)
     mydb.commit()
     st.success("Deleted")


 with st.container():
       st.write("---")
       st.header("GET IN TOUCH")
       st.write("##")#اعطاء مساحه 

       contact_form = """
          <form action="https://formsubmit.co/youseftiti08@gmail.com" method="POST">
              <input type="hidden" name="_captcha" value="false">هاي كود مشان يخفي التحقق من الايميل يعني يسهل على المستخدم يرسل ايميل بدون تحقق
     <input type="text" name="name" placeholder ="your name" required>
     <input type="email" name="email" placeholder="your email" required>
     <textarea name="message" placeholder="your message here" required></textarea>
     <button type="submit">Send</button>
     <button type = "need"> need</button>
</form>


"""
       st.markdown(contact_form, unsafe_allow_html=True)
             




if __name__ == "__main__":
  main()
