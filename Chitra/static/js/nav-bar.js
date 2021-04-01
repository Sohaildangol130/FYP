var id = $('.user_id').val();
$.ajax({
    type: "POST",
    url: "/auth/header",
    data: {'id': id},
    datatype: 'json',
    success: (data) => {
        $('.nav-item--profile').css("background-image", "url(/media/"+data.user_image+")")
    }
})

const toggle = (clicked_item, class_name, toggle_class) => {
    $(clicked_item).click(function(){
        $(class_name).toggleClass(toggle_class);
    })
}

toggle('.nav-item--mobile-burger', '.header-nav-bar-mobile', 'header-nav-bar-mobile--display');
toggle('.shopping-cart', '.nav-item--checkout-box', 'display-block');
toggle('.profile-btn', '.nav-item--profile-box', 'display-block');

$('.nav-item').click(function(){
    for (i=0; i<$('.nav-item').length; i++){
        $('.nav-item')[i].dataset["click"]=false;
    }
    console.log($(this)[0])
    $(this).dataset["click"] = true;
    // console.log($(this).closest('.header__nav-bar--all-nav-items--item').find('.nav-item--checkout-box'))
    // var a=$(this).closest('.all-nav-items__user').find('li');
    // for (i=0;i<a.length;i++){
    //     a[i].dataset["click"] = false;
    // }
    // $(this).dataset["click"] = true;
    // for (i=0;i<a.length;i++){
    //     if (a[i].dataset["click"] == true){

    //     }
    // }
})

const display_checkout_items = () => {
    $.ajax({
        type: "POST",
        url: "/checkout/show",
        data: {'items': items},
        datatype: 'json',
        success: (data) => {
            if(items.includes($(".post__buy").data("id"))){
                $('.post__buy p').text("Added to cart!!");
            }
            $('.nav-item--checkout-box__container__all-checkout-items').empty();
            $.each(data, (key, value)=>{
                value.forEach(element => {
                    $('.nav-item--checkout-box__container__all-checkout-items').prepend(
                        `<div class='nav-item--checkout-box__container__all-checkout-items--checkout-item col-lg-12'><div class='row align-items-center'><div class='col-4'><a href="/posts/`+element.post_id+`"><img class='checkout-item--photo' src='../media/`+element.img_url+`'></a></div><div class='col-8'><a href="/posts/`+element.post_id+`"><h6 class='checkout-item--name'>`+element.post_title+`</h6></a><p class='checkout-item--price'>Rs `+element.price+`</p></div></div></div>` 
                    );
                });
            })
            
        }
    })
}

let items = Cookies.get("items") == undefined ? []:JSON.parse(Cookies.get("items"));

if(items.length > 0){
    $('.checkout--total-items-number').removeClass('display-none');
    $('.checkout--total-items-number p').text(items.length);
}

display_checkout_items();

$(".post__buy").on('click',(e)=>{
    if ($(".post__buy").data("id")){
        e.preventDefault(); 
        if (!items.includes($(".post__buy").data("id"))){
            items.push($(".post__buy").data("id"));
            Cookies.set("items", items)
            $('.checkout--total-items-number').removeClass('display-none');
            $('.checkout--total-items-number p').text(items.length);
        }

        display_checkout_items();
        $('.post__buy p').text("Added to cart!!")
        }
})

// nav-buttons working only one at a time

// $('.nav-item').click(function(){
//     var a = $(".nav-item");
//     for (var i=0; i<a.length; i++){  
//         // console.log(a[i].getAttribute("data-click"));  
//         a[i].setAttribute("data-click","false");
//         // console.log(a[i].getAttribute("data-click"));  
//     }
//     $(this).attr("data-click","true");
//      console.log($(this).attr("data-click"));  
//     for (var i = 0; i<a.length; i++){
//         if (a[i].getAttribute("data-click")==="true"){
//             console.log($(this).parent().find('.nav-box'));
//             var c = $(this).parent().find('.nav-box');
//             $(c).addClass('display-block');
//         }
//         else{  
//             $(this).parent().find('.nav-box').removeClass('display-block');
//         }
//     }
// })