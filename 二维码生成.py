import pyqrcode

# 设置二维码信息
s = input("输入二维码信息")

# 生成二维码
url = pyqrcode.create(s)

# 保存二维码
print("已在桌面上生成二维码")
url.svg("code.svg", scale=8)
