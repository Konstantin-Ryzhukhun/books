// var hashTags = new Bloodhound({
//     datumTokenizer: Bloodhound.tokenizers.obj.whitespace('q'),
//     queryTokenizer: Bloodhound.tokenizers.whitespace,
//     prefetch: '/hashtag.json?q=%QUERY',
//     remote: {
//     url: '/hashtag.json?q=%QUERY',
//     wildcard: '%QUERY'
//     }
// });
var hashTags = new Bloodhound({
    datumTokenizer: Bloodhound.tokenizers.obj.whitespace('q'),
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    prefetch: '/hashtag.json?q=%QUERY',
    remote: {
        url: '/hashtag.json?q=%QUERY&page=%PAGE',
        wildcard: '%QUERY',
        replace: function (url, query) {
            var page = Math.ceil(query.length / 30); // Вычисляем номер страницы пагинации
            return url.replace('%QUERY', query).replace('%PAGE', page);
        }
    }
});
hashTags.initialize(); // Инициализируем Bloodhound

// $('.search-tag-query').typeahead({
//     hint: true,
//     highlight: true,
//     minLength:1,
//     // limit: 30,
// },

//     {
//     name: 'hashTags',
//     display: 'q',
//     // displayKey: 'count',
//     source: hashTags.ttAdapter(),
//     templates: {
//     empty: '<div class="search_nofing">Ничего не найдено</div>',
//     //header1: "<div><ul>",
//     footer: "</div>",

//         suggestion: function (data) {

//             // console.log(data.old_price)

//             rub1='<svg height="11" style="fill: #000;    margin-left: 3px;" version="1.1" viewBox="0 0 510.127 510.127" width="11" x="0px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" y="0px"><g><g><path d="M34.786,428.963h81.158v69.572c0,3.385,1.083,6.156,3.262,8.322c2.173,2.18,4.951,3.27,8.335,3.27h60.502c3.14,0,5.857-1.09,8.152-3.27c2.295-2.166,3.439-4.938,3.439-8.322v-69.572h182.964c3.377,0,6.156-1.076,8.334-3.256                            c2.18-2.178,3.262-4.951,3.262-8.336v-46.377c0-3.365-1.082-6.156-3.262-8.322c-2.172-2.18-4.957-3.27-8.334-3.27H199.628v-42.75                            h123.184c48.305,0,87.73-14.719,118.293-44.199c30.551-29.449,45.834-67.49,45.834-114.125c0-46.604-15.283-84.646-45.834-114.125                            C410.548,14.749,371.116,0,322.812,0H127.535c-3.385,0-6.157,1.089-8.335,3.256c-2.173,2.179-3.262,4.969-3.262,8.335v227.896                            H34.786c-3.384,0-6.157,1.145-8.335,3.439c-2.172,2.295-3.262,5.012-3.262,8.151v53.978c0,3.385,1.083,6.158,3.262,8.336                            c2.179,2.18,4.945,3.256,8.335,3.256h81.158v42.754H34.786c-3.384,0-6.157,1.09-8.335,3.27c-2.172,2.166-3.262,4.951-3.262,8.322                            v46.377c0,3.385,1.083,6.158,3.262,8.336C28.629,427.887,31.401,428.963,34.786,428.963z M199.628,77.179h115.938                            c25.6,0,46.248,7.485,61.953,22.46c15.697,14.976,23.549,34.547,23.549,58.691c0,24.156-7.852,43.733-23.549,58.691                            c-15.705,14.988-36.354,22.473-61.953,22.473H199.628V77.179z"></path></g></g></svg>'
//             rub2='<svg height="9" style="fill: #101010;    margin-left: 3px;" version="1.1" viewBox="0 0 510.127 510.127" width="9" x="0px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" y="0px"><g><g><path d="M34.786,428.963h81.158v69.572c0,3.385,1.083,6.156,3.262,8.322c2.173,2.18,4.951,3.27,8.335,3.27h60.502c3.14,0,5.857-1.09,8.152-3.27c2.295-2.166,3.439-4.938,3.439-8.322v-69.572h182.964c3.377,0,6.156-1.076,8.334-3.256                            c2.18-2.178,3.262-4.951,3.262-8.336v-46.377c0-3.365-1.082-6.156-3.262-8.322c-2.172-2.18-4.957-3.27-8.334-3.27H199.628v-42.75                            h123.184c48.305,0,87.73-14.719,118.293-44.199c30.551-29.449,45.834-67.49,45.834-114.125c0-46.604-15.283-84.646-45.834-114.125                            C410.548,14.749,371.116,0,322.812,0H127.535c-3.385,0-6.157,1.089-8.335,3.256c-2.173,2.179-3.262,4.969-3.262,8.335v227.896                            H34.786c-3.384,0-6.157,1.145-8.335,3.439c-2.172,2.295-3.262,5.012-3.262,8.151v53.978c0,3.385,1.083,6.158,3.262,8.336                            c2.179,2.18,4.945,3.256,8.335,3.256h81.158v42.754H34.786c-3.384,0-6.157,1.09-8.335,3.27c-2.172,2.166-3.262,4.951-3.262,8.322                            v46.377c0,3.385,1.083,6.158,3.262,8.336C28.629,427.887,31.401,428.963,34.786,428.963z M199.628,77.179h115.938                            c25.6,0,46.248,7.485,61.953,22.46c15.697,14.976,23.549,34.547,23.549,58.691c0,24.156-7.852,43.733-23.549,58.691                            c-15.705,14.988-36.354,22.473-61.953,22.473H199.628V77.179z"></path></g></g></svg>'

