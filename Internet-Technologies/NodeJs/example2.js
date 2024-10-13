const http = require("http");
const hostname = "localhost";
const port = 10000;
const server = http.createServer((req,res)=>{
    res.statusCode = 200;
    res.setHeader("Content=Type","text/html");
    res.end("<html><head><h2>Hello World,This is a HTML response: </h2></head><body> <ul><li>One</li> <li>Two</li> <li>Three</li> </ul></body></html>");
});
server.listen(port, hostname, ()=>{
    console.log(`Server running at http://${hostname}:${port}/`);
});