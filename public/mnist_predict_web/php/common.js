var can;
var ct;
var ox=0,oy=0,x=0,y=0;
var mf=false;

function mam_draw_init(){
    can=document.getElementById("can");
    can.addEventListener("touchstart",onDown,false);
    can.addEventListener("touchmove",onMove,false);
    can.addEventListener("touchend",onUp,false);
    can.addEventListener("mousedown",onMouseDown,false);
    can.addEventListener("mousemove",onMouseMove,false);
    can.addEventListener("mouseup",onMouseUp,false);
    ct=can.getContext("2d");
    ct.strokeStyle="#000000";
    ct.lineWidth=5;
    ct.lineJoin="round";
    ct.lineCap="round";
    clearCan();
}

function StopYure(event){
    event.preventDefault();
    event.stopPropagation();
}

function onDown(event){
    mf=true;
    ox=event.touches[0].pageX-event.target.getBoundingClientRect().left-scx();
    oy=event.touches[0].pageY-event.target.getBoundingClientRect().top -scy();
    event.stopPropagation();
}
function onMove(event){
    if(mf){
        x=event.touches[0].pageX-event.target.getBoundingClientRect().left-scx();
        y=event.touches[0].pageY-event.target.getBoundingClientRect().top -scy();
        drawLine();
        ox=x;
        oy=y;
        event.preventDefault();
        event.stopPropagation();
    }
}
function onUp(event){
    mf=false;
    event.stopPropagation();
}

function onMouseDown(event){
    ox=event.clientX-event.target.getBoundingClientRect().left;
    oy=event.clientY-event.target.getBoundingClientRect().top ;
    mf=true;
}
function onMouseMove(event){
    if(mf){
        x=event.clientX-event.target.getBoundingClientRect().left;
        y=event.clientY-event.target.getBoundingClientRect().top ;
        drawLine();
        ox=x;
        oy=y;
    }
}
function onMouseUp(event){
    mf=false;
}

function drawLine(){
  ct.strokeStyle="#000000";
    ct.lineWidth=5;
    ct.lineJoin="bevel";
    ct.lineCap="bevel";

    rx=Math.abs(x-ox)+2;
    ry=Math.abs(y-oy)+2;
    ww=Math.atan2(ry,rx)*10+1;
    ct.lineWidth=ww;

    ct.beginPath();
    ct.moveTo(ox,oy);
    ct.lineTo(x,y);
    ct.stroke();
}

function clearCan(){
    ct.fillStyle="rgb(255,255,255)";
    ct.fillRect(0,0,can.getBoundingClientRect().width,can.getBoundingClientRect().height);
}

function savePic(){
    var imgPng=can.toDataURL('image/png');
    imgPng=imgPng.replace(/^data:image\/png;base64,/,'');
    document.getElementById("imgBase64").value=imgPng;
    document.getElementById("fm").submit();
}

function scx(){return document.documentElement.scrollLeft || document.body.scrollLeft;}
function scy(){return document.documentElement.scrollTop  || document.body.scrollTop ;}
