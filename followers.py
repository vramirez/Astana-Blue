import ConfigParser,math,sys,time,twitter,json

config = ConfigParser.RawConfigParser()
config.read('twauth.properties')


key=config.get('OAuth','key')
key_secret=config.get('OAuth','key_secret')
token=config.get('OAuth','token')
token_secret=config.get('OAuth','token_secret')


auth=twitter.oauth.OAuth(token,token_secret,key,key_secret)
twitter_api= twitter.Twitter(auth=auth)

#Defaults

scream_name="bikthor"
curzord = -1

if len(sys.argv)>1 :
	scream_name=sys.argv[1]

if len(sys.argv)>2 :
	curzord = sys.argv[2]


def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

print "Iniciando escaneo de Followers para: "+scream_name+", desde cursor:"+str(curzord)

if not os.path.exists(scream_name):
    os.makedirs(scream_name)

while (curzord != 0):
	generalist=twitter_api.followers.ids(screen_name=scream_name,cursor=curzord)
	follow_ids=generalist["ids"] #5000 ids
	curzord=generalist["next_cursor"]
	las50=split_list(follow_ids, wanted_parts = int(math.ceil(len(follow_ids)/float(100))))
	filename=scream_name+"/"+scream_name+'_'+str(curzord)+'.json'
	for i in range(len(las50)):
		ids100 = twitter_api.users.lookup(user_id=",".join([str(x) for x in las50[i]]))
		with open(filename, 'a+') as outfile:
	    		json.dump(ids100, outfile)
			outfile.write("\n")
			outfile.close()
	time.sleep(55)


