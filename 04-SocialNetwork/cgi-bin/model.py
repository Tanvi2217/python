import pymysql
import os
import cgi

connection = pymysql.connect(host='localhost', port=3306, user='root',
                             database='socialNetwork', autocommit=True)

cursor = connection.cursor()


class User():
    def __init__(self, name, email, pwd, city, gender):
        self.name = name
        self.email = email
        self.pwd = pwd
        self.city = city
        self.gender = gender

    def __str__(self):
        return self.name + "," + self.email + "," + self.pwd + "," + self.city + "," + self.gender


# users = []

def register(name, email, pwd, city, gender):
    try:
        user = User(name, email, pwd, city, gender)
        # users.append(user)
        query = "insert into users values (%s, %s, %s, %s, %s)"
        cursor.execute(query, (user.name, user.email, user.pwd, user.city, user.gender))
        return user
    except pymysql.IntegrityError:
        return "Email ID Already Exist"


def loginUser(email, pwd):
    query = "select * from users where email=%s and pwd = %s"
    cursor.execute(query, (email, pwd))
    # data_length = cursor.rowcount
    data = cursor.fetchall()
    if len(data) < 1:
        return "User do not exist"
    else:
        return data


def editProfile(mobile, dob, occupation, interest,email,pic):
    if pic.filename:
        # print("Image is",image)
        # print("Filename is",image.filename)
        fn = os.path.basename(pic.filename)
        # open("profile_pic/" + fn, 'wb').write(pic.file.read())
        image = pic.file.read()
        file = open('profile_pic/' + fn, 'wb')
        file.write(image)
        file.close()
    query = "insert into profile values (%s,%s,%s,%s,%s,%s)"
    cursor.execute(query, (mobile, dob, occupation, interest,email,pic.filename))


def profile(email):
    query = "select * from profile where email = %s"
    cursor.execute(query, (email))
    data = cursor.fetchall()
    return data


def emailValidation(email):
    query = "select * from users where email = %s"
    cursor.execute(query, (email))
    num = cursor.rowcount
    if num == 0:
        return "Valid"
    else:
        return "EmailId Already Exist"

def post(p_data,post_pic,email):
    if post_pic.filename :
        fn_1 = os.path.basename(post_pic.filename)
        img = post_pic.file.read()
        file = open('post_pic/'+fn_1 , 'wb')
        file.write(img)
        file.close()
        query = "insert into post values (%s,%s,%s)"
        cursor.execute(query,(p_data,post_pic.filename,email))

def post_show(email):
    print("Email id is",email)
    query = "select * from post where email=%s"
    cursor.execute(query, (email))
    data = cursor.fetchall()
    # print(data)
    return data

# post_show('ram@gmail.com')
def com(comment):
    query = "insert into table_1 values (%s)"
    cursor.execute(query,(comment))
