function greeting() {
  $('#name').val();
  var username = $('#name').val();
  alert('Hello ' + username);
}

$('#submit').click(grade);


function grade() {
  var score = 0;
  var username = $('#name').val();
  var answer1 = $('#Q1').val();
  var answer2 = $('#Q2').val();
  var subject = $('[name=subject]:checked').val();


  if (answer1 === 'Sacramento' || answer1 === 'sacramento') {
    score++;
}
  if (answer2 === 'blue' || answer2 === 'purple' || answer2 === 'red') {
    score++;
  }

  alert('Hello ' + username + ', your score was: ' + score);
  alert('I cannot belive your fav subject is ' + subject);

}
