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

    var canvas = document.getElementById("myCanvas");
var canvasWidth = canvas.width;
var canvasHeight = canvas.height;
var ctx = canvas.getContext("2d");
var canvasData = ctx.getImageData(0, 0, canvasWidth, canvasHeight);

// That's how you define the value of a pixel //
function drawPixel (x, y, r, g, b, a) {
    var index = (x + y * canvasWidth) * 4;

    canvasData.data[index + 0] = r;
    canvasData.data[index + 1] = g;
    canvasData.data[index + 2] = b;
    canvasData.data[index + 3] = a;
}

	// That's how you update the canvas, so that your //
	// modification are taken in consideration //
	function updateCanvas() {
	    ctx.putImageData(canvasData, 0, 0);
	}


	function drawGrid(){

		for (i = 0; i < dim; i += 1) {
        	for (j = 0; j < dim; j += 1) {    
        		if(a[i][j] == 1){
        			drawPixel(1, 1, 0, 255, 0, 255);
        		} else {
        			drawPixel(1, 1, 255, 0, 0, 255);
        		}
				
        	}
    	}
    	ctx.putImageData(canvasData, 0, 0);

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
            	if(a[i][j] === 1){
    				total += 1;
    			}
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
				changelights(function(){ return 1; },coords);
			}

			if(line.indexOf('toggle') >= 0){
				console.log("toggle");
				changelights(function(a){ return (a === 0) ? 1 : 0; },coords);
			}

			if(line.indexOf('turn off') >= 0){
				console.log("off");
				changelights(function(){ return 0; },coords);
			}	
		};		

		console.log(calculateLights());

		
	}
    
}());