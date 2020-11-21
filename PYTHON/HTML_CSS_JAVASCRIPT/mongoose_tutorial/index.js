// getting-started.js
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/maulikKart', { useNewUrlParser: true, useUnifiedTopology: true });

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));

// db.once('open', function() {
//     // we're connected!
//     console.log("We are connected bro/sis..")
// });

const kittySchema = new mongoose.Schema({
    name: String
});

// NOTE: methods must be added to the schema before compiling it with mongoose.model()
kittySchema.methods.speak = function() {
    const greeting = "My name is " + this.name
    console.log(greeting);
}

const Kitten = mongoose.model('Kitten', kittySchema);

const silence = new Kitten({ name: 'Silence' });
// console.log(silence.name); // 'Silence'
// silence.speak();

silence.save({ name: "Silence" }, function(err, fluffy) {
    if (err) return console.error(err);
    silence.speak();
});