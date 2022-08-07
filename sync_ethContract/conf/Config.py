from sync_ethContract.conf.Parse import Parse
from sync_ethContract.db import mongodb_connect


class Config(object):

    def __init__(self):
        """
        init conf
        """

        self.conf_file = "sync_ethContract/conf/Config.ini"
        self.cfg = Parse(self.conf_file)
        self.cfg.init()
        self.module_name = ['Moralis', "Atalas_mongo","Moralis_mongo","Webhook"]
        # 循环获取配置文件中的所有配置，务必保证能读取到相关的配置
        self.module_conf_dict = dict()
        for module in self.module_name:
            self.module_conf_dict.update(self.cfg.get_conf(module))

        # moralis config
        self.application_id = self.module_conf_dict.get(
            "application_id")
        self.master_key = self.module_conf_dict.get(
            "master_key")
        self.api_key = self.module_conf_dict.get(
            "api_key")
        self.request_url = self.module_conf_dict.get(
            "request_url")
        self.api_url = self.module_conf_dict.get(
            "api_url")

        # mongodb config
        mongodb = mongodb_connect.Mongodb(self.module_conf_dict)
        self.atals_mongodb = mongodb.altas_mongodb()
        self.morailis_mongodb = mongodb.morailis_mongodb()
