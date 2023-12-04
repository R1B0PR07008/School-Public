let key1 = 0;
let key2 = 0;

screenX = window.innerWidth
screenY = window.innerHeight

let song;
let img;
let vid1;
let vid2;

let playing = true;

let toggle1 = false;
let toggle2 = false;

function setup() {
  createCanvas(screenX, screenY);

  img = loadImage('./img/img.png')
  song = loadSound('./sound/osng.mp3')

  vid1 = createVideo('./video/Earth_render.mp4')
  vid2 = createVideo('./video/galaxy_render.mp4')
}

document.addEventListener('keydown', (event)=> {    
  console.log(event); // all event related info
  console.log(event.type);
  console.log(event.key);
  console.log(event.code);

  if (event.key == 'a') {
    document.getElementById('div1-submit-1').click();
    if (key1 == 0) {
      song.loop();
      vid1.time(0);
      key1 = 1;
    } else if (key1==1) {
      song.stop();
      key1 = 0
    }
    console.log('key1 = '+key1)
  } else if (event.key == 'd') {
    document.getElementById('div1-submit-2').click();
    if (key2 == 0) {
      song.loop();
      vid2.time(0);
      key2 = 1;
    } else if (key2==1) {
      song.stop();
      key2 = 0
    }console.log('key2 = '+key2)
  } else {
  }
});

function draw() {
  background(img)
  
  if (key1 == 1) {
    background(img)
    
    if (vid1.time() >= 5.0) {
      vid1.pause();
      let img1 = vid1.get();
      image(img1,0,0)
    }else {
      vid1.play();
      let img1 = vid1.get();
      image(img1,0,0)
    }

    console.log(vid1.time())

    playing = !playing;
  } else if (key2 == 1) {
    background(img);

    if (vid2.time() >= 4.4) {
      vid2.pause();
      let img1 = vid2.get();
      image(img1,0,0)
    } else {
      vid2.play();
      let img1 = vid2.get();
      image(img1,0,0)
    }

    console.log(vid2.time())

    playing = !playing;
  } else {
    vid1.hide();
    vid2.hide();
  }

}