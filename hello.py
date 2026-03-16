# 基本输出
print("Hello, World!")

# 变量与数据类型
name = "Alice"
age = 25
height = 1.68
is_student = True

print(f"姓名: {name}, 年龄: {age}, 身高: {height}, 是否学生: {is_student}")

# 列表
fruits = ["apple", "banana", "cherry"]
print("水果列表:", fruits)
print("第一个水果:", fruits[0])

# 字典
person = {"name": "Bob", "age": 30, "city": "Beijing"}
print("人员信息:", person)

# 条件判断
if age >= 18:
    print(f"{name} 是成年人")
else:
    print(f"{name} 是未成年人")

# 循环
print("1 到 5 的平方:")
for i in range(1, 6):
    print(f"  {i}^2 = {i ** 2}")

# 函数
def greet(name, greeting="你好"):
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))

# 列表推导式
squares = [x ** 2 for x in range(1, 6)]
print("平方列表:", squares)

# 异常处理
try:
    result = 10 / 0
except ZeroDivisionError:
    print("错误: 除数不能为零")
