<?php
/**
 * Created by PhpStorm.
 * User: murray
 * Date: 10/12/15
 * Time: 01:25
 */

function solve($fileName){

    $handle = fopen($fileName, "r");

    if ($handle) {
        $totalC = 0;
        while (($line = fgets($handle)) !== false) {
            $totalC += 2 + (substr_count($line, '"')) + (substr_count($line, '\\'));
        }
        fclose($handle);
        echo $totalC;
    }
}
solve('input.txt');
die;