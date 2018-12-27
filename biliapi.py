# -*- coding: utf-8 -*-

import requests
import json

class bilivid():
  def __init__(self, aid):
    raw = requests.get('https://api.bilibili.com/x/web-interface/view/detail?aid=' + str(aid))
    self.__INFO = json.loads(raw.text)
    if self.__INFO['code'] != 0:
      raise RuntimeError('Failed to get video info')

  @property
  def avid(self):
    return self.__INFO['data']['View']['aid']

  @property
  def title(self):
    return self.__INFO['data']['View']['title']

  @property
  def parts(self):
    return self.__INFO['data']['View']['videos']

  @property
  def date(self):
    return self.__INFO['data']['View']['pubdate']

  @property
  def desc(self):
    return self.__INFO['data']['View']['desc']

  @property
  def upname(self):
    return self.__INFO['data']['View']['owner']['name']
