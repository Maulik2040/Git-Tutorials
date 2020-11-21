"use strict";

// console.log("Hello World");
var http = require('http');

var hostname = '127.0.0.1';
var port = 3000;
var server = http.createServer(function (req, res) {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html'); // res.end('Hello World This is Maulik Mishra');

  res.end("<!DOCTYPE html>\n    <html lang=\"en\">\n    <head>\n        <meta charset=\"UTF-8\">\n        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n        <meta http-equiv=\"X-UA-Compatible\" content=\"ie=edge\">\n        <title>Pseudo selectors & more designing</title>\n        <style>\n            .container{\n                border: 2px solid red;\n                background-color: rgb(223, 245, 201);\n                padding: 34px;\n                margin: 34px auto;\n                width: 666px;\n            }\n            a{\n                text-decoration: none;\n                color: black;\n            }\n            a:hover{\n                color: rgb(5, 0, 0);\n                background-color: rgb(221, 166, 38);\n            }\n            a:visited{\n                background-color: yellow;\n            }\n            a:active{\n                background-color:darkblue;\n            }\n            .btn{\n                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;\n                font-weight: bold;\n                background-color: crimson;\n                padding:6px;\n                border: none;\n                cursor:pointer;\n                font-size: 13px;\n                border-radius: 4px;\n            }\n            .btn:hover{\n                color:darkgoldenrod;\n                background-color:rgb(223, 245, 201);\n                border: 2px solid black;\n            }\n        </style>\n    </head>\n    <body>\n        <div class=\"container\" id=\"cont1\">\n            <h3>This is my heading</h3>\n            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Obcaecati, reprehenderit. Quam culpa eius aliquam id cumque saepe, provident odio sed eos quia nihil modi error voluptate vero autem quibusdam aperiam exercitationem! Quam, consequuntur velit.</p>\n            <a href=\"https://yahoo.com\" class=\"btn\">Read more</a>\n            <button class=\"btn\">Contact us</button>\n        </div>\n    </body>\n    </html>");
});
server.listen(port, hostname, function () {
  console.log("Server running at http://".concat(hostname, ":").concat(port, "/"));
});