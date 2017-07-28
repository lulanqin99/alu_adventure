var names = ['Kaiwen', 'Vincent','Kayla','Margaret'];
var favFoods = {'Kaiwen': 'water', 'Vincent': 'coffee', 'Kayla':'pasta','Margaret' :'fruits'}


$('body').css({'background':'red'})

$('p').css({'background':'black', 'font-size': '150px','color': 'white'})
function sayHi() {
  $('#hi').css({'color' : 'blue'});
}

function growBox() {
  var newSize = $('#box').width() + 100;
  $('#box').animate({'width':newSize,'height':newSize}, 10000);
}

function shrinkB() {
  $('#box').animate({'width':20,'height':20});
}

function moveRight() {
  var newLeft = $('#box').position().left + 100;
  $('#box').animate({'left':newLeft})
}

function moveLeft() {
  var newRight = $('#box').position().left - 100;
  $('#box').animate({'left':newRight})
}

function moveDown() {
  var newUp = $('#box').position().top + 100;
  $('#box').animate({'top':newUp})
}

function moveUp() {
  var newDown = $('#box').position().top - 100;
  $('#box').animate({'top':newDown})
}

function handleKeyDown(event) {
  console.log(event['keyCode']);
  if (event['keyCode'] === 39) {
    moveRight();
  }
}



$('#grow').hover(growBox);
$('#hi').click(sayHi);
$('#shrink').click(shrinkB);
$('#moveRight').click(moveRight);
$('#moveLeft').click(moveLeft);
$('#moveDown').click(moveDown);
$('#moveUp').click(moveUp);
$(window).keydown(handleKeyDown);

//fadeIn, fadeOut, slideUp/Down

//append - add something to end
//prepend - add something to begining
