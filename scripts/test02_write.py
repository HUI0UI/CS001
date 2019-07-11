import yaml

data = {"name":"张三","age":18,"height":178.5}

with open('../data/write.yaml','w',encoding='utf-8') as f:
    yaml.dump(data,f,allow_unicode=True)