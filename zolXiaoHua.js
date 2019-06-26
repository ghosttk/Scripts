var Crawler = require("crawler");
var fs = require('fs');

var file = "zolConfig.json"
var config = JSON.parse(fs.readFileSync(file));
console.log(config)
/*
var ifrom = process.argv[2];//5400
var ito = process.argv[3] ;//5500;
*/
var ifrom = config.iStart
var ito = config.iEnd
var fileStream = ifrom+'-'+ito+'.txt';
var c = new Crawler({
    //rateLimit: 1000, // `maxConnections` will be forced to 1
    callback: function(err, res, done){
        var article = res.$(".article-text").text();
        fs.appendFile(fileStream, article, function (err) {
    if(err){
        return console.log(err);
    }else {
        console.log(article);
    }

});
        done();
    }
});

var arrUrl = [];
for (i=ifrom; i<ito; i++){
        arrUrl.push('http://xiaohua.zol.com.cn/detail5/'+i+'.html');
}

c.queue(arrUrl);//between two tasks, minimum time gap is 1000 (ms)
