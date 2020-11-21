// function greet() {
//     console.log('Good Morning');
// }
// Arrow Function
let greet = () => {
    console.log("Good Moring");
}

let sum = (a, b, c) => a + b + c;
let half = a => a / 2;

greet();
a = sum(500, 500, 501)
console.log(a);

setTimeout(() => {
    console.log("We are Inside SetTimeOut");

}, 3000);