console.log('This is tutorial 58');
// setTimeout --> Allows us to run the function once after the interval of time
// clearTimeout --> Allows us to run the function repetedly after the interval of time

function greet(name, byeText) {
    console.log("Hello , Good Morning " + name + " " + byeText);
}

// timeOut = setTimeout(greet, 5000, "Maulik", "Take Care");
// console.log(timeOut);

// clearTimeout(timeOut)
// IntervalId = setInterval(greet, 3000, "Maulik", "Good Night")
// clearInterval(IntervalId)

function displayTime() {
    time = new Date();
    console.log(time);
    document.getElementById('time').innerHTML = time;
}