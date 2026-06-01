students = [{"name": "Tom", "score": 85}, {"name": "Jerry", "score": 92}, {"name": "Spike", "score": 78}]

# 按分数排序
sorted_students = sorted(students, key=lambda s: s['score'])
print(sorted_students)

nums = [1, 5, 12, 8, 3, 20, 15]
