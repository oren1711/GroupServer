var express         =       require("express");
var multer          =       require('multer');
var app             =       express();
var upload      =   multer({ dest: './uploads/'});

app.use(multer({ dest: './uploads/',
    rename: function (fieldname, filename) {
        return filename+Date.now();
    },
    onFileUploadStart: function (file) {
        console.log(file.originalname + ' is starting ...');
    },
    onFileUploadComplete: function (file) {
        console.log(file.fieldname + ' uploaded to  ' + file.path)
    }
}));

app.get('/',function(req,res){
    console.log("\n\n\n"+req);
    
      res.sendFile(__dirname + "/index.html");
});

app.get('/getfile',function(req,res){
      res.sendFile(__dirname + "/BeatYoursFriends.apk");
});

app.post('/api/photo',function(req,res){
    console.log("\n\n\n"+req);
    console.log("\n"+req.files);
    upload(req,res,function(err) {
        if(err) {
            return res.end("Error uploading file.");
        }
        res.end("File is uploaded");
    });
});

app.post('/api/iLoveNodar',function(req,res){

    upload(req,res,function(err) {
        if(err) {
            return res.end("Error uploading file.");
        }
        res.end("And She loves oren");
    });
});

app.post('/api/showfiles', function(req, res) {
  console.log(req.body) // form fields
    console.log(req.files) // form files
    res.status(204).end()
});

app.listen(process.env.PORT,function(){
    console.log("Working on port "+process.env.PORT);
});