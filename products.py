import os # operating system

# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 結束此迴圈並繼續下一迴圈
			name, price = line.strip().split(',')
			products.append([name, price])
			# strip()函式會去除空格及換行符號
			# 使用split切割後會回傳清單[]
	return products

# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱： ')
		if name == 'q':
			break
		price = input('請輸入商品價格： ')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f: 
		# 如果沒有這個檔案，會產生
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')


def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # 檢查檔案是否存在
		print('yeah! 找到檔案了!')
		products = read_file(filename)
	else:
		print('找不到檔案......')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)


main()