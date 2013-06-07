import sys
import socket
import urllib
import urllib2
import re
from collections import deque
import os

def testurl(temp):
    try:
	if temp[0:8]=="https://":
		temp=temp[8:]
	if temp[0:7]=="http://":
		temp=temp[7:]
	urltest = socket.gethostbyname(temp)
	if (urltest):
            print "IP address of the host : "+urltest
    except:
	print >> sys.stdout, "Error:\n\tHost not valid."
	sys.exit(0)
def geturlcontents(URL):
	try:
		if URL[0:7]!="http://":
			URL="http://"+URL
		print URL
		queue2.append(URL)
		response = urllib2.urlopen(URL)
		html = response.readlines()
		urlpattern = (URL,"","\"/","\"\\","\"\\#" )
		for line in html:
			if "href" in line:
				if scope in line:
					p =re.compile('"http://([^"]*)"')
					q = p.findall(line)
					if q != []:
						queue.append(q)

				for x in urlpattern:
					if scope in line:
						p = re.compile('href="([^"]*)"')
						q = p.findall(line)
						if q != []:
							queue.append(q)
				for x in urlpattern:
					if x in line:
						p = re.compile(URL)
						q = p.findall(line)
						if q != []:
							queue.append( q)
					if x in line:
						p =re.compile('href="([^"]*)"')
						q = p.findall(line)
						if q != []:
							queue.append(q)
		for line in html:
			if "src" in line:
				for x in urlpattern:
					if x in line:
						p = re.compile(URL)
						q = p.findall(line)
						if q != []:
							queue.append(q)
					if x in line:
						p =re.compile('src="([^"]*)"')
						q = p.findall(line)
						if q != []:
							queue.append(q)
	except:
		pass
def sortlist(a,b):
	for x in a:
		if x not in b:
			for z in x:
				if z not in b:
					b.append(z)
			
	return b	
def cmscaner(b):
	try:
		print "Done with crawlling the site \n"
		print "default files found so far ..... \n"
		for x in CMS:
			i=0
			for y in x:
				for z in b:
					if y in z:
						i=i+1
						print y
						break
				if i>= 4: 
					print "scanner identified the above default files and as per signatures "
					if x == Silverstripe:
						print "CMS MAY BE Silverstripe"
					elif x ==  Joomla :
						print "CMS MAY BE Joomla"
					elif x == Wordpress:
						print "CMS MAY BE Wordpress"
						break
					elif x == Drupal:
						print "CMS MAY BE Drupal"
					elif x == ColdFusion:
						print "CMS MAY BE ColdFusion"
					elif x == Fatwire:
						print "CMS MAY BE Fatwire"
					elif x  == Sharepoint:
						print "CMS MAY BE Sharepoint"
					elif x == Vignette:
						print "CMS MAY BE Vignette"
					else:
						print ""+exception
							
		return b
	except:
		print "No Luck"
	"""MAIN"""

print "CMS SCANNER BY SHYAMKUMAR SOMANA" 
if len(sys.argv) < 2 or len(sys.argv) > 5:
		print "usage : xs3k.py hostname";
if len(sys.argv) == 2:
		temp = sys.argv[1]
