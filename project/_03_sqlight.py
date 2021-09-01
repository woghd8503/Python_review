# sqlite는?
# ; 파일에 저장하는 관계형 데이터베이스
#   안드로이드에서도 사용한다
#   굉장히 가볍기 때문에 부담없이 사용할 수 있다

import sqlite3

#1) DB파일과 연결된 연결 객체 생성
connection = sqlite3.connect('student.db')
print(connection)

#2) sql명령문 수행을 위한 커서 객체 가져오기
cursor = connection.cursor()
print(cursor)

#3) student 테이블이 있다면 제거하기
cursor.execute("DROP TABLE IF EXISTS student")

#4) student 테이블 생성하기
cursor.execute("""
    CREATE TABLE student(
        name VARCHAR(20),
        addr VARCHAR(50),
        sex CHAR(1),
        birth DATE,
        korean Int,
        math Int,
        english INT
    )
""")

#5) 데이터 1개 저장하기
cursor.execute("""
    INSERT INTO student VALUE('홍길동', '지리산',
        'm', '2021-08-26', 99, 97, 98)
""")

connection.commit()

# 6) 데이터 여러 개 저장하기
cursor.executescript("""
    INSERT INTO student VALUE('홍길동', '지리산',
        'm', '2021-08-26', 99, 97, 98);
            INSERT INTO student VALUE('아이유', '지리산',
        'f', '2021-08-26', 99, 97, 98);
            INSERT INTO student VALUE('장나라', '지리산',
        'f', '2021-08-26', 99, 97, 98);
            INSERT INTO student VALUE('제니', '지리산',
        'f', '2021-08-26', 99, 97, 98);
            INSERT INTO student VALUE('차돌바위', '지리산',
        'm', '2021-08-26', 99, 97, 98);
""")
connection.commit()

# 7) 데이터 1개 읽어오기
cursor.execute("SELECT * FROM student")
print(cursor.fetchone())
print()

# 8) 데이터 여러 개 읽어오기
cursor.execute("SELECT * FROM student")

# 9) 3개만 읽어와라
print(cursor.fetchmany(3))

# 10) (나머지)모두 일기
listSt = cursor.fetchall()
print(len(listSt))
for st in listSt:
    print(st)
print()

# 11) 전체를 읽어오기
cursor.execute("SELECT * FROM student")
listSt = cursor.fetchall()
print(len(listSt))
for st in listSt:
    print(st)
print()

print('-' * 60)

# 12) 다른 방법으로 모두 일기
cursor.execute("SELECT * FROM student")
for row in cursor:
    print(row)
print()

print('-' * 60)

# 13) 또 다른 방법으로 모두 일기
for row in cursor.execute("SELECT * FROM student"):
    print(row)
print()

print('-' * 60)

# 14) 이름만 추출하기 - 1
for row in cursor.execute("SELECT name FROM student"):
    print(row)
print()

print('-' * 60)

# 15) 이름만 추출하기 - 2
for row in cursor.execute("SELECT name FROM student"):
    print(row[0])
print()

print('-' * 60)

# 16) 컬럼명 확인하기
print(cursor.description)
attrName = [column[0] for column in cursor.description]
print(attrName)
print()

print('-' * 60)

columns = []
for field in cursor.description:
    columns.appen(field[0])
print(columns)

#데이터베이스 연결 종료
cursor.close()
connection.close()