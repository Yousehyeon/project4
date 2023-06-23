window.onload = function(){
// alert("testing");

/* 메인사진변경함수 */
let picture = ["./images/sokcho1.jpg", "./images/sokcho2.jpg",
                "./images/sokcho3.jpg"]
let imgIdx = 0;

changePicture();

function changePicture(){
    let img = document.getElementById("pic")
    document.getElementById("pic").src = picture[imgIdx];
    imgIdx++;

    if(imgIdx == picture.length){
        imgIdx = 0;
    }

    setTimeout(changePicture, 5000); //콜백함수
} //
}