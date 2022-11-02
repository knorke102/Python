import json
import urllib.request
import requests
from bs4 import BeautifulSoup
import re


def get_ids_rel(json_object):
    new_ids = []
    root_id = json_object.get("id", None)
    if root_id is not None:
        new_ids.append(root_id)
    relatedgroups = json_object.get("relatedgroups", None)
    if relatedgroups is not None:
        for r in relatedgroups:
            for ri in r["relateditems"]:
                new_ids += get_ids_rel(ri)
    items = json_object.get("items", None)
    if items is not None:
        for i in json_object["items"]:
            new_ids += get_ids_rel(i)
    return new_ids


def check_url(req):
    soup_text = BeautifulSoup(req.text, 'html.parser')
    for link in soup_text.findAll('a'):
        title = link.getText('title=""')
        href = (link.get('href'))

        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        valid_url = (re.match(regex, href) is not None)  # True or False

        if valid_url:
            try:
                url_check = requests.head(href)
                if not url_check.status_code == 200:
                    print('failed', href, title)
            except:
                print('failed', href, title)

        # else:
        #     mail_dictonary = []
        #     if not valid_url == mail_dictonary:
        #         print('failed', valid_url)


def get_text(req):
    soup_text = BeautifulSoup(req.text, 'html.parser')
    get = list(set([text for text in soup_text.stripped_strings]))
    get = [i.replace('\n', ' ') for i in get]
    with open('req.txt', encoding='utf-8', mode='a') as file:
        file.write('\n'.join(get))


with urllib.request.urlopen("https:/example/en/toc.json") as url:
    data = json.load(url)
    rel = list(set(get_ids_rel(data)))

    for i in rel:
        req = requests.get("https://example/en/{}.html".format(i))
        req.encoding = str('utf-8')
        check_url(req)
        get_text(req)
