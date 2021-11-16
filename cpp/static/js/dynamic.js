let target = document.querySelector("#dynamic");
function randomString(){
    let stringArr = ["CPP에 오신 것을 환영합니다."]
    let selectString = stringArr[0];
    let selectStringArr = selectString.split("");
    return selectStringArr;
}

function dynamic(randomArr){
    if(randomArr.length > 0){

    target.textContent += randomArr.shift();
    setTimeout(function(){
        dynamic(randomArr);
    }, 100);
    }else{
        setTimeout(resetTyping, 3000);
    }
}
dynamic(randomString());
function resetTyping(){
    target.textContent = "";
    dynamic(randomString());
}
