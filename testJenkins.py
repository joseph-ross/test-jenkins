import sys
import os
##sys.path.append(os.environ['WORKSPACE'])
##sys.path.append('/Users/joeross/Documents')
##sys.path.append('/usr/local/bin')
##sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages')
##sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/google/cloud')
##hold = ['', '/Users/joeross/Documents', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages']
##for item in hold:
##	sys.path.append(item)
##print(sys.path)
sys.path = ['/Users/joeross/Documents/GitHub/test-jenkins', '/Users/joeross/Documents', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages', '/usr/local/bin', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages']



import gcloud
from google.cloud import datastore

if __name__ == '__main__':

        print("start")
	print("Credentials :: " + sys.argv[1])
	print("Word :: " + sys.argv[2])

	ds_client = datastore.Client(project='leanplum',credentials=sys.argv[1])
	query = ds_client.query(kind='App')
	appKey = ds_client.key('App',int(5631331257679872))
	query.add_filter('app','=',appKey)
	qList = list(query.fetch())

	print(qList[0]['name'])
