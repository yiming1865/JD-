# 引入PySimpleGUI库
import PySimpleGUI as sg
# 引入requests、re、urllib库
import requests
import re
import urllib.parse

# 定义获取排名函数GetNum，输入关键词和SKU，返回SKU在商品列表中的排名
def GetNum(keyword,sku):
    # 将SKU转换为字符串类型
    sku = str(sku)
    # 对关键词进行编码，避免乱码
    encode_keyword = urllib.parse.quote(keyword.encode(('utf-8')))
    i = 0
    mid_list = []
    another_list = []
    # 目标列表（暂时不用）
    # target_list = ['10053519801625', '10071041259659']
    # 在前10页中循环检索
    while i < 10:
        url = 'https://search.jd.com/Search?keyword=' + encode_keyword + '&qrst=1&psort=3&wq=' + encode_keyword + '&stock=1&psort=3&pvid=ccc7952b79074bb1be4623cabc734e1a&page=' + str(
            i) + '&s=61&click=0'
        # 通过requests库获取网页内容
        req = requests.get(url=url).text
        # 使用正则表达式匹配抓取信息
        s = re.findall(r"wids:'(.*?)'", req)
        # 将抓取到的信息分割并存储到mid_list中
        for string_num in s:
            mid_list = string_num.split(',')
        # 将mid_list里的元素添加到another_list里
        another_list.extend(mid_list)
        i += 1
    # 如果SKU在another_list中，则返回其排名；否则返回-1
    if sku in another_list:
        index = another_list.index(sku)
        return index + 1
    else:
        return -1

# 定义布局，确定窗口内容及输入框的数量、位置等
layout = [
    [sg.Text('请输入关键词(仅检索前10页)')],
    [sg.Text('关键词'),sg.InputText('',key='keyword')],
    [sg.Text('请输入SKU')],
    [sg.Text('SKU'),sg.InputText('',key='sku')],
    [sg.Button('确认')]
]
# 创建窗口
window = sg.Window('JD关键词排名查询-张嘉予专用',layout)

# 事件循环：检测窗口中的事件，收集用户输入等
while True:
    event, values = window.read()

    if event == None:
        break
    # 根据不同事件调用相应的响应函数
    if event == '确认':
        rank = GetNum(values['keyword'], values['sku'])
        if rank != -1:
            sg.Popup(f"SKU'{values['sku']}'在商品列表中的排名第：{rank}")
        else:
            sg.Popup(f"SKU'{values['sku']}'不在商品列表中")
    if event == '取消':
        sg.Popup('执行取消任务')

# 关闭窗口
window.close()




