import mysql.connector 
con=mysql.connector.connect(host="local host",user="root",password="devi",database='student')
cur=con.cursor()
def createusers():
    query="create table if not exists users(uid int primary key,username varchar(30) not null)"
    cur.execute(query)
    print("user table created successfully")
def createtansaction():
    query="CREATE TABLE if not exists transactions (tid int primary key auto_increment ,uid int not null unique ,ttype varchar(30) NOT NULL,     amount float NOT NULL,    category varchar(30),    tdate date  NOT NULL,    mode_of_transaction varchar(30)) "
    cur.execute(query)
    print("transaction table created successfully")
def create_budget():
    query="create table if not exists budgets( bid int auto_increment,uid int not null,budget_amount float not null,date1 date, date2 date"
    cur.execute(query)
def add_transaction():
    usid=int(input("enter user id:"))
    typ=input("enter transaction type(income/expense):")
    amt=float(input("enter the amount:"))
    cat=input("enter the category(shopping/salary/needs/bills/outing/etc):")
    dat=input("enter the date(dd/mm/year):")
    mod=input("enter mode of transaction(credit/debit/upi/cheque/online/etc):")
    query="INSERT INTO transactions ( uid,ttype, amount, category, tdate, mode_of_transaction) VALUES ({},'{}', {}, '{}', '{}', '{}')".format(usid,typ, amt, cat, dat, mod)
    cur.execute(query)
    con.commit()
    print("values inserted")
def add_user():
    usid=int(input("enter your user id:"))
    usernam=input("enter username:")
    query="INSERT INTO Users  VALUES ({},'{}')".format(usid,usernam)
    cur.execute(query)
    conn.commit()
    print("values inserted")
def update_user():
    uid=int(input("enter user id:"))
    username=input("enter the new username")
    query="update users set username='{}' where uid={}".format(uid,username)
    cur.execute(query)
    print("username updated successfully")
    con.commit()
def delete_user():
    uid=int(input("enter customer id to be deleted"))
    query="delete from users where cid={}".format(uid)
    cur.execute(query)
    print(" customer id deleted successfully")
    con.commit()
def update_transaction():
    usid=int(input("enter user id in which update has to be done"))
    query="select * from transactions where uid={}".format(usid)
    cur.execute(query)
    data = cur.fetchall
    print(data)
    tnid=("enter the transaction id in which update has to be done:")
    typ=input("enter the type of transaction;")
    amt=float(input("enter amount :"))
    cat=input("enter the category:")
    dat=input("enter the transaction date:")
    mod=input("enter mode of transaction:")
    query="update transactions set ttype='{}',amount={},category='{}',tdate='{}',mode_of_transaction='{}' where tid={}".format(typ,amt,cat,dat,mod,tnid)
    cur.execute(query)
    con.commit()
    print("transaction updated successfully")
def delete_transaction():
    usid=int(input("enter user id in which update has to be done"))
    query="select * from transactions where uid={}".format(usid)
    cur.execute(query)
    data = cur.fetchall()
    print(data)
    tnid=int(input("enter transaction id to be deleted: "))
    query="delete from transactions where tid={}".format(tnid)
    cur.execute(query)
    con.commit()
    print("transaction details deleted successfully")
def view_transactions():
    usid=int(input("enter transaction id :"))
    query="select t.tid,t.uid,t.type,t.amount,t.category,t.mode_of_transaction,u.username from transactions t, users u where t.uid=u.uid"
    cur.execute(query)
    data=cur.fetchall()
    print ("the details of transaction id",tnid ,"is")
    for i in data:
        print(i)
def tot_income():
    usid=int(input("enter user id to check your income:"))
    query="select sum(amount) from transactions where uid={} and ttype='income'".format(usid)
    cur.execute(query)
    total=cur.fetchone()
    print("total income=",total)
def tot_expense():
    usid=int(input("enter user id to check your expenses;"))
    query="select sum(amount)from transactions where ttype = 'expense' and uid={}".format(usid)
    cur.execute(query)
    total=cur.fetchone()
    print("total expense=",total)
def check_balance():
    usid=int(input("enter user id to check your current balance:"))
    q1="select sum(amount) from transactions where uid={} and ttype='income'".format(usid)
    cur.execute(q1)
    income=cur.fetchone()
    q2="select sum(amount)from transactions where ttype = 'expense' and uid={}".format(usid)
    cur.execute(q2)
    expense=cur.fetchone()
    balance=income-expense
    print("current total income=",income)
    print("current total expense=",expense)
    print("current balance =",balance)
def transactions_by_date():
    usid=int(input("enter user id :"))
    date1=input("enter the starting date(dd/mm/year):")
    date2=input("enter the ending date(dd/mm/year):")
    query="select * from transactions where uid ={} and date between '{}' and '{}'".format(usid,date1,date2)
    cur.execute(query)
    data=cur.fetchall()
    print("the transaction details between the date range",date1,"and",date2)
    for i in data:
        print(i)
