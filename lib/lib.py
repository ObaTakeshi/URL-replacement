import json


class URL_lib:
    @staticmethod
    def search_url_list(current_url_host, url_list_file):
        with open(url_list_file, 'r') as jsonfile:
            url_list = json.load(jsonfile)

        for url_blocks in url_list['data']:
            for url_block in url_blocks:
                if current_url_host in url_block['url']:
                    return url_blocks

        return 0

    @staticmethod
    def get_url_host(url):
        return '/'.join(url.split('/')[:3])

    @staticmethod
    def get_url_path(url):
        return '/'.join(url.split('/')[3:])
