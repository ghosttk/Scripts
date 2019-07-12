<?php
$lines = file('2835.txt');
$handle = null;
foreach ($lines as $line_num => $line) {
    if($rtn=strpos($line, '分节阅读') ){
    	var_dump($rtn);
	if($handle){
	    fclose($handle);
	    $handle=fopen(trim($line), 'a');
	}
    }
    
    if($handle){
	var_dump($handle);
	fwrite($handle, $line);
    }
}
?>
