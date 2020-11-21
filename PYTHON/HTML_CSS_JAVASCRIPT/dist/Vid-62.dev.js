"use strict";

var jsonObj = {
  name: "Maulik",
  Channel: "Maulik's Coding World",
  food: "Bhindi"
};
console.log(jsonObj);
var myjsonstr = JSON.stringify(jsonObj);
console.log(myjsonstr);
myjsonstr = myjsonstr.replace("Maulik", "Harry");
console.log(myjsonstr);
var newjsonobj = JSON.parse(myjsonstr);
console.log(newjsonobj);