import sys
import os
import json
from pprint import pprint


contador = 0;
output = open("outputTags.txt", "w");


output.write("{\n");
output.write('\t"rollCalls": [\n');

for file in os.listdir ("motions.min"):
	with open('motions.min/' + file) as data_file:    
		data = json.load(data_file);
		#print data["type"];
		output.write("\t\t{\n");
		output.write('\t\t\t"name": "' + data["type"].encode('utf-8') + data["number"].encode('utf-8') + '",\n');
		output.write('\t\t\t"year": "' + data["year"].encode('utf-8') + '",\n');
		tags = unicode(data["tags"].encode('utf-8'), 'utf-8').lower();
		output.write('\t\t\t"tags": "' + tags.encode('utf-8') + '"\n');
		output.write("\t\t},\n");
output.write("\t]\n");
output.write("}\n")
#for file in os.listdir ("motions.min"):
#	motion = file.split(".txt")[0];
#	arq = open(motion + ".txt", "r");
	
#	contador = contador + 1;
#	output.write(motion + "\n");
#print contador; 
