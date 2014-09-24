from pprint import pprint

class Character(object):

    def __init__(self):
        self.whoami = {
            'name': '',
            'sex': '',
            'class': '',
            'race': '',
        }

        self.skills = {
            'str': 1,
            'dex': 1,
            'int': 1,
            'wis': 1,
            'con': 1,
            'cha': 1,
        }
        
        self.status = {
            'level': 0,
            'defense': 0,
            'offense': 0,
            'hitpoints': 20,
            'mana': 1,
            'experience': 1,
        }

        self.accounting = {
            'gold': 0,
            'latinum': 0,
            'plantinum': 0,
            'silver': 0,
            'bronze': 0,
            'steel': 20,        
        }
        
        self.stash = []

        self.equiped = {
            'hands': '',
            'head': '',
            'chest': '',
            'legs': '',
            'feet': '',
            'waist': '',
            'right_hand': '',
            'left_hand': '',
            'fingers':'',
        }

        self.commands = [
            'commands',
            'whoami',
            'stash',
            'equiped',
            'status',
            'skills',
        ]

    def fetch_commands(self):
        return self.commands
        
    def fetch(self, command='commands'):
        if command == 'whoami':
            return self.whoami

        if command == 'stash':
            return self.stash

        if command == 'equiped':
            return self.equiped

        if command == 'status':
            return self.status

        if command == 'skills':
            return self.skills

        if command == 'accounting':
            return self.accounting

        return str(self.commands)


    def dump(self):
        return {
            'whoami': self.whoami,
            'skills': self.skills,
            'status': self.status,
            'stash': self.stash,
            'equiped': self.equiped,
            'accounting': self.accounting,
            'commands': self.commands,
            }
