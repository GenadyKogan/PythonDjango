
function uploadFiles() {

    file_path = document.getElementById("standard-upload-files").value
    if (file_path == "") {
        window.alert("No file was selected!");
        return false;
    }

    startUpload(document.getElementById("standard-upload-files").files)
    return true;
}

var dropZone=document.getElementById('drop-zone');

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

var startUpload = async function(files){
    var amountFiles = files.length
    var jumpPercent = 100 / files.length
    var currentPercent = 0

    // Reset progress bar
    document.getElementById("bar-fill").style="width:" + currentPercent + "%"

    Array.prototype.forEach.call(files, function(file) {
        var file_name = file.name

        var res = fetch('/upload/', {
            method: 'POST',
            headers: { "X-CSRFToken": csrftoken,
                        "filename" : file_name , "username":name},
            body: file
        })
        
        currentPercent = currentPercent + jumpPercent
        document.getElementById("bar-fill").style="width:" + currentPercent + "%"
        document.getElementById("bar-fill-text").innerHTML = currentPercent + "%"
        
    })
}

dropZone.ondrop=function(e){
    //fileinput.files=e.dataTransfer.files;
    e.preventDefault();
    this.className='upload-console-drop';

    //console.log();
    startUpload(e.dataTransfer.files);
}

//Drop functionality
dropZone.ondragover=function(){
    this.className='upload-console-drop drop';
    return false;
};

//console.log(dropZone);
dropZone.ondragleave=function(){
    this.className='upload-console-drop';
    return false;
}

(function() {
    "user strict";
    var dropZone=document.getElementById('drop-zone');
    var startUpload=function(files){
        console.log(files);
    };
    //standard form upload
    document.getElementById('standard-upload').addEventListener('click', function(e){
        var standardUploadFiles=document.getElementById('standard-upload-files').files;
       e.preventDefault();
       
        startUpload(standardUploadFiles);
    });
    
    dropZone.ondrop=function(e){
        e.preventDefault();
        this.className='upload-console-drop';

        //console.log();
        startUpload(e.dataTransfer.files);
    }
    //Drop functionality
    dropZone.ondragover=function(){
       this.className='upload-console-drop drop';
       return false;
    };
    //console.log(dropZone);
    dropZone.ondragleave=function(){
        this.className='upload-console-drop';
        return false;
    }
}());