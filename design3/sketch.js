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

