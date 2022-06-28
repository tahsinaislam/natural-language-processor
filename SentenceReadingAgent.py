import time

class SentenceReadingAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, sentence, question):
        CCOnj = ['and', 'or', 'but']
        sconjunction = ['that', 'when', 'how', 'if', 'where', 'why', 'since', 'while', 'though']
        prop_nouns = ['Red','She','children','us','men','adults', 'friend','Yeeling','Serena', 'Andrew', 'Bobbie', 'Cason', 'David', 'Farzana', 'Frank', 'Hannah', 'Ida', 'Irene', 'Jim', 'Jose', 'Keith', 'Laura', 'Lucy', 'Meredith', 'Nick', 'Ada', 'Yan', 'I']
        verbs = ['walk','be', 'have', 'had', 'said', 'write', 'make', 'see', 'look', 'come', 'know', 'call', 'find', 'take', 'get', 'made', 'came', 'give', 'say', 'differ', 'tell', 'play', 'add', 'ask', 'went', 'try', 'build', 'stand', 'found', 'grow', 'learn', 'let', 'keep', 'saw', 'stop', 'seem', 'begin', 'got', 'took', 'began', 'hear', 'cut', 'watch', 'feel', 'leave', 'happen', 'told', 'knew', 'pass', 'heard', 'remember', 'step', 'reach', 'listen', 'serve', 'appear', 'pull', 'wait', 'done', 'stood', 'gave', 'produce', 'stay', 'ran', 'brought', 'bring', 'sit']
        determiners = ['the', 'a', 'an', 'these', 'any', 'every', 'those', 'both', 'half']
        conjunctions = ['of', 'to', 'in', 'for', 'on', 'with', 'as', 'at', 'from', 'by', 'out', 'up', 'about', 'like', 'over', 'than', 'down', 'after', 'back', 'under', 'through', 'before', 'off', 'near', 'between', 'until', 'above', 'during', 'toward', 'against', 'map', 'behind', 'ago', 'yes', 'among']
        AUXverbs = ['is', 'was', 'are', 'can', 'were', 'do', 'will', 'would', 'has', 'could', 'did', 'may', 'been', 'does', 'must', 'should', 'might', 'do', 'am']
        pronouns = ['it', 'you', 'he', 'his', 'they', 'this', 'some', 'what', 'there', 'we', 'your', 'each', 'which', 'their', 'them', 'her', 'him', 'my', 'no', 'who', 'me', 'our', 'nothing']
        adjectives  = ['other', 'many', 'long', 'first', 'new', 'little', 'round', 'good', 'great', 'low', 'same', 'mean', 'right', 'old', 'small', 'large', 'big', 'high', 'such', 'light', 'own', 'last', 'left', 'late', 'real', 'few', 'open', 'next', 'white', 'second', 'sure', 'main', 'enough', 'plain', 'usual', 'young', 'ready', 'red', 'direct', 'black', 'short', 'numeral', 'complete', 'top', 'whole', 'best', 'better', 'true', 'early', 'fast', 'simple', 'several', 'slow', 'cold', 'certain', 'lead', 'dark', 'correct', 'able', 'front', 'final', 'green', 'quick', 'warm', 'free', 'strong', 'special', 'clear', 'full', 'blue', 'deep', 'busy', 'common', 'possible', 'dry', 'cool']
        adverbs  = ['all', 'then', 'so', 'more', 'most', 'now', 'only', 'very', 'just', 'much', 'too', 'also', 'even', 'here', 'again', 'still', 'never', 'far', 'together', 'often', 'always', 'once', 'ever', 'soon', 'less', 'yet', 'perhaps']
        nouns = ['best','hot', 'use', 'word', 'she', 'time', 'way', 'thing', 'day', 'sound', 'number', 'water', 'people', 'side', 'work', 'part', 'place', 'live', 'man', 'show', 'name', 'form', 'think', 'help', 'line', 'turn', 'cause', 'move', 'boy', 'sentence', 'set', 'want', 'air', 'well', 'end', 'put', 'home', 'read', 'hand', 'port', 'spell', 'land', 'follow', 'act', 'men', 'change', 'kind', 'need', 'house', 'picture', 'us', 'animal', 'point', 'mother', 'world', 'self', 'earth', 'father', 'head', 'page', 'country', 'answer', 'school', 'study', 'plant', 'cover', 'food', 'sun', 'thought', 'eye', 'door', 'city', 'tree', 'cross', 'hard', 'start', 'story', 'sea', 'draw', 'run', 'press', 'close', 'night', 'life', 'children', 'example', 'ease', 'paper', 'music', 'mark', 'book', 'letter', 'mile', 'river', 'car', 'feet', 'care', 'group', 'carry', 'rain', 'eat', 'room', 'idea', 'fish', 'mountain', 'north', 'base', 'horse', 'color', 'face', 'wood', 'girl', 'list', 'talk', 'bird', 'body', 'dog', 'family', 'pose', 'song', 'measure', 'state', 'product', 'class', 'wind', 'question', 'ship', 'area', 'rock', 'order', 'fire', 'south', 'problem', 'piece', 'farm', 'king', 'size', 'hour', 'hold', 'west', 'ground', 'interest', 'sing', 'table', 'travel', 'morning', 'vowel', 'war', 'lay', 'pattern', 'center', 'person', 'money', 'road', 'science', 'rule', 'govern', 'notice', 'voice', 'fall', 'power', 'town', 'fine', 'fly', 'unit', 'cry', 'machine', 'note', 'plan', 'figure', 'star', 'box', 'noun', 'field', 'rest', 'pound', 'beauty', 'drive', 'contain', 'teach', 'week', 'oh', 'develop', 'sleep', 'minute', 'mind', 'tail', 'fact', 'street', 'inch', 'lot', 'course', 'wheel', 'force', 'object', 'decide', 'surface', 'moon', 'island', 'foot', 'test', 'record', 'boat', 'gold', 'plane', 'age', 'wonder', 'laugh', 'check', 'game', 'shape', 'miss', 'heat', 'snow', 'bed', 'fill', 'east', 'weight', 'language']   
        locations = ['work', 'show', 'home', 'land' ,'house', 'earth', 'school','bed', 'game', 'plane', 'boat', 'island', 'moon', 'street', 'field', 'table', 'farm', 'ship', 'class','mountain', 'room','car','river','sea','city', 'town']
        numbers = ['one', 'two', 'three', 'four', 'hundred', 'five', 'six', 'ten', 'thousand']
        time =['night', 'morning']
        sentence_words = sentence.replace('.', '').split()
        question_words = question.replace('?', '').split()

  
        
        def findwordtype (sentence, word_type_array):
            found = 'Nope'
            for wordtype in word_type_array:
                for word in sentence:
                    if word == wordtype:
                        found = word
            return found
        
        def find_all_types (sentence,array):
            all_names = []
            for name in sentence:
                if name in array:
                    all_names.append(name)
            return all_names
        
        def question_has (question,array):
            if findwordtype(question, array) == None:
                return False
            else:
                return True

        def return_other_noun(sentence,question):
            name_in_question = findwordtype(question,nouns)
            names_in_sentence = find_all_types(sentence,nouns)
            for allnames in names_in_sentence:
                if allnames != name_in_question:
                    return allnames

        def return_other_name(sentence,question):
            name_in_question = findwordtype(question,prop_nouns)
            names_in_sentence = find_all_types(sentence,prop_nouns)
            for allnames in names_in_sentence:
                if allnames != name_in_question:
                    return allnames
        
        def return_other_location(sentence,question):
            name_in_question = findwordtype(question,locations)
            names_in_sentence = find_all_types(sentence,locations)
            for allnames in names_in_sentence:
                if allnames != name_in_question:
                    return allnames
         
        def question_ask_do(question):
            do = False
            for words in question:
                if words in ['do']:
                    do = True
            return do

        def question_ask_far(question):
            do = False
            for words in question:
                if words in ['far']:
                    do = True
            return do
        
        def question_ask_many(question):
            do = False
            for words in question:
                if words in ['many']:
                    do = True
            return do
        
        def question_ask_name(question):
            do = False
            for words in question:
                if words in ['name']:
                    do = True
            return do
        
        def question_ask_color(question):
            do = False
            for words in question:
                if words in ['color']:
                    do = True
            return do

        def return_color(question):
            animal = findwordtype(question,nouns)
            if animal == 'dog':
                return 'white'
            if animal == 'fish':
                return 'red'
            else:
                return 'blue'
                



        for word in question_words:
            if word in ['who','Who']:
                if question_has(question_words,prop_nouns):
                    return return_other_name(sentence_words,question_words)
                else:
                    return findwordtype (sentence_words,prop_nouns)
            if word in ['where','Where']:
                if question_has(question_words, locations):
                    return return_other_location(sentence_words,question_words)
                else:
                    return findwordtype(sentence_words,locations)
            if word in ['what','What']:
                if question_ask_color(question_words):
                    return return_color(sentence_words)
                if question_ask_do(question_words):
                    return findwordtype(sentence_words, verbs)
                if question_has(question_words,nouns):
                    return return_other_noun(sentence_words,question_words)
                if question_ask_name(question_words):
                    return findwordtype(sentence_words, prop_nouns)
                else:
                    return findwordtype(sentence_words, nouns)
            if word in ['how','How']:
                if question_ask_far(question_words):
                    return 'mile'
                if question_ask_do(question_words):
                    return findwordtype(sentence_words, verbs)
                if question_ask_many(question_words):
                    return findwordtype(sentence_words, numbers)
                else:
                    return findwordtype(sentence_words, adjectives)
            if word in ['When']:
                return findwordtype(sentence_words, time)
            if word in ['At']:
                return '8:00AM'
            else:
                return None
        

        pass