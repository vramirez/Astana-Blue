import os,configparser,math,sys,time,twitter,json
from datetime import datetime
import pytz

config = configparser.RawConfigParser()
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
#print (sys.argv[1])
if len(sys.argv)>1 :
	scream_name=str.lower(sys.argv[1])

if len(sys.argv)>2 :
	curzord = sys.argv[2]

#Splits a list into several *wanted* lists
def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

def stringToDate(deit):
	return datetime.strptime(deit,'%a %b %d %H:%M:%S %z %Y')

print ("Iniciando escaneo de Followings para: "+scream_name+", desde cursor:"+str(curzord))

if not os.path.exists(scream_name):
    os.makedirs(scream_name)

while (curzord != 0):
	generalist=twitter_api.friends.ids(screen_name=scream_name,cursor=curzord,count=5000)
	follow_ids=generalist["ids"] #5000 ids
	curzord=generalist["next_cursor"]
	las50=split_list(follow_ids, wanted_parts = int(math.ceil(len(follow_ids)/float(100))))
	#filename=scream_name+"/"+scream_name+'_'+str(curzord)+'.json'
	print("longitud ",len(follow_ids))
	print("las50 ",len(las50))
	for accounts in las50:
		print("loops! ################################## ",len(accounts))
		yusers =twitter_api.users.lookup(user_id= ",".join([str(x )for x in accounts]))
		for yuser in yusers: #Will run mostly 100 users
			if 'status' in yuser:
				deit=yuser['status']['created_at']
				ndeit=stringToDate(deit)
				tdelta=datetime.now(pytz.utc)-ndeit
				if(tdelta.days>180):
					print("removing",yuser['screen_name'],yuser['name'])
					#twitter_api.friendships.destroy(user_id=yuser['id'])
					#time.sleep(5)
			else:
				print("no status for ",yuser['screen_name'],yuser['name'])
	#time.sleep(45)


