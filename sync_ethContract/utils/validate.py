import json

def request_parse(req_data):
    """
    解析传入的参数
    :param req_data:
    :return:
    """

    args_data = req_data.args
    json_data = req_data.json

    return args_data,json_data


# 参数校验

def validate_param(request, kwargs):
    '''

    :param request:
    :param required_args: 必须的args参数
    :param required_json: 必须的json参数
    :return: http请求的参数
    '''
    request_args,request_json = request_parse(request)

    params = []
    data = dict()

    # 校验参数
    required_json = kwargs.get('required_json',None)
    required_args = kwargs.get('required_args',None)
    exclude_args = kwargs.get('exclude_args',None)
    extra_args = kwargs.get('extra_args',None)

    if required_args is not None:
        for i in required_args:
            if i not in request_args:
                raise ValueError(f"{i} 参数是必需的")
    if required_json is not None:
        for i in required_json:
            if i not in request_json:
                raise ValueError(f'{i} 参数是必需的')

    # 拼接请求参数
    for i in request_args:
        if exclude_args is None:
           params.append((i,request_args.get(i)))
        else:
           if i in exclude_args:
               continue


    if extra_args is not None:
        for key in extra_args:
            params.append((key,extra_args.get(key)))

    for i in request_json:
        data[i] = request_json.get(i)

    return params,json.dumps(data)





