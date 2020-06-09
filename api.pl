#!/usr/bin/perl

print "Set update Install SSH2 Linux By Ra\n";
print "Would you like to install the required packages? [Y/n]\n";
chomp($req=<STDIN>);
if(lc ($req) eq "y" || $req eq ""){
	print "Installing required packages...\n";
	sleep(2);
	system("yum -y update");
	system("yum -y install gcc make gcc-c++ screen dstat iptraf");
                system("yum -y install libstdc++.so.6");
                system("yum -y install libssl.so.6");
                system("yum -y install ld-linux.so.2");
                system("yum -y install nano");
	system("yum -y install httpd mod_ssl");
	system("yum -y install php-mysql php-devel php-gd php-pecl-memcache php-pspell php-snmp php-xmlrpc php-xml");
                system("sudo /usr/sbin/apachectl restart");
                system("sudo /usr/sbin/httpd restart");
	system("sudo /sbin/chkconfig httpd on");
	print "\nInstalling required packages completed!\n";
}

print "Would you like to install SSH2? [Y/n]\n";
chomp($ssh=<STDIN>);
if(lc ($ssh) eq "y" || $ssh eq ""){
	print "Installing SSH2...\n";
	sleep(2);
	system("yum -y install gcc php-devel php-pear libssh2 libssh2-devel");
	system("pecl install -f ssh2");
	system("touch /etc/php.d/ssh2.ini");
	system("echo extension=ssh2.so > /etc/php.d/ssh2.ini");
	system("setsebool -P httpd_can_network_connect 1");
	system("/etc/init.d/httpd restart");
	print "\nChecking...\n";
	system("php -m | grep ssh2");
	print "If you see \"ssh2\" then it has been successfully installed!\n";
}

