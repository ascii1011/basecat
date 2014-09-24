from io import analysis

class Comm(object):
    name = 'catacombs'
    title = 'Catacombs'

    def __init__(self, request):
        self.internal = {
            'sessionid': request.COOKIES.get('sessionid'),
            'ip': request.META.get('REMOTE_ADDR'),
        }

        self.input = str(request.POST.get('i')).lower()

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

        return self.res