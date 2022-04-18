import easygui
# 询问加密代码
word = easygui.enterbox("你想加密什么字母？（仅支持英文）","输入字母")
# 询问凯撒移位信息
moveNumbers = int(easygui.enterbox("移动几位?","获取信息"))
# 加密信息
#转十六进制
hexNumbersList = []
for i in word:
    hexNumbersList.append(hex(ord(i)).strip('0x'))
# 处理信息
output = ' '.join(hexNumbersList)
# 创建文件
fileName = easygui.enterbox("请问要生成的文件名是什么？")
_print = open(fileName+".txt","w+")
_print.write(output)
easygui.msgbox("已生成名为"+_print.name+"的文件")
_print.close()