//FUNÇÃO DO SLIDE

var posi =0 // posição atual do slide

function slide(sentido){
    if (sentido == -1 && posi <2){ // puxa para esquerda
        posi++
        document.getElementById(posi-1).classList.remove('imgAtual')
    }
   else if (sentido == 1 && posi>0){ //puxa para direita
       posi--
       document.getElementById(posi+1).classList.remove('imgAtual')
    }
    document.getElementById(posi).classList.add('imgAtual')  
    document.getElementById("atual").style.marginLeft = -1040*posi+"px"
    //window.alert(posi)
}


//FUNÇÃO DO AUDIO

var musik = document.getElementById('musik');
var animacao = document.getElementById('audiowave');

musik.addEventListener("playing", function(){
    if (musik.paused){
        animacao.src = "icons/audio-wave.png";
    }else{
        animacao.src = "icons/audio-wave.gif";
    }
    
});
musik.addEventListener("pause", function(){
    if (musik.paused){
        animacao.src = "icons/audio-wave.png";
    }else{
        animacao.src = "icons/audio-wave.gif";
    }
    
}); 