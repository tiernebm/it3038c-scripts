var path = require("path")

var hello = "hello from js variable"
console.log(`printing variable hello: ${hello}`);
console.log("directory name:" + __dirname);
console.log("directory and filename: " + __filename);

console.log(`hello from file ${path.basename(__filename)}`);

console.log(`Process args: ${process.argv}`);