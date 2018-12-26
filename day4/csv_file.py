# csv (Comma Separated Value : 콤마로 구분된 값(들))

# .csv 파일을 연다 (import csv)
# 1. 읽기(Read)
# 2. 쓰기(Write)
# 3. 수정(Append)
# 파일을 닫는다

import csv
# csv 쓰기
# f = open('sspy1.csv','w',encoding="utf-8")
# sspy1 = csv.writer(f)
# sspy1.writerow(["Alpha", "for@example.com", "1123234", "CSV"])
# f.close()

# csv 읽기
f = open('sspy1.csv','r',encoding="utf-8")
sspy1 = csv.reader(f)
for i in sspy1:
    for j in i:
        print(j)
f.close()

# csv 수정(추가)
# f = open('sspy1.csv','a',encoding="utf-8")
# sspy1 = csv.writer(f)
# sspy1.writerow(["Gamma","in@example.com","4123231","HTML"])
# f.close()