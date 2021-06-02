function previewFile(input, view_image){
    var file = $(input).get(0).files[0];
    if(file){
        var reader = new FileReader();
        reader.onload = function(){
            $(view_image).css("background-image","url(" + reader.result + ")");
        }
        reader.readAsDataURL(file);
        $('.upload__text').addClass('display-none');
    }
}