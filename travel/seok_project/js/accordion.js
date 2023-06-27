const q_titles = document.querySelectorAll(".q_title");

q_titles.forEach(q_title1 => {
    q_title1.addEventListener("click", event => {

        q_title1.classList.toggle("active");
        const q_content = q_title1.nextElementSibling;
        if(q_title1.classList.contains("active")){
            q_content.style.maxHeight = q_content.scrollHeight + "px";
        }else{
            q_content.style.maxHeight = 0;
        }
    });
});