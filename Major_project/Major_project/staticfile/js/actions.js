var action_user = document.getElementById("user");
var action_heart = document.getElementById("heart");
var action_message = document.getElementById("message");
var action_call = document.getElementById("call");
var action_location = document.getElementById("location");


action_user.addEventListener("click", ()=>{
    var clr = getComputedStyle(action_user).getPropertyValue("color");
    if(clr==="rgb(255, 255, 255)")
        action_user.setAttribute("style","color:#40a8c4;background-color: rgba(255, 255, 255, 0.5);");
    else
    action_user.removeAttribute("style","color:#40a8c4;background-color: rgba(255, 255, 255, 0.5);");
})

action_heart.addEventListener("click", ()=>{
    var clr = getComputedStyle(action_heart).getPropertyValue("color");
    if(clr==="rgb(255, 255, 255)")
        action_heart.setAttribute("style","color:hotpink;background-color: rgba(255, 255, 255, 0.5);");
    else
    action_heart.removeAttribute("style","color:hotpink;background-color: rgba(255, 255, 255, 0.5);");
})

action_message.addEventListener("click", ()=>{
    var clr = getComputedStyle(action_message).getPropertyValue("color");
    if(clr==="rgb(255, 255, 255)")
        action_message.setAttribute("style","color:#40c45a;background-color: rgba(255, 255, 255, 0.5);");
    else
    action_message.removeAttribute("style","color:#40c45a;background-color: rgba(255, 255, 255, 0.5);");
})

action_call.addEventListener("click", ()=>{
    var clr = getComputedStyle(action_call).getPropertyValue("color");
    if(clr==="rgb(255, 255, 255)")
        action_call.setAttribute("style","color:orange;background-color: rgba(255, 255, 255, 0.5);");
    else
    action_call.removeAttribute("style","color:orange;background-color: rgba(255, 255, 255, 0.5);");
})

action_location.addEventListener("click", ()=>{
    var clr = getComputedStyle(action_location).getPropertyValue("color");
    if(clr==="rgb(255, 255, 255)")
        action_location.setAttribute("style","color:#454444;background-color: rgba(255, 255, 255, 0.5);");
    else
    action_location.removeAttribute("style","color:#454444;background-color: rgba(255, 255, 255, 0.5);");
})



