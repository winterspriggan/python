python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[0].islower())
print(len(python))
print(python.replace("Python", "Java"))
print(python)

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)
print(python.index("P")) #python에서 P의 위치를 인덱스로 반환
print(python.find("n"))
print(python.find("Java"))


print(python.find("is")) # is 의 첫 글자인 i의 위치를 반환
# print(python.index("Java")) 오류남

print(python.count("n"))