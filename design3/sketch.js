let btn1,btn2,btn3,btn4,btn5,btn6 = 0;

function toggle(btn) {
    if (btn == '1') {
        if (btn1 == 1) {
            btn1 = 0
        } else {
            btn1 = 1
        }
    }else if (btn == '2') {
        if (btn2 == 1) {
            btn2 = 0
        } else {
            btn2 = 1
        }
    }else if (btn == '3') {
        if (btn3 == 1) {
            btn3 = 0
        } else {
            btn3 = 1
        }
    }else if (btn == '4') {
        if (btn4 == 1) {
            btn4 = 0
        } else {
            btn4 = 1
        }
    }else if (btn == '5') {
        if (btn5 == 1) {
            btn5 = 0
        } else {
            btn5 = 1
        }
    }else if (btn == '6') {
        if (btn6 == 1) {
            btn6 = 0
        } else {
            btn6 = 1
        }
    }

    console.log(btn1,btn2,btn3,btn4,btn5,btn6, " daoiwjd", btn);
}

//! p5.js sound

let song1;
let song2;
let song3;
let song4;
let song5;
let song6;

let file1 ='./sounds/bass-loops-003-with-drums-long-loop-120-bpm-24371.mp3';
let file2 ='./sounds/bass-loops-006-with-drums-long-loop-120-bpm-6111.mp3';
let file3 ='./sounds/layered-snare_A_minor.wav';
let file4 ='./sounds/powerful-electric-guitar-notes-uptempo-loop_128bpm_B_major.wav';
let file5 ='./sounds/short-bass.wav';
let file6 ='./sounds/sunflower-street-drumloop-85bpm-163900.mp3';

// the code that handles the file input that doesn't curretly work.

// if (document.getElementById('files1').files.length == 1) {
//     file1 = document.getElementById('files1').files
// } else {
//     file1 = ['./sounds/bass-loops-003-with-drums-long-loop-120-bpm-24371.mp3', 1]
// }
// if (document.getElementById('files2').files.length == 1) {
//     file2 = document.getElementById('files1').files
// } else {
//     file2 = ['./sounds/bass-loops-006-with-drums-long-loop-120-bpm-6111.mp3', 1]
// }
// if (document.getElementById('files3').files.length == 1) {
//     file3 = document.getElementById('files1').files
// } else {
//     file3 = ['./sounds/layered-snare_A_minor.wav', 1]
// }
// if (document.getElementById('files4').files.length == 1) {
//     file4 = document.getElementById('files1').files
// } else {
//     file4 = ['./sounds/powerful-electric-guitar-notes-uptempo-loop_128bpm_B_major.wav', 1]
// }
// if (document.getElementById('files5').files.length == 1) {
//     file5 = document.getElementById('files1').files
// } else {
//     file5 = ['./sounds/short-bass.wav', 1]
// }
// if (document.getElementById('files6').files.length == 1) {
//     file6 = document.getElementById('files1').files
// } else {
//     file6 = ['./sounds/sunflower-street-drumloop-85bpm-163900.mp3', 1]
// }

// function loadFiles() {
//     if (document.getElementById('files1').files.length == 1) {
//         song1.pause();
//         file1 = document.getElementById('files1').files
//         preload();
//     } else {
//         file1 = ['./sounds/bass-loops-003-with-drums-long-loop-120-bpm-24371.mp3', 1]
//     }
//     if (document.getElementById('files2').files.length == 1) {
//         song2.pause();
//         file2 = document.getElementById('files1').files
//         preload();
//     } else {
//         file2 = ['./sounds/bass-loops-006-with-drums-long-loop-120-bpm-6111.mp3', 1]
//     }
//     if (document.getElementById('files3').files.length == 1) {
//         song3.pause();
//         file3 = document.getElementById('files1').files
//         preload();
//     } else {
//         file3 = ['./sounds/layered-snare_A_minor.wav', 1]
//     }
//     if (document.getElementById('files4').files.length == 1) {
//         song4.pause();
//         file4 = document.getElementById('files1').files
//         preload();
//     } else {
//         file4 = ['./sounds/powerful-electric-guitar-notes-uptempo-loop_128bpm_B_major.wav', 1]
//     }
//     if (document.getElementById('files5').files.length == 1) {
//         song5.pause();
//         file5 = document.getElementById('files1').files
//         preload();
//     } else {
//         file5 = ['./sounds/short-bass.wav', 1]
//     }
//     if (document.getElementById('files6').files.length == 1) {
//         song6.pause();
//         file6 = document.getElementById('files1').files
//         preload();
//     } else {
//         file6 = ['./sounds/sunflower-street-drumloop-85bpm-163900.mp3', 1]
//     }
// }

function preload() {
    song1 = loadSound(file1[0]+'');
    song2 = loadSound(file2[0]+'');
    song3 = loadSound(file3[0]+'');
    song4 = loadSound(file4[0]+'');
    song5 = loadSound(file5[0]+'');
    song6 = loadSound(file6[0]+'');
}

function setup() {

    if (btn1 == 1) {
        song1.pause();
        song1.loop();
        console.log("playing sound!!")
    }else {
        song1.pause();
        console.log("not playing sound")
    } 
    if (btn2 == 1) {
        song2.pause();
        song2.loop();
        console.log("playing sound!!")
    } else {
        song2.pause();
        console.log("not playing sound")
    } 
    if (btn3 == 1) {
        song3.pause();
        song3.loop();
        console.log("playing sound!!")
    } else {
        song3.pause();
        console.log("not playing sound")
    } 
    if (btn4 == 1) {
        song4.pause();
        song4.loop();
        console.log("playing sound!!")
    } else {
        song4.pause();
        console.log("not playing sound")
    } 
    if (btn5 == 1) {
        song5.pause();
        song5.loop();
        console.log("playing sound!!")
    } else {
        song5.pause();
        console.log("not playing sound")
    } 
    if (btn6 == 1) {
        song6.pause();
        song6.loop();
        console.log("playing sound!!")
    } else {
        song6.pause();
        console.log("not playing sound")
    } 
}