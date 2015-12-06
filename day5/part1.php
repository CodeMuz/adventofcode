<?php 

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

function isWordNice($word){

	$vowels = array('a','e','i','o','u');

	$vowelCount = 0;
    $prev = "";
    $hasDouble = false;
    for ($i = 0;$i < strlen($word);$i++){
    	if(in_array($word[$i], $vowels)){
    		$vowelCount++;
    	}
    	if(($prev) && ($word[$i] == $prev)){
    		$hasDouble = true;
    	}

    	$prev = $word[$i];
    }        

    if(($vowelCount >= 3) && (badWordCheck($word) == true) && ($hasDouble == true)){        	
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
    fclose($handle);
} else {
    // error opening the file.
}

echo $niceStrings;