def insert_budget():
    usid=int(input("enter user id:"))
    amt=float(input("enter the budget amount:"))
    dat1=input("enter starting date(dd/mm/year)")
    dat2=intput("enter ending date(dd/mm/year)")
    query="insert into budgets(uid,budget_ammount,date1,date2) values({},{},'{}','{}')".format(usid,amt,dat1,dat2)
    cur.execute(query)
    con.commit()
    print("buget inserted successfully")
def check_budget():
    usid=int(input("enter user id:"))
    dat1=input("enter starting date(dd/mm/year)")
    dat2=intput("enter ending date(dd/mm/year)")
    query1="select budget_amount from budgets where uid={} and date1='{}'and date2='{}'" 
    cur.execute(query1)
    budget=cur.fetchone()
    query2="select sum(amount)from transactions where ttype = 'expense' and uid={} and  tdate between '{}'and '{}'".format(usid,dat1,dat2)
    cur.execute(query2)
    expense=cur.fetchone()
    if expense < budget:
        print("the buget is:",budget)
        print("total expence is:",expense)
        print("buget achieved successfully!!")
    else:
        print("the buget is:",budget)
        print("total expence is:",expense)
        print("buget not achieved successfull")
def delete_budget():
    usid=int(input("enter user id:"))
    q1="select * from budgets where uid={}".format(usid)
    cur.execute(q1)
    data=cur.fetchall()
    print("tid,uid,budget_amount,date1,date2")
    for i in data:
        print(i)
    bgid=int(input("enter budget id  to be deleted;"))
    q2="delete from budgets where bid={}".format(bgid)
    cur.execute(q2)
    con.commit()
    print("budget details deleted successfully")
def update_budget():
    usid=int(input("enter user id:"))
    q1="select * from budgets where uid={}".format(usid)
    cur.execute(q1)
    data=cur.fetchall()
    print("tid,uid,budget_amount,date1,date2")
    for i in data:
        print(i)
    bgid=int(input("enter budget id  to be updated;"))
    bgamt=float(input("enter the  budget amount"))
    dat1=input("enter starting date(dd/mm/year):")    
    dat2=input("enter ending date(dd/mm/year)")
    q2="update budgets set budget_amount={},date1='{}',date2='{}' where bid={}".format(bgamt,dat1,dat2,bgid)
    cur.execute(q2)
    con.commit()
    print("budget updated successfully")
def view_transaction_by_mode():
    usid=int(input("enter user id:"))
    mod=input("enter mode of transaction(credit/debit/upi/cheque/online/etc):")
    query="select * from transactions where uid={} and mode_of_transaction={}".format(usid,mod)
    cur,execute(query)
    data=cur.fetchall()
    print("the transactions by the mode of transaction",mod,"is:")
    print("tid,uid,ttype,amt,category,tdate,mode of transaction")
    for i in data:
        print(i)
def view_budget():
    usid=int(input("enter user id:"))
    query="select b.bid,b.uid ,u.username,b.budget_amount,b.date1,b.date2 from budgets b , users u  where b.uid=u.uid and  b.uid={}".format(usid)
    cur.execute(query)
    data=cur.fetchall()
    print("the budgets for the user is:")
    print("budgetid,user id,username,budget amount,date1, date2")
    for i in data:
        print(i)
while True:
    print("1.add user")
    print("2.update user")
    print("3.delete user")
    print("4.add transaction")
    print("5.update transaction")
    print("6.delete transaction")
    print("7.view transactions")
    print("8.view total income")
    print("9.view total expense")
    print("10.view current balance")
    print("11.view transactions by date")
    print("12.view transactions by mode of transaction")
    print("13.insert budget")
    print("14.check budget")
    print("15.delete budget")
    print("16.update budget")
    print("17.view budget")
    ch=int(input("enter the no from menu to perform task:"))
    if ch=="1":
        add_user()
    elif ch=="2":
        update_user()
    elif ch=="3":
        delete_user()
    elif ch=="4":
        add_transaction()
    elif ch=="5":
        update_transaction()
    elif ch=="6":
        delete_transaction()
    elif ch=="7":
        view_transaction()
    elif ch=="8":
        tot_income()
    elif ch=="9":
        tot_expense()
    elif ch=="10":
        check_balance()
    elif ch=="11":
        transactions_by_date()
    elif ch=="12":
        view_transaction_by_mode()
    elif ch=="13":
        insert_budget()
    elif ch=="14":
        check_budget()
    elif ch=="15":
        delete_budget()
    elif ch=="16":
        update_budget()
    elif ch=="17":
        view_budget()
    else:
        break
