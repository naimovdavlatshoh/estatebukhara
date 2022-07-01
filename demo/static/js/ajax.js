

$(function(){
    $('.addToFavourite').on('click', function() {
        let btn = $(this)
        let token = $('[name = csrfmiddlewaretoken').val()
        let url = btn.attr('data-url')
        let flatId = btn.attr('data-id')
        
        console.log('ok')
    
        $.ajax({
            url:url,
            type:'POST',
            data:{flatId},
            headers:{
                'X-CSRFToken':token
            },
            


            success: (data)=>{
                $('.cart_parent').load( ' .cart_child ')
                if(data == 'ok'){
                    btn.removeClass('btn-yellow')
                    btn.addClass('btn-red')

                    btn.html('Избранное')
                } else {
                    btn.addClass('btn-yellow')
                    btn.removeClass('btn-red')

                    btn.html('Избранное')
                }
                console.log('ok');
            },

            error: (msg)=> {
                console.log(msg)
            }
        })  
        
    })
})