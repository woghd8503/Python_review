import cx_Oracle
import os
import sys

os.environ['NLS_LANG'] = '.AL32UTF8'
dsn = cx_Oracle.makedsn("127.0.0.1", 1521, "xe")

# 1) 연결 객체 생성
conn = cx_Oracle.connect("bitPython", "bitPython", dsn)
# 2) 커서 객체 생성
cursor = conn.cursor()

# 3) student 테이블 데이터 삽입

cursor.execute("""INSERT INTO student (id, name, age, addr)VALUES(student_id_swq.nextval,'홍길동', '24','지리산')""")

# cursor.excute("""INSERT INTO student ('id', 'name', 'age', 'addr')
#  VALUES(student_id_swq.nextval, '장산', 31, '구월산');""")
# cursor.excute("""INSERT INTO student ('id', 'name', 'age', 'addr')
#  VALUES(student_id_swq.nextval, '장산', 31, '해주');""")
# cursor.excute("""INSERT INTO student ('id', 'name', 'age', 'addr')
#  VALUES(student_id_swq.nextval, '원반', 24, '강원도');""")
# cursor.excute("""INSERT INTO student ('id', 'name', 'age', 'addr')
#  VALUES(student_id_swq.nextval, '이유', 32, '서울');""")


# cursor.executescript("""
# INSERT INTO student (id, name, age, addr)
#  VALUES(student_id_swq.nextval, '홍길', 24, '지리산');
# INSERT INTO student (id, name, age, addr)
#  VALUES(student_id_swq.nextval, '임정', 24, '구월산');
# INSERT INTO student (id, name, age, addr)
#  VALUES(student_id_swq.nextval, '장산', 24, '해주');
# INSERT INTO student (id, name, age, addr)
#  VALUES(student_id_swq.nextval, '원qks', 24, '강원도');
# INSERT INTO student (id, name, age, addr)
#  VALUES(student_id_swq.nextval, '이유', 24, '서울');
# """)

conn.commit()

# 3) student 테이블 데이터 가져오기
cursor.execute("SELECT * FROM student")
for row in cursor:
    print(row)

cursor.close()
conn.close()