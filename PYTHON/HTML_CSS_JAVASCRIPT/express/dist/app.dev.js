"use strict";

var express = require("express");

var path = require("path");

var fs = require("fs");

var app = express();
var port = 80; // EXPRESS SPECIFIC STUFF

app.use('/static', express["static"]('static')); // For serving static files

app.use(express.urlencoded()); // PUG SPECIFIC STUFF

app.set('view engine', 'pug'); // Set the template engine as pug

app.set('views', path.join(__dirname, 'views')); // Set the views directory
// ENDPOINTS

app.get('/', function (req, res) {
  var con = "This is the best content on the internet so far so use it wisely";
  var params = {
    'title': 'PubG is the best game',
    "content": con
  };
  res.status(200).render('index.pug', params);
});
app.post('/', function (req, res) {
  name = req.body.name;
  age = req.body.age;
  gender = req.body.gender;
  address = req.body.address;
  more = req.body.more;
  var outputtowrite = "The name of the client is ".concat(name, ", ").concat(age, " years old, ").concat(gender, ", residing atr ").concat(address, ". More about him/her ").concat(more);
  fs.writeFileSync("output.txt", outputtowrite);
  var params = {
    "message": "Your form has been submitted successfully"
  };
  res.status(200).render("index.pug", params);
}); // START THE SERVER

app.listen(port, function () {
  console.log("The application started successfully on port ".concat(port));
});