import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r= requests.get(url)
print("status code",r.status_code)
response_dict = r.json()
# print(response_dict.keys())

print("Total repositories:",response_dict['total_count'])
repo_dicts= response_dict['items']
print("repositories returned:" ,len(repo_dicts))
# repo_dict=repo_dicts[0]
# print('\nKeys:',len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
for repo_dict in repo_dicts:
    print('\nselected information about first repository:')
    print('name:',repo_dict['name'])
    print('owner:',repo_dict['owner']['login'])
    print('stars:',repo_dict['stargazers_count'])
    print('Respository:',repo_dict['html_url'])
    print('Created:',repo_dict['created_at'])
    print('Updated:',repo_dict['updated_at'])
    print('Description:',repo_dict['description'])