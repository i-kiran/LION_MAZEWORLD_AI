import random as rnd
class g_file:
	def __init__(self):
		self.b_s = [[1, 0, 0, 400, 0, 400]]#id, s, x1, x2, y1, y2 
		self.cleave_d = 'x'
		self.no_buckets = 1		
		self.size_b = int(input('Enter Bucket Size: '))
		f = open('bucket1.txt', 'w')
		f.close()
	def bucket(self, x, y):
		for b in self.b_s:
			x_l = b[2]
			x_r = b[3]
			y_l = b[4] 
			y_r = b[5]
			if x > x_l and y > y_l and x <= x_r  and y <= y_r:
				return b	
	def bucket_full(self, size):
		if self.size_b < size:
			return 1
		return 0	

	def transfer_coods(self, old, new):
		co_ods = []
		with open(old, 'r') as fd:
			lines = fd.readlines()
			fd.close()
			for l in lines:
				co_ods.append(l)		
		f_o = open(old,'w')
		f_n = open('bucket'+str(new[0])+'.txt', 'w')
		x_l = new[2]
		x_r = new[3]
		y_l = new[4] 
		y_r = new[5]	
		for i in co_ods:
			p_x , p_y = i.strip().split(',')[1:]
			p_x = int(p_x)
			p_y = int(p_y)
			if p_y > y_l and p_y <= y_r and p_x > x_l and p_x <= x_r :
				f_n.write(i)
			else:
				f_o.write(i)
		f_n.close()
		f_o.close()
		
	def cleave(self, bucket):
		name = 'bucket'
		extension ='.txt'
		f_o = name+ str(bucket[0])+extension
		lst = []#co-ods from old bucket
		with open(f_o, 'r') as fd:
			lines = fd.readlines()
			fd.close()
			for l in lines:
				lst.append(l.strip().split(','))	
		bucket_list = []	
		for i in self.b_s:
			if bucket[0] == i[0]:
				n  = 0
				x_l = i[2]
				x_r = i[3]
				y_l = i[4]
				y_r = i[5]
				for pt in lst:
					x = pt[1]
					x = int(x)
					y = pt[2]
					y = int(y)
					if x > x_l and x <= x_r and y > y_l and y <= y_r:
						n += 1				
				bucket_list.append((i,n))#logical cleavage exists reqd only physical
		if len(bucket_list) > 1:					
			maxm = max(bucket_list, key = lambda x:int(x[1]))[0]
			l = len(self.b_s)
			for i in range(l):
				if self.b_s[i] == maxm:
					size_n = 0
					for pt in lst:
						if (int(pt[1]) > maxm[2] and int(pt[2]) > maxm[4] and int(pt[1]) <= maxm[3]  and int(pt[2]) <= maxm[5]):
							size_n += 1
					if not self.bucket_full(size_n):
						size_n2 = len(lst) - size_n
						self.b_s[i][1] = size_n
						for j in range(len(self.b_s)):
							if (self.b_s[j][0] == bucket[0]):
								if(self.b_s[j] != maxm):
									self.b_s[j][1] = size_n2
						self.no_buckets += 1
						self.b_s[i][0] = self.no_buckets
						self.transfer_coods(f_o, self.b_s[i])
						break
					else:#both logical and physical cleavage required
						if self.cleave_d == 'x':
							lst = sorted(lst, key = lambda x:int(x[1]))
							cleave_x = (int(lst[len(lst)//2-1][1]) + int(lst[len(lst)//2][1])) //2
							size_n = 0
							for points in lst:
								if (int(points[1]) <= cleave_x):
									size_n += 1
								else:
									break						
							size_n2 = len(lst) - size_n
							for j in range(len(self.b_s)):
								if (self.b_s[j][0] == bucket[0]):		
										self.b_s[j][1] = size_n
								if (self.b_s[j][2] < cleave_x and self.b_s[j][3] > cleave_x):
									n = 0
									x1, x2, y1, y2 = self.b_s[j][2:]
									for point in lst:
										x, y = point[1:]
										if (int(x) > x1 and int(x) <= x2 and int(y) > y1 and int(y) <= y2):
											n += 1
									temp = self.b_s[j][3]
									self.b_s[j][3] = cleave_x
									if (self.b_s[j][0] == bucket[0]):
										if(self.bucket_full(n)):
											self.no_buckets += 1
											self.b_s.append([self.no_buckets,size_n2,cleave_x,temp,self.b_s[j][4],self.b_s[j][5]])
											self.transfer_coods(f_o, [self.no_buckets,size_n2,cleave_x,temp,self.b_s[j][4],self.b_s[j][5]])
									else:	
										self.b_s.append([self.b_s[j][0],self.b_s[j][1],cleave_x,temp,self.b_s[j][4],self.b_s[j][5]])
							self.cleave_d = 'y'
						else:
							lst = sorted(lst, key = lambda x:int(x[2]))
							a = int(lst[len(lst)//2-1][2])
							b = int(lst[len(lst)//2][2])
							y_split_point = (a + b) //2
							size_n = 0
							for pt in lst:
								if (int(pt[2]) <= y_split_point):
									size_n += 1
								else:
									break
							size_n2 = len(lst) - size_n
							for j in range(len(self.b_s)):
								if (self.b_s[j][4] < y_split_point and self.b_s[j][5] > y_split_point):
									n = 0
									x_l = self.b_s[j][2]
									x_r = self.b_s[j][3]
									y_l = self.b_s[j][4]
									y_r = self.b_s[j][5] 
									for pt in lst:
										x = pt[1]
										x = int(x)
										y = pt[2]
										y = int(y)
										if x > x_l and x <= x_r and y > y_l and y <= y_r:
											n = n+1
									temp = self.b_s[j][5]
									self.b_s[j][5] = y_split_point
									self.b_s[j][1] = size_n
									if (self.b_s[j][0] == bucket[0] and self.bucket_full(n)):
										self.no_buckets += 1
										self.b_s.append([self.no_buckets,size_n2,self.b_s[j][2],self.b_s[j][3],y_split_point,temp])
										self.transfer_coods(f_o, [self.no_buckets,size_n2,self.b_s[i][2],self.b_s[i][3],y_split_point,temp])
									else:	
										self.b_s.append([self.b_s[j][0],self.b_s[j][1],self.b_s[j][2],self.b_s[j][3],y_split_point,temp])
							
							self.cleave_d = 'x'
						break
					
		else:
			if (self.cleave_d == 'x'):
				lst = sorted(lst, key = lambda x:int(x[1]))
				a = int(lst[len(lst)//2-1][1])
				b = int(lst[len(lst)//2][1])
				cleave_x = (a + b) //2
				size_n = 0
				for points in lst:
					if int(points[1]) <= cleave_x:
						size_n = size_n + 1
					else:
						break
				size_n2 = len(lst) - size_n
				for j in range(len(self.b_s)):
					if (self.b_s[j][2] < cleave_x and self.b_s[j][3] > cleave_x):
						temp = self.b_s[j][3]
						self.b_s[j][3] = cleave_x
						if self.b_s[j][0] == bucket[0]:
							self.b_s[j][1] = size_n
							self.no_buckets += 1
							self.b_s.append([self.no_buckets,size_n2,cleave_x,temp,self.b_s[j][4],self.b_s[j][5]])
							self.transfer_coods(f_o, [self.no_buckets,size_n2,cleave_x,temp,self.b_s[j][4],self.b_s[j][5]])
						else:	
							self.b_s.append([self.b_s[j][0],self.b_s[j][1],cleave_x,temp,self.b_s[j][4],self.b_s[j][5]])
				self.cleave_d = 'y'
			else:
				lst = sorted(lst, key = lambda x:int(x[2]))
				a_ = int(lst[len(lst)//2-1][2])
				b_ = int(lst[len(lst)//2][2])
				y_split_point = (a_ + b_) //2
				size_n = 0
				for points in lst:
					if int(points[2]) <= y_split_point:
						size_n += 1
					else:
						break						
				size_n2 = len(lst) - size_n				
				for j in range(len(self.b_s)):
					if self.b_s[j][4] < y_split_point and self.b_s[j][5] > y_split_point:
						temp = self.b_s[j][5]
						self.b_s[j][5] = y_split_point
						if self.b_s[j][0] == bucket[0]:
							self.b_s[j][1] = size_n
							self.no_buckets += 1
							self.b_s.append([self.no_buckets,size_n2,self.b_s[j][2],self.b_s[j][3],y_split_point,temp])
							self.transfer_coods(f_o, [self.no_buckets,size_n2,self.b_s[j][2],self.b_s[j][3],y_split_point,temp])
						else:	
							self.b_s.append([self.b_s[j][0],self.b_s[j][1],self.b_s[j][2],self.b_s[j][3],y_split_point,temp])
				self.cleave_d = 'x'
				
	def insert(self, id, x, y):
		bucket = self.bucket(x, y)
		file = open('bucket'+str(bucket[0])+'.txt', 'a')
		file.write(str(id) + ',' + str(x) + ',' + str(y) + '\n')
		file.close()
		for i in range(len(self.b_s)):
			if self.b_s[i][0] == bucket[0]:
				self.b_s[i][1] += 1
					
		if self.bucket_full(bucket[1]):
			self.cleave(bucket)

