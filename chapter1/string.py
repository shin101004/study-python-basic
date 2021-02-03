# Python에서 문자열을 만드는 방법

# 큰따옴표로 양쪽 둘러싸기
a = "Hello World"
# 작은 따옴표로 양쪽 둘러싸기
b = 'Python is fun'
# 큰 따옴표를 3개 연속 사용하기
c = """Life is too short, You need python"""
# 작은 따옴표를 3개 연속으로 써서 둘러싸기
d = '''Life is too short, You need python'''

# 문자열에 작은 따옴표 포함시키기
e = "Jaemin's life is good"

print(e)

# 여러 줄인 문자열을 대입하고 싶을 때
multiline = "Lufe is too short\nYou need Python."

print(multiline)

multiline = '''
Life is too short
You need Python
'''

print(multiline)

# 문자열 길이 구하기
a = "Life is too short"
print(len(a))

# 문자열 포매팅 따라하기
print("I eat %d apples" % 3)
num = 3
print("I eat %d apples" % num)
day = "monday"
print ("I eat %d apples on %s" % (num,day))