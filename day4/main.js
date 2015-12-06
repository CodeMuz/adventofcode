var hash = "";
var key = 'bgvyzdsv';
var i = 0;
var trailCode = "000000";

while(1){
	hash = md5(key + i);
	if(hash.substring(0, trailCode.length) == trailCode){
		break;
	} else {
		i++;
	}	
}

console.log(i);