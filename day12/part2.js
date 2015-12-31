(function () {

    // Warms my legs up while on cold train
    //var r = function w(){
    //    if(true){
    //        console.log("hang on in there");
    //        w();
    //    }
    //}();

    'use strict';

    Object.hasOwnValue = function (val) {
        for (var prop in this) {
            if (this.hasOwnProperty(prop) && this[prop] === val) {
                return true;
            }
        }
        return false;
    };

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
                            if (!Object.hasOwnValue.call(v, "red")) {
                                //operating on pure object type
                                t += addNumbers(v);
                            }
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