var inputElement = document.getElementById("file-upload");
inputElement.addEventListener("change", handleFiles, true);

function returnFileSize(number) {
    if (number < 1024) {
        return number + 'bytes';
    } else if (number > 1024 && number < 1048576) {
        return (number / 1024).toFixed(1) + 'KB';
    } else if (number > 1048576) {
        return (number / 1048576).toFixed(1) + 'MB';
    }
}

function handleFiles() {
    var fileList = this.files; /* now we can work with the file list */
    var infoDiv = document.getElementById("infoDiv")
    infoDiv.innerHTML = "";
    for (var i = 0; i < fileList.length; i++) {
        file = fileList[i];
        //alert(file.name +returnFileSize(file.size) + file.type);
        infoP = document.createElement('p');
        infoDiv.appendChild(infoP);
        infoP.innerHTML = `${file.name} <span style="color:blue;">${returnFileSize(file.size)}</span> ${file.type}`;
    }
}
