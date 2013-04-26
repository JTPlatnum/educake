$(document).ready(function(){
      $(function() {
    $( "#accordion" ).accordion({
        collapsible: true
      });
    });
    
    $('.checkbox').buttonset()

    $('.button').button()
    
    $(".favorites-icon").click(function(){
        icon = $(this)
        var className = $(this).attr('class');
        if(className.indexOf('icon-star-empty') >= 0)
        {
            icon.removeClass('icon-star-empty').addClass('icon-star selected')
        }
        else
        {
            icon.removeClass('icon-star selected').addClass('icon-star-empty')
        }
    })
})