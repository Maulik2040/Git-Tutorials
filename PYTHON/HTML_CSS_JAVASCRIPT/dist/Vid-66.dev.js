"use strict";

var http = require("http");

var fs = require("fs");

var fileContent = fs.readFileSync("Vid-61.html");
var server = http.createServer(function (req, res) {
  res.writeHead(200, {
    "content-type": "text/html"
  });
  res.end(fileContent);
});
server.listen(80, "127.0.0.1", function () {
  console.log("Listening on post 80");
});