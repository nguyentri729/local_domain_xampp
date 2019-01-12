f_hosts = open("C:\Windows\System32\drivers\etc\hosts", "a+")
f_xampp = open(r'''C:\xampp\apache\conf\extra\httpd-vhosts.conf''', "a+")
def check_domain(domain):
	#check_host file
    vt_host = f_hosts.read().find('127.0.0.1 '+domain+'\n')
    vt_xampp = f_xampp.read().find('ServerName '+domain+'\n')
    print(f_xampp.read())
    if (vt_host<0 and vt_xampp<0):
    	return True
    else:
    	return False
def add_domain():
    print('---------THEM DOMAIN AO VAO XAMPP----------')
    domain = input('Domain: ')
    folder  = input('Thu muc: ')
    #kiem tra domain
    if check_domain(domain):
    	print('Da them domain thanh cong !')
    	f_hosts.write('127.0.0.1 '+domain+'\n')
    	f_xampp.write('<VirtualHost *:80>\n    DocumentRoot "C:/xampp/htdocs/'+folder+'"\n    ServerName '+domain+'\n</VirtualHost>\n')
   		
   		
    else:
    	print('Domain da ton tai!')
    	add_domain()	    
def menu():  
	# print('''
	# 1: Them domain moi
	# 2: Xoa domain      
	# ''')

	# chose = input('Nhap lua chon cua ban: ')
	# if chose == '1':
	# 	add_domain()
	# else:
	# 	domain = input('Domain: ')
	add_domain()

       
menu()
