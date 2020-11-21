"use strict";

var fs = require('fs');

fs.readFile("dele.txt", "utf-8", function (err, data) {
  console.log(data);
});
console.log("This is a message");