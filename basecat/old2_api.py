
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

from locations.models import LocationBase

from io import analysis
#from character import Character
#from locations import Location



class Comm(object):
    """
    
    """

    name = 'catacombs'
    title = 'Catacombs'

    def __init__(self, request):
        self.internal = {
            'sessionid': request.COOKIES.get('sessionid'),
            'ip': request.META.get('REMOTE_ADDR'),
        }

        self._input = str(request.POST.get('i'))
        self.input = self._input.lower()

        self.setDefault()


    def setDefault(self):

        self.res = {
            'messages': {
                'hints': [],
            },
            'location': dict(),
            'character': dict(),
            'output': {
                'data': ['Welcome to %s' % self.title,
                         'an ever changing adventure game.',
                         'If you wish to a explore, then type "wow" and press &lt;enter&gt;'
                     ],
                'klass': ''
            },
        }

    def generate(self):
        #input analysis

        #determine mode types: chat, play/game, me, settings

        #character

        #location

        #switch, if needed, to the determined mode
            #chat
            #play
            #market
            #me
            #settings

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