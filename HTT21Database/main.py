from database import cursor, db

def add_log(aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,user):
    sql = ("INSERT INTO logs(zero,one,two,three,four,five,six,seven,eight,nine,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,user) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(sql, (aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,user, ))
    db.commit()
    log_id = cursor.lastrowid
    return log_id

def add_user(user):
    id = add_log(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,user)
    return id

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

def add_letters(id, letter,amount):
    x = ord(letter)
    if (x>60 and x<91):
        x = x+32
    if (x>96 and x<123):
        t = get_letter(id,chr(x)) + amount
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
        t = get_letter(id,chr(x)) + amount
        sql = ("UPDATE logs SET "+ m + " = %s WHERE id = %s")
        cursor.execute(sql, (t, id))
        db.commit()

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

def add_str(id, str):
    for element in str:
        add_letter(id,element)

def add_list(id,list):
    array=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    i = 0
    for element in list:
        if (element > 47 and element <58):
            array[element - 48] = array[element - 48] + 1
        elif(element>64 and element <91):
            array[element-65+10] = array[element-65+10]+1
    while (i < 36):
        if (i<10):
            add_letters(id,chr(48+i),array[i])
        else:
            add_letters(id,chr(55+i),array[i])
        i+=1


# user_id = 1
# str_text = '01234567891234567890'
# # dict = {'a':7,'b':6,'c':9}
# add_str(1,str_text)
# print("HI")
# print(get_max(user_id))
# print(get_min(user_id))
# print(get_letter(user_id,get_min(user_id)))
# print(total_clicks(user_id))

# list =[49,50,51,52,53,66,67,69,66,66,66]
# add_list(2,list)
