export function AjaxLikeCom(id){
    $.ajax({
        url : "/comment/" + id + "/like/",
        dataType: "json",
        success : function (data) {
                $('#like-count-' + id).text( data.like_count);
                if (data.liked){
                    likeBtn.css({ fill: 'red' });
                } else{
                    likeBtn.css({ fill: 'black' });
                }
                }
            });
        });