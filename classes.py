class A(object):
	def __init__(self):
		self.str = "It worked!!"

	def fun(self):
		print("function printed something for you")
class B(A):
	def __init__(self):
		self.txt="B's Init"

def main():
	x = A()
	x.fun()
	print(x.str)

	y=B()
	#print(y.str)
	print(y.txt)
	y.fun()

if __name__ == '__main__':
	main()