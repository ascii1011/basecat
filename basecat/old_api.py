
"""
This api determines from a sentence, what is being stated, yelled, or requested.

a request could be in the following forms:
 - action('move').direction('south'):
    ex: 's', 'south', 'South', 'go south'

 - action('look').direction('down'):
    ex: 'look down', 'pan room left', 'sit', 'lay down'

 - action('pick').object('lock')
 - action('talk').object('MVC-sally')
 - action('fight').objects('troll')
 - action('describe').objects('book')
"""
import re
from pprint import pprint

from basecat.models import LocationBase as Loc

from character import Character

catacombs = {
    'docs': [],
    'levels': {
        'id': 1,
        'docs': [
            'Welcome to "catacombs"',
        ],
        'rooms': {
            'id': 1,
            'words': {
                'north': 2,
                },
        },
    },
}

def begin():
    return catacombs['levels']


class Locations(object):
    
    def move(self, direction):
        pass


def response():
    return {
        'i': '',
        'messages': {
            'hints': [],
            },
        'location': 0,
        'character': None,
        'output': {},
    }


class Comm(object):

    name = 'catacombs'
    title = 'Catacombs'

    def __init__(self, request):
        self.internal = {
            'sessionid': request.COOKIES.get('sessionid'),
            'ip': request.META.get('REMOTE_ADDR'),
        }

        #self.user = request.user
        #self.profile = self.user.get_profile()

        self._input = str(request.POST.get('i'))
        self.input = self._input.lower()
        if not self.input:  
            self.null = True

        try:
            float(self.input)
            self.isnum = True
        except: 
            self.isnum = False



    def reset_character(self):

        self.res = {
            'messages': {
                'hints': [],
            },
            'location': 0,
            'character': None,
            'output': {
                'data': ['Welcome to %s' % self.title,
                         'an ever changing adventure game.',
                         'If you wish to a explore, then type "wow" + &lt;enter&gt;'
                     ],
                'klass': ''
            },
        }

    def generate(self):
        #input analysis

        #character

        #location

        return self.res
    
def comm(request):
    input = request.POST.get('i')
    _in = str(input).lower()

    print 'input: %s => %s' % ( str(input), str(_in) ) 

    session = request
    print 'session:'
    pprint( session )

    res = response()

    _character = Character()
    res.update({'character': _character.dump()})
    
    print 'input: %s' % _in
    if not _in:
        res['output'] = {
            'klass': 'red',
            'data': 'Sorry, I do not recognize that request',
            }
    
    if _in.isalnum(): 
        words = _in.split(' ')

        print 'words: %s' % str(words)

        if isinstance(words, list): 

            if len(words) != 1:
                #error... at the moment
                """
                at some point this is where the nltk would come into play
                """
                res['output'].update( {
                    'klass': 'red',
                    'data': ['Please state one word commands,', 
                             'I am a basic program.',
                             'Thank you.'] 
                })
            else:
                word = str(words[0])
                if word == '0':
                    res['output'].update( {
                        'klass': 'yellow',
                        'data': 'Welcome to Catacombs!!!'
                    })

                elif word in res['character']['commands']:
                    res.update({ 'output': _character.fetch(word) })

                elif word in ['north', 'south', 'east', 'west', 'up', 'down']:
                    res.update({'output': 'heading %s' % word})
                    
                else:
                    #error
                    res.update({'color': 'red',
                                'output': 'unrecognized command.'})

    else:
        #error
        res.update({'color': 'red',
                    'output': ['Letters and numbers only please...',
                               'Special characters are rejected.'] })
        
    return res

def temp():
    punct = ''
    if input[-1] in ['.', ',', '?', '!', ';']:
        punct = input[-1]
        input = input[:-2]