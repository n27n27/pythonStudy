kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

# zip
print(list(zip(kor, eng)))

# unzip
mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed)))

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)
