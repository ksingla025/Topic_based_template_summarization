#!/usr/bin/python

import re,os

symptom_name_mapping = {'low self-esteem': 'low-self-esteem', 'obsessive behavior': 'obsessive-behavior', 'social inhibition': 'social-inhibition', 'withdrawal sickness': 'withdrawal-sickness', 'racing thoughts': 'racing-thoughts', 'compulsive behavior': 'compulsive-behavior', 'academic failure': 'academic-failure', 'chronic pain': 'chronic-pain', 'suicidal ideation': 'suicidal-ideation', 'problems concentrating': 'problems-concentrating', 'detached behavior': 'detached-behavior', 'suicidal behavior': 'suicidal-behavior', 'back pain': 'back-pain', 'loss of appetite': 'loss-of-appetite', 'general pain': 'general-pain', 'sexual dysfunction': 'sexual-dysfunction', 'acting out': 'acting-out', 'disorganized thoughts': 'disorganized-thoughts', 'severe sensitivity': 'severe-sensitivity', 'danger to others': 'danger-to-others', 'danger to self': 'danger-to-self', 'phantom pain': 'phantom-pain', 'family issues':'family-issues', 'family history':'family-history'}

def uccfilereader(filename):

	file = open(filename,'r').readlines()
	file_data = {}
	file_lines = []
	for line in file[1:]:

		try:
			role, data = line.lstrip().strip().split(":")
			text,tags = preprocess(data)

			#normalize codes
			for i in range(0,len(tags)):
				if tags[i] in file_data.keys():
					file_data[tags[i]].append(text)
				else:
					file_data[tags[i]] = []
					file_data[tags[i]].append(text)	
					file_lines.append(text)

#                        tags = list(set(tags))
#                        file_data.append([text,role,tags])
		except:
			continue
#		print(file_dat)
	for key in file_data.keys():
			output_file = open("data/"+os.path.basename(filename)+"_"+key+".txt",'w')
			for line in file_data[key]:
				output_file.write(line+" .\n")
			output_file.close()


#        output_file
	return " .".join(file_lines)

def preprocess(text):

        tags = re.findall('\{.*?\}',text)

        #remove all tags
        for tag in tags:
                text = text.replace(tag,'')
        for i in range(0,len(tags)):
                tags[i] = tags[i].replace("{","")
                tags[i] = tags[i].replace("}","")


        for key in symptom_name_mapping.keys():
        	text = text.replace(key, symptom_name_mapping[key])
#        	print("~~~searching")
        return text.lstrip(),tags
