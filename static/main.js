function copyFunction() {
    /* Get the text field */
    var copyText = document.getElementById("myURL");
    console.log(copyText)
  
    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */
}