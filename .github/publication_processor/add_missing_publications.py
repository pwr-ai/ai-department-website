import json
import os
from typing import List, Dict


def get_file_content(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()


def get_scholar_users_files() -> List[str]:
    files = os.listdir('scholar/scholar_user')
    return [f'scholar/scholar_user/{it}' for it in files]


def get_scrapped_uid() -> List[str]:
    return list(set([it.split('.')[0] for it in os.listdir('scholar/scholar_publication')]))


def get_user_mapping() -> Dict[str, str]:
    return {
        json.loads(get_file_content(it))['name']: it.split('/')[-1].split('.')[0]
        for it in get_scholar_users_files()
    }


def get_bib_path(pub_scrapped_id: str) -> str:
    return f'scholar/scholar_publication/{pub_scrapped_id}.bib'


def get_json_path(pub_scrapped_id: str) -> str:
    return f'scholar/scholar_publication/{pub_scrapped_id}.json'


def add_pub_with_id(pub_scrapped_id: str):
    print(f'adding publication {pub_scrapped_id}')
    bib_path = get_bib_path(pub_scrapped_id)
    print(get_file_content(bib_path))
    os.system(f'academic import'
              f' --publication-dir content/en/publication'
              f' --bibtex {bib_path}')


if __name__ == '__main__':
    all_pubs = json.load(open('scholar/pubs.json', 'r'))
    for pub_id in get_scrapped_uid()[:2]:
        title = json.load(open(get_json_path(pub_id), 'r'))['bib']['title']
        if title in all_pubs:
            add_pub_with_id(pub_id)
    # for pub_id in get_scrapped_uid()[:10]:
    #     title = json.load(open(get_json_path(pub_id), 'r'))['bib']['title']
    #     print(title in all_pubs, title)
