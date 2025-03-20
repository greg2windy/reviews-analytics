
data = []
count = 0

with open('reviews.txt.crdownload', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 ==0:
			print(len(data))

print('The file has been read, total has', len(data), 'sets data')

sum_len = 0
for d in data:
	sum_len += len(d)
	print(sum_len)

print('The average length of each comment is', sum_len/len(data))

new =[]
for d in data:
	if len(d) < 100:
	    new.append(d) 
print('Total has', len(new), 'comments lower than 100')
print(new[0])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('Total has', len(good), 'comments mentioned about good')

#for快寫法
good = [d for d in data if 'good' in d]