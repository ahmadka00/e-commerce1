$(document).on('click', '#add-button', function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '{% url "basket:add_basket" %}',
        data: {
            product_id: $('#add-button').val(),
            csrfmiddlewaretoken: '{{ csrf_token }}',
            action: 'post'


        },
        success: function(json){
            console.log(json)
        },

        error: function(xhr, errmsg, err){

        }


    });
})