import mysql.connector
from mysql.connector import errorcode
from database import cursor

DB_NAME = 'trial2'

TABLES = {}

TABLES['logs'] = (
    "CREATE TABLE `logs` ("
    " `id` int(11) NOT NULL AUTO_INCREMENT,"
    " `0` int(11) NOT NULL,"
    " `1` int(11) NOT NULL,"
    " `2` int(11) NOT NULL,"
    " `3` int(11) NOT NULL,"
    " `4` int(11) NOT NULL,"
    " `5` int(11) NOT NULL,"
    " `6` int(11) NOT NULL,"
    " `7` int(11) NOT NULL,"
    " `8` int(11) NOT NULL,"
    " `9` int(11) NOT NULL,"
    " `a` int(11) NOT NULL,"
    " `b` int(11) NOT NULL,"
    " `c` int(11) NOT NULL,"
    " `d` int(11) NOT NULL,"
    " `e` int(11) NOT NULL,"
    " `f` int(11) NOT NULL,"
    " `g` int(11) NOT NULL,"
    " `h` int(11) NOT NULL,"
    " `i` int(11) NOT NULL,"
    " `j` int(11) NOT NULL,"
    " `k` int(11) NOT NULL,"
    " `l` int(11) NOT NULL,"
    " `m` int(11) NOT NULL,"
    " `n` int(11) NOT NULL,"
    " `o` int(11) NOT NULL,"
    " `p` int(11) NOT NULL,"
    " `q` int(11) NOT NULL,"
    " `r` int(11) NOT NULL,"
    " `s` int(11) NOT NULL,"
    " `t` int(11) NOT NULL,"
    " `u` int(11) NOT NULL,"
    " `v` int(11) NOT NULL,"
    " `w` int(11) NOT NULL,"
    " `x` int(11) NOT NULL,"
    " `y` int(11) NOT NULL,"
    " `z` int(11) NOT NULL,"
    " `user` varchar(250) NOT NULL,"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)


def create_database():
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Database {} created!".format(DB_NAME))


def create_tables():
    cursor.execute("USE {}".format(DB_NAME))

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table ({}) ".format(table_name), end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already Exists")
            else:
                print(err.msg)


create_database()
create_tables()