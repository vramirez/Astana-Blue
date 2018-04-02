import os,ConfigParser,math,sys,time,twitter,json

config = ConfigParser.RawConfigParser()
config.read('twauth.properties')


key=config.get('OAuth','key')
key_secret=config.get('OAuth','key_secret')
token=config.get('OAuth','token')
token_secret=config.get('OAuth','token_secret')

print key
print key_secret
print token
print token_secret

auth=twitter.oauth.OAuth(token,token_secret,key,key_secret)
twitter_api= twitter.Twitter(auth=auth)

#Defaults

failname="bikthor"
curzord = -1

if len(sys.argv)>1 :
	failname=str.lower(sys.argv[1])

if len(sys.argv)>2 :
	curzord = sys.argv[2]

fail = open(failname)

for scream_name in fail:
	statuses=twitter_api.statuses.user_timeline(screen_name=scream_name,count=200)
	with open(scream_name[:-1]+".json", 'a+') as outfile:
		json.dump(statuses,outfile)
		outfile.close()
	time.sleep(1) 


