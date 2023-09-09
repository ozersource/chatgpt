<?php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept');
header('Content-Type:application/json; charset=utf-8');
//主要为跨域CORS配置的两大基本信息,Origin和headers

$file = fopen("client/css/id.json", "r") or exit("Unable to open file!");
while (! feof($file)){
    $jsontext .=  fgets($file);
    
}
fclose($file);
$obj=json_decode($jsontext,true);
$updateser=json_decode(file_get_contents("php://input"),true);
$uname=$updateser['uname'];
$pwd=$updateser['pwd'];
$user=$obj['user'];
$json['code']=300;
$json['message']=$uname . "登录失败！" ;
for ($i=0; $i <count($user) ; $i++) { 
    if($user[$i]['uname']==$uname && $user[$i]['pwd']==$pwd){
        $json['code']=200;
        $json['message']=$user[$i]['uname']  . "登录成功！" ;
        break;
    }
}
print json_encode($json,JJSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT );

?>
