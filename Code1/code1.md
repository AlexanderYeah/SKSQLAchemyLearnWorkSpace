# 安装pymysql

报错  : No module named 'MySQL'  
在stackoverflow 上找到了答案    

* step1: 先找到当前可用的mysql-connector

> $ pip search mysql-connector | grep --color mysql-connector-python  

* step2: 根据可用的 进行安装

> $ pip install mysql-connector-python-rf


