from pathlib import Path
from typing import List, Dict


def get_all_pub_dirs() -> List[Path]:
    return [it for it in Path('content/publication').iterdir() if it.joinpath('index.md').is_file()]


def get_all_user_dirs() -> List[Path]:
    return [it for it in Path('content/authors').iterdir() if it.joinpath('_index.md').is_file()]


def get_full_user_name(user_directory: Path) -> str:
    with open(user_directory.joinpath('_index.md'), 'r') as f:
        return [it.replace('title: ', '') for it in f.read().splitlines(keepends=False) if it.startswith('title: ')][0]


def get_user_mapping() -> Dict[str, str]:
    return {
        get_full_user_name(it): it.name
        for it in get_all_user_dirs()
        if it.joinpath('_index.md').is_file()
    }


def process_publication(publication_dir: Path, user_mapping: Dict[str, str]):
    with open(publication_dir.joinpath('index.md'), 'r') as f:
        all_content_lines = f.read().splitlines(keepends=False)
    start_index = all_content_lines.index('authors:')
    end_index = all_content_lines.index('tags: []')
    all_keys = user_mapping.keys()
    for index in range(start_index, end_index):
        if all_content_lines[index].replace('- ', '') in all_keys:
            key = all_content_lines[index].replace('- ', '')
            all_content_lines[index] = f'- {user_mapping[key]}'
    with open(publication_dir.joinpath('index.md'), 'w') as f:
        f.write('\n'.join(all_content_lines))


def main():
    user_mapping = get_user_mapping()
    for pub in get_all_pub_dirs():
        process_publication(pub, user_mapping)


def print_all_emails() -> None:
    for it in get_all_user_dirs():
        print(it.joinpath('_index.md'))


if __name__ == '__main__':
    print_all_emails()
