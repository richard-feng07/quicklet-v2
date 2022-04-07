document.addEventListener("DOMContentLoaded", function(){
    get.addEventListener('click',function(){
        SendStatement();
    })
})

function SendStatement(){
    var statement = document.getElementById("term").value;
    alert(statement)
}