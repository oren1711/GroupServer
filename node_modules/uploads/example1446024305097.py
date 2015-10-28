import urllib.request
import urllib
import os

def getString(tag,str):
	start = str.index("<"+tag+">")
	end = str.index("</"+tag+">")
	name = str[start+tag.__len__()+2:end-14]
	year = str[end-12:end-8] 
	return name,year

def getFrom(subString,text,plus=0,minus=0):
	try:
		text = str(text)
		subString = str(subString)
		start = text.index(subString)
		subText = text[start+subString.__len__()+plus:]
		end = subText.index("<")
		return subText[:end-minus],subText
	except ValueError as e:
		return "",""
def extract(url,pathOption,position):
	# x = urllib.request.urlopen("http://www.imdb.com/title/tt0172495/?ref_=tt_rec_tt").read()
	# x = urllib.request.urlopen("http://www.imdb.com/title/tt0268978/?ref_=nv_sr_1").read()
	x = urllib.request.urlopen(url).read()
	# print (x)
	xStr = str(x)
	
	name = "********************************************"
	year = "********************************************"
	datePublished = "********************************************"
	country = "********************************************"
	length = "********************************************"
	category = "********************************************"
	director = "********************************************"
	actors = "********************************************"
	description = "********************************************"
	image = "********************************************"

	name,year =getString("title",xStr)
	datePublished,rem = getFrom("\"See all release dates\" > ",x)

	country,rem = getFrom("/country/",x,36)
	anCountry,rem = getFrom("/country/",rem,36)
	if (anCountry!=""):
		country+=", "+anCountry

	length,rem = getFrom("M\" >\\n",x,16,6)

	category , rem = getFrom("?ref_=tt_stry_gnr\"\\n> ",x)
	for i in range(0,2):
		anCategory,rem = getFrom("?ref_=tt_stry_gnr\"\\n> ",rem)
		if (anCategory!=""):
			category+=", "+anCategory
		
	director, rem = getFrom("Director:",x,105)

	actors , rem = getFrom("tt_ov_st\"\\nitemprop=\\'url\\'><span class=\"itemprop\" itemprop=\"name",x,2)
	for i in range(0,4):
		anactors,rem = getFrom("tt_ov_st\"\\nitemprop=\\'url\\'><span class=\"itemprop\" itemprop=\"name",rem,2)
		if (anactors!=""):
			actors+=", "+anactors

	description , rem = getFrom("itemprop=\"description\">\\n",x)
	description = description.replace("""\\""","")

	image , rem = getFrom("Poster\"\\nsrc=\"",x,0,24)
	if pathOption==1:
		relPath = "assets/images/rec/"+name+".jpg"
		fullPath = "D:/study/year4/rec/rec project/recuserstudy/recuserstudy/client/"+ relPath
		fullPath = fullPath.replace("""\\""","")
	else:
		relPath = "assets/images/all/"+str(position+1)+".jpg"
		fullPath = "D:/study/year4/rec/rec project/recuserstudy/recuserstudy/client/"+ relPath
	f = open(fullPath,"wb")
	f.write(urllib.request.urlopen(image).read())
	f.close()

	print (",")
	print ("\t  \""+str(position)+"\": {")
	print ("\t\tname: \""+name+"\""+",")
	print ("\t\tyear: \""+year+"\""+",")
	print ("\t\tdatePublished: \""+datePublished+"\""+",")
	print ("\t\tcountry: \""+country+"\""+",")
	print ("\t\tlength: "+length+",")
	print ("\t\tcategory: \""+category+"\""+",")
	print ("\t\tdirector: \""+director+"\""+",")
	print ("\t\tactors: \""+actors+"\""+",")
	print ("\t\tdescription: \""+description+"\""+",")
	print ("\t\timage: \""+relPath+"\"")
	if pathOption==2:
		print ("\t\trecommend: [**,**,**,**]")
	print ("\t  }")

	textToCopy = ""
	textToCopy+= (","+"\\n")
	textToCopy+= ("\t  \""+str(position)+"\": {"+"\\n")
	textToCopy+= ("\t\tname: \""+name+"\""+","+"\\n")
	textToCopy+= ("\t\tyear: \""+year+"\""+","+"\\n")
	textToCopy+= ("\t\tdatePublished: \""+datePublished+"\""+","+"\\n")
	textToCopy+= ("\t\tcountry: \""+country+"\""+","+"\\n")
	textToCopy+= ("\t\tlength: "+length+","+"\\n")
	textToCopy+= ("\t\tcategory: \""+category+"\""+","+"\\n")
	textToCopy+= ("\t\tdirector: \""+director+"\""+","+"\\n")
	textToCopy+= ("\t\tactors: \""+actors+"\""+","+"\\n")
	textToCopy+= ("\t\tdescription: \""+description+"\""+","+"\\n")
	textToCopy+= ("\t\timage: \""+relPath+"\""+"\\n")
	if pathOption==2:
		textToCopy+= ("\t\trecommend: [**,**,**,**]"+"\\n")
	textToCopy+= ("\t  }"+"\\n")
	# addToClipboard(textToCopy)

def addToClipboard(text):
	command = "echo " + text.strip()  + "| clip"
	os.system(command)
REC = 1
ALL = 2
x = 176
url = "http://www.imdb.com/title/tt2224026/?ref_=nv_sr_1"
extract(str(url),REC,x)
# url = "http://www.imdb.com/title/tt0082340/?ref_=fn_al_tt_1"
# extract(str(url),REC,x+1)
# url = "http://www.imdb.com/title/tt0081505/?ref_=tt_rec_tt"
# extract(str(url),REC,x+2)
# url = "http://www.imdb.com/title/tt0221027/?ref_=nv_sr_1"
# extract(str(url),REC,x+3)