import json


def read_json(file_path):
    with open(file_path, encoding='utf-8') as news_file:
        news = json.load(news_file)
        print(news)


if __name__ == '__main__':
    read_json('newsafr.json')