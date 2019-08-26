var http = require ("http");
var fs = require("fs");
var os = require("os");
var ip = require("ip");
http.createServer(function(req, res){

    if (req.url === "/") {

        fs.readFile("./public/index.html", "UTF-8", function(err, body){

            res.writeHead(200, {"Content-Type": "text/html"});

            res.end(body);

        });

    }

    else if (req.url.match("/sysinfo")) {
            myHostName=os.hostname();
            myServerUptime = secondsToDhms(os.uptime());
            myTotalMemory = ((os.totalmem())/1000000) +"MB";
            myFreeMemory =  ((os.freemem())/1000000) +"MB";
            myCPUCount = parseCPU( os.cpus());            



            html=`
            <!DOCTYPE HTML>
            <HTML>
                <HEAD>
                    <title> NodeJS SysInfo </title>
                </head>
                <body>
                    <p> Hostname: ${myHostName} </p>
                    <p> IP: ${ip.address()} </p>
                    <p> Server Uptime: ${myServerUptime}</p>
                    <p> Total Memory: ${myTotalMemory} </p>
                    <p> Free Memory: ${myFreeMemory}</p>
                    <p> Number of CPUs: ${myCPUCount}</p>
                </body>
            </html>

            `
            res.writeHead(200, {"Content-Type": "text/html"});
            res.end(html);

    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end("404 file not found");
    }

}).listen(3000);

function secondsToDhms(seconds) {
    seconds = Number(seconds);
    var d = Math.floor(seconds / (3600*24));
    var h = Math.floor(seconds % (3600*24) / 3600);
    var m = Math.floor(seconds % 3600 / 60);
    var s = Math.floor(seconds % 3600 % 60);
    
    var dDisplay = d > 0 ? d + (d == 1 ? " day, " : " days, ") : "";
    var hDisplay = h > 0 ? h + (h == 1 ? " hour, " : " hours, ") : "";
    var mDisplay = m > 0 ? m + (m == 1 ? " minute, " : " minutes, ") : "";
    var sDisplay = s > 0 ? s + (s == 1 ? " second" : " seconds") : "";
    return dDisplay + hDisplay + mDisplay + sDisplay;
    }
function parseCPU(cpuArr)
{
    var count =0;
    cpuArr.forEach(element => {
        count++
    });
    return count;
}
console.log("Server listening on port 3000");