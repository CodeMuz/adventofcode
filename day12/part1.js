var t = 0;

var text = document.getElementById("1").innerHTML;

var numberPattern = /-?\d+/g;

var numbers = text.match( numberPattern );

for(var i = 0;i < numbers.length;i++){t += parseInt(numbers[i],10);}

console.log(t);
