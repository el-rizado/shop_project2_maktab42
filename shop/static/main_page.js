
box = document.getElementById('sample_box')
new_box = box.cloneNode('deep')
new_box = document.getElementById('sample_box');
new_box.addEventListener("click", function() {
        window.location.replace("/myProduct/api/v1/resources/products/all")
    }, false);

function click(obj){
    window.location.replace("order")
}