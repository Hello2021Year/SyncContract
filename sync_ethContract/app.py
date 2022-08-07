#!/usr/bin/env python
# encoding: utf-8
import requests
from flask import Flask, request

from sync_ethContract.conf.Config import Config
from sync_ethContract.utils.utils import build_header_masterKey
from sync_ethContract.utils.utils import builder_header_apiKey
from sync_ethContract.utils.validate import validate_param

app = Flask(__name__)

config = Config()



# Config


@app.route('/index')
def hello_world():
    return 'Hello World!'


@app.route('/getContractEvents', methods=['POST'])
def get_contract_event():
    """
    Get the events in descending order based on block number. Returns an object with the number of Contract events and the array of Contract events (asynchronous)

    Parameters:
     - chain(optional): The blockchain to get data from. Valid values are listed on Supported Chains. Default value Eth.
     - offset(optional): Offset.
     - limit(optional): Limit.
     - from_block (optional): To get contract events starting from this block
     - to_block (optional): To get contract events up to this block
     - topic (required): The topic of the event
     - address (required): A smart contract address
     - abi (required): Event ABI (do not insert the ABI of the whole smart contract). ABI has a JSON format.

    Returns:
        events

    Raises:
       KeyError - raises an exception
    """

    # 获取参数，校验
    if request.args.get("chain") is None:
       request.args["chain"]="eth"
    if request.args.get("limit") is None:
        request.args['limit'] = 500

    # 获取参数，校验

    kwargs = dict()
    required_args=["address","topic"]
    #required_json=["abi"]

    exclued_args=["address"]
    kwargs['exclued_args'] = exclued_args
    kwargs['required_args'] = required_args
    #kwargs['required_json'] = required_json


    params,data = validate_param(request,kwargs)
    headers = builder_header_apiKey(config.api_key)


    # 执行函数
    response = requests.post("{}/{}/events".format(config.api_url,request.args.get('address')),
                             headers=headers, params=params, data=data)

    # 返回结果
    return response.content


    # 执行函数

    # 返回结果




@app.route('/addSyncContract', methods=['POST'])
def add_Sync_contract():
    """
    Get the events in descending order based on block number. Returns an object with the number of Contract events and the array of Contract events (asynchronous)

    Parameters:
     - chain(optional): The blockchain to get data from. Valid values are listed on Supported Chains. Default value Eth.
     - limit(optional): Limit.
     - topic (required): The topic of the event
     - address (required): A smart contract address
     - abi (required): Event ABI (do not insert the ABI of the whole smart contract). ABI has a JSON format.

    Returns:
        events

    Raises:
       KeyError - raises an exception
    """
    # to do : 加几个默认参数，比如chainId,limit
    if request.args.get("chainId") is None:
       request.args["chainId"]="0x1"
    if request.args.get("limit") is None:
        request.args['limit'] = 500

    # 获取参数，校验
    kwargs = dict()

    required_args=["address","topic","tableName","sync_historical"]
    required_json=["abi"]

    extra_args = dict()
    extra_args["_ApplicationId"] = config.application_id
    kwargs['extra_args'] = extra_args
    kwargs['required_args'] = required_args
    kwargs['required_json'] = required_json

    params,data = validate_param(request,kwargs)
    headers = build_header_masterKey(config.master_key)


    # 执行函数
    response = requests.post('{}/functions/watchContractEvent'.format(config.request_url),
                             headers=headers, params=params, data=data)

    # 返回结果
    return response.content




if __name__ == '__main__':
    #app.run(debug=True, host="0.0.0.0", port="5000")
    app.run()
