
function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function()
    {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
        {
            callback(xmlHttp.responseText);
        }
    }

    xmlHttp.open("GET", theUrl, true);
    xmlHttp.send(null);

    return;
}

function tenorCallback_search(responsetext)
{
    var response_objects = JSON.parse(responsetext);

    top_10_gifs = response_objects["results"];
    for(let i =0;i<top_10_gifs.length;i++)
    {
        var src= top_10_gifs[i]["media_formats"]["nanogif"]["url"];
        document.getElementsByClassName("ddc-tenor")[0].innerHTML += `<img src="${src}" class="inner-tenor">`;
    }

    return;

}

// document.getElementsByClassName("micro-btn").addEventListener("click", ()={

// });

document.getElementsByClassName("emoji_comman")[0].addEventListener("click", ()=>{
open_gif("trending");
});

function open_gif(nam){
    var apikey = "AIzaSyC20vM_Y4-eq3eYHRHi017Ycd_s4zJ-1UE";
    var clientkey = "my_test_app";
    var lmt = 20;
    document.getElementsByClassName("ddc-tenor")[0].innerHTML="";

    var search_term = nam;

    var search_url = "https://tenor.googleapis.com/v2/search?q=" + search_term + "&key=" +
            apikey +"&client_key=" + clientkey +  "&limit=" + lmt;

    httpGetAsync(search_url,tenorCallback_search);
    return
}

function grab_data()
{

    
    var apikey = "AIzaSyC20vM_Y4-eq3eYHRHi017Ycd_s4zJ-1UE";
    var clientkey = "my_test_app";
    var lmt = 20;
    document.getElementsByClassName("ddc-tenor")[0].innerHTML="";

    var search_term = document.getElementById("tenor-search").value;

    var search_url = "https://tenor.googleapis.com/v2/search?q=" + search_term + "&key=" +
            apikey +"&client_key=" + clientkey +  "&limit=" + lmt;

    httpGetAsync(search_url,tenorCallback_search);

    return;
}
function Rec_On()
{
    
    document.getElementById("recordedAudio").style.display="None";
    const aud = document.createElement('audio');
   
    navigator.mediaDevices.getUserMedia({audio:true})
        .then(stream => {handlerFunction(stream)})
        
        
    function handlerFunction(stream) 
        {
                
                rec = new MediaRecorder(stream);
                rec.ondataavailable = e => {
                    audioChunks.push(e.data);
                    if(rec.state == "inactive"){
                    let audio_src;
                    let blob = new Blob(audioChunks,{type:'audio/mpeg-3'});
                    audio_src = URL.createObjectURL(blob);
                    recordedAudio.src = audio_src;
                    recordedAudio.controls=true;
                    recordedAudio.autoplay=false;
                    aud.setAttribute('src' , audio_src)
                    aud.setAttribute('controls' , '')
                    aud.setAttribute('style' , 'width: 16rem; height: 40px;')
                    
                    
                    // alert(<audio src="audio_src"></audio>)

                    stream.getTracks().forEach((track) => {
                        track.stop();
                      });
                    
                    
                    }
                }
                audioChunks = [];
                rec.start();
                const canvas = document.querySelector('.visualizer');
                let audioCtx;
                const canvasCtx = canvas.getContext("2d");
                visualize(stream);

                function visualize(stream) {
                    if(!audioCtx) {
                      audioCtx = new AudioContext();
                    }
                  
                    const source = audioCtx.createMediaStreamSource(stream);
                  
                    const analyser = audioCtx.createAnalyser();
                    analyser.fftSize = 2048;
                    const bufferLength = analyser.frequencyBinCount;
                    const dataArray = new Uint8Array(bufferLength);
                  
                    source.connect(analyser);
                    //analyser.connect(audioCtx.destination);
                  
                    draw()
                  
                    function draw() {
                      const WIDTH = canvas.width
                      const HEIGHT = canvas.height;
                  
                      requestAnimationFrame(draw);
                  
                      analyser.getByteTimeDomainData(dataArray);
                      canvasCtx.fillStyle = '#dcdedf';
                      canvasCtx.fillRect(0, 0, WIDTH, HEIGHT);
                      canvasCtx.lineWidth = 4;
                      canvasCtx.strokeStyle = "black";
                      canvasCtx.beginPath();
                  
                      let sliceWidth = WIDTH * 1.0 / bufferLength;
                      let x = 0;
                  
                  
                      for(let i = 0; i < bufferLength; i++) {
                  
                        let v = dataArray[i] / 128.0;
                        let y = v * HEIGHT/2;

                        if(i === 0) {
                          canvasCtx.moveTo(x, y);
                        } else {
                            
                          canvasCtx.lineTo(x,y);
                        }
                  
                        x += sliceWidth;
                      }
                      canvasCtx.lineTo(canvas.width, canvas.height/2);
                      canvasCtx.stroke();
                  
                    }
                }
             }
                  
                //   window.onresize = function() {
                //     canvas.width = mainSection.offsetWidth;
                //   }
                //   window.onresize();
                
            
                const pause = document.querySelector('.pause');
                const play = document.querySelector('.play');
                const resm = document.querySelector('.audiores');
                const vs = document.querySelector('.visualizer');
                const sennd = document.querySelector('.Audio_Send');

                pause.onclick = function() {
                    if(rec.state == "recording")
                    {
                        document.getElementById("recordedAudio").style.display="flex";
                        vs.style.display="none";
                        rec.stop();
                        
                        pause.style.display="none";
                        play.style.display="block";
                    }  
                }
                
                sennd.onclick = function()
                {
                    if(rec.state == "recording")
                        rec.stop();
                    pause.style.display="block";
                    play.style.display="none";
                    document.getElementsByClassName("hid")[0].style.display="flex";
                    document.getElementsByClassName("audio")[0].style.display="None";
                    vs.style.display="flex";
                    document.getElementById("recordedAudio").style.display="None";
                    document.getElementById("recordedAudio").src = "";
                    const time = new Date();
                    let hrs = time.getHours();
                    let min = time.getMinutes();
                    let tm = hrs+":"+min;
                    let mc= document.getElementById("mess-cont");
                    // mc.innerHTML+=`<div class="chat-rightmessage"><div class="main-cont"><div class="chat-mess"><audio src=${audio_src} controls ></audio></div></div><div class="h"><span class="time">${tm}</span><i class="las la-check-double"></i></div></div>`;
                    const Chat_Rght_mess = document.createElement('div');
                    Chat_Rght_mess.setAttribute('class' , 'chat-rightmessage');
                    const main_cont = document.createElement('div');
                    main_cont.setAttribute('class' , 'main-cont');
                    const chat_mess = document.createElement('div');
                    chat_mess.setAttribute('class' , 'chat-mess');
                    chat_mess.appendChild(aud);
                    main_cont.appendChild(chat_mess);
                    Chat_Rght_mess.appendChild(main_cont);
                    const h1 = document.createElement('div');
                    h1.setAttribute('class' , 'h');
                    const time_real = document.createElement('span');
                    time_real.setAttribute('class' , 'time');
                    time_real.innerText = tm;
                    const chk_double = document.createElement('i');
                    chk_double.setAttribute('class' , 'las la-check-double');
                    h1.appendChild(time_real);
                    h1.appendChild(chk_double);
                    Chat_Rght_mess.appendChild(h1);

                    document.getElementById("mess-cont").appendChild(Chat_Rght_mess);
                    var scroll = document.getElementById("mess-cont");
                    scroll.scrollTop = scroll.scrollHeight;

                    // document.getElementById('chat-message-container').scrollTop = mc.offsetHeight + mc.offsetTop;




                
                
                }
           
            document.getElementsByClassName("hid")[0].style.display="None";
            document.getElementsByClassName("audio")[0].style.display="flex";
            console.log('I was clickeds')
        
}



