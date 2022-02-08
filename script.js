// window.onload = function() {
//     // console.log(document.getElementById("logo"))

//     document.getElementById("logo").onload = function() {
//         alert("image loaded")
//         document.getElementById("loader").hidden = true;
//         document.getElementById("container").hidden = false;
//     }
    
// }

function whenLoaded() {
    document.getElementById("loader").hidden = true;
    document.getElementById("container").hidden = false;
}