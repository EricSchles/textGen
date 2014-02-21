This is a simple text generator.  It makes use of the following article:

http://grammar.about.com/od/basicsentencegrammar/a/basicstructures.htm

Sentences are broken up into simple categories:
	
	simple sentences
	compound sentences
	complex sentences
	compound-complex sentences

basic usage:
import textGen as tg

tg.subjects = ["Eric","Brandon","Steve","Mark"]
tg.verbs = ["walk","walked","run","code","write"]
tg.objects = tg.subjects
tg.adjectives = ["well","poorly","slow","slowly"]

print text = tg.textgen(num_words)

