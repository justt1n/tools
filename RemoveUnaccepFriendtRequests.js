var btns  = document.querySelectorAll('div[aria-label="Hủy yêu cầu"]');

btns.forEach(function(btn) {

    var clickEvent = new Event('click', {
      'bubbles': true, 
      'cancelable': true 
    });
  
    btn.dispatchEvent(clickEvent);
});