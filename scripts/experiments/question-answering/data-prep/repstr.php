<?php

//Read from standard input
$fpf = file("php://stdin");

foreach($fpf as $sentence){
	#atstarpes
	$count = preg_match_all('/ (\S+) \1 \1 /', $sentence, $matches);
	while($count){
		for($i = 0; $i < count($matches[0]); $i++){
			$sentence = str_replace($matches[0][$i], " ".$matches[1][$i]." ".$matches[1][$i]." ", $sentence);
		}
		$count = preg_match_all('/ (\S+) \1 \1 /', $sentence, $matches);
	}
	#atstarpes-komati
	$count = preg_match_all('/ (\S+) , \1 , \1 /', $sentence, $matches);
	while($count){
		for($i = 0; $i < count($matches[0]); $i++){
			$sentence = str_replace($matches[0][$i], " ".$matches[1][$i]." , ".$matches[1][$i]." ", $sentence);
		}
		$count = preg_match_all(' /(\S+) , \1 , \1 /', $sentence, $matches);
	}
	
	echo $sentence;
}
