window.onload = function(){
// alert("testing");

// 디지털 시계
//setInterval(mywatch, 1000); //함수 호출
//
//function mywatch(){
//    const date = new Date();
//    let now = date.toLocaleTimeString();
//    document.getElementById("demo").innerHTML = now;
//}
// 시계 함수 끝



/* 메인사진변경함수 */
let picture = ["../static/tour/images/sokcho1.jpg", "../static/tour/images/sokcho2.jpg", "../static/tour/images/sokcho3.jpg",
                "../static/tour/images/gangneung1.png", "../static/tour/images/gangneung2.jpg", "../static/tour/images/gangneung3.jpg" ];

//사진 변경 스크립트 원본
let imgIdx = 0;
// console.log(Math.round((Math.random()*picture.length))); 혹시나 랜덤으로 할 경우대비
// let first_pic = Math.round((Math.random()*picture.length));


changePicture();

function changePicture(){
    let img = document.getElementById("pic1")
    //img.setAttribute("src",picture[imgIdx]);
    img.src = picture[imgIdx];
    imgIdx++;

    if(imgIdx == picture.length){
        imgIdx = 0;
    }

    setTimeout(changePicture, 4000); //콜백함수
}
}   // 사진 변경 함수 끝