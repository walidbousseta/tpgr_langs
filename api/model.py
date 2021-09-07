

class Repository():
    def __init__(self, full_name, url):
        self.full_name = full_name
        self.url = url

class Language():
    def __init__(self, name, count, repositories):
        self.name = name
        self.count = count
        self.repositories = repositories



