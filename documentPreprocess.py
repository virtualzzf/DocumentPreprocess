import nltk
import re
from nltk.corpus import stopwords

def camel_to_space(camel_format):
	space_format=''
	for i in range(len(camel_format)-1):
		if(camel_format[i].islower() and camel_format[i+1].isupper()):
			space_format+=camel_format[i]+' '
		else:
			space_format+=camel_format[i]
	space_format+=camel_format[-1]
	return space_format

key_words=[u'org',u'apache']
infile=open('./in.txt')
outfile=open('./out.txt','w')

for line in infile:
	src_noncamel=camel_to_space(line)
	src_lower=src_noncamel.lower()
	src_list=re.findall(r'\w+',src_lower)
	src_rmKey=[w for w in src_list if not w in key_words]
	src_nonstop=[w for w in src_rmKey if not w in stopwords.words('english')]	
	porter = nltk.PorterStemmer()
	src_stem=[porter.stem(t) for t in src_nonstop]
	src_long=[w for w in src_stem if len(w)>2]
	src_string=' '.join(src_long)
	outfile.write(src_string+"\n")
infile.close()
outfile.close()