testuri = temp
b=[temp]
queue = deque()
queue2 = deque() 
testurl(temp)
Silverstripe =["/assets/","cms/","/framework/","/mysite/","/vendor/","web.config"  ]
Drupal = ["/misc/","/modules/","/profiles/","/scripts/","/sites/","/corn.php"]  
Joomla = ["/administrator/","/cache/","/cli/","/components/","/language/","/libraries/","/logs/","/media/","/modules/","/plugins/","/templates/","/tmp/","/configuration.php","/htaccess.txt","/LICENSE.txt","/README.txt","/robots.txt"  ]
Wordpress = ["/wp-admin","/wp-content","/wp-includes","/license.txt","/readme.html","/wp-activate.php","/wp-blog-header.php","/wp-comments-post.php","/wp-config-sample.php","/wp-config.php","/wp-links-opml.php","/wp-load.php","/wp-login.php","/wp-mail.php","/wp-settings.php","/wp-signup.php","/wp-trackback.php","/xmlrpc.php"]
Coldfusion = ["CFIDE","CFIDE/administrator","CFIDE/administrator/aboutcf.cfm","CFIDE/administrator/Application.cfm","CFIDE/administrator/checkfile.cfm","CFIDE/administrator/enter.cfm","CFIDE/administrator/header.cfm","CFIDE/administrator/homefile.cfm","CFIDE/administrator/homepage.cfm","CFIDE/administrator/index.cfm","CFIDE/administrator/left.cfm","CFIDE/administrator/linkdirect.cfm","CFIDE/administrator/login.cfm","CFIDE/administrator/logout.cfm","CFIDE/administrator/navserver.cfm","CFIDE/administrator/right.cfm","CFIDE/administrator/tabs.cfm","CFIDE/administrator/welcome.cfm","CFIDE/administrator/welcomedoc.cfm","CFIDE/administrator/welcomeexapps.cfm","CFIDE/administrator/welcomefooter.cfm","CFIDE/administrator/welcomegetstart.cfm"]
Fatwire = ["servlet/HelloCS","servlet/ContentServer","servlet/Satellite","servlet/CatalogManager","servlet/BlobServer","servlet/TreeManager","servlet/CookieServer","servlet/CacheServer","servlet/EvalServer","servlet/DebugServer","servlet/FlushServer","servlet/SeedDispatchServer","servlet/Inventory","servlet/SyncSeedDispatchServer","servlet/PageDispatchServer","servlet/DispatchManager","servlet","HelloCS","ContentServer","Satellite","CatalogManager","BlobServer","TreeManager","CookieServer","CacheServer","EvalServer","DebugServer","FlushServer","SeedDispatchServer","Inventory","SyncSeedDispatchServer","PageDispatchServer","DispatchManager","Xcelerate/Admin/LoginPage.html","Xcelerate","Admin","LoginPage","LoginPage.html","Xcelerate/LoginPage.html","futuretense_cs/adminforms.html","futuretense_cs","adminforms","adminforms.html","futuretense","openmarket","fatwire","divine","contentserver","xcelerate","assetmaker"]
Sharepoint =["_layouts/AccessDenied.aspx","_layouts/AclInv.aspx","_layouts/AddContentTypeToList.aspx","_layouts/AddFieldFromTemplate.aspx","_layouts/AddNavigationLinkDialog.aspx","_layouts/AddWrkfl.aspx","_layouts/AdminRecycleBin.aspx","_layouts/AreaCacheSettings.aspx","_layouts/AreaNavigationSettings.aspx","_layouts/AreaTemplateSettings.aspx","_layouts/AreaWelcomePage.aspx","_layouts/AspXform.aspx","_layouts/AssetEditHyperLink.aspx","_layouts/AssetImagePicker.aspx","_layouts/AssetPortalBrowser.aspx","_layouts/AssetUploader.aspx","_layouts/AssocWrkfl.aspx","_layouts/AuditSettings.aspx","_layouts/Authenticate.aspx","_layouts/BackLinks.aspx","_layouts/BestBet.aspx","_layouts/BulkWrkTaskHandler.aspx","_layouts/BulkWrkTaskIP.aspx","_layouts/BusinessDataSynchronizer.aspx","_layouts/ChangeContentTypeOptionalSettings.aspx","_layouts/ChangeContentTypeOrder.aspx","_layouts/ChangeFieldOrder.aspx","_layouts/ChangeSiteMasterPage.aspx","_layouts/CmsSlwpAddEditGroup.aspx","_layouts/CmsSlwpAddEditLink.aspx"]
Vignette = ["/Deleting","/Docs/","/Editing/","/HOME/","/Images/","/Report/","/Select/","/TMT/","/allvars/","/asp/","/aspstatus/","/controller/","/diag/","/edit/","/error/","/errorpage/","/errors/","/executequery/","/external/","/ibm/","/initialize/","/internal/","/jspstatus/","/jsptest/","/legacy/","/listcolumns/","/loginlogo/","/logo/","/main/","/menu/","/metadataupdate/","/performance/","/portal/","/ppstats/","/preview/","/previewer/","/record/","/reset/","/save/","/stat/","/status/","/storyserver/","/style/","/stylepreviewer/","/utils/","/vdc/","/vgn/","/vr/","/Ping.jsp","/HelloWorld.jsp"]
CMS = [Silverstripe,Drupal,Joomla,Wordpress,Coldfusion,Fatwire,Sharepoint,Vignette]

if temp[0:8]=="https://":
	scope=temp[8:]
if temp[0:7]=="http://":
	scope=temp[7:]
else:
	scope=temp
print scope
print "printed" 
print "crawlling pages"
for URL in b:
	if "http://" in URL:
		if temp not in URL:
			pass
	elif "https://" in URL:
		if temp not in URL:
			pass
	elif "mailto:" in URL:
		pass
	else:
		if temp not in URL:
			if URL[0:1] == '/' :
				URL=temp+URL
			else:
				URL=temp+'/'+URL
		geturlcontents(URL)
		a=list(queue)
		a.sort()
		sortlist(a,b)
cmscaner(b)
	
	