//             if (data.old_price == '') {
//                 old_price = ''
//             }else{
//                 old_price = '<del aria-hidden="true"><span class="woocommerce-Price-amount amount"><bdi>' + data.old_price + rub2 + '</bdi></span></del>'
//             }


//             // nike

//             if (data.image == ''){
//                 image = '<img class="search-image" style="    border-radius: 0;" src="/media/modules/seach/mimo.png">'
//             }else{
//                 image = '<img class="search-image" src="'+data.image+'">'
//             }

//             if (data.price == null){
//                 price = '<div class="noprice_search">Товар в наличии, цену уточняйте</div>'
//             }else{
//                 price = '<ins><span class="woocommerce-Price-amount amount"><bdi>'+data.price+rub1+'</bdi></span></ins>'
//             }

//             return '<div svm_modal_name="' + data.q + '" svm_variants_tovar_id="' + data.id + '" svm_variants_tovar_url="/tovar/' + data.url + '/"><a svm_modal_full_triger href="/tovar/' + data.url + '/">\
//             <div class="autocomplete-suggestion " data-index="0">\
//             <div class="autocomplete-suggestion-wrp " data-index="0">\
//             <div class="autocomplete-suggestion-wrp-l " data-index="0">\
//             '+image+'\
//             </div>\
//             <div class="autocomplete-suggestion-wrp-r" data-index="0">\
//             <div class="search-name">'+data.q+'</div>\
//             <span class="search-price">\
//             '+price+'\
//             '+old_price+'\
//             </span>\
//             </div>\
//             </div>\
//             </div></a></div>';
            

//         }
//     }
// });


var template;

$.ajax({
    url: 'template.html',
    async: false,
    success: function (data) {
        template = data;
    }
});

$('.search-tag-query').typeahead({
    hint: true,
    highlight: true,
    minLength: 1,
}, {
    name: 'hashTags',
    display: 'q',
    source: hashTags.ttAdapter(),
    templates: {
        empty: '<div class="search_nofing">Ничего не найдено</div>',
        suggestion: function (data) {
            var renderedTemplate = template.replace(/{{(.*?)}}/g, function (match, key) {
                return data[key] || '';
            });

            return renderedTemplate;
        }
    }
});
 
