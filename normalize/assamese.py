import re

def normalize_assamese(input_text: str) -> str:
	input_text1 = input_text
	
	########################################
	one_unicode_char = "ড় ঢ় য়  ো  ৌ"
	two_unicode_char1 = "ড ়"
	two_unicode_char2 = "ঢ ়"
	two_unicode_char3 = "য ়"
	two_unicode_char5 = "ে া"
	two_unicode_char6 = "ে ৗ"
	#############################################
	one_unicode_char1 = one_unicode_char.split()
	two_unicode_char11 = two_unicode_char1.split()
	two_unicode_char21 = two_unicode_char2.split()
	two_unicode_char31 = two_unicode_char3.split()
	two_unicode_char51 = two_unicode_char5.split()
	two_unicode_char61 = two_unicode_char6.split()
	#######################################################
	out = ''
	for i in range (len(input_text1)-1):
		text = str(input_text1[i])
		modified_text = ''
		for chr in text:
			flag = 0
			if (chr==one_unicode_char1[0]):
				res = ''.join(r'\u{:04X}'.format(ord(str(two_unicode_char11[0]))))
				modified_text = modified_text + res
				res = ''.join(r'\u{:04X}'.format(ord(str(two_unicode_char11[1]))))
				modified_text = modified_text + res
				flag = 1
			if (chr==one_unicode_char1[1]):
				res = ''.join(r'\u{:04X}'.format(ord(str(two_unicode_char21[0]))))
				modified_text = modified_text + res
				res = ''.join(r'\u{:04X}'.format(ord(str(two_unicode_char21[1]))))
				modified_text = modified_text + res
				flag = 1
			if (chr==one_unicode_char1[2]):
				res = ''.join(r'\u{:04X}'.format(ord(str(two_unicode_char31[0]))))
				modified_text = modified_text + res
				res = ''.join(r'\u{:04X}'.format(ord(str(two_unicode_char31[1]))))
				modified_text = modified_text + res 
				flag = 1
			if (chr==one_unicode_char1[3]):
				res = ''.join(r'\u{:04X}'.format(ord(str(two_unicode_char51[0]))))
				modified_text = modified_text + res
				res = ''.join(r'\u{:04X}'.format(ord(str(two_unicode_char51[1]))))
				modified_text = modified_text + res 
				flag = 1	
			if (chr==one_unicode_char1[4]):
				res = ''.join(r'\u{:04X}'.format(ord(str(two_unicode_char61[0]))))
				modified_text = modified_text + res
				res = ''.join(r'\u{:04X}'.format(ord(str(two_unicode_char61[1]))))
				modified_text = modified_text + res 
				flag = 1		
			###############################################################
			#same for all languages	
			if ((chr == '“') or (chr == '”')):
				res = ''.join(r'\u{:04X}'.format(ord('"')))
				modified_text = modified_text + res
				flag = 1
			if ((chr == "‘") or (chr == "’")):
				res = ''.join(r'\u{:04X}'.format(ord("'")))
				modified_text = modified_text + res
				flag = 1
			if ((chr =="৷") or (chr == "|")):
				res = ''.join(r'\u{:04X}'.format(ord("।")))
				modified_text = modified_text + res
				flag = 1 
			if ((chr == "৷৷") or (chr == "||") or (chr == "।।") or (chr == "।।")):
				res = ''.join(r'\u{:04X}'.format(ord("॥")))
				modified_text = modified_text + res
				flag = 1 				
			if ((chr=='‐') or (chr=='‒') or (chr=='–') or (chr=='—') or (chr=='―')):
				res = ''.join(r'\u{:04X}'.format(ord("-")))
				modified_text = modified_text + res	
				flag = 1
			if (chr=="_"):
				res = ''.join(r'\u{:04X}'.format(ord("_")))
				modified_text = modified_text + res	
				flag = 1				
			if (chr=="‥"):
				res = ''.join(r'\u{:04X}'.format(ord(".")))
				modified_text = modified_text + res
				res = ''.join(r'\u{:04X}'.format(ord(".")))
				modified_text = modified_text + res
				flag = 1
			if (chr=="…"):
				res = ''.join(r'\u{:04X}'.format(ord(".")))
				modified_text = modified_text + res
				res = ''.join(r'\u{:04X}'.format(ord(".")))
				modified_text = modified_text + res
				res = ''.join(r'\u{:04X}'.format(ord(".")))
				modified_text = modified_text + res
				flag = 1	
			if (flag==0):
				res = ''.join(r'\u{:04X}'.format(ord(chr)))
				modified_text = modified_text + res

		a1 = bytes(modified_text, 'utf-8').decode('unicode_escape') 
		out += str(a1)
	###############################################################
	#replace white spaces before special symbol
	out = out.replace(' ।', '।')
	out = out.replace(' ,', ',')
	out = out.replace(' ;', ';')
	out = out.replace(' ?', '?')
	out = out.replace(' :', ':')
	out = out.replace(' - ','-')
	out = out.replace(' -', '-')
	out = out.replace('- ','-')
	out = out.replace('( ','(')
	out = out.replace('[ ','[')
	out = out.replace('{ ','{')
	out = out.replace('< ','<')
	out = out.replace(' )',')')
	out = out.replace(' ]',']')
	out = out.replace(' }','}')
	out = out.replace(' >','>')
	out = out.replace(' /','/')
	out = out.replace('/ ','/')
	out = out.replace(' ॥','॥')
	out = out.replace(' ।।','॥')
	out = out.replace('।।','॥')
	out = out.replace(' ...', '...')
	out = out.replace(' ..', '..')
	out = out.replace(' .', '.')
	out = out.replace(" !", "!")
	out = out.replace("&quot;",'"')
	out = out.replace("''",'"')

	############ remove multi new lines ################
	match = re.findall(r'\n{2,}', out)
	#print("==>",len(match))
	for k in range(len(match)):
		no_space = match[k]
		space1 = ''
		for k1 in range(len(no_space)):
			space1 = space1 + "\n"
		out = out.replace(space1,"\n")
	out = out.replace("\n"," ")	

	match = re.findall(r'\s{2,}', out)
	for k in range(len(match)):
		no_space = match[k]
		space1 = ''
		for k1 in range(len(no_space)):
			space1 = space1 + " "
		out = out.replace(space1," ")	
	
	###########################################
	#replace white space after "
	substr1 = '"'
	a = [i.start() for i in re.finditer(substr1, out)]
	#print("a==>",a)
	b = 0
	if (len(a)>0):
		for j in range (0,len(a),2):
			#print("len(out)==>",len(out))
			out1 = ''
			start_index = a[j]-b
			end_index = a[j]-b + 1
			#print("start_index and end_index", start_index,end_index)
			if (start_index!=0):
				for i in range (start_index):
					chr1 = str(out[i])
					out1 = out1 + chr1
			if (str(out[end_index]) == " "):
				out1 = out1 + str(out[start_index])
				b = b+1
			else:
				out1 = out1 + str(out[start_index])
				out1 = out1 + str(out[end_index])
			if (end_index+1<=len(out)):
				for i in range (end_index+1, len(out), 1):
					out1 = out1 + str(out[i])
		
			out = out1
	
	#####################################################
	#replace white space before "
	substr1 = '"'
	a = [i.start() for i in re.finditer(substr1, out)]
	#print("a==>",a)
	b = 0
	if (len(a)>0):
		if (len(a)%2==0):
			r = len(a)+1
		else:
			r = len(a)
		for j in range (1,r,2):
			#print("len(out)==>",len(out))
			out1 = ''
			start_index = a[j]-b-1
			end_index = a[j]-b 
			#print("start_index and end_index", start_index,end_index)
			if (start_index!=0):
				for i in range (start_index):
					chr1 = str(out[i])
					out1 = out1 + chr1
			if (str(out[start_index]) == " "):
				out1 = out1 + str(out[end_index])
				b = b+1
			else:
				out1 = out1 + str(out[start_index])
				out1 = out1 + str(out[end_index])	
			if (end_index+1<=len(out)):
				for i in range (end_index+1, len(out), 1):
					out1 = out1 + str(out[i])
			
			out = out1
	###########################################
	#replace white space after '
	substr1 = " ' "
	a = [i.start() for i in re.finditer(substr1, out)]
	#print("a==>",a)
	b = 0
	if (len(a)>0):
		for j in range (0,len(a),2):
			#print("len(out)==>",len(out))
			out1 = ''
			start_index = a[j]+1-b
			end_index = a[j]+1-b + 1
			#print("start_index and end_index", start_index,end_index)
			if (start_index!=0):
				for i in range (start_index):
					chr1 = str(out[i])
					out1 = out1 + chr1
			if (str(out[end_index]) == " "):
				out1 = out1 + str(out[start_index])
				b = b+1
			else:
				out1 = out1 + str(out[start_index])
				out1 = out1 + str(out[end_index])
			if (end_index+1<=len(out)):
				for i in range (end_index+1, len(out), 1):
					out1 = out1 + str(out[i])
			out = out1
	
	#####################################################
	#replace white space before '
	substr1 = " ' "
	a = [i.start() for i in re.finditer(substr1, out)]
	#print("a==>",a)
	b = 0
	if (len(a)>0):
		for j in range (0,len(a),1):
			#print("len(out)==>",len(out))
			out1 = ''
			start_index = a[j]+1-b-1
			end_index = a[j]+1-b 
			#print("start_index and end_index", start_index,end_index)
			if (start_index!=0):
				for i in range (start_index):
					chr1 = str(out[i])
					out1 = out1 + chr1
			if (str(out[start_index]) == " "):
				out1 = out1 + str(out[end_index])
				b = b+1
			else:
				out1 = out1 + str(out[start_index])
				out1 = out1 + str(out[end_index])	
			if (end_index+1<=len(out)):
				for i in range (end_index+1, len(out), 1):
					out1 = out1 + str(out[i])
			out = out1
	######################################################
	#remove joinner character 200d at end of word 	
	substr1 = "\\u200d "
	a = [i.start() for i in re.finditer(substr1, out)]
	#print("a==>",a)	
	b = 0
	if (len(a)>0):
		for j in range (0,len(a),1):
			out1 = ''
			start_index = a[j]-b
			end_index = a[j]-b+1 
			#print("start_index and end_index", start_index,end_index)
			if (start_index!=0):
				for i in range (start_index):
					chr1 = str(out[i])
					out1 = out1 + chr1
			out1 = out1 + str(out[end_index])
			if (end_index+1<=len(out)):
				for i in range (end_index+1, len(out), 1):
					out1 = out1 + str(out[i])
			b = b+1	
			out = out1
	#################################################
	#remove joinner character 200c at end of word 		
	substr1 = "\\u200c "
	a = [i.start() for i in re.finditer(substr1, out)]
	#print("a==>",a)	
	b = 0
	if (len(a)>0):
		for j in range (0,len(a),1):
			out1 = ''
			start_index = a[j]-b
			end_index = a[j]-b+1 
			#print("start_index and end_index", start_index,end_index)
			if (start_index!=0):
				for i in range (start_index):
					chr1 = str(out[i])
					out1 = out1 + chr1
			out1 = out1 + str(out[end_index])
			if (end_index+1<=len(out)):
				for i in range (end_index+1, len(out), 1):
					out1 = out1 + str(out[i])
			b = b+1		
			out = out1
	####################################################
	return out