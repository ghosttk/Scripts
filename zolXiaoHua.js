var Crawler = require("crawler");
var fs = require('fs');

var ifrom = 4904;
var ito = 5400;
var fileStream = ifrom+'-'+ito+'.txt';
var c = new Crawler({
    //rateLimit: 1000, // `maxConnections` will be forced to 1
    callback: function(err, res, done){
        var article = res.$(".article-text").text();
        fs.appendFile(fileStream, article, function (err) {
    if(err){
        return console.log(err);
    }else {
        console.log("追加成功");
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
