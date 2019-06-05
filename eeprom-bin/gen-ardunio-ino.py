import sys
import os
import pathlib
directory = pathlib.Path(sys.argv[0]).parent
print(directory)

if __name__ == '__main__':
    template_file = open(directory/"template.ino")
    template_str = template_file.read()
    li = os.listdir(directory) #获取当前目录下所有文件
    for adir in li:#遍历链表
        if os.path.isfile(directory/adir):#判断路径是否为文件
            fext = os.path.splitext(adir)[1]#获取后缀名
            fext = str(fext).upper()
            if fext == ".BIN":
                f = open(directory/adir,'rb')
                len = 0
                data_str = ""
                while True:
                    abyte = f.read(1)
                    if not abyte:
                        break
                    len += 1
                    byte_str = "0x{:0>2X}".format(int.from_bytes(abyte,byteorder="big"))
                    data_str += byte_str
                    data_str += ","
                f.close()
                code = template_str.replace("{size}",str(len))
                code = code.replace("{content}",data_str)
                f = open(directory / "arduino" / (adir +".ino"),'w')
                f.write(code)
    c = input("enter any key to exit...")
