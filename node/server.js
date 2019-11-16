var http = require ("http");
var fs = require("fs");
var os = require("os");
var ip = require("ip");

function format(seconds){
    function pad(s){
      return (s < 10 ? '0' : '') + s;
    }
    var hours = Math.floor(seconds / (60*60));
    var minutes = Math.floor(seconds % (60*60) / 60);
    var seconds = Math.floor(seconds % 60);
  
    return pad(hours) + ':' + pad(minutes) + ':' + pad(seconds);
  }
  

http.createServer(function(req, res){
    if (req.url === "/") {
   fs.readFile("./public/index.html", "UTF-8", function(err,body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if (req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        var uptime = process.uptime();
        myServerUptime = format(uptime);
        myTotalMemory = os.totalmem;
        myFreeMemory = os.freemem;
        myCPUCount = os.cpus().length;
        
        html = `
        <!DOCTYPE HTML>
        <HTML>
            <HEAD>
                <title> Node JS SysInfo </title>
            </head>
            <body>
                <p> Hostname: ${myHostName} </p>
                <p> IP: ${ip.address()} </p>
                <p> Server Uptime: ${myServerUptime} </p>
                <p> To tal Mem: ${myTotalMemory} </p>
                <p> Free Mem: ${myFreeMemory} </p>
                <p> Number of CPUs: ${myCPUCount} </p>
            </body>
        </html>
         `
         res.writeHead(200, {"Content-Type": "text/html"});
         res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end("404 file not found")
    }
}).listen(3001)



console.log("Server listening on port 3001");