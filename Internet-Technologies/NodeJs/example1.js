const http = require("http");
const hostname = "localhost";
const port = 10002;
const server = http.createServer((req,res)=>{
    res.statusCode = 200;
    res.setHeader("Content=Type","text/html");
    res.end("<html><head><h2>Hello World,This is a HTML response: One Two Three</h2></head></html>");
});
server.listen(port, hostname, ()=>{
    console.log(`Server running at http://${hostname}:${port}/`);
});