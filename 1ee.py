def dist(bost):
    def wrap(kv,kvnull,kt):
        bost(kv,kvnull,kt)
        print("S:",(kv+kvnull)*kt/2)
    return wrap


@dist
def boost(vnull,v,t):
	print("a:",(v-vnull)/t)

try:
    boost(int(input()),int(input()),int(input()))
except ValueError:
    print("Ошибка: не все значения - числовые")
except ZeroDivisionError:
    print("Ошибка: некорректное время")