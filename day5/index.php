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

    // echo $vowelCount."<br/>";
    // echo (int)$hasDouble."<br/>";
    // echo (int)badWordCheck($word)."<br/>";        

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

	$string = 'ugknbfddgicrmopn';
    echo $string." ".(int)isWordNice($string)."<br/>";

    $string = 'aaa';
    echo $string." ".(int)isWordNice($string)."<br/>";

    $string = 'jchzalrnumimnmhp';
    echo $string." ".(int)isWordNice($string)."<br/>";

    $string = 'haegwjzuvuyypxyu';
    echo $string." ".(int)isWordNice($string)."<br/>";

    $string = 'dvszwmarrgswjxmb';
    echo $string." ".(int)isWordNice($string)."<br/>";

    fclose($handle);
} else {
    // error opening the file.
}

echo $niceStrings;