function openemj(name){
    var dc = document.getElementsByClassName("footer");
    for(let i=0;i<dc.length;i++)
    {
        dc[i].style.display="none";
    }
    document.getElementById(name).style.display="block";
}

document.getElementsByClassName("chat-button")[0].addEventListener("click",()=>{
let v = document.getElementsByClassName("chat-button")[0];
let b = getComputedStyle(v);
let n = b.getPropertyValue("margin-left");
// alert(n);
if(n==="288px"){
    v.setAttribute("style","margin-left:0rem;");
}
else{
    v.setAttribute("style","margin-left:18rem;");
}
});

let emj = document.getElementsByClassName("ddc-moji")[0];
let st = "&#";
for(let i = 128512; i<= 128690;i++)
{
    emj.innerHTML+= `<span class="ddc-emojis">${st+i}</span>`;
}

var emoj  = document.querySelectorAll('.ddc-emojis');

for(let i = 0; i<emoj.length;i++)
{
    emoj[i].addEventListener("click", (e)=>{
        document.getElementById("message-input").value += e.target.innerHTML;
        document.getElementById("message-input").focus();
    });
}

document.getElementsByClassName("yyy")[0].addEventListener("click", ()=>{
    // ele1.setAttribute("style", "display:block;");
    let mc= document.getElementById("mess-cont");
    let ele1 =document.getElementsByClassName("footer")[0];
    let ele = document.getElementsByClassName("emoji_comman");
    let var1 = getComputedStyle(ele[0]).getPropertyValue("display");
    if(var1 ==="none"){
    ele[0].setAttribute("style", "display:block;");
    ele[1].setAttribute("style", "display:block;");
    ele1.setAttribute("style", "display:block;");
    mc.setAttribute("style", "height: 50%;border-bottom-left-radius: 0rem;border-bottom-right-radius: 0rem;");
    }
    else{
        ele[0].setAttribute("style", "display:none;");
    ele[1].setAttribute("style", "display:none;");
    ele1.setAttribute("style", "display:none;");
    mc.setAttribute("style", "height: 100%;border-bottom-left-radius: 1.5rem;border-bottom-right-radius: 1.5rem;");
    }
    
});

document.getElementsByClassName("dropdown")[0].addEventListener("click", ()=>{
let ele = document.getElementsByClassName("dropdown-content")[0];
let var1 = getComputedStyle(ele);
let var2 = var1.getPropertyValue("display");

if(var2 === "none")
ele.setAttribute("style", "display:block;");
else
ele.setAttribute("style", "display:none;");

});
// document.getElementsByName("body").addEventListener("click",()=>{
//     let v = document.getElementsByClassName("dropdown-content")[0];
//     v.setAttribute("style", "display:none;");

// });

