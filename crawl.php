<?php
require_once 'vendor/autoload.php';
use Symfony\Component\Finder\Finder;
use Symfony\Component\DomCrawler\Crawler;

$finder = new Finder();
$finder->in(__DIR__);


main();
function main(){
	$html = curl_get_https('https://www.zhiliti.com.cn/html/jizhuanwan/');
	$crawler = new Crawler($html);
	$article = $crawler->filterXPath('//ul/li');
	$titles = $article->filterXPath('//h2/a')->extract(array('_text'));
	$answers = $article->filterXPath('//span')->extract(array('onclick'));
	$result = array();
	foreach($titles as $key=>$value){
		$line = $titles[$key].$answers[$key];
	    	array_push($result, $line);	
	}
	var_dump($result);
}

function curl_get_https($url)

    {
        $curl = curl_init();

        curl_setopt($curl, CURLOPT_URL, $url);

        curl_setopt($curl, CURLOPT_HEADER, 0);

        curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);

        curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);  // 跳过检查

        curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);  // 跳过检查

        $tmpInfo = curl_exec($curl);

        curl_close($curl);

        return $tmpInfo;   //返回json对象

    }
?>
