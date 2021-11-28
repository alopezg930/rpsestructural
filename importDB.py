from hello.models import tessiu
import csv
fields = ['temperature','color','inflammation']
for row in csv.reader(open('C:/Users/wall-E/Documents/sintantico estructural/bd.csv')):
	tessiu.objects.create(**dict(zip(fields, row)))