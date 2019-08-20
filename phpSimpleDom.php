<?php
require 'https_curl.php';
function main(){
    $result = curl_get_https('https://www.cnblogs.com/wlphp/p/8600945.html');
    $xml = new SimpleXMLElement($result);
    $div = $xml->xpath('//div');
    print_r($div);
}

main();
?>
