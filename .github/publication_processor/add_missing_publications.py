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


if __name__ == '__main__':
    print(get_user_mapping())
