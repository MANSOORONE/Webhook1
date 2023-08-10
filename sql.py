import mysql.connector as mysql
def main():
    cn=mysql.connect(database=&quot;db6pm&quot;,user=&quot;root&quot;,password=&quot;root&quot;)
    c=cn.cursor()
    rno=int(input(&quot;Enter Rollno&quot;))
    c.execute(&quot;delete from student where rollno=%s&quot;,params=[rno])
    if c.rowcount==1:
    print(&quot;Student Deleted...&quot;)
    cn.commit()
    cn.close()
    else:
    print(&quot;Invalid Rollno&quot;)
main()
