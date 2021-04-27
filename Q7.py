#Question7
students=[("Suleman","8","1694"),("Talha","9","1695"),("Zoraiz","10","1696"),("Mohtad","9","1697"),("Usama","6","1698"),("Hassaan","10","1699"),("Mustafa","5","1701"),("Rizwan","3","1702"),("Taimur","2","1703"),("Hadi","1","1704")]

students = sorted(students, key=lambda x: (x[0], x[2], x[1]))
print(students)