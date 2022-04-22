# 讀取檔案
products = []

with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue # 結束此迴圈並繼續下一迴圈
		name, price = line.strip().split(',')
		products.append([name, price]) 
		
		# strip()函式會去除空格及換行符號
		# 使用了split切割後會回傳清單[]

print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	price = int(price)
	products.append([name, price])
print(products)

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f: 
	# 如果沒有這個檔案，會產生
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')