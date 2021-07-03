import csv

class URL_lib:
    @staticmethod
    def hoge():
        return 0

    @staticmethod
    def search_url_list(current_url_host, url_list_file):
        with open(url_list_file, 'r') as csvfile:
            url_list = csv.reader(csvfile, skipinitialspace=True)

            for row in url_list:
                for col in row:
                    if current_url_host in col:
                        return row

        return 0

    @staticmethod
    def get_url_host(url):
        return '/'.join(url.split('/')[:3])

    @staticmethod
    def get_url_path(url):
        return '/'.join(url.split('/')[3:])


