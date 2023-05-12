from atlassian import Confluence
from Readers.AbstratctReader import AbstractReader


class ConfluenceReader(AbstractReader):
    def __init__(self, url, username, password, space):
        self.confluence = Confluence(
            url=url,
            username=username,
            password=password,
            cloud=True)
        self.space = space

    def read(self):
        return self.confluence.get_space_content(self.space)