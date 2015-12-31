/* Pure ReGeX Solution:
var t = 0;
var text = document.getElementById("1").innerHTML;
var numberPattern = /-?\d+/g;
var numbers = text.match( numberPattern );
for(var i = 0;i < numbers.length;i++){t += parseInt(numbers[i],10);}
*/

//recursive Depth First search soln O(n^2)
(function () {

        'use strict';

        var instructions = "";

        $.ajax({
            url: 'http://localhost:8000/input.txt',
            method: 'GET'
        }).done(function (response) {
            instructions = response;
            solvePuzzle();
        });

        var total = 0;

        function addNumbers(group) {
            var t = 0;

            for (var key in group) {

                if (group.hasOwnProperty(key)) {
                    var v = group[key];

                    if (!isNaN(v)) {
                        t += parseInt(v, 10);
                    } else {
                        if (!(typeof v === "string")) {

                            if (v.length) {
                                //operating on array object type
                                t += addNumbers(v);
                            } else {
                                //operating on pure object type
                                t += addNumbers(v);
                            }

                        }

                    }
                }
            }

            return t;
        }


        function solvePuzzle() {

            var inst = JSON.parse(instructions);

            total = addNumbers(inst);

            console.log(total);

        }

    }());
