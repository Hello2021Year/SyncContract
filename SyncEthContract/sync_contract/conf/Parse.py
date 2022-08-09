# coding=utf-8

"""配置解析
"""

import configparser
import getopt
import sys
import json
import traceback


class Parse(object):
    """配置解析类
    """

    def __init__(self, conf, encoding='utf-8'):
        """构造函数
        """
        self._conf_file = conf
        self._cf = configparser.ConfigParser(
            interpolation=configparser.ExtendedInterpolation())
        self._conf_map = dict()
        self._encoding = encoding

    def init(self):
        """加载配置信息
        """
        try:
            self._cf.read(self._conf_file, encoding=self._encoding)
        except Exception as e:
            print(repr(e))
            return False

        for section in self._cf.sections():
            if section not in self._conf_map:
                self._conf_map[section] = dict()

            options = self._cf.options(section)
            for option in options:
                self._conf_map[section][option] = self._cf.get(section, option)

        return True

    def setConf(self, new_dict):
        """update conf
        """
        for sec_k, sec_v in new_dict.items():
            for k, v in sec_v.items():
                self._cf.set(str(sec_k), str(k), str(v))

        for sec_map_k, sec_map_v in new_dict.items():
            self._conf_map[sec_map_k] = sec_map_v

    def saveConf(self, path):
        """save conf
        """
        self._cf.write(open(path, "w"))

    def get_conf(self, conf_path=None):
        """获取配置项
        """
        if conf_path is None:
            conf_path = '/'

        conf_path = conf_path.strip()
        if not conf_path.startswith('/'):
            conf_path = '/' + conf_path

        conf_path = conf_path.rstrip('/')

        fields = conf_path.split('/')[1:]
        value = self._conf_map
        try:
            for field in fields:
                value = value[field]
        except BaseException:
            return dict()

        return value

    def get_all_conf(self):
        """
        获取所有的配置
        """
        return self._conf_map


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "hc:d:", [
                               "help", "conf=", "dict="])
    for op, value in opts:
        if op in ("-d", "--dict"):
            new_dict = json.loads(value)
        if op in ("-c", "--conf"):
            print(value)
            conf_file = value
        elif op == "-h":
            print(
                "python routine_score.py -c f.conf -d 20190101 or python routine_score.py")
