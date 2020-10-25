eg: 02-用面向对象的思想来实现.py
from pymysql import connect


class JD(object):
	def __init__(self):
		# 创建Connection链接
		self.conn = connect(host='localhost',port=3306,user='root',password='mysql',database='jing_dong',charset='utf8')
		# 获得Cursor对象
		self.cursor = self.conn.cursor()

	def __del__(self):
		# 关闭Cursor对象
		self.cursor.close()
		self.conn.close()

	def execute_sql(self, sql):
		self.cursor.execute(sql)  # cursor是游标，execute()执行sql语句
		for temp in self.cursor.fetchall():  # 返回值是个元组
			print(temp)

	def show_all_items(self):
		'''显示所有的商品'''
		sql = "select * from goods;"
		self.execute_sql(sql)
		
	def show_cates(self):
		sql = "select name from goods_cates;"
		self.execute_sql(sql)

	def show_brands(self):
		sql = "select name from goods_brands;"
		self.execute_sql(sql)

	@staticmethod
	def print_menu():
		print("--------京东--------")
		print("1:所有的商品")
		print("2:所有的商品分类")
		print("3:所有的商品品牌分类")
		return input("请输入功能对应的序号:")
		
	def run(self):
		while True:
			num = self.print_menu()
			if num == "1":
				# 查询所有商品
				self.show_all_items()
			elif num == "2":
				# 查询分类
				self.show_cates()
			elif num == "3":
				# 查询品牌分类
				self.show_brands()
			else:
				print("输入有误，重新输入...")
			


def main():	
	# 1. 创建一个京东商城对象
	jd = JD()

	# 2. 调用这个对象的run方法，让其运行
	jd.run()



if __name__ == "__main__":
	main()







eg: 03-添加一个商品分类.py（实现对数据库的增删改）
from pymysql import connect


class JD(object):
	def __init__(self):
		# 创建Connection链接
		self.conn = connect(host='localhost',port=3306,user='root',password='mysql',database='jing_dong',charset='utf8')
		# 获得Cursor对象
		self.cursor = self.conn.cursor()

	def __del__(self):
		# 关闭Cursor对象
		self.cursor.close()
		self.conn.close()

	def execute_sql(self, sql):
		self.cursor.execute(sql)  # cursor游标,execute()执行sql语句
		for temp in self.cursor.fetchall():  # 返回值是个元组
			print(temp)

	def show_all_items(self):
		'''显示所有的商品'''
		sql = "select * from goods;"
		self.execute_sql(sql)
		
	def show_cates(self):
		sql = "select name from goods_cates;"
		self.execute_sql(sql)

	def show_brands(self):
		sql = "select name from goods_brands;"
		self.execute_sql(sql)

	def add_brands(self):
		item_name = input("输入新商品分类的名称：")
		sql = """insert into goods_brands (name) values("%s")""" % item_name
		self.cursor.execute(sql)  # execute()执行sql语句
		self.conn.commit()  # 提交数据到数据库

	@staticmethod
	def print_menu():
		print("--------京东--------")
		print("1:所有的商品")
		print("2:所有的商品分类")
		print("3:所有的商品品牌分类")
		print("4:添加一个商品分类")
		return input("请输入功能对应的序号:")
		
	def run(self):
		while True:
			num = self.print_menu()
			if num == "1":
				# 查询所有商品
				self.show_all_items()
			elif num == "2":
				# 查询分类
				self.show_cates()
			elif num == "3":
				# 查询品牌分类
				self.show_brands()
			elif num == "4":
				# 添加商品分类
				self.add_brands()
			else:
				print("输入有误，重新输入...")
			




def main():	
	# 1. 创建一个京东商城对象
	jd = JD()

	# 2. 调用这个对象的run方法，让其运行
	jd.run()



if __name__ == "__main__":
	main()





sql注入：
##非安全的方式
##输入" or 1=1 or "(双引号也要输入)
# sql = ' select from goods where name="%s"' find_name
# print("""sql--->%s<----""" % sql)
##执行 select语句 ,并返回受影响的行数: 查询所有数据
# countcsl. execute(sql)

#安全的方式
#构造参数列表
params = [find_name]
#执行 select语句,并返回受影响的行数: 查询所有数据
count = cs1.execute( 'select from goods where name=%s',  params)
#注意:
#如果要是有多个参数,需要进行参数化
#那么params=[数值1, 数值2...] ,此时sql语句中有多个%s即可

#打印受影响的行数
 print(count)
#获取查询的结果
 #result = cs1. fetchone()
 result = cs1.fetchall()
#打印查询的结果
 print(result)
#关闭Cursor对象
 cs1.close()
#关闭Connection对象
 conn.close()
 
if __name__ == '__main__':
 	main()




eg: 防止sql注入.py
from pymysql import connect


class JD(object):
	def __init__(self):
		# 创建Connection链接
		self.conn = connect(host='localhost',port=3306,user='root',password='mysql',database='jing_dong',charset='utf8')
		# 获得Cursor对象
		self.cursor = self.conn.cursor()

	def __del__(self):
		# 关闭Cursor对象
		self.cursor.close()
		self.conn.close()

	def execute_sql(self, sql):
		self.cursor.execute(sql)  # cursor游标,execute()执行sql语句
		for temp in self.cursor.fetchall():  # 返回值是个元组
			print(temp)

	def show_all_items(self):
		'''显示所有的商品'''
		sql = "select * from goods;"
		self.execute_sql(sql)
		
	def show_cates(self):
		sql = "select name from goods_cates;"
		self.execute_sql(sql)

	def show_brands(self):
		sql = "select name from goods_brands;"
		self.execute_sql(sql)

	def add_brands(self):
		item_name = input("输入新商品分类的名称：")
		sql = """insert into goods_brands (name) values("%s")""" % item_name
		self.cursor.execute(sql)  # execute()执行sql语句
		self.conn.commit()  # 提交数据到数据库

	def get_info_by_name(self):
		find_name = input("请输入要查询的商品的名字：")
		# sql = """select * from goods where name='%s';""" % find_name
		# print("---->%s<-----" % sql)  # 进行调试
		# self.execute_sql(sql)
		sql = "selcet * from goods where name=%s"  # %s左右不加引号，以达到防止sql注入的目的  
		self.cursor.execute(sql, [find_name])  # 把值放入一个列表中，从列表中取值
		print(self.cursor.fetchall())

	@staticmethod
	def print_menu():
		print("--------京东--------")
		print("1:所有的商品")
		print("2:所有的商品分类")
		print("3:所有的商品品牌分类")
		print("4:添加一个商品分类")
		print("5:根据名字查询一个商品")
		return input("请输入功能对应的序号:")
		
	def run(self):
		while True:
			num = self.print_menu()
			if num == "1":
				# 查询所有商品
				self.show_all_items()
			elif num == "2":
				# 查询分类
				self.show_cates()
			elif num == "3":
				# 查询品牌分类
				self.show_brands()
			elif num == "4":
				# 添加商品品牌分类
				self.add_brands()
			elif num == "5":
				# 根据名字查询商品
				self.get_info_by_name()
			else:
				print("输入有误，重新输入...")
			

def main():	
	# 1. 创建一个京东商城对象
	jd = JD()

	# 2. 调用这个对象的run方法，让其运行
	jd.run()


if __name__ == "__main__":
	main()
