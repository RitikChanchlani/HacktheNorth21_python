from database import cursor, db

user_id=0

def add_log(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,user):
    sql = ("INSERT INTO logs(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,user) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(sql, (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,user, ))
    db.commit()
    log_id = cursor.lastrowid
    user_id = log_id
    print(user_id)
    print("Added log {}".format(log_id))

def add_user(user):
    add_log(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,user)

def get_letter(id, letter):
    sql = ("SELECT * FROM logs WHERE id = %s")
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    x = int(ord(letter)-96)

    print(result[x])

def add_letter(id, letter):
    t = 1
    if (letter == 'a'):
        sql = ("UPDATE logs SET "+ letter + " = %s WHERE id = %s")
        cursor.execute(sql, (t, id))
        db.commit()
    print("Log updated")


def get_logs():
    sql = ("SELECT * FROM logs ORDER BY id DESC")
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(row[1])



    
# def get_logs():
#     sql = ("SELECT * FROM logs ORDER BY created DESC")
#     cursor.execute(sql)
#     result = cursor.fetchall()

#     for row in result:
#         print(row[1])


# def get_log(id):
#     sql = ("SELECT * FROM logs WHERE id = %s")
#     cursor.execute(sql, (id,))
#     result = cursor.fetchone()

#     for row in result:
#         print(row)


# def update_log(id, text):
#     sql = ("UPDATE logs SET text = %s WHERE id = %s")
#     cursor.execute(sql, (text, id))
#     db.commit()
#     print("Log updated")


# def delete_log(id):
#     sql = ("DELETE FROM logs WHERE id = %s")
#     cursor.execute(sql, (id,))
#     db.commit()
#     print("Log removed")

# add_user("yang")
# add_log('This is log two', 'Jeff')
# add_log('This is log three', 'Jane')

add_letter(1,'a')
get_letter(1,'a')
# get_log(2)

# update_log(2, 'Updated log')

# delete_log(2)
# get_logs()