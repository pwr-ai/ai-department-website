import json
import logging
import os
import traceback
import uuid
from pathlib import Path
from typing import List, Optional, Dict
from urllib.parse import urlparse

logging.basicConfig()

import scholarly

scholarly.scholarly.set_logger(True)

from scholarly import scholarly, ProxyGenerator

_PUBS_LIST_PATH = 'scholar/pubs.json'


def get_all_pubs_scrapped() -> List[str]:
    if os.path.isfile(_PUBS_LIST_PATH):
        with open(_PUBS_LIST_PATH, 'r') as f:
            return json.loads(f.read())
    else:
        return []


def mark_pub_as_downloaded(publication_name: str) -> None:
    all_pubs = get_all_pubs_scrapped()
    all_pubs.append(publication_name)
    with open(_PUBS_LIST_PATH, 'w') as f:
        f.write(json.dumps(all_pubs))


def get_user_id_from_scholar_link(link: str) -> Optional[str]:
    query_dict = {
        it.split('=')[0]: it.split('=')[1]
        for it in urlparse(link).query.split('&')
        if len(it.split('=')) == 2
    }
    return query_dict['user'] if 'user' in query_dict else None


def get_file_lines(path: str) -> List[str]:
    with open(path, 'r') as f:
        return f.readlines()


def get_scholar_link_from_path(path: str) -> Optional[str]:
    lines = [
        it
        for it in get_file_lines(str(path))
        if 'https://scholar.google' in it
    ]
    if len(lines) == 0:
        return None
    elif len(lines) == 1:
        return [it for it in lines[0][:-1].split() if 'https://scholar.google' in it][0]
    else:
        raise Exception('too many lines with scholar lik')


def find_all_scholar_ids(path_root: str) -> Dict[str, str]:
    path_authors = Path.joinpath(Path(path_root), 'content/en/authors')
    scholar_dict = dict()
    for it in os.listdir(path_authors):
        user_md_path = Path.joinpath(path_authors, it, '_index.md')
        user_link = get_scholar_link_from_path(str(user_md_path))
        if user_link is not None:
            user_id = get_user_id_from_scholar_link(user_link)
            if user_id is not None:
                scholar_dict[it] = user_id
    return scholar_dict


def scrap_user(username: str, user_id: str):
    user_filename = f'scholar/scholar_user/{username}.json'
    if os.path.isfile(user_filename):
        print(f'username {username} already scrapped')
        return
    print(f'start scrap {username} {user_id}')
    author = scholarly.search_author_id(user_id, filled=True)
    user_json = json.dumps(author)
    print(user_json)
    with open(user_filename, 'w') as f:
        f.write(user_json)


def get_users():
    scholar_ids = find_all_scholar_ids('.')
    with open('scholar/scholar_ids.json', 'w') as f:
        f.write(json.dumps(scholar_ids))
    print(scholar_ids)
    for user in scholar_ids:
        scrap_user(user, scholar_ids[user])


def get_pubs_names() -> List[str]:
    to_return = []
    for it in os.listdir('scholar/scholar_user'):
        path = f'scholar/scholar_user/{it}'
        with open(path, 'r') as f:
            for pub in json.loads(f.read())['publications']:
                to_return.append(pub['bib']['title'])
    return to_return


def scrap_publication(publication_name: str):
    if publication_name not in get_all_pubs_scrapped():
        print('scrap publication', publication_name)
        pub = scholarly.search_single_pub(publication_name, filled=True)
        scholarly.pprint(pub)
        publication_json = json.dumps(pub)
        bib_title = json.loads(publication_json)['bib']['title']
        print(bib_title, publication_name == bib_title)
        with open(f'scholar/scholar_publication/{uuid.uuid4()}.json', 'w') as f:
            f.write(publication_json)
        mark_pub_as_downloaded(publication_name)
    else:
        print('already scraped publication', publication_name)


def create_dir_soft(dir_path: str):
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)


def main_scrap() -> bool:
    try:
        print("start new main")
        pg = ProxyGenerator()
        pg.Tor_Internal(tor_cmd="tor")
        scholarly.use_proxy(pg)
        create_dir_soft('scholar')
        create_dir_soft('scholar/scholar_user')
        create_dir_soft('scholar/scholar_publication')

        get_users()
        print(get_pubs_names())
        for pub_name in get_pubs_names():
            scrap_publication(pub_name)
        return True
    except Exception as e:
        print(e)
        traceback.print_exc()
    return False


if __name__ == '__main__':
    try_count = 1000
    is_success = False
    while not is_success and try_count > 0:
        try_count = try_count - 1
        is_success = main_scrap()
        scholarly.use_proxy(None)
        os.system('sudo killall -9 tor')
