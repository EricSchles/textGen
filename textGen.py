import random #for testing
import re


class textgenerator():
    
    def __init__(self):
        self.subjects = []
        self.verbs = []
        self.objects = []
        self.adjectives = []

    def simple_textgen(self,num_words,compound=False):
        """
        num_words := expects the number of words to generate
        returns a randomly generated sentence
        Must include at least two words
        """
        if num_words < 2:
            raise Exception('must enter at least 2 words for a valid sentence')
        final_text = ""
        for i in xrange(num_words+1):
            if i%4 == 0:
                word = random.choice(self.subjects)
            elif i%4 == 1:
                word = random.choice(self.verbs)
            elif i%4 == 2:
                one_or_zero = random.randint(0,1000)%2
                if one_or_zero == 1:
                    obj_or_adj = "obj"
                else:
                    obj_or_adj = "adj"
                if obj_or_adj == "obj":
                    word = random.choice(self.objects)
                else:
                    word = random.choice(self.adjectives)
                    word += " " + random.choice(self.objects)
            else:
                if compound:
                    continue
                word = "."
            final_text += word + " "
        #it may be necessary to remove the space created before the '.'
        #the code for that goes here, depending on how well the classifier handles
        #this case in the data.
        
        return final_text

    def findall(self,string,pattern):
        return [m.start() for m in re.finditer(pattern,string)]

    #and, or
    def compound_textgen(self,num_words):
        if num_words < 5:
            raise Exception('must enter at least 5 words for a valid sentence')
        final_text = self.simple_textgen(num_words,True)
        for i in self.objects:
            offsets = self.findall(final_text,i)
            end = offsets[-1] + len(final_text[offsets[-1]:])
            offsets = offsets[:-1]
            offset = 0 #offset for the future offsets
            for j in offsets:
                j += len(i) + offset
                one_or_zero = random.randint(0,1000)%2
                if one_or_zero == 1:
                    final_text = final_text[:j] + " or" + final_text[j:]
                    offset += 3
                else:
                    final_text = final_text[:j] + " and" + final_text[j:]
                    offset += 4
            final_text += "."
        return final_text


    #when, if, therefore, because, because of
    def complex_textgen(self,num_words):
        complex_choices = [" when"," if"," therefore"," because", " because of"] 
        if num_words < 5:
            raise Exception('must enter at least 5 words for a valid sentence')
        final_text = self.simple_textgen(num_words,True)
        for i in self.objects:
            offsets = self.findall(final_text,i)
            offsets = offsets[:-1]
            offset = 0 #offset for the future offsets
            for j in offsets:
                j += len(i) + offset
                decision = random.choice(complex_choices)
                final_text = final_text[:j] + decision + final_text[j:]
                offset += len(decision)
            final_text += "."
        return final_text
            

    def complete_textgen(self,num_words):
        complex_choices = [" when"," if"," therefore"," because", " because of"] 
        compound_choices =[" or", " and"]
        if num_words < 5:
            raise Exception('must enter at least 5 words for a valid sentence')
        final_text = self.simple_textgen(num_words,True)
        for i in self.objects:
            offsets = self.findall(final_text,i)
            offsets = offsets[:-1]
            offset = 0 #offset for the future offsets
            counter = 0
            first = random.randint(0,5000)%2
            second = abs(first - 1)
            for j in offsets:
                j += len(i) + offset
                if counter % 3 == first:
                    decision = random.choice(complex_choices)
                if counter % 3 == second:
                    decision = random.choice(compound_choices)
                else:
                    decision = "."
                final_text = final_text[:j] + decision + final_text[j:]
                offset += len(decision)
                counter += 1
            final_text += "."

        return final_text
    


   
