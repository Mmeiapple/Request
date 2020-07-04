import os
import xlrd


current=os.path.dirname(__file__)
data_path=os.path.join(current,'../data/test_data.xlsx')


# 选择排序
def SelectionSort(data):
    lenth=len(data)
    for i in range(lenth):
        max_indenx=i




# 冒泡排序法

def BubbleSort(data):
    lenth=len(data)-1
    for i in range(lenth):
        j=0
        for j in range(lenth-i):
            if data[j]<data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
    return data
# 判断是否属于合并单元范围，返回合并单元格值
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

#读取最后一行分数值，并且排序
def GetScores(merged, sheet):
    data = []
    for i in range(1, row):
        row_index = i
        cow_index = 3
        value = sheet.cell_value(i, 3)
        data.append(value)
        a = WhetherMergeCells(merged, row_index, cow_index, sheet)
        if WhetherMergeCells(merged, row_index, cow_index, sheet) != None:
            data.pop()
            data.append(a)
    data=BubbleSort(data)
    return data

if __name__=="__main__":
    workbook=xlrd.open_workbook(data_path)
    sheet=workbook.sheet_by_index(0)
    merged=sheet.merged_cells
    row=sheet.nrows
    print(GetScores(merged,sheet))
    # data =[]
    # for i in range(1,row):
    #     row_index=i
    #     cow_index=3
    #     value = sheet.cell_value(i, 3)
    #     data.append(value)
    #     a=WhetherMergeCells(merged,row_index,cow_index,sheet)
    #     if WhetherMergeCells(merged,row_index,cow_index,sheet)!=None:
    #         data.pop()
    #         data.append(a)
    # print(data)


