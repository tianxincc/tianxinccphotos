import os
import time
import requests

new_list = {}

def get_hitokoto(url):
    response = requests.get(url)
    if response.status_code == 200:
        time.sleep(1)
        return response.json()['hitokoto']
    else:
        return '获取一言失败，请稍后再试。'

dir_list = {'marry':'marry'}
for typea in dir_list:
  dir = dir_list[typea]
  file_list = os.listdir(dir)
  for name in file_list:
      new_list[name.split('.')[0]] = typea


new_lists = sorted(new_list.keys())
for names in new_lists:
  
  dir = new_list[names]
  filename = names+'.jpg'
  file_path = 'images/'+dir+'/'+filename
  content = '''
        <div data-sjsel="%s">
            <div class="card">
                <a href="%s" target="_blank">
                  <img class="card__picture" src="%s">
                </a>
                <div class="card-infos">
                    <h2 class="card__title">%s</h2>
                    <p class="card__text">
                      %s
                    </p>
                </div>
            </div>
        </div>''' % (dir,file_path,file_path,get_hitokoto('https://v1.hitokoto.cn/?c=e&max_length=10'),get_hitokoto('https://v1.hitokoto.cn/?c=f'))

  print(content)
