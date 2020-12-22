const productGroups = {
    "beverage": "نوشیدنی",
    "food": "خوردنی",
    "cloth": "پوشیدنی"
  };
  
  products = [
    {
        id: 101,
        name: 'pr_101',
        picPath: '../static/picture/pr_101.jpeg',
        price: 10100,
        groupId: 'beverage'
    },
    {
        id: 102,
        name: 'pr_102',
        picPath: '../static/picture/pr_102.jpeg',
        price: 10200,
        groupId: 'beverage'
    },
    {
        id: 103,
        name: 'pr_103',
        picPath: '../static/picture/pr_103.jpeg',
        price: 10300,
        groupId: 'food'
    },
    {
        id: 104,
        name: 'pr_104',
        picPath: '../static/picture/pr_104.jpeg',
        price: 10400,
        groupId: 'cloth'
    },
    {
        id: 105,
        name: 'pr_105',
        picPath: '../static/picture/pr_105.jpeg',
        price: 10500,
        groupId: 'beverage'
    },
    {
        id: 106,
        name: 'pr_106',
        picPath: '../static/picture/pr_106.jpeg',
        price: 10600,
        groupId: 'food'
    },
    {
        id: 107,
        name: 'pr_107',
        picPath: '../static/picture/pr_107.jpeg',
        price: 10700,
        groupId: 'food'
    },
    {
        id: 108,
        name: 'pr_108',
        picPath: '../static/picture/pr_108.jpeg',
        price: 10800,
        groupId: 'beverage'
    }
];


container = document.getElementById('container');
box = document.getElementById('sample_box')


for(pr of products){
    new_box = box.cloneNode('deep')
    new_box.addEventListener("click", function() {
        console.log(this.myObject);
    }, false);
    box_ch = new_box.children;
    info = box_ch[0].children;
    img = box_ch[1];

    img.src = pr.picPath
    img.alt = pr.name

    info[0].innerHTML = 'Item: ' + pr.name
    info[1].innerHTML = 'Price: ' + pr.price

    new_box.myObject = pr

    container.appendChild(new_box);

}

box.remove()


filler = document.createElement('div')
filler.className = "pr_box filler"
container.appendChild(filler);

filler = document.createElement('div')
filler.className = "pr_box filler"
container.appendChild(filler);


function click(obj){
    console.log(obj)
}