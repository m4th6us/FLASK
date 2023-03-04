function MudaCor(id){
    let count = 0
    let btn = document.getElementById(`${id}`)

    btn.onclick = function () {
        count ++;

        console.log(count)
        if (count === 1){
            btn.style.backgroundColor = '#5f2cb8'
        }
        else if (count === 2){
            btn.style.backgroundColor = ''
        }
        else{
            count = 0
        }
    }
}

function Registrar(){
    
}