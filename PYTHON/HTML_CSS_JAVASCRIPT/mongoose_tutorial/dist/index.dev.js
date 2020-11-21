"use strict";

// getting-started.js
var mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/maulikKart', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:')); // db.once('open', function() {
//     // we're connected!
//     console.log("We are connected bro/sis..")
// });

var kittySchema = new mongoose.Schema({
  name: String
}); // NOTE: methods must be added to the schema before compiling it with mongoose.model()

kittySchema.methods.speak = function () {
  var greeting = "My name is " + this.name;
  console.log(greeting);
};

var Kitten = mongoose.model('Kitten', kittySchema);
var silence = new Kitten({
  name: 'Silence'
}); // console.log(silence.name); // 'Silence'
// silence.speak();

silence.save({
  name: "Silence"
}, function (err, fluffy) {
  if (err) return console.error(err);
  silence.speak();
});