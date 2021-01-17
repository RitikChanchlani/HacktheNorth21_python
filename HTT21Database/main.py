from database import cursor, db

def add_log(aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,user):
    sql = ("INSERT INTO logs(zero,one,two,three,four,five,six,seven,eight,nine,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,user) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(sql, (aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,user, ))
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))

def add_user(user):
    add_log(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,user)

def get_letter(id, letter):
    sql = ("SELECT * FROM logs WHERE id = %s")
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    if (ord(letter)>96 and ord(letter)<123):
        x = int(ord(letter)-96)
        return(result[x+10])
    elif (ord(letter)>47 and ord(letter)<58):
        x = int(ord(letter)-47)
        return(result[x])
    else:
        print("not in range")
        return("NOT IN RANGE")

def add_letter(id, letter):
    x = ord(letter)
    if (x>60 and x<91):
        x = x+32
    if (x>96 and x<123):
        t = get_letter(id,chr(x)) + 1
        sql = ("UPDATE logs SET "+ letter + " = %s WHERE id = %s")
        cursor.execute(sql, (t, id))
        db.commit()
    elif (x>47 and x<58):
        m='zero'
        if (letter == '0'):
            m = 'zero'
        elif (letter == '1'):
            m = 'one'
        elif (letter == '2'):
            m = 'two'
        elif (letter == '3'):
            m = 'three'
        elif (letter == '4'):
            m = 'four'
        elif (letter == '5'):
            m = 'five'
        elif (letter == '6'):
            m = 'six'
        elif (letter == '7'):
            m = 'seven'
        elif (letter == '8'):
            m = 'eight'
        elif (letter == '9'):
            m = 'nine'
        t = get_letter(id,chr(x)) + 1
        sql = ("UPDATE logs SET "+ m + " = %s WHERE id = %s")
        cursor.execute(sql, (t, id))
        db.commit()
    else:
        print(ord(letter))

def get_max(id):
    letter = 'a'
    value = get_letter(id, 'a')
    i = 1
    t = 1
    while (i < 26):
        if (value < get_letter(id,chr(97+i))):
            value = get_letter(id,chr(97+i))
            letter = chr(97+i)
        i+=1  
    while (t < 11):
        if (value < get_letter(id,chr(47+t))):
            value = get_letter(id,chr(47+t))
            letter = chr(47+t)
        t += 1
    return letter

def get_min(id):
    letter = 'a'
    value = get_letter(id, 'a')
    i = 1
    t = 1
    while (i < 26):
        if (value > get_letter(id,chr(97+i))):
            value = get_letter(id,chr(97+i))
            letter = chr(97+i)
        i+=1  
    while (t < 11):
        if (value > get_letter(id,chr(47+t))):
            value = get_letter(id,chr(47+t))
            letter = chr(47+t)
        t += 1
    return letter

def total_clicks(id):
    value = 0
    i = 0
    t = 1
    while (i < 26):
        value += get_letter(id,chr(97+i))
        i+=1  
    while (t < 11):
        value += get_letter(id,chr(47+t))
        t += 1
    return value

user_id = 1
add_user("YANG")
str_text = '0123456789abcdefghijklmnopqrstuvwxyz'
for element in str_text:
    add_letter(user_id,element)
print(get_max(user_id))
print(get_min(user_id))
print(get_letter(user_id,get_min(user_id)))
print(total_clicks(user_id))
