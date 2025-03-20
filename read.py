data = []
count = 0
with open('reviews.txt', 'r') as f:
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


#文字計數
wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key進wc字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Eddie'])

while True:
	word = input('請問你想查什麼字： ')
	if word == 'q':
		break
	if word in wc:
		print(f'{word}出現過的次數為{wc[word]}')
	else:
		print('這個字沒有出現過')


print('感謝使用本查詢功能')

