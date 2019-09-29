import os
class Lampp:
  def __init__(self):
    #check status Virtual hosts
    httpd = open('httpd.conf', 'r')
    read_h = httpd.read()
    self.stt = read_h.find("# Virtual hosts\nInclude etc/extra/httpd-vhosts.conf")
  def add_domain(self, domain, folder):
  	#check domain exist in hosts file
	f = open('/etc/hosts', 'a+')
	
	if f.read().find('\n127.0.0.1 '+domain+'') < 0:
		#add domain to hosts file
		f.write('\n127.0.0.1 '+domain+'')
		f.close()
	#edit httpd-vhosts.conf file
	vhosts_conf = open('/opt/lampp/etc/extra/httpd-vhosts.conf', 'a+')

	if vhosts_conf.read().find('ServerName '+folder+'') < 0:
		a = '\n<VirtualHost *:80>\n\
		    ServerAdmin xxxxxx@domain.com\n\
		    DocumentRoot "/opt/lampp/htdocs/{}"\n\
		    ServerName {}\n\
		    ErrorLog "logs/examplevhost.local-error_log"\n\
		    CustomLog "logs/examplevhost.local-access_log" common\n</VirtualHost>'
		vhosts_conf.write(a.format(folder, domain))
		vhosts_conf.close()
		#create folder
		print('Created folder in ' + '/opt/lampp/htdocs/'+folder+'....')
		os.mkdir('/opt/lampp/htdocs/'+folder+'')
	else:
		print("error ! domain exist ")
lampp = Lampp()
#if lampp.stt < 0:
	# check = raw_input('Do you want enable virtual hosts ? (Y/N) :')
	# if check.upper() == 'Y':
	# 	httpd = open('/opt/lampp/etc/httpd.conf', 'a+')
	# 	read_httpd = httpd.read()
	# 	print(read_httpd);
	# 	x = read_httpd.replace("# Virtual hosts\n#Include etc/extra/httpd-vhosts.conf", "# Virtual hosts\nInclude etc/extra/httpd-vhosts.conf")
	# 	print(x)
	# 	httpd.write(x)
	# 	httpd.close()
	# else:
	# 	print('--------------')

stop = 1;
print('----------LAMPP CONTROLLER----------')
print("""
1. LAMPP start                   4. Add domain
2. LAMPP stop				     5. Edit domain
3. LAMPP restart                 6. Remove domain
7: Exit
""")
while stop:

	choice = int(input('Please enter your choice (1-6): '))

	if choice == 1:
		print('-----------\n')
		os.system('/opt/lampp/lampp start')
		print('-----------\n')

	elif choice == 2:
		print('-----------\n')
		os.system('/opt/lampp/lampp stop')
		print('-----------\n')
	elif choice == 3:
		print('-----------\n')
		os.system('/opt/lampp/lampp restart')
		print('-----------\n')

	elif choice == 4:
		domain = raw_input('your domain: ')
		folder = raw_input('your folder: ')
		if (domain != '' and folder != ''):
			print('--------------------')
			lampp.add_domain(domain, folder)
			
			os.system('/opt/lampp/lampp restart')

			print('--------------------')
		else:
			print('domain or folder empty ! ')
	elif choice == 5:
		print('update')
	elif choice == 6:
		print('update')
	else:
		stop = 0
		print('bye!!!')
