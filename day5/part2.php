<?php 

error_reporting(-1);
ini_set('display_errors', 'On');

$niceStrings = 0;

$handle = fopen("input.txt", "r");

function badWordCheck($mystr){
	$badString = array('ab','cd','pq','xy');

	foreach ($badString as $key => $badword) {
		if(strpos($mystr, $badword) !== false){			
			return false;
		}
	}
	return true;
}

function doesWordContainPair($word){

    $strlen = strlen($word);

    for($i = 0; $i < $strlen - 1; $i++) {

        $phrase = $word[$i].$word[$i + 1];
        
        if($i > 1){
            $before = ($i - 1);
            if(strpos(substr($word, 0,$before), $phrase) !== false){         
                return true;
            }
        }

        if($i < $strlen - 2){
            $after = $i + 2;
            if(strpos(substr($word, $after, $strlen), $phrase) !== false){         
                return true;
            }
        }    
    }

    return false;

}

function isWordNice($word){
	
    $hasDouble = false;
    for ($i = 0;$i < strlen($word) - 2;$i++){
    	if($word[$i] == $word[$i + 2]){
    		$hasDouble = true;
    	}
    }
    
    if((doesWordContainPair($word) == true) && $hasDouble){
    	return true;	
    } else {
    	return false;
    }

}

if ($handle) {
    while (($line = fgets($handle)) !== false) {        
        if(isWordNice($line) == true){
        	$niceStrings++;
        }
    }

	// $string = 'qjhvhtzxzqqjkmpb';
 //    echo $string." ".(int)isWordNice($string)."<br/>";

 //    $string = 'xxyxx';
 //    echo $string." ".(int)isWordNice($string)."<br/>";

 //    $string = 'uurcxstgmygtbstg';
 //    echo $string." ".(int)isWordNice($string)."<br/>";

 //    $string = 'ieodomkazucvgmuy';
 //    echo $string." ".(int)isWordNice($string)."<br/>";

    fclose($handle);
} else {
    // error opening the file.
}

echo $niceStrings;
