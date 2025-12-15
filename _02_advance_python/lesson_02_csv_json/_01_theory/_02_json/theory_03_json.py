import json


class MyCat:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


def write_data_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as fp:
        json.dump(obj=data, fp=fp,
                  default=lambda data: data.__dict__,
                  ensure_ascii=False, indent=4)
        return True


def get_json_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as fp:
        data = json.load(fp=fp)
    return data


if __name__ == '__main__':
    cat = MyCat('Барсик', 3, 'самец')
    write_data_json(r'json_files\cat_data.json', cat)

    cat_from_file = get_json_data(r'json_files\cat_data.json')
    new_cat = MyCat(cat_from_file['name'], cat_from_file['age'], cat_from_file['gender'])
    print(new_cat.name, new_cat.age, new_cat.gender)
