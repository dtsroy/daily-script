import random
import time

def test(fun):
	def real(*args, **kwargs):
		b = time.time()
		ret = fun(*args, **kwargs)
		e = time.time()
		print(e-b)
		return ret
	return real

def get_data(num, single):
	ret = []
	for i in range(0, num):
		ret.append(i)
		ret.append(i)
	ret.append(single)
	random.shuffle(ret)
	return ret

@test
def solution1(lst):
	another = [] # 临时列表,增减都在里面
	for i in lst:
		try:
			del another[another.index(i)]
		except:
			another.append(i)
	return another[0]

@test
def solution1_better(lst):
	lst.sort()
	for i in range(0, len(lst), 2):
		try:
			if lst[i] != lst [i+1]:
				return lst[i]
		except:
			return lst[i]

@test
def solution2(lst):
	result = 0
	for i in lst:
		result ^= i
	return result

data = get_data(int(1e6), int(1e6-19))

print(solution1_better(data))
print(solution2(data))
