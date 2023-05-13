import yaml
from Readers.ConfluenceReader import ConfluenceReader

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)


def get_reader():
    if config['reader_type'] == 'confluence':
        api_token = config['api_token']
        base_url = config['base_url']
        username = config['username']
        space = config['space']
        return ConfluenceReader(base_url, username, api_token, space)
    else:
        raise ValueError(f"Unknown reader type: {config['reader_type']}")


