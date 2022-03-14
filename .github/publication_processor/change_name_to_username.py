import os
from pathlib import Path
from typing import Dict, List

import unidecode


def get_full_name_from_path(path: str) -> str:
    with open(path, 'r') as file:
        line = [it for it in file.read().splitlines() if it.startswith('title: ')][0]
        return line[6:].strip()


def get_username_from_path(path: str) -> str:
    return path.split('/')[-2]


def find_all_users(path_root: str) -> Dict[str, str]:
    path_authors = Path.joinpath(Path(path_root), 'content/en/authors')
    user_paths = [str(Path.joinpath(path_authors, it, '_index.md')) for it in
                  os.listdir(path_authors)]
    return {unidecode.unidecode(get_full_name_from_path(it)): get_username_from_path(it)
            for it in user_paths}


def find_lines_with_authors_indexes(all_lines: List[str]) -> List[int]:
    start_index = [it for it in range(len(all_lines)) if all_lines[it].startswith('authors:')][0]
    to_return = []
    index = start_index + 1
    while index < len(all_lines) and all_lines[index].strip().startswith('-'):
        to_return.append(index)
        index = index + 1
    return to_return


def get_all_index_publications(path_root: str) -> List[str]:
    path_authors = Path.joinpath(Path(path_root), 'content/en/publication')
    return [str(Path.joinpath(path_authors, it, 'index.md')) for it in os.listdir(path_authors)]


def get_fixed_author_line(line: str, authors_dict: Dict[str, str]) -> str:
    fixed_line = unidecode.unidecode(line)
    keys = authors_dict.keys()
    found_keys = [it for it in keys if it in fixed_line]
    if len(found_keys) == 0:
        print('not_found')
        print(line, fixed_line)
        return line
    else:
        key = found_keys[0]
        return fixed_line.replace(key, authors_dict[key])


def main():
    user_mapping = find_all_users('.')
    get_all_index_publications('.')
    for itt in get_all_index_publications('.'):
        if os.path.exists(itt):
            print(itt)
            with open(itt, 'r') as f:
                content_lines = f.read().splitlines()
            indexes = find_lines_with_authors_indexes(content_lines)
            new_content_lines = [
                content_lines[line_index] if line_index not in indexes else get_fixed_author_line(
                    content_lines[line_index], user_mapping)
                for line_index in range(len(content_lines))
            ]
            # print(new_content_lines)
            with open(itt, 'w') as f:
                f.write('\n'.join(new_content_lines) + '\n')


if __name__ == '__main__':
    main()
