import yaml


def test_yaml_load():
    with open("../page/main.yaml", encoding="utf-8") as f:
        steps = yaml.safe_load(f)
    for step in steps:
        if "by" in step.keys():
            print("查找元素")
        if "action" in step.keys():
            print("多个动作解析")
            action = step["action"]
            if "click" == action:
                print("click操作")
            if "send" == action:
                value = step["value"]
                print(f"send({value})")


def test_replace():
    _parame={"name":"12345"}
    str = "xxxxxxxxx ${name}lll${name}llll${name}lllllllllllllll"
    for key,value in _parame.items():
        print(_parame.items())
        print(key)
        # str = str.replace('${'+key+'}', value)
        #最里面的{}表示变量，外面2个{}表示{},-->此外我们可以使用大括号 {} 来转义大括号
        #加上$是以便与用户定义的变量区分开来。
        str = str.replace(f'${{{ key}}}', value)
    print(str)