import re

from jinja2 import Template, FileSystemLoader, Environment
import yaml


def regex_sub(value, pattern, repl):
    return re.sub(pattern, repl, value)


env = Environment(loader=FileSystemLoader('.'))
env.filters['regex_sub'] = regex_sub
template = env.get_template('template.html')

with open('me.yaml', 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

data['research grants'].sort(key=lambda x: (x['from']['year'], x['from']['month'], x['from']['day']), reverse=True)
data['educational background'].sort(key=lambda x: (x['from']['year'], x['from']['month']))
data['teaching experiences'] = [x for x in data['teaching experiences'] if x['type'] != '担当' and x['type'] != '代講']

print(template.render(data=data))
