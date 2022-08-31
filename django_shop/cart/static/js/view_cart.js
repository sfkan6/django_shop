const token = document.querySelector('[name=csrfmiddlewaretoken]');


const buttonDecrement = document.querySelectorAll('.decrement');
const buttonIncrement = document.querySelectorAll('.increment');


buttonDecrement.forEach(function (item) {
    item.addEventListener('click', decrement);
})

buttonIncrement.forEach(function (item) {
    item.addEventListener('click', increment);
})


function decrement() {
    if (this.nextElementSibling.innerHTML > 1) {
        this.nextElementSibling.innerHTML--;

        const formData = new FormData();
        formData.append('product_id', this.dataset.id);

        fetch('decrement/', {
            method: 'POST',
            headers: {'X-CSRFToken': token.value},
            body: formData,
        });
    }

}

function increment() {
    this.previousElementSibling.innerHTML++;

    const formData = new FormData();
    formData.append('product_id', this.dataset.id);

    fetch('increment/', {
        method: 'POST',
        headers: {'X-CSRFToken': token.value},
        body: formData,
    })
}


function selectAll(elem) {
    const checks = document.querySelectorAll('.check');
    let sum = 0;

    if (elem.checked){
        const prices = document.querySelectorAll('.price');
        const quantity = document.querySelectorAll('.quantity');
        for (var i = 0; i < checks.length; i++){
            checks[i].checked = true;
            sum += parseFloat(prices[i].innerHTML) * parseFloat(quantity[i].innerHTML);
        }
    }
    else{
        for (var i = 0; i < checks.length; i++){
            checks[i].checked = false;
        }
    }

    document.querySelector('.order_price').innerHTML = sum;
}


function makeOrder(elem) {
    const checks = document.querySelectorAll('.check:checked');

    if (checks.length){
        body = String(checks[0].dataset.id);
        for (var i = 1; i < checks.length; i++){
            body += ',' + checks[i].dataset.id;
        }
        elem.parentElement.action += '?id_products=' + body;
        elem.parentElement.submit();
    }
}


function orderSum(elem) {
    const orderPrice = document.querySelector('.order_price');
    const sum = parseFloat(orderPrice.innerHTML);
    const price = parseFloat(elem.parentElement.querySelector('.price').innerHTML);
    const quantity = parseFloat(elem.parentElement.querySelector('.quantity').innerHTML);

    if (elem.checked) {
        orderPrice.innerHTML = sum + (price * quantity);
    } else {
        orderPrice.innerHTML = sum - (price * quantity);
    }
}

const buttonRemove = document.querySelectorAll('.remove');

buttonRemove.forEach(function (item) {
    item.addEventListener('click', remove);
})

function remove() {
    const formData = new FormData();
    formData.append('product_id', this.dataset.id);

    fetch('remove/', {
        method: 'POST',
        headers: {'X-CSRFToken': token.value},
        body: formData,
    });

    this.parentElement.remove();
}
