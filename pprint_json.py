import json


def load_data(filepath):
    with open(filepath, encoding='UTF-8') as data_file:
        return json.load(data_file)


def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=1))


if __name__ == '__main__':
    data = load_data(input('Введите путь до файла: '))
    pretty_print_json(data)