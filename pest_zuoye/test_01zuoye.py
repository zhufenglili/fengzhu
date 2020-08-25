import os

# 判断目录是否存在
os.path.exists('pest_zuoye1')
# 如果目录不存在
if not os.path.exists('pest_zuoye1'):
    os.mkdir("pest_zuoye1")
    if not os.path.exists('pest_zuoye1/aa.yml'):
        hah = open("pest_zuoye1/aa.yml", 'w',encoding='utf-8')
        hah.write('aasdf')
        hah.close()