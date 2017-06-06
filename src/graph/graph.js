var w = 750;
var h = 1000
var a = w/3;
var abig =w/2.2 //확대 반지름
var x=w/2;
var y=h*9/16;
var r1 = w/4.9;
var r = w/7.5
var r0 =w/9;
var angle = 0;
var rf = r/4;

var a1=w/3;
var a2=w/3;
var a3=w/3;
var a4=w/3;
var a5=w/3;
var cordi =[
    { "x_axis": 0, "y_axis": 0},
    {"x_axis": 0, "y_axis": -a1},
    {"x_axis": +a2*0.5878*2*0.809, "y_axis": -a2+a2*0.5878*2*0.5878},
    {"x_axis": +a3*0.5878, "y_axis": +a3*0.809},
    {"x_axis": -a4*0.5878, "y_axis": +a4*0.809},
    {"x_axis": -a5*0.5878*2*0.809, "y_axis": -a5+a5*0.5878*2*0.5878}
];

//sin36=0.5878,cos36=0.809
var dataset = [
   { "x_axis": 0, "y_axis": 0,"index":0,"img" :"/home/lamph/data/inmul.png","tag":"url(#0)","r":r0,
    "fr":[
        {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": -3*rf,"index":0,"tag":"url(#0)","r":0},
        {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": 0,"index":1,"tag":"url(#1)","r":0},
        {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": 3*rf,"index":2,"tag":"url(#2)","r":0}
    ]
},
   { "x_axis": 0, "y_axis": -a1,"index":1,"img" :"sajin/wafle.jpg","tag":"url(#1)","r":r,
   "fr":[
       {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": -3*rf,"index":0,"tag":"url(#0)","r":0},
        {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": 0,"index":1,"tag":"url(#1)","r":0},
        {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": 3*rf,"index":2,"tag":"url(#2)","r":0}
   ]
},
   { "x_axis": +a2*0.5878*2*0.809, "y_axis": -a2+a2*0.5878*2*0.5878,"index":2,"img" :"sajin/streetcafe.jpg","tag":"url(#2)","r":r,
   "fr":[
        {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": -3*rf,"index":0,"tag":"url(#0)","r":0},
        {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": 0,"index":1,"tag":"url(#1)","r":0},
        {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": 3*rf,"index":2,"tag":"url(#2)","r":0}
   ]
},
   { "x_axis": +a3*0.5878, "y_axis": +a3*0.809,"index":3,"img" :"sajin/masilzari.jpg","tag":"url(#3)","r":r,
   "fr":[
        {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": -3*rf,"index":0,"tag":"url(#0)","r":0},
        {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": 0,"index":1,"tag":"url(#1)","r":0},
        {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": 3*rf,"index":2,"tag":"url(#2)","r":0}
   ]
},
   { "x_axis": -a4*0.5878, "y_axis": +a4*0.809,"index":4,"img" :"sajin/fryfan.jpg","tag":"url(#4)","r":r,
   "fr":[
        {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": -3*rf,"index":0,"tag":"url(#0)","r":0},
        {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": 0,"index":1,"tag":"url(#1)","r":0},
        {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": 3*rf,"index":2,"tag":"url(#2)","r":0}
   ]
},
   { "x_axis": -a5*0.5878*2*0.809, "y_axis": -a5+a5*0.5878*2*0.5878,"index":5,"img" :"sajin/postre.jpg","tag":"url(#5)","r":r,
   "fr":[
        {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": -3*rf,"index":0,"tag":"url(#0)","r":0},
        {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": 0,"index":1,"tag":"url(#1)","r":0},
        {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": 3*rf,"index":2,"tag":"url(#2)","r":0}
   ]
}
   ];

var jsonstr = "{\"nodes\": [\"Wafle Star\", \"Street Cafe\", \"마실자리\", \"Fryfan-Gogi\", \"Postre\", \"호치킨\", \"밥은\"]}";

// "friend":["문재인","김민석","박종균"]
var friendset = [
    {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": -3*rf,"index":0,"tag":"url(#0)"},
    {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": 0,"index":1,"tag":"url(#1)"},
    {"x_axis": -a*0.5878*2*0.809-r+rf, "y_axis": 3*rf,"index":2,"tag":"url(#2)"}
];

var temp = JSON.parse(jsonstr);
var frtemp = {"friends":[
                ["문재인","김민석","박종균"],
                ["조우영","민연홍","이상혁"],
                ["진종인","김철수","이영희"],
                ["해리포터","김정균","정노철"],
                ["메모리","디버거","검사기"]
                    ]};
temp["nodes"].unshift("dummy");
frtemp ["friends"].unshift("dummy");

// console.dir(temp["nodes"]);

// dataset.join(temp["nodes"]);
// temp["nodes"].(dataset);

// console.dir(temp["nodes"]);
for (var i=0;i<dataset.length;i++)
{
    dataset[i]["name"]=temp["nodes"][i];
}
console.dir(dataset);

var svg = d3.select("body")
            .append("svg")
            .attr("width",w)
            .attr("height",h);

        
var defs = svg.append("defs");
var g = svg.append("g")
            .attr("transform",function(){
                return  "translate("+x+","+y+")"+" rotate("+angle+")";
            })
            .attr("id","source")
            .attr("class","group");
            


var gg = g.selectAll("g")
            .data(dataset)
            .enter()
            .append("g")
            .attr("class",function(d){return d.index;})
            .attr("transform",function(d){
                return  "translate("+d.x_axis+","+d.y_axis+")"+"rotate(-"+angle+")";});

var ggg=gg.selectAll("g")
            .data(function(d){return d.fr;})
            .enter()
            .append("g")
            .attr("class",function(d){return d.index;})
            .attr("transform",function(d){
                return  "translate(0, 0)"});


 //여기부터 클릭 설정

          var click= gg .on("click",function(d){
            if(d.index == 1){
                angle =0;
                for(var i=1;i<6;i++)
                {
                    dataset[i].x_axis=cordi[i].x_axis;
                    dataset[i].y_axis=cordi[i].y_axis;
                    dataset[i].r=r;
                    for(var j=0;j<3;j++){
                    dataset[i].fr[j]["name"]=null;
                    dataset[i].fr[j]["r"]=0;
                    }
                    
                }
                    d.x_axis=(cordi[d.index].x_axis)/a*abig;
                    d.y_axis=(cordi[d.index].y_axis)/a*abig;
                    d.r=r1;
                    for(var i=0;i<3;i++){
                    d.fr[i]["name"]=frtemp["friends"][d.index][i];
                    d.fr[i]["r"]=rf;}
                    
                    d.fr.r=rf;
            }
            else if(d.index ==2 ){
                angle = 72*1;
                for(var i=1;i<6;i++)
                {
                    dataset[i].x_axis=cordi[i].x_axis;
                    dataset[i].y_axis=cordi[i].y_axis;
                    dataset[i].r=r;
                    for(var j=0;j<3;j++){
                    dataset[i].fr[j]["name"]=null;
                    dataset[i].fr[j]["r"]=0;
                    }
                }
                    d.x_axis=(cordi[d.index].x_axis)/a*abig;
                    d.y_axis=(cordi[d.index].y_axis)/a*abig;
                    d.r=r1;
                    for(var i=0;i<3;i++){
                    d.fr[i]["name"]=frtemp["friends"][d.index][i];
                    d.fr[i]["r"]=rf;}
                    
                    d.fr.r=rf;
            }
            else if(d.index ==3 ){
                angle = 72*2;
                 for(var i=1;i<6;i++)
                {
                    dataset[i].x_axis=cordi[i].x_axis;
                    dataset[i].y_axis=cordi[i].y_axis;
                    dataset[i].r=r;
                    for(var j=0;j<3;j++){
                    dataset[i].fr[j]["name"]=null;
                    dataset[i].fr[j]["r"]=0;
                    }
                }
                    d.x_axis=(cordi[d.index].x_axis)/a*abig;
                    d.y_axis=(cordi[d.index].y_axis)/a*abig;
                    d.r=r1;
                    for(var i=0;i<3;i++){
                    d.fr[i]["name"]=frtemp["friends"][d.index][i];
                    d.fr[i]["r"]=rf;}
                    
                    d.fr.r=rf;
            }
            else if(d.index ==4 ){
                angle = 72*3;
                for(var i=1;i<6;i++)
                {
                    dataset[i].x_axis=cordi[i].x_axis;
                    dataset[i].y_axis=cordi[i].y_axis;
                    dataset[i].r=r;
                    for(var j=0;j<3;j++){
                    dataset[i].fr[j]["name"]=null;
                    dataset[i].fr[j]["r"]=0;
                    }
                }
                    d.x_axis=(cordi[d.index].x_axis)/a*abig;
                    d.y_axis=(cordi[d.index].y_axis)/a*abig;
                    d.r=r1;
                    for(var i=0;i<3;i++){
                    d.fr[i]["name"]=frtemp["friends"][d.index][i];
                    d.fr[i]["r"]=rf;}
                    
                    d.fr.r=rf;
            }
            else if(d.index ==5 ){
                angle = 72*4;
                for(var i=1;i<6;i++)
                {
                    dataset[i].x_axis=cordi[i].x_axis;
                    dataset[i].y_axis=cordi[i].y_axis;
                    dataset[i].r=r;
                    for(var j=0;j<3;j++){
                    dataset[i].fr[j]["name"]=null;
                    dataset[i].fr[j]["r"]=0;
                    }
                }
                    d.x_axis=(cordi[d.index].x_axis)/a*abig;
                    d.y_axis=(cordi[d.index].y_axis)/a*abig;
                    d.r=r1
                    for(var i=0;i<3;i++){
                    d.fr[i]["name"]=frtemp["friends"][d.index][i];
                    d.fr[i]["r"]=rf;}
                    
                    d.fr.r=rf;
            }
            //여기까지 각 노드별 클릭 셋팅

            //여기부터 클릭시 속성값 편짐
            g.transition()
            // .delay(10)
            .attr("transform","translate("+x+","+y+") rotate(-"+angle+")");

            gg.transition()
            // .delay(10)
            .attr("transform",function(d){
                return  "translate("+d.x_axis+","+d.y_axis+")"+"rotate("+angle+")";});

            circle
            .transition()
            .attr("r",function(d){return d.r;});

            image
            .transition()
            .attr("x",function(d){return -d.r;})
            .attr("y",function(d){return -d.r;})
            .attr("width",function(d){return d.r*2;})
            .attr("height",function(d){return d.r*2;});

            text.
            transition()
            .attr("y",function(d){return -d.r-5;});

            ggg.transition()
            .attr("transform",function(d){
                return  "translate("+d.x_axis+","+d.y_axis+")";});
   
                // console.log(angle);
                // console.log(dataset[1].y_axis);

            gggcircle
            .transition()
            .attr("r",function(d){return d.r;})
            .attr("fill","#98ff98");

            gggtext
            .text(function(d){return d.name;});

            console.dir(dataset);
        });
        
            
//여기까지 클릭 설정

//gg설정

var clip = gg.append("clipPath")
            .attr("id",function(d){return d.index;});
            
            
            
  var circle =  clip.append("circle")
        .attr("r",function(d){return d.r;})
        .attr("fill","orange")
        .attr("boder",5)
        .attr("boder-radius","#98ff98");
        
        
          

 var image =  gg.append("image")
        .attr("xlink:href",function(d){return d.img;})
        .attr("x",function(d){return -d.r;})
        .attr("y",function(d){return -d.r;})
         .attr("width",function(d){return d.r*2;})
        .attr("height",function(d){return d.r*2;})
        .attr("clip-path",function(d){return d.tag;}); 

var text=   gg.append("text")
        .text(function(d){return d.name;})
    .attr("x",0)
    .attr("y",function(d){return -d.r-5;})
    .attr("font-family","sans-serif")
    .attr("font-size","1.4em")
    .attr("fill","black")
    .attr("text-anchor","middle");


// 여기 부터ggg 설정



  
            
    var gggclip = ggg.append("clipPath")
            .attr(function(d){return d.index;})
            
    var gggcircle=  ggg.append("circle")
            .attr("r",function(d){return d.r;})
            .attr("fill","#98ff98");

    var gggtext = ggg.append("text")
            // .text(function(d){return d.name;})
            .attr("x",2*rf)
        .attr("font-family","sans-serif")
        .attr("font-size","1em")
        .attr("fill","black");