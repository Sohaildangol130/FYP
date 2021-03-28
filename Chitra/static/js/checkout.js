const checkout = () => {
    $.ajax({
        type: "POST",
        url: "/checkout/show",
        data: {'items': items},
        datatype: 'json',
        success: (data) => {
            $('.input__all-posts').val(Cookies.get("items"))
            var price = 0;
            $.each(data, (key, value)=>{
                value.forEach(element => {
                    $('.checkout-items__container').prepend(
                        `<div class="container__single-item row" style="margin-top: 30px;">
                        <div class="single-item__image col-3">
                            <div class="image__container" style="width:100%; background-size: cover; background-position: center; height: 75px; background-image: url('/media/`+element.img_url+`')"></div>
                        </div>
                        <div class="col-6">
                            <div class="single-item__name"><a href="../posts/`+element.post_id+`"><h6>`+element.post_title+`</h6></a></div>
                            <div class="single-item__username"><a href="../profile/`+element.user.id+`"><p>`+element.user.first_name+` `+element.user.last_name+`</p></a></div>
                        </div>
                        <div class="single-item__price col-3">
                            <p style="text-align: right;">Rs `+element.price+`</p>
                        </div>
                        </div>`
                    );
                    price = price+ parseInt(element.price)
                });
                $('.total-price__price p').text("Rs "+price);
            })            
        }
    })
}

checkout();