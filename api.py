import csv
import fatch
Product_Name,name,rating,commentHead,custComment,productLink=[],[],[],[],[],[]


def read(query):
	file_name=fatch.data_fatch(query)
	print(file_name)
	with open(f"{file_name}.csv",'r',encoding="utf8" )as csv_file:
		csv_reader=csv.reader(csv_file)
		header= next(csv_reader)
		for i in csv_reader:
			Product_Name.append(i[0])
			name.append(i[1])
			rating.append(i[2])
			commentHead.append(i[3])
			custComment.append(i[4])
			productLink.append(i[5])
# read("motog31")
