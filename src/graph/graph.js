var w = 750;
var h = 1000
var a = w/3;
var x=w/2;
var y=h*9/16;
var r1 = w/4.9;
var r = w/7.5
var r0 =w/9;
var angle = 0;

//sin36=0.5878,cos36=0.809
var dataset = [
   { "x_axis": 0, "y_axis": 0,"index":0,"img" :"/home/lamph/data/inmul.png","tag":"url(#0)"},
   { "x_axis": 0, "y_axis": -a,"index":1,"img" :"/home/lamph/data/mcdonalds.jpg","tag":"url(#1)"},
   { "x_axis": +a*0.5878*2*0.809, "y_axis": -a+a*0.5878*2*0.5878,"index":2,"img" :"/home/lamph/data/hipo.jpg","tag":"url(#2)"},
   { "x_axis": +a*0.5878, "y_axis": +a*0.809,"index":3,"img" :"/home/lamph/data/hoya.jpg","tag":"url(#3)"},
   { "x_axis": -a*0.5878, "y_axis": +a*0.809,"index":4,"img" :"/home/lamph/data/somun.jpg","tag":"url(#4)"},
   { "x_axis": -a*0.5878*2*0.809, "y_axis": -a+a*0.5878*2*0.5878,"index":5,"img" :"/home/lamph/data/mcdonalds.jpg","tag":"url(#5)"}
   ];

var jsonstr = "{\"nodes\": [\"맥도날드\", \"Hippo Coffee\", \"호야네\", \"소문날라\", \"신서방 족발\", \"호치킨\", \"밥은\"]}";

var temp = JSON.parse(jsonstr);
temp["nodes"].unshift("dummy");


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

            // .on("click",function(d){angle+=72;
            // console.log(angle);});

// var defs = svg.append("defs").attr("id", "imgdefs")

// var catpattern = defs.data(dataset)
//                         .append("pattern")
//                         .attr("id", "catpattern")
//                         .attr("height", function(d){if(d.index==0) return r0/4;
//         else if (d.index==1) return r1/4;
//         else return r/4;})
//                         .attr("width",function(d){if(d.index==0) return r0/4;
//         else if (d.index==1) return r1/4;
//         else return r/2;})
//                         .attr("x", "0")
//                         .attr("y", "0");
                        
// catpattern.append("image")
//      .attr("x", -130)
//      .attr("y", -220)
//      .attr("height", 640)
//      .attr("width", 480)
//      .attr("xlink:href", function(d){return d.img;});
// var defs = svg.append("defs");
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
                return  "translate("+d.x_axis+","+d.y_axis+")"+"rotate(-"+angle+")";})
            .on("click",function(d){
                
                // if(d.index==0)
                // alert ("index no.0!");
                // else if(d.index==1){
                
                // alert ("index no.1!");}
                // else if(d.index==2){
                // var temp;
                // var tempcordi;
                // temp=dataset[1];
                // dataset[1]=dataset[2];
                // dataset[2]=temp;

                // tempcordi=dataset[1].x_axis;
                // dataset[1].x_axis=dataset[2].x_axis;
                // dataset[2].x_axis=tempcordi;

                // tempcordi=dataset[1].y_axis;
                // dataset[1].y_axis=dataset[2].y_axis;
                // dataset[2].y_axis=tempcordi;

                console.dir(dataset);
                
                // d3.select(this)
                // .transition()
                // .attr("transform",function(d){
                // return  "translate("+d.x_axis+","+d.y_axis+")"+"rotate(-"+angle+")";})
            
                angle +=72;
            g
            .transition()
            .attr("transform","translate("+x+","+y+") rotate("+angle+")")
   
            gg.transition()
            .attr("transform",function(d){
                return  "translate("+d.x_axis+","+d.y_axis+")"+"rotate(-"+angle+")";})
            // }
            //     else if(d.index ==3)
            //     return;
            //     else if(d.index ==4)
            //     return;
            //     else if(d.index ==5)
            //     return;
            //     console.log(angle);
            });
            
            
var clip = gg.append("clipPath")
            .attr("id",function(d){return d.index;});
            
            
            
  var circle =  clip.append("circle")
        .attr("r",function(d){if(d.index==0) return r0;
        else return r;})
        .attr("fill","orange");
        
        
          

 var image =  gg.append("image")
        .attr("xlink:href",function(d){return d.img;})
        .attr("x",function(d){
            if(d.index==0)return -r0;
            else if(d.index==1)return -r1;
            else return -r;
        })
        .attr("y",function(d){
            if(d.index==0)return -r0;
            else if(d.index==1)return -r1;
            else return -r;
        })
         .attr("width",function(d){if(d.index == 0)return 2*r0;
        else if(d.index ==1 )return r1*2;
        else return r*2;})
        .attr("height",function(d){if(d.index == 0)return 2*r0;
        else if(d.index ==1 )return r1*2;
        else return r*2;})
        .attr("clip-path",function(d){return d.tag;}); 

var text=   gg.append("text")
        .text(function(d){return d.name;})
    .attr("x",0)
    .attr("y",function(d){if(d.index == 0)return -r0-5;
        else if(d.index ==1 )return -r1-5;
        else return -r-5;})
    .attr("font-family","sans-serif")
    .attr("font-size","1.4em")
    .attr("fill","black")
    .attr("text-anchor","middle");


        
// $("g").rotate({ 
//    bind: 
//      { 
//         click: function(){
//             angle +=90;
//             $(this).rotate({ animateTo:value})
//         }
//      } 
   
// });


var gelement = document.getElementById("0");
gelement.addEventListener("click", myFunction);


function myFunction(){
    alert ("Hello!");
}

// var anim = selectAll("gg")
//             .on("click",function(d){
//                 if(d.index==0) return;
//                 else if(d.index==1){
//                 angle = 72*0;
//                 alert ("hello!");}
//                 else if(d.index==2)
//                 angle = 72*1;
//                 else if(d.index ==3)
//                 angle = 72*2;
//                 else if(d.index ==4)
//                 angle = 72*3;
//                 else if(d.index ==5)
//                 angle =72*4;
//                 console.log(angle);
//             });