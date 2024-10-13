var http = require('http');
var fs = require('fs');
const { text } = require('stream/consumers');
http.createServer('example1.js',function(req,res){
    fs.readFile('example1.js',function(err, data){
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);
        return res.end();
    });
}).listen(8080);