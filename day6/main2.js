(function () {

    'use strict';

    var instructions = "";

    $.ajax({
    	url:'http://localhost:8000/input.txt',
    	method:'GET'
    }).done(function( response ) {
    	instructions = response;
    	solvePuzzle();
  	});

	var a = [];
    var i, j;
    var dim = 1000;

    for (i = 0; i < dim; i += 1) {
    	a[i] = [];
        for (j = 0; j < dim; j += 1) {
            a[i][j] = 0;
        }
    }	

    function changelights(action, c) {
		
    	for (var i = c.x1; i <= c.x2; i++) {
    		for (var j = c.y1; j <= c.y2; j++) {
    			a[i][j] = action(a[i][j]);
    		}
    	};

    }

    function calculateLights(){
    	var total = 0
    	for (i = 0; i < dim; i += 1) {    
        	for (j = 0; j < dim; j += 1) {            	
    			total += a[i][j];    			
        	}
    	}	
    	return total;
    }

	function getCoordinates(input){

		var myRe = new RegExp("[0-9]+,[0-9]+", "g");
			var arr;
			var results= [];

			while ((arr = myRe.exec(input)) !== null) {
			    results.push(arr[0]);
			}

			var pos1arr = results[0].split(',');
			var pos2arr = results[1].split(',');

		return {
			x1: parseInt(pos1arr[0],10),
			y1: parseInt(pos1arr[1],10),
			x2: parseInt(pos2arr[0],10),
			y2: parseInt(pos2arr[1],10)
		}
	}
	function solvePuzzle(){

		//drawGrid();
		var lines = instructions.split("\n");

		for (var i = 0; i < lines.length - 1; i++) {
			var line = lines[i];			
			var coords = getCoordinates(line);

			if(line.indexOf('turn on') >= 0){		
				console.log("on");
				changelights(function(a){ return (a + 1); },coords);
			}

			if(line.indexOf('toggle') >= 0){
				console.log("toggle");
				changelights(function(a){ return (a + 2); },coords);
			}

			if(line.indexOf('turn off') >= 0){
				console.log("off");
				changelights(function(a){ return (a === 0) ? 0 : (a - 1); },coords);
			}	
		};		

		console.log(calculateLights());

		
	}
    
}());