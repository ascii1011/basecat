
from locations.models import LocationBase



def translateToResponse(action, method):
    if method in []:
        pass
    

class analysis(object):
    """
    For now this api will take in one or two word commands and give a directive response.
    example:
        a = analysis({'i':'Go South'})
        action, method = a.generate()  
            - where action, in this case, would equal 'move' command 
            - method is probably a app or service like character or location in this case
        context = {'o': translateToResponse(action, method)}


    ======== later ========
    Idealy this api will take in:
     - a word
     - string of words (sentences are in my mind)
     - possibly callback or dict that would eventually give a response directive

    Use cases:

    from input import analysis

    request = {'i': 'move south'}
    request = {'i': 'pickup axe'}
    request = {'i': 'buy sword'}
    request = {'i': 'attack spider'}
    request = {'i': 'hit bookcase'}
    request = {'i': 'read book'}
    request = {'i': 'learn ice blast'}
    request = {'i': 'heal gabriel'}
    request = {'i': 'display my gear'}
    request = {'i': 'look at gabriels gear'}
    request = {'i': 'embue sword with emerald'}
    request = {'i': 'create mana potion'}

    a = analysis(request)
    a.tokenize()
    a.sentiment()
    a.action()
    a.act_upon()
    a.request_history()

    Models:
     - input_analysis (current request)
     - input_history (past results)

    Functionality:
     - record of action words (ex. go or move) translate to one api action 'moveTo'.
     - grab the object to which the user is attmepting to work against 
          (ex things, places, people)
     - determine intent, positive or negative sentence, etc
    """

    def __init__(self, request={}):
        self.request = request
        if request.get('i'):
            self.text = str(request.get('i')).lower()
            if not self.text:  
                self.null = True

            try:
                float(self.text)
                self.isnum = True
            except: 
                self.isnum = False

            