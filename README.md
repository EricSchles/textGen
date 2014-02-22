This is a simple text generator.  It makes use of the following article:

http://grammar.about.com/od/basicsentencegrammar/a/basicstructures.htm

Sentences are broken up into simple categories:
	
	simple sentences := of the form subject verb object
	compound sentences := of the form subject verb object and/or subject verb object
	complex sentences : = of the form subject verb object if/when/because/therefore subject verb object
	compound-complex sentences : has both complex and compound parts

basic usage:
import textGen 

tg = textGen.textgenerator()

tg.subjects = ["Eric","Brandon","Steve","Mark"]
tg.verbs = ["walk","walked","run","code","write"]
tg.objects = tg.subjects
tg.adjectives = ["well","poorly","slow","slowly"]

print text = tg.simple_textgen(num_words) #simple sentences
print text = tg.complete_textgen(num_words) #compoud and complex sentences
print text = tg.complex_textgen(num_words)  #complex sentences
print text = tg.compound_textgen(num_words) #compound setences

Dependencies:

https://bitbucket.org/leapfrogdevelopment/rstr/