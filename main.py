print("***欢迎使用凯撒加密器***")
plaintext=input("请输入您需要加密的明文:")        ##定义plaintext用以存储从键盘输入的明文
plaintext_list=list(plaintext) ##将输入的明文转换为明文列表

move_default=3            ##定义move_default表示凯撒加密密钥默认为偏移3位
move_define=input("请输入加密偏移量（默认为3）：")   ##从键盘输入加密偏移量
move=0

if len(move_define)==0:   ##若不输入偏移量则使用默认偏移3
    move = move_default
else:
    move = move_define
    move = int(move)  ##将输入的字符move转换为整型

cipher_list=[]            ##定义密文列表

##定义字母表与数字表
LOW_Letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
CAP_Letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Numbers=["0","1","2","3","4","5","6","7","8","9"]


##对明文进行加密
for index in plaintext_list:
    if index in LOW_Letters:   ##若明文中字符是小写字母
        temp=LOW_Letters.index(index)+move
        if temp > 25:
            temp = temp - 26
        cipher_list.append(LOW_Letters[temp])

    elif index in CAP_Letters:    ##若明文中字符是大写字母
        temp = CAP_Letters.index(index) + move
        if temp > 25:
            temp = temp - 26
        cipher_list.append(CAP_Letters[temp])

    elif index in Numbers:  ##若明文字符是数字
        temp = Numbers.index(index) + move
        if temp > 9:
            temp = temp - 10
        cipher_list.append(Numbers[temp])

cipher=''.join(cipher_list)   ##将密文列表转换为密文字符串

print("您当前输入的明文为："+plaintext)
print("加密密钥（偏移量）:"+repr(move))
print("加密后密文为："+cipher)

#解密器如下
solution =input("输入回车键继续")

print("***欢迎使用淦淦凯撒解密器***")

cipher_word =input("请输入你要输入的密文")   #定义 cipher_word 来存放密文

cipher1_list=list(cipher_word)

realWord_list =[]
for zhuanma in cipher1_list:
    zhuanma = ord(zhuanma)
    if zhuanma >= 97 and zhuanma <=122:
        temp1=zhuanma-move
        if temp1< 97:
            temp1 = temp1 + 26
        realWord_list.append(chr(temp1))

    if zhuanma >= 65 and zhuanma <= 90:
        temp2 = zhuanma - move
        if temp2 < 65:
            temp2 = temp2 + 26
        realWord_list.append(chr(temp2))


    if zhuanma >= 48 and zhuanma <= 57:
        temp3 = zhuanma - move
        if temp3 < 48:
            temp3 = temp3 + 10
        realWord_list.append(chr(temp3))
realWord = ''.join(realWord_list)

print("您当前输入为：" + cipher_word)
print("加密密钥（偏移量）:" + repr(move))
print("加密前的原文为：" + realWord)