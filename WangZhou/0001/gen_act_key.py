import uuid


def gen_act_key(n):
    """
    生成 n 个激活码，保存在字典。
    :param n: int
    :return: dict
    """
    act_code_store = {}

    for i in range(n):
        code0 = str(uuid.uuid1()).split('-')[0]
        code1 = '-'.join(str(uuid.uuid3(uuid.NAMESPACE_DNS, f'{i}')).split('-')[1:])
        act_code = code0 + '-' + code1
        act_code_store[f'id-{i}'] = act_code
    return act_code_store


if __name__ == "__main__":
    activity_code = gen_act_key(200)
