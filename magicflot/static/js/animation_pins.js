window.onload = function() {
    let add_animation = document.getElementsByClassName('add_animation');
  
    for (let ia = 0; ia < add_animation.length; ia++) {
        if (add_animation[ia].classList.contains('technical')) {
            add_animation[ia].classList.add('roll_t');
        } 
        else if (add_animation[ia].classList.contains('general')) {
            add_animation[ia].classList.add('roll_h');
        } 
    }
}