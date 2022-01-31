f = open('demo.txt', 'r')
lines = f.readlines()
mystr = "".join([line.strip() for line in lines])
print(mystr)