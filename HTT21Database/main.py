from database import cursor, db

# def add_log(aa,bb,cc,dd,ee,ff,gg,hh,ii,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,user):
#     sql = ("INSERT INTO logs(0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,user) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
#     cursor.execute(sql, (aa,bb,cc,dd,ee,ff,gg,hh,ii,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,user, ))
#     db.commit()
#     log_id = cursor.lastrowid
#     print("Added log {}".format(log_id))

# def add_user(user):
#     add_log(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,user)

# def get_letter(id, letter):
#     if (ord(letter)>96 and ord(letter)<123):
#         sql = ("SELECT * FROM logs WHERE id = %s")
#         cursor.execute(sql, (id,))
#         result = cursor.fetchone()
#         x = int(ord(letter)-96)
#         return(result[x])
#     else:
#         print("not in range")
#         return("NOT IN RANGE")

def add_log(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,user):
    sql = ("INSERT INTO logs(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,user) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(sql, (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,user, ))
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))

def add_user(user):
    add_log(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,user)

def get_letter(id, letter):
    if (ord(letter)>96 and ord(letter)<123):
        sql = ("SELECT * FROM logs WHERE id = %s")
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        x = int(ord(letter)-96)
        return(result[x])
    else:
        print("not in range")
        return("NOT IN RANGE")

def add_letter(id, letter):
    x = ord(letter)
    if (x>54 and x<91):
        x = x+32
    if (x>96 and x<123):
        t = get_letter(id,chr(x)) + 1
        sql = ("UPDATE logs SET "+ letter + " = %s WHERE id = %s")
        cursor.execute(sql, (t, id))
        db.commit()
        print("Log updated")
    else:
        print("not in range")

def get_max(id):
    letter = 'a'
    value = get_letter(id, 'a')
    i = 1
    while (i < 26):
        print(chr(97+i))
        if (value < get_letter(id,chr(97+i))):
            value = get_letter(id,chr(97+i))
            letter = chr(97+i)
        i+=1
            
    return letter

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

add_user("yang")
# add_log('This is log two', 'Jeff')
# add_log('This is log three', 'Jane')

# add_letter(1,'u')
# print(get_max(1))
# print(get_letter(1,'y'))
# get_log(2)

# update_log(2, 'Updated log')

# delete_log(2)
# get_logs()