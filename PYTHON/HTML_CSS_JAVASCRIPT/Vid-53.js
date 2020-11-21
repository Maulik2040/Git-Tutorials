console.log("This is tutorial 53");

function greet(name, greetText = "Greetings From JavaScript") {
    let name1 = "Name1";
    console.log(greetText + " " + name);
    console.log(name + " is a good boy");
}

function sum(a, b, c) {
    let d = a + b + c;
    return d;
    // This line will never execute(Unreachable code)

}
let name = "Harry";
let name1 = "rohit";
let name2 = "rohan";
let name3 = "maulik";
let greetText = "Good Morning";
greet(name, greetText);
greet(name1, greetText);
greet(name2, greetText);
let returnVal = sum(1, 2, 3);
console.log(returnVal);
// console.log(name + " is a good boy")
// console.log(name1 + " is a good boy")
// console.log(name2 + " is a good boy")
// console.log(name3 + " is a good boy")