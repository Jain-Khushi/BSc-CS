var mysql = require('mysql');
var con = mysql.createConnection({
    host : "localhost",
    user : "Khushi Jain",
    password : "khushi1234",
    database: "mydb"
});
con.connect(function(err){
  
    con.query("select * from customer where CustCity = 'Delhi' ", function(err, result){
        if (err) throw err;
        console.log(result);
    })
});