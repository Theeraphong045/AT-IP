<?php

//API
define("SSH_IP", "188.166.213.166");
define("SSH_PORT", "22");
define("SSH_USER", "root");
define("SSH_PASSWORD", "onlyyou0Flook");

set_time_limit(0);

if(empty($_GET['host']) || empty($_GET['port']) || empty($_GET['time']) || empty($_GET['method']) || empty($_GET['key'])) die("APIDDOS : ONLINE");

$host = escapeshellcmd($_GET['host']);
$port = escapeshellcmd($_GET['port']);
$time = escapeshellcmd($_GET['time']);
$method = escapeshellcmd($_GET['method']);
$key = escapeshellcmd($_GET['key']);
if($_GET['key'] === "3480a3a2e7c5b47bf9e6d2229715875b"){
	if(!function_exists("ssh2_connect")) die("Please install the SSH2 Dependency on the Linux Server First.");

if(!($con = ssh2_connect(SSH_IP, SSH_PORT))) die("Could not connect to SSH...");
else
{
	if(!ssh2_auth_password($con, SSH_USER, SSH_PASSWORD)) die("Invalid Credentials...\n");
    else
    {
		if($method == "CMSPIN" || $method == "CM-SPIN")
    	{
			$cm = $port/2;
			
	        if(!($stream = ssh2_exec($con, "screen -dm php run.php ".$host." ".$port.""))&($stream = ssh2_exec($con, "screen -dm php run.php ".$host." ".$cm."")) ) die("Command couldn't be executed, something went wrong...\n");
	        else
	        {
	            echo "" . stream_get_contents($stream);
	            echo "Coin Master SPIN : Success ! $cm ครั้ง" ;
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
		
	    else die("Please Choose Method!");
    }

}
}else{
	die("Key Error");
}
?>