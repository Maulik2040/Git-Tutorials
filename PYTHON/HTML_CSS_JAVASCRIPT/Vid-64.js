const fs = require("fs");

let text = fs.readFileSync("dele.txt", "utf-8");
text = text.replace("My", "Your");

console.log(text);
console.log("Creating a new file");

fs.writeFileSync("Maulik.txt", text);