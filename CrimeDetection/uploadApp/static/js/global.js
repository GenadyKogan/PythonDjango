console.log('Test.');

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