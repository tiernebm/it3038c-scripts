if (process.argv.length <= 2) {
    console.log("Usage: node" + __filename + " IPADDR");
    process.exit(-1);
}
var ip = process.argv[2]
console.log(`Checking IP: ${ip}`);