const fs = require('fs');
const pdf = require('pdf-parse');

let dataBuffer = fs.readFileSync('C:\\Users\\Hon3y Chauhan\\Downloads\\Documents\\20260306143620930.pdf');

pdf(dataBuffer).then(function(data) {
    console.log("--- PDF CONTENT START ---");
    console.log(data.text);
    console.log("--- PDF CONTENT END ---");
}).catch(function(error){
    console.error("Error reading PDF:", error);
});
