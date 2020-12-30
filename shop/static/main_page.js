
box = document.getElementById('sample_box')
new_box = box.cloneNode('deep')
new_box = document.getElementById('sample_box');
new_box.addEventListener("click", function() {
        console.log(this)
        // window.location.replace("/api/product")
    }, false);

function click(obj){
    console.log(obj)
    // window.location.replace("order")
}