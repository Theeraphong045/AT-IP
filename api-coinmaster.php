<?php 

class coinmaster{
	const CURL_TIMEOUT = 3600;
	const CONNECT_TIMEOUT = 30;
	private function Curl($method, $url, $header, $data, $cookie){
		$ch = curl_init();
		curl_setopt($ch, CURLOPT_URL, $url);
		curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode(array()));
		curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36');
		curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
		curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($ch, CURLOPT_TIMEOUT, self::CURL_TIMEOUT);
		curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, self::CONNECT_TIMEOUT);
		curl_setopt($ch, CURLOPT_CUSTOMREQUEST, $method);
		curl_setopt($ch, CURLOPT_ENCODING, '');
		curl_setopt($ch, CURLOPT_IPRESOLVE, CURL_IPRESOLVE_V4);
		if ($header) {
			curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
		}
		if ($data) {
			curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
		}
		if ($cookie) {
			curl_setopt($ch, CURLOPT_COOKIESESSION, true);
			curl_setopt($ch, CURLOPT_COOKIEJAR, $cookie);
			curl_setopt($ch, CURLOPT_COOKIEFILE, $cookie);
		}
		return curl_exec($ch);
	}
	private function header(){
		$header = array(
			"Expect: 100-continue",
			"Connection: keep-alive",
			"Host: vik-game.moonactive.net"
		);
		return $header;
	}
	private function headerwhittoken($devicetoken){
		$header = array(
			"Expect: 100-continue",
			"Connection: keep-alive",
			"X-CLIENT-VERSION: 3.5.191",
			"Cookie: cme=global;",
			"Content-Type: application/x-www-form-urlencoded",
			"Authorization: Bearer ".$devicetoken,
			"Host: vik-game.moonactive.net"
		);
		return $header;
	}
	private function gen_uuid() {
		return sprintf( '%04x%04x-%04x-%04x-%04x-%04x%04x%04x',
			mt_rand( 0, 0xffff ), mt_rand( 0, 0xffff ),
			mt_rand( 0, 0xffff ),
			mt_rand( 0, 0x0fff ) | 0x4000,
			mt_rand( 0, 0x3fff ) | 0x8000,
			mt_rand( 0, 0xffff ), mt_rand( 0, 0xffff ), mt_rand( 0, 0xffff )
		);
	}
	private function gettokenfb(){
		$access_tokenfb = [
			'206496203601706|adVW-UPw6deH-XBcjxVTO1VyTf8',
			'1849428255351522|DWEDMaWUoF9SOKHo9R8ge8qOjEU',
			'233815504558902|8UQH_fjNDfcHGFlWwy2TPgAqIfQ',
			'288860622426675|ceo2XK1dzkL6Y6hzEDg2ZpPSdmQ',
			'3480695258683075|MjeH3rPg3EuQsi4T82lfewdHJPk',
			'389886755725006|jTDN4y6l4XkEL14oFI9LS2NqrCY',
			'121735912920877|VSm62PN9dgpsYke7CnKHpJ-FMH4',
			'2736586129939075|IfhJnyNoJDFf0f2URPZGtqBHu7w',
			'998094330596054|8nMOqCZwYFO--0mGxhJqMH0bLzA',
			'132951328314784|teVS2CipaC7HwpRmmW96RNS5GnU',
			'3392411950812116|QmHLVUGvDoHPWPr7e02WXCkU6ZA',
			'1331177197223557|YBbZXItWLFyx3NU-NcW6nOgV-hQ',
			'794198004809022|xEzbD1Hy_e41DEO8MRq8nfAZQuo',
			'2736314633248681|-L8vD2UXzT2KQf04NVnWb4FdWu0',
			'3597511766938510|S1jjWTwk9Te4A8aMHzNhH-AOSEU',
			'286736216066457|qi_NtYW9tTwGB9QLEaVvFuPBMSM',
			'1283307002044222|7WsxepcR6Uba27m9Dl3JJaOZSmY',
			'1306137716406316|YmAiWxi1suQDLoH9ulduzKDDwUE',
			'1775763172602474|ArPvgWGZdGStCR_tRzJqs2LAg8Y',
			'221937902636084|P75XVeqtiyy6ZKuHZaaguBghZ9g',
			'2436093080027590|VEsmlfn2poPNjQPoJQbWVrlyDTw',
			'320554242726253|bq6tbW0u-tLehsCsO4enZXjwSts',
			'185538843182505|QNiAtwdJpFGNlgorQVEB_xD_FUU',
			'362581048177285|ySxPbODq_SuSZ-Ob2FFCW8TrpQo',
			'175331380896035|G6t94SqFKXojODoWEFMJH6HajPU',
			'384257329568998|8TpotjiiPKMQusdZnPMNYx3dJfA',
			'723902724902312|mIXL9WmK92AAd78wOIDoMC604Gc',
			'135857651317163|JJprAzstD0SNTD02IOxfXnVV0NQ',
			'491290418518427|a6EiioJV97NrBP94mk8W1RP-HWE',
			'438634317540418|XJTi6bDzuwUyuW0pPMlrPTHSsA8',
			'1331948590495337|BDovI97qJZ_8Qef1uCblLFBH8u4',
			'198575465056357|2I-FnbuXNK5-g0f-vkPeOtmHNvk',
			'495343691440605|Cy96dhgWxFlaGu601O0OYi4dkPU',
			'295501635060050|7Jl5MFYttufN2uDxQntBmP6ePnU',
			'383628982978359|ceDK5-kCDtGKmrSn_cZFUCfbUsk',
			'706321696989870|udWLL2kB0Hx918V9x1c62dw8nCI',
			'296371054969419|DzYYqvAOQ0mgsxl2mC9kloHUC68',
			'435164837879315|nQ8ZeAsGAzZjI4j4pa7_RYIHtuc',
			'668072677413959|TQZwDiePGC_9ZzaJmrYbQRFlumk',
			'1970446906431216|mGwWEGqbYCYMlu4RSmJTybOOffs',
			'431178774545132|8GQstMJ-rqVjZV9cT0wO90cKLcU',
			'375715253763922|j2RHHR6kM7HZ8tttnX5xBZ6pkfI',
			'378162536578070|8ldGt9-uIuAge4g-qmuZ822xubc',
			'136385811251997|THtBYnu4AeoAOzzj0sy_eUEfVEU',
			'225934875548439|A4k6xhqINZtkkQno7H0BGZbU9pU',
			'417780579223644|XDWgVvLwVaCQWwWL51oF9N4717c',
			'208943484136904|DbxpTHKf_oEa232k6CTljHEuu-Y',
			'3866849800026554|Wv_0M_Ariv3Tpwh3syI63uKIbqM',
			'210624563833345|pQPHJADYEBTKdW2rnUWeIiG646E',
			'703693033897661|A8Ik-XeFHnSMHbQVoK1Mtd61UBc',
			'2499049560400189|sliCWGC_1sv8vehN1Dy3dp5dQjU',
			'411430053224226|8ab3uGfcbiztNfuds5Wm6vvr7E8',
			'752306552310652|fxTGCAzl5qeW6zxb9N2T84zeTtA',
			'415281839514693|bbtFKL8aR6tw6vN2LCEt09cI5Ek',
			'211396020358923|cbeBJVpwpd8UNKwe4yuIAzrrxyw',
			'407738490266678|ZVIs5JgVn_NDXVyUeI_uspyR7RE',
			'384401996173547|35-4qzo9r3O5RNg7nrSkGcrIdoA',
			'378109190089241|JdBdbiyU_8K6Vi65jmWoLe75tyw',
			'2878712859039647|l4CkqACeZ0J0cCbdP5z0mD6pBfY',
			'194804272149039|9XYbbStJqRdfBBsNGNOSHIv4TAo',
			'1376094989394554|0man-5PeFCuM0bZciPkyuD6D168',
			'388894415562061|NfPrZ7FXMva1moKbxRZnRMehJtA',
			'417315755967566|MjlmUr69FXQacXBJGOkP6A1a1yU',
			'1080091782508686|f75AVJDw8w1AcqJg3n2Dyz6SYG0',
			'1022207241581339|1f6hp4TWkmbD0jbeta2tgPhLcdI',
			'386726389266172|GXeO3XL6wvcxu0JoibpmhbJV8Wo',
			'499665987603794|95jP8AWLHjf1DgIJMCvKzJbvpO4',
			'369176411035910|P4OGRc6ecLKzd6wWdsPz_dpyziM',
			'701909480748398|n_bJLZAgeK2CkmWxWv8fsocJOYg',
			'',
			
			
		];
		$bz = 0;
		do {
			//$facebookgen = $this->Curl("GET", "http://127.0.0.1/token/", false, false, false);
			$facebookgen = $this->Curl("GET", "https://graph.facebook.com/206496203601706/accounts/test-users?access_token=".$access_tokenfb[$bz]."&installed=true&permissions=read_stream&method=post", false, false, false);
			$token = json_decode($facebookgen,true);
			$bz++;
			if ($bz > 70) {
				$bz = 0;
			}
			echo "SPIN CHAMP BOONPRASET  >>>> : ".$bz."\n";
		} while (empty($token['access_token']));
		$this->fb['access_token'] = $token['access_token'];
		return $this->fb['access_token'];
	}
	private function Login($deviceID,$devicetoken){
		$data = "Device%5budid%5d=".$deviceID."&API_KEY=viki&API_SECRET=coin&Client%5bversion%5d=3.5_fband&Device%5bchange%5d=20201105_5&fbToken=&seq=0";
		$login = $this->Curl("POST", "https://vik-game.moonactive.net/api/v1/users/login", $this->headerwhittoken($devicetoken), $data, false);
		$info = json_decode($login,true);
		$res = array(
			"deviceID" => $deviceID,
			"info" => array(
				"change_timestamp" => $info['change_timestamp'],
				"profile" => $info['profile'],
				"sessionToken" => $info['sessionToken'],
				"userId" => $info['userId']
			)
		);
		return json_encode($res,JSON_UNESCAPED_SLASHES);
	}
	private function Loginfbgame($deviceID,$devicetoken,$userid,$fbtoken){
		$data = "Device%5budid%5d=".$deviceID."&API_KEY=viki&API_SECRET=coin&User%5bfb_token%5d=".$fbtoken."&p=fb&Client%5bversion%5d=3.5.191_fband&Device%5bchange%5d=20201105_5";
		$startlogin = $this->Curl("POST", "https://vik-game.moonactive.net/api/v1/users/".$userid."/update_fb_data", $this->headerwhittoken($devicetoken), $data, false);
		return $startlogin;
	}
	private function Start(){
		$deviceID = $this->gen_uuid();
		$data = array( 
			'deviceId' => $deviceID 
		);
		$start = $this->Curl("POST", "https://vik-game.moonactive.net/api/v1/authentication/register", $this->header(), $data, false);
		$register = json_decode($start, true);
		$startlogin = $this->Login($deviceID,$register['deviceToken']); //รับค่าทั่งหมด
		$startlogin = json_decode($startlogin,true); //แปลงเป็น array
		$this->deviceID = $startlogin['deviceID'];
		$this->nonfbuserId = $startlogin['info']['userId'];
		$this->sessionToken = $startlogin['info']['sessionToken'];
	}
	private function Start2($link){
		$facetoken = $this->gettokenfb();
		//$facetoken ="EAAxdrIR3FsMBAOgJc7IWMFHGH8zaNh3Oc80Bm9Bk5bKC8d5B2iDQbxC9ZAmdWazWBlQMrT0ZCeRuMP05DnKxxYQdDtGcdwnWYrHWY8QGsGYOZAq68K2TN3naq8cZAIk0PuD6fMaQzH4HTRZBiJ4qsvd03uuhZCX48RUGb3sMHGQP9gTGPRk30AgIPvZClFyZAtiVZCeG20lYd68ckyZBfIaPcT";
		$startloginfb = $this->Loginfbgame($this->deviceID,$this->sessionToken,$this->nonfbuserId,$facetoken);
		$startloginfb = json_decode($startloginfb,true);
		
		//echo $facetoken;
		
		if (empty($startloginfb['userId'])) {
			$this->addspin($link);
			exit();
		}
		$this->userId = $startloginfb['userId'];
		$this->fbUserId = $startloginfb['fbUserId'];
		$this->fbToken = $startloginfb['fbToken'];
	}
	
	
	public function addspin($link){
		$this->Start();
		$this->Start2($link);
		$bossnz = preg_match_all('/~[^}]*?s=m/', $link, $a);
		if ($bossnz == NULL) {
			$bossnz = preg_match_all('/~[^}]*/', $link, $a);
			$edit1 = str_replace('~', '', $a[0]);
			$edit2 = str_replace('', '', $edit1[0]);
			$link = $edit2;
		}else{
			$edit1 = str_replace('~', '', $a[0]);
			$edit2 = str_replace('?s=m', '', $edit1[0]);
			$link = $edit2;
		}
		//หาuseridของคนแชร์ลิ้ง
		$getuseridaddlink = $config = $this->Curl("GET", "https://vik-game.moonactive.net/external/users/~".$link."/invite?s=m", false, false, false);
		$getuseridaddlinkpor = preg_match_all('/&amp;c=[^}]*/', $getuseridaddlink, $pora);
		$getuseridaddlink1 = str_replace('&amp;c=', '', $pora[0]);
		$getuseridaddlink2 = str_replace('', '', $getuseridaddlink1[0]);
		//data post
		$data = "Device%5budid%5d=".$this->deviceID."&API_KEY=viki&API_SECRET=coin&Device%5bchange%5d=20201105_4&fbToken=".$this->fbToken."&locale=th&1604586433725=delete";
		$data2 = "Device%5budid%5d=".$this->deviceID."&API_KEY=viki&API_SECRET=coin&Device%5bchange%5d=20201105_4&fbToken=".$this->fbToken."&locale=th";
		$data3 = "Device%5budid%5d=".$this->deviceID."&API_KEY=viki&API_SECRET=coin&Device%5bchange%5d=20201105_4&fbToken=".$this->fbToken."&locale=th&item=House&state=0&include%5b0%5d=pets";
		$data4 = "Device%5budid%5d=".$this->deviceID."&API_KEY=viki&API_SECRET=coin&Device%5bchange%5d=20201105_4&fbToken=".$this->fbToken."&locale=th&item=House&state=1&include%5b0%5d=pets";
		$data5 = "Device%5budid%5d=".$this->deviceID."&API_KEY=viki&API_SECRET=coin&Device%5bchange%5d=20201105_4&fbToken=".$this->fbToken."&locale=th&item=Farm&state=0&include%5b0%5d=pets";
		$data6 = "Device%5budid%5d=".$this->deviceID."&API_KEY=viki&API_SECRET=coin&Device%5bchange%5d=20201105_4&fbToken=".$this->fbToken."&locale=th&item=Ship&state=0&include%5b0%5d=pets";
		$dataconfig = "Device%5budid%5d=".$this->deviceID."&API_KEY=viki&API_SECRET=coin&Device%5bchange%5d=20201105_5&fbToken=".$this->fbToken."&locale=th&map%5blocale%5d=th";
		$balanceconfig = "Device%5budid%5d=".$this->deviceID."&API_KEY=viki&API_SECRET=coin&Device%5bchange%5d=20201105_5&fbToken=&locale=en&Device%5bos%5d=Android&Client%5bversion%5d=3.5.210&extended=true&config=all&segmented=true&include%5b0%5d=pets&include%5b1%5d=vquestRewards";
		$datafriends = "Device%5budid%5d=".$this->deviceID."&API_KEY=viki&API_SECRET=coin&Device%5bchange%5d=20201105_5&fbToken=".$this->fbToken."&locale=en&non_players=500&p=fb&snfb=true";
		$dataaccept_invitation = "Device%5budid%5d=".$this->deviceID."&API_KEY=viki&API_SECRET=coin&Device%5bchange%5d=20201105_5&fbToken=&locale=en&inviter=".$getuseridaddlink2;
		//เริ่มเล่นเกม
		$accept_invitation = $this->Curl("POST", "https://vik-game.moonactive.net/api/v1/users/".$this->userId."/accept_invitation", $this->headerwhittoken($this->sessionToken), $dataaccept_invitation, false);
		$config = $this->Curl("POST", "https://vik-game.moonactive.net/api/v1/users/".$this->userId."/config", $this->headerwhittoken($this->sessionToken), $dataconfig, false);
		$balance = $this->Curl("POST", "https://vik-game.moonactive.net/api/v1/users/".$this->userId."/balance", $this->headerwhittoken($this->sessionToken), $balanceconfig, false);
		$friends = $this->Curl("POST", "https://vik-game.moonactive.net/api/v1/users/".$this->userId."/friends", $this->headerwhittoken($this->sessionToken), $datafriends, false);
		$upgread = $this->Curl("POST", "https://vik-game.moonactive.net/api/v1/users/".$this->userId."/upgrade", $this->headerwhittoken($this->sessionToken), $data3, false);
		$coun = 1;
		for ($i=0; $i < 18; $i++) { 
			$coun++;
			$dataspin = "Device%5budid%5d=".$this->deviceID."&API_KEY=viki&API_SECRET=coin&Device%5bchange%5d=20201105_4&fbToken=".$this->fbToken."&locale=en&seq=".$coun."&auto_spin=False&bet=1&Client%5bversion%5d=3.5.210_fband";
			$startspin = $this->Curl("POST", "https://vik-game.moonactive.net/api/v1/users/".$this->userId."/spin", $this->headerwhittoken($this->sessionToken), $dataspin, false);
		}
		$start = $this->Curl("POST", "https://vik-game.moonactive.net/api/v1/users/".$this->userId."/read_sys_messages", $this->headerwhittoken($this->sessionToken), $data, false);
		$upgread2 = $this->Curl("POST", "https://vik-game.moonactive.net/api/v1/users/".$this->userId."/upgrade", $this->headerwhittoken($this->sessionToken), $data4, false);
		$upgread3 = $this->Curl("POST", "https://vik-game.moonactive.net/api/v1/users/".$this->userId."/upgrade", $this->headerwhittoken($this->sessionToken), $data5, false);
		$upgread4 = $this->Curl("POST", "https://vik-game.moonactive.net/api/v1/users/".$this->userId."/upgrade", $this->headerwhittoken($this->sessionToken), $data6, false);
		$dataconfigloop = "Device%5budid%5d=".$this->deviceID."&API_KEY=viki&API_SECRET=coin&Device%5bchange%5d=20201105_5&fbToken=".$this->fbToken."&locale=th&map%5bMaxXP%5d=4";
		$configloop = $this->Curl("POST", "https://vik-game.moonactive.net/api/v1/users/".$this->userId."/config", $this->headerwhittoken($this->sessionToken), $dataconfigloop, false);
		return $accept_invitation;
	}
}
?>