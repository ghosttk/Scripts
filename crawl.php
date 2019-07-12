<?php
require_once 'vendor/autoload.php';

use Symfony\Component\Finder\Finder;

$finder = new Finder();
$finder->in(__DIR__);

use Symfony\Component\DomCrawler\Crawler;

main();
function main(){
	$html = curl_get_https('https://www.zhiliti.com.cn/html/jizhuanwan/');
	$crawler = new Crawler($html);
	$article = $crawler->filterXPath('//ul/li');
	$title = $article->filterXPath('//h2/a');
	$answer = $article->filterXPath('//span');
	var_dump($answer);
	foreach ($answer as $crw) {
	    var_dump($crw);
	}
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
