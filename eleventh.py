# coding=utf-8
import xlsxwriter
import datetime
workbook = xlsxwriter.Workbook('demo2.xlsx')   #创建一个excel文件
worksheet = workbook.add_worksheet()    #创建一个工作表对象

worksheet.set_column('A:A', 20)   #创建第一列的宽度为20
bold = workbook.add_format({'bold':True})  #定义一个加粗的格式

worksheet.write('A1', 'Hello')
worksheet.write('A2', 'Hello world',bold)
worksheet.write('B2', 20, bold)
worksheet.write('B1', 10, bold)
worksheet.write('B3', 30)
worksheet.write('B4', 35)
worksheet.write('B5', 45)
worksheet.write('C1', 40)
worksheet.write('C2', 35)
worksheet.write('C3', 50)
worksheet.write('C4', 20)
worksheet.write('C5', 10)



worksheet.write(2, 0, 32)
worksheet.write(3, 0, 36)
worksheet.write(4, 0, "=SUM(A3:A4)")
f=datetime.date.today()
print f
# worksheet.write_datetime(7,0,datetime.datetime.strftime(f,'%Y-%m-%d'),workbook.add_format({'num_format':'yyyy-mmm-dd'}))
worksheet.insert_image('B5', './20181227095953.png')

worksheet.write('A7', 'Hello world')
cell_format = workbook.add_format({'bold': 'True'})
worksheet.set_row(7, 40, cell_format)
worksheet.set_column(0, 1, 10, cell_format)
worksheet.set_column('C:D', 50)
chart = workbook.add_chart({'type': 'column'})
worksheet.insert_chart('A8',chart)
chart.add_series({'categories': 'Sheet1!$A$1:$A$5','values':'=Sheet1!$B$1:$B$5','line':{'color':'red'},})
workbook.close()



