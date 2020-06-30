<?php

//Read from standard input
$fpf = file("php://stdin");

foreach($fpf as $sentence){
	
	$count = preg_match_all('/(.)\1{3,}/', $sentence, $matches);
	
	$output_sentence = $sentence;
	
	if(count($matches[0]) > 0){
		for($i = 0; $i < count($matches[0]); $i++){
			$output_sentence = str_replace($matches[0][$i], $matches[1][$i].$matches[1][$i].$matches[1][$i], $output_sentence);
		}
	}
	
	echo $output_sentence;
}
