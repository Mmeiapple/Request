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
    return call_values

def IfMerge(merged,row_index,col_index,sheet):
    if WhetherMergeCells(merged,row_index,col_index,sheet):
        print("属于合并单元格")
    else:
        print("不属于合并单元格")

if __name__=="__main__":
    workbook=xlrd.open_workbook(data_path)
    sheet=workbook.sheet_by_index(0)
    merged=sheet.merged_cells
    a=IfMerge(merged,3,4,sheet)
