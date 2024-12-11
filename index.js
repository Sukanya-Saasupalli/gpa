var grades = document.querySelectorAll(".grades-input");
var credits = document.querySelectorAll(".credits-input");
var data = document.querySelector("#submit");
var num=0, denom=0, result = 0;
var tc = document.getElementById("tc-cont");
var gr = document.getElementById("gpa-cont");

data.addEventListener("click",onclick);

function onclick(){

    if(denom>0 && num >0){
        num  = 0;
        denom = 0;
    }

    for(let i=0;i<grades.length;i++){
        if((grades[i].value) != "" || credits[i].value != ""){
            num += (Number(grades[i].value))*(Number(credits[i].value));
            denom += (Number(credits[i].value));
        }
    }

    var result = (num/denom);
    const fresult = result.toFixed(2);
    tc.innerHTML = denom;
    gr.innerHTML = fresult;

    result = 0;


}


