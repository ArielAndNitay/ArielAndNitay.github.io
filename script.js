function whenLoaded() {
    console.log('ok')
    document.getElementById("loader").hidden = true;
    document.getElementById("loader-container").style
    .setProperty("display", "none", "important");
    document.getElementById("container").hidden = false;
}