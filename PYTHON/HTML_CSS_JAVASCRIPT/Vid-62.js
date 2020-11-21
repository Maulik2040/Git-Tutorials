let jsonObj = {
    name: "Maulik",
    Channel: "Maulik's Coding World",
    food: "Bhindi"
}
console.log(jsonObj);
let myjsonstr = JSON.stringify(jsonObj);
console.log(myjsonstr);

myjsonstr = myjsonstr.replace("Maulik", "Harry");
console.log(myjsonstr);

let newjsonobj = JSON.parse(myjsonstr);
console.log(newjsonobj);