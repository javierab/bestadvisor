#!/usr/bin/python

#get areas array for professors. 

#first load the map of topics.
map = {'predictive models' : 1, 
'human-computer interaction' : 2, 
'multicores' : 8, 
'networks' : 4, 
'systems for ml' : 1, 
'distributed data' : 3, 
'distributed systems' : 3, 
'web architecture' : 4, 
'computational geometry' : 5, 
'big data' : 1, 
'cognitive neuroscience' : 6, 
'programming languages and systems' : 7, 
'deep learning science' : 1, 
'languages' : 7, 
'systems' : 3, 
'internet architectures' : 4, 
'motion planning' : 8, 
'zero-knowledge proofs' : 7, 
'signal processing' : 8, 
'cryptography' : 1, 
'performance modeling' : 3, 
'cybersecurity (w3c ceo)' : 1, 
'web decentralization' : 4, 
'mobile systems' : 3, 
'operating systems' : 9, 
'human language technologies' : 1, 
'software analysis' : 9, 
'architecture' : 8, 
'statistical inference' : 1, 
 'security' : 1, 
'compilers' : 7, 
'image compression' : 5, 
'vision' : 5, 
'programming methodology' : 9, 
 'cybersecurity' : 1, 
'navigation/mapping' : 7, 
'self-driving cars' : 4, 
'high-performance computing' : 3, 
'software design' : 9, 
'communications  policy' : 9, 
'classic ai' : 1, 
'programming languages' : 7, 
'interactive data exploration' : 2, 
'health' : 6, 
'motion planning and control' : 8, 
'medicine' : 6, 
'real-time computing' : 3, 
'graph processing' : 7, 
'spoken language systems' : 1, 
'perception' : 7, 
'performance engineering' : 3, 
'theory' : 7, 
'perception/cognition' : 7, 
'medical imaging' : 6, 
'human language' : 1, 
'statistics' : 1, 
'computer-aided design' : 1, 
 'rsa public-key encryption' : 1, 
'software development' : 9, 
'helping people manage information' : 1, 
'systems for processing and manipulating data' : 1, 
'web policy' : 1, 
'parallel and distributed operating systems' : 3, 
'economics' : 1, 
'programming' : 7, 
'software' : 9, 
'programming languages and verification' : 7, 
'inference' : 1, 
'data science' : 1, 
'robotics' : 1, 
'healthcare' : 6, 
'app inventor' : 9, 
'supercomputers' : 3, 
'applied algorithms' : 7, 
'genomics' : 6, 
'touch sensing' : 2, 
 'privacy' : 1, 
 'encryption' : 1, 
'complexity theory' : 7, 
'multiprocessors' : 3, 
'memory' : 6, 
'data management' : 1, 
'computational genomics' : 6, 
'wireless' : 4, 
'systems for social change and creative expression' : 9, 
'ml for systems' : 1, 
'graphics' : 5, 
'computational imaging' : 5, 
'functional programming' : 7, 
'online education' : 9, 
'computational photography' : 5, 
'machine learning' : 1, 
'optimization' : 1, 
'speech and language processing' : 1, 
'artificial intelligence' : 1, 
'languages and systems' : 7, 
'theory of computation' : 7, 
'data-driven inference' : 1, 
'game theory' : 7, 
'parallel computing' : 3, 
'ai' : 1, 
'3d printing' : 8, 
'web standards' : 9, 
'web accessibility' : 9, 
'hardware' : 8, 
'applied ai and ml in cybersecurity' : 1, 
'education' : 9, 
'ml security' : 1, 
'autonomy' : 1, 
'formal methods' : 7, 
'storage' : 8, 
'security and privacy' : 1, 
'bayesian modeling' : 1, 
'natural language processing' : 1, 
'mathematics' : 7, 
'computational biology' : 6, 
'user interfaces' : 2, 
'databases' : 8, 
'complexity' : 7, 
'architectures' : 8, 
'neuroscience' : 6, 
'inventor of the world wide web' : 4, 
'fabrication' : 8, 
'software engineering' : 9, 
'algorithms' : 7}



#now read files and build array for each prof.

out = open("profarray","w")

for line in  open("topicsbyprof"):

	arr = [0]*10

	(name, topic) = line.replace(')\n','').split(':');
	topics = topic.split(',')

	for t in topics:
		st = t.strip(' \t\n.').lower()
		n = map.get(st)
		if n != None and n > 0: 
			arr[n-1]+=1

	sarr = [str(a) for a in arr]
	out.write(name + ", '" + topic + "', '{" + ','.join(sarr) + "}'),\n")
	
