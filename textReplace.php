<?php
$fcontent = file_get_contents($argv[1],filesize($argv[1]));
/*
if(preg_match_all("/【.*】.*\d/", $fcontent, $strResult)){
    var_dump($strResult);
}
else{
        echo strpos($fcontent, "解析");
}
 */
$arrContent = explode("\r\n", $fcontent);
foreach($arrContent as $p){
    if(preg_match("/^\d/", $p)){
            print($p);
            echo "\t";
    }
}
?>
