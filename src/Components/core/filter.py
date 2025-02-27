# Copyright 2025 oppj4, cathome1, GOVNO-TON
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re

class Filter:
  def __init__(self, bad_words: list, text: str = "", link_flag: str = "approved"):
    self.text = text
    self.bad_words = bad_words
    self.link_flag = link_flag
    
  def text_filtration(self, text):
    result = text
    for word in self.bad_words:
      if word[:3] == "re:":
        try:
          search_word = re.compile(rf"\b{word[3:]}\b", flags=re.IGNORECASE)
          result = search_word.sub("*****", result)
        except:
          pass
      else:
        search_word = re.compile(rf"\b{re.escape(word)}\b", flags=re.IGNORECASE)
        result = search_word.sub(f"{'*' * len(word)}", result)
    return result
  
  def link_filtration(self, text):
    result = text
    url_pattern = re.compile(
        r'''
        (?:                            # Группа для опционального протокола или www
            https?://                  # http или https
            | ftp://                   # ftp
            | www\.                     # www без протокола
        )?                             # Всё опционально
        (?:                            # Основная структура домена:
            [a-zа-яё0-9-]+            # Субдомен (латиница, кириллица, цифры, дефисы)
            \.                         # Точка после субдомена
        )+                             
        (?:                            # TLD (доменная зона):
            [a-z]{2,}             # Минимум 2 символа (латиница)
            | xn--[a-z0-9]+            # Punycode-домены (например, .рф → xn--p1ai)
        )
        (?::\d+)?                      # Порт (:8080) опционально
        (?:/ [^\s?#<>]* )*             # Путь (/path) опционально
        (?:\? [^\s#<>]* )?             # Параметры (?query) опционально
        (?:\# [^\s<>]* )?              # Якорь (#anchor) опционально
        ''',
        flags=re.IGNORECASE | re.VERBOSE | re.UNICODE
    )
    
    if self.link_flag == "approved":
      pass
    elif self.link_flag == "censored":
      result = url_pattern.sub("*****", result)
    elif self.link_flag == "ignored" and re.findall(url_pattern, result):
      result = ""
    return result
  
  def full_filtration(self):
    unlinked_text = self.link_filtration(self.text)
    if unlinked_text:
      censored_text = self.text_filtration(unlinked_text)
      return censored_text
    else:
      return ""
