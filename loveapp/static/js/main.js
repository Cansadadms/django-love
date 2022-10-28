function manipula_texto(){
    let txt = document.getElementById('id_cnpj')
    console.log(txt.value)
}

function regex_cnpj(evento){
    const padrao = /[0-9]/
    var tecla = evento.key
    if(!padrao.test(tecla)){
        return evento.preventDefault()
    }
    let txt = document.getElementById('id_cnpj')
    if(txt.value.length==2){
        txt.value += "."
    }
    if(txt.value.length==6){
        txt.value += "/"
    }
    if(txt.value.length==11){
        txt.value += "-"
    }

    console.log(tecla)
} 

function regex_nomeloja(evento){
    const padrao = /[a-z]/
    var tecla = evento.key
    if(!padrao.test(tecla)){
        return evento.preventDefault()
    }
    console.log(tecla)
}

function regex_email(evento){
    const padrao = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/gi
    var tecla = evento.key
    if(!padrao.test(tecla)){
        return evento.preventDefault()
    }
    console.log(tecla)

}