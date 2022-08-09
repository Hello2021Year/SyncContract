import pymongo as pymongo


class Mongodb(object):

    def __init__(self, module_conf_dict):
        """
        init conf
        """

        # mongo atals config
        self.mongo_cluster = module_conf_dict.get(
            "mongo_cluster")
        self.mongo_username = module_conf_dict.get(
            "mongo_username")
        self.mongo_pwd = module_conf_dict.get("mongo_pwd")
        self.mongo_table = module_conf_dict.get("mongo_table")
        self.mongo_database = module_conf_dict.get(
            "mongo_db")

        # moralis mongo confi
        self.moralis_mongo_uri = module_conf_dict.get("moralis_mongo_uri")

    def altas_mongodb(self):
        connect_uri = "mongodb+srv://{}:{}@{}/?retryWrites=true&w=majority".format(
            self.mongo_username, self.mongo_pwd, self.mongo_cluster)
        client = pymongo.MongoClient(connect_uri)
        db = client[self.mongo_table]
        #table = self.mongodb_table
        #collection = db[table]  # 连接的表
        return db

    def morailis_mongodb(self):
        connect_uri = self.moralis_mongo_uri
        client = pymongo.MongoClient(connect_uri)
        return client
