<?php

function getStringCount($string){

    $string = trim($string);

    $codeCount = strlen($string);

    $string = str_replace('\\\\','1',$string);
    $string = preg_replace('/\\\\x[a-z0-9][a-z0-9]/', "1", $string);
    $string = str_replace('\"','1',$string);

    $strlen = strlen( $string ) -2;

    return array('cC' => $codeCount,'sC' => $strlen);

}

function solve($fileName){

    $handle = fopen($fileName, "r");

    if ($handle) {
        $totalC = 0;
        $totalS = 0;
        while (($line = fgets($handle)) !== false) {
            $arr = getStringCount($line);

            $totalC += $arr['cC'];
            $totalS += $arr['sC'];
        }

        fclose($handle);

        echo $totalC - $totalS;
    }

}
solve('input.txt');
die;
