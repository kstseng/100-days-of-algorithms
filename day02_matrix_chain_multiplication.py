def mult(chain):
	'''
	Dynamic Programming!!

	概念：建構一個 n*n 的矩陣，依序從斜對角，一路做到最右上角
	'''
	
	# get total number of matrix
	n = len(chain)

	# 建立一個 n*n 的矩陣，並都填 0，每一個 element 代表該矩陣的最小相乘次數
	mat = [[0 for i in range(n)] for j in range(n)]

	# 建立一個 n*n 的矩陣，代表最小相乘次數的矩陣組合。並將對角線先擺上個矩陣的名字
	name_mat = [['' for i in range(n)] for j in range(n)]
	for i in range(n):
		name_mat[i][i] = chain[i][0]

	# 以左上右下的對角線，從最大的斜對角(d=0)，到最右上角(d=n-1)依序迴圈
	for d in range(1, n):
		# 對第 i 個斜對角，依序跑每一個 element
		for i in range(0, n - d):
			# 因為要跑斜對角，所以給定 i 後，便給定了 j
			j = i + d
			# 先設定為無限大，然後一但找到比較小的，變記錄起來
			mat[i][j] = float('inf')
			for k in range(i, j):
				# 取 n = 3 自行推導，便能取得以下公式
				val = mat[i][k] + mat[k + 1][j] + \
					chain[i][1] * chain[k][2] * chain[j][2] # 最後矩陣相乘的總計算次數
				name = '(' + name_mat[i][k] + name_mat[k + 1][j] + ')'
				if val < mat[i][j]:
					mat[i][j] = val
					name_mat[i][j] = name

	res = {
		'cost': mat[0][n-1], 
		'order': name_mat[0][n-1], 
		'row': chain[0][1],
		'col': chain[n-1][2]
	}
	
	return res


chain = [('A', 10, 20), ('B', 20, 30), ('C', 30, 40)]
#chain = [('A', 10, 20), ('B', 20, 30), ('C', 30, 40), ('D', 40, 3), ('E', 3, 20), ('F', 20, 60)]
print(mult(chain))