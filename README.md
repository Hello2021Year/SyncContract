# SyncContract

Conf: 配置文件类
db: 数据库连接
utils: utils

app.py 程序主入口

flask 框架

云函数参考： https://docs.moralis.io/moralis-dapp/web3-api/native#getcontractevents
             https://docs.moralis.io/moralis-dapp/web3-api/native \
webhook参考： http://docs.parseplatform.org/cloudcode/guide/#cloud-code-beforesave-triggers

to do:
1.视图分开，不要都写在app.py里面，把webhook和contract相关的分开 \
2. 添加一个同步合约请求，tableName不允许重复，是否引入用户概念，tableName为uuid+用户填写的tableName,添加webhook功能用户也只能添加自己创建的合约请求的webhook

