class Plant(object):

    def __init__(self, name, regions, rarity='', description='', notes=''):
        self.name = name
        self.regions = regions
        self.rarity = rarity
        self.description = description
        self.notes = notes

        foo = f'{self.name}.json'.lower().replace(' ', '_')
        self.filename = ''.join(ch for ch in foo if ch.isalnum() or ch == '.' or ch == '_')

    def __repr__(self):
        return f'{self.name} ({self.regions})'
