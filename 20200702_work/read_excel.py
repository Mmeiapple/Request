import os
import xlrd

curent=os.path.dirname(__file__)
data_path=os.path.join(curent,'../data/test_data.xlsx')


def WhetherMergeCells(merged,row_index,col_index,sheet):
    call_values=None
    # 遍历合并单元格的起始行和结束行、起始列、结束列
    for (rlow, rhigh, clow, chigh) in merged:
        # 判断行数是否在合并单元格的行内
        if (row_index>=rlow and row_index < rhigh):
            # 判断列数是否在合并单元格的列内
            if (col_index>=clow and col_index < chigh):
                call_values=sheet.cell_value(rlow,clow)
    print(call_values)
    return call_values

def IfMerge(merged,row_index,col_index,sheet):
    if WhetherMergeCells(merged,row_index,col_index,sheet):
        print("属于合并单元格")
    else:
        print("不属于合并单元格")



def ReadRowValues(sheet,values):
    return sheet.row_values(values)

if __name__=="__main__":
    workbook=xlrd.open_workbook(data_path)
    sheet=workbook.sheet_by_index(0)
    merged=sheet.merged_cells

    a=WhetherMergeCells(merged,3,0,sheet)
    print(a)
    data1=ReadRowValues(sheet,1)
    print(data1)
# call1=sheet.cell_value(1,0)
# print("01:",sheet.cell_value(1,0))
# print("02:",sheet.cell_value(2,0))
# print("03:",sheet.cell_value(3,0))
#
# # merged_cells 返回的是一个列表，每一个元素是合并单元格的位置信息的数组，数组包含四个元素（起始行，结束行，起始列，结束列）
# if sheet.merged_cells:
#     print( sheet.merged_cells )
# #读取一行
# print(sheet.row_values(1))

