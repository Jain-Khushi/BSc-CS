var fs = require('fs');

fs.writeFile('mynewfile.txt','Hello content', function(err){
    if (err) throw err;
    console.log('Saved!');
});