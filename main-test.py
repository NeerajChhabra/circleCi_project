from main import add

def testApp():
	assert add(10,20) == 30
	print('It is working')

if __name__ == '__main__':
	testApp()