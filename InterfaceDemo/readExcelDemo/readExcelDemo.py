# /user/bin/env
# _*_ coding: utf-8 _*_
# @date:20180702
# @author:shangxudong
import xlrd
import os


def get_cell_value(names, rows, cols):
    file_path = os.path.join(os.getcwd(), '企业类型数据字典（21301）.xlsx')
    print(file_path)

    excel_file = xlrd.open_workbook(file_path)
    # 返回所有sheetname
    sheet_name = excel_file.sheet_names()
    print(sheet_name)
    # 指定某个sheet,打印行数，列数
    # sheet_one = excel_file.sheet_by_name('Sheet1')
    sheet_one = excel_file.sheet_by_name(names)
    print(sheet_one.name, sheet_one.nrows, sheet_one.ncols)

    # 获取整行，整列值
    rows_value = sheet_one.row_values(1)
    print(rows_value)

    cols_value = sheet_one.col_values(1)
    print(cols_value)


    # 读取某个值
    cell_value = sheet_one.cell_value(rows, cols)
    print(cell_value)


if __name__ == '__main__':
    get_cell_value('企业类型', 1, 1)