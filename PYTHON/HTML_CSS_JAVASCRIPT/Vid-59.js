console.log('This is date and time tutorial');
let now = new Date();
console.log(now);

let dt1 = new Date(1000);
console.log(dt1);

// let newDate = new Date("2020-09-30");
// console.log(newDate)

// let newDate = new Date(year, month, date, hours, minutes, seconds, milliseconds);
let newDate = new Date(2020, 1, 10, 5, 40, 59, 10000);
console.log(newDate);

let yr = newDate.getFullYear();
console.log("The year is ", yr);

let dt = newDate.getDate();
console.log("The date is ", dt);

let mo = newDate.getMonth();
console.log("The month is ", mo);

let ho = newDate.getHours();
console.log("The hour is ", ho);

let da = newDate.getDay();
console.log("The day is ", da);

newDate.setDate(32);
console.log(newDate);

newDate.setMinutes(29);
console.log(newDate);

setInterval(updateTime, 1000);

function updateTime() {
    time.InnerHTMl = new Date()
}