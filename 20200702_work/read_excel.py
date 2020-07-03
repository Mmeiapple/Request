import os
import xlrd

curent=os.path.dirname(__file__)
data_path=os.path.join(curent,'../data/test_data.xlsx')


workbook=xlrd.open_workbook(data_path)
sheet=workbook.sheet_by_index(0)
call1=sheet.cell_value(1,0)
print("01:",sheet.cell_value(1,0))
print("02:",sheet.cell_value(2,0))
print("03:",sheet.cell_value(3,0))

# merged_cells 返回的是一个列表，每一个元素是合并单元格的位置信息的数组，数组包含四个元素（起始行，结束行，起始列，结束列）
if sheet.merged_cells:
    print( sheet.merged_cells )
#读取一行
print(sheet.row_values(1))

