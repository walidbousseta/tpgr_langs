

class Repository():
    """
    the repository information model
    paramters:
        full_name: the title of the repository
        url: api url to the repository information
    """
    def __init__(self, full_name, url):
        self.full_name = full_name
        self.url = url

class Language():
    """
    language information, contain list of repository using this language and there count
    paramters : 
        name: the language name
        count: number of repositories using the language
        repositories: list of Repository objects
    """
    def __init__(self, name, count, repositories):
        self.name = name
        self.count = count
        self.repositories = repositories



