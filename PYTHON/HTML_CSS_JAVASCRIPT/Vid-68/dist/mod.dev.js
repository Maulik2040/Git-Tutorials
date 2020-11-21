"use strict";

console.log("This is module");

function average(arr) {
  var sum = 0;
  arr.forEach(function (element) {
    sum += element;
  });
  return sum / arr.length;
} // module.exports = {
//     avg: average,
//     name: "Harry",
//     repo: "GitHub"
// }


module.exports.name = "Harry";