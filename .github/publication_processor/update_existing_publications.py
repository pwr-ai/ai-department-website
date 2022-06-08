def get_scholar_tag(publication_uuid: str) -> str:
    path = f'scholar/scholar_publication/{publication_uuid}.bib'
    with open(path, 'r') as f:
        return f.readline().split('{')[1][:-2]


def is_publication_created(publication_tag) -> bool:
    pass


if __name__ == '__main__':
    print(get_scholar_tag('0a0f0a68-f8be-4dc4-a20b-189611f48a86'))
