var express         =       require("express");
var multer          =       require('multer');
var app             =       express();
var upload          =       multer({ dest: './uploads/'});
var fs              =       require('fs');

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
    res.sendFile(__dirname + "/index.html");
});

// app.get('/getfile',function(req,res){
//       res.sendFile(__dirname + "/BeatYoursFriends.apk");
// });

app.get('api/getAllFilesName',function(req,res){
    fs.readdir("./uploads/",function(err, items) {
        console.log("\n\nAll items:")
        console.log(items);

        for (var i=0; i<items.length; i++) {
            console.log(items[i]);
        }
    });
    res.status(200).end()
});

app.post('/api/upload',function(req,res){
    console.log("\n\n\n"+req);
    console.log("\n"+req.files);
    upload(req,res,function(err) {
        if(err) {
            return res.end("Error uploading file.");
        }
        res.end("File is uploaded");
    });
});

//add error function**
app.get('/api/download/:fileName', function(req, res){
  console.log("starting download:"+ req.params.fileName);
  var file = './uploads/'+req.params.fileName;
  console.log("finished");
  res.download(file); // Set disposition and send it.
});

app.post('/api/iLoveNodar',function(req,res){
    res.status(200).end()
});

app.post('/api/showfiles', function(req, res) {
  console.log(req.body) // form fields
    console.log(req.files) // form files
    res.status(204).end()
});

app.listen(process.env.PORT,function(){
    console.log("Working on port "+process.env.PORT);
});

// app.listen(3000,function(){
//     console.log("Working on port "+3000);
// });