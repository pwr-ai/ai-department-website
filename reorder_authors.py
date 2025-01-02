from pathlib import Path
from typing import List, Dict
import yaml 

def get_all_user_dirs() -> List[Path]:
    # get all directories in content/authors
    return [it for it in Path('content/authors').iterdir() if it.joinpath('_index.md').is_file()]


def get_user_info(user_directory: Path) -> dict:
    
    # get the title and role from the _index.md file using yaml parser
    with open(user_directory.joinpath('_index.md'), 'r') as f:
        # Czytamy tylko pierwszą część YAML (frontmatter)
        content = f.read()
        if content.startswith('---'):
            # Znajdujemy drugi znacznik ---
            parts = content.split('---', 2)
            if len(parts) >= 3:
                yaml_content = yaml.safe_load(parts[1])
                return {
                    'title': yaml_content.get('title', ''),
                    'role': yaml_content.get('role', '')
                }
        return {
            'title': '',
            'role': ''
        }

def get_user_mapping() -> Dict[str, tuple[str, str]]:
    # get the user mapping with both title and role
    return {
        it.name: get_user_info(it)
        for it in get_all_user_dirs()
        if it.joinpath('_index.md').is_file()
    }

def order_authors_in_roles(user_mapping: Dict[str, dict]) -> List[str]:
    # grupujemy autorów według ról i sortujemy w obrębie każdej roli
    roles_dict = {}
    for author, info in user_mapping.items():
        role = info['role'] or ''
        if role not in roles_dict:
            roles_dict[role] = []
        roles_dict[role].append(author)
    
    # sortujemy autorów w każdej roli
    for role in roles_dict:
        roles_dict[role] = sorted(roles_dict[role])
        
    return roles_dict

def get_ordered_authors_with_weights(roles_dict: Dict[str, list[str]]) -> Dict[str, int]:
    # get the ordered authors with weights
    return {
        author: i+10 if role == "Associate Professor, Deputy Head of the Department"
               else i+100 if role == "Full Professor"
               else i+200 if role == "Associate Professor"
               else i+300 if role == "Assistant Professor" 
               else i+400 if role == "Assistant"
               else i+1000 if role == "PhD Student"
               else i+2000 if role == "Alumni PhD"
               else i+500 if role == "Projects' office"
               else i+400 if role == "Team leader"
               else i+600 if role == "Project's staff"
               else i+1
        for role, authors in roles_dict.items() 
        for i, author in enumerate(authors)
    }

def update_author_weights(ordered_authors_with_weights: Dict[str, int]) -> None:
    for author, weight in ordered_authors_with_weights.items():
        author_file = Path(f'content/authors/{author}/_index.md')
        if not author_file.is_file():
            continue
            
        with open(author_file, 'r') as f:
            content = f.read()
            
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                yaml_content = yaml.safe_load(parts[1])
                yaml_content['weight'] = weight
                
                new_content = '---\n' + yaml.dump(yaml_content, allow_unicode=True) + '---' + parts[2]
                
                with open(author_file, 'w') as f:
                    f.write(new_content)


def main():
    user_mapping = get_user_mapping()
    # print(user_mapping) 
    ordered_authors = order_authors_in_roles(user_mapping)
    ordered_authors_with_weights = get_ordered_authors_with_weights(ordered_authors)
    
    print(ordered_authors)
    print(ordered_authors_with_weights)

    update_author_weights(ordered_authors_with_weights)




if __name__ == '__main__':
    main()