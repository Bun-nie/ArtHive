// document.addEventListener('DOMContentLoaded', function() {
//     if (window.hasCartLoaded) return;
//     window.hasCartLoaded = true;
//     var updateBtns = document.getElementsByClassName('add-btn');
//     var loginUrl = "{% url 'login' %}";
//     if (updateBtns.length > 0) {
//         console.log('updateBtns is not null and has items');
//         for (var i = 0; i < updateBtns.length; i++) {
//             updateBtns[i].addEventListener('click', function () {
//                 var productId = this.dataset.product;
//                 var action = this.dataset.action;
//                 console.log('productId:', productId, 'Action:', action);
//                 console.log('USER:', user)
//                 if(user === 'AnonymousUser'){
//                     console.log('User is not Authenticated')
//                     Swal.fire({
//                         icon: "error",
//                         title: "Oops...",
//                         text: "Log In First!",
//                         confirmButtonText: "Go to Login",
//                         confirmButtonColor: '#FED154',
//                         allowEscapeKey: true,
//                         customClass: 'swal-background',
//                     }).then((result) => {
//                         if (result.isConfirmed) {
//                             window.location.href = "/";
//                         }
//                     });
//                 } else {
//                     updateUserOrder(productId,action)
//                 }
//             });
//         }
//     } else {
//         console.log('No update buttons found (updateBtns is null or empty).')
//     }
//     function updateUserOrder(productId, action){
//         console.log('User is authenticated, sending data...')
//         var url = '/shop/update_item/'
//
//         fetch(url, {
//             method: 'POST',
//             headers:{
//                 'Content-Type':'application/json',
//                 'X-CSRFToken':csrftoken,
//             },
//             body:JSON.stringify({'productId':productId, 'action':action})
//         })
//             .then((response) => {
//                 return response.json();
//             })
//             .then((data) => {
//                 console.log('Data:', data)
//                 location.reload()
//             })
//     }
// });


// document.addEventListener('DOMContentLoaded', function() {
//     if (window.hasCartLoaded) return;
//     window.hasCartLoaded = true;
//
//     var updateBtns = document.getElementsByClassName('add-btn');
//     var buyNowBtns = document.getElementsByClassName('buy-now-btn');
//     var loginUrl = "{% url 'login' %}";
//     var checkoutUrl = "http://127.0.0.1:8000/shop/checkout/";
//
//     if (updateBtns.length > 0) {
//         console.log('updateBtns is not null and has items');
//         for (var i = 0; i < updateBtns.length; i++) {
//             updateBtns[i].addEventListener('click', function () {
//                 var productId = this.dataset.product;
//                 var action = this.dataset.action;
//                 console.log('productId:', productId, 'Action:', action);
//                 console.log('USER:', user)
//                 if(user === 'AnonymousUser'){
//                     console.log('User is not Authenticated')
//                     Swal.fire({
//                         icon: "error",
//                         title: "Oops...",
//                         text: "Log In First!",
//                         confirmButtonText: "Go to Login",
//                         confirmButtonColor: '#FED154',
//                         allowEscapeKey: true,
//                         customClass: 'swal-background',
//                     }).then((result) => {
//                         if (result.isConfirmed) {
//                             window.location.href = "/";
//                         }
//                     });
//                 } else {
//                     updateUserOrder(productId,action)
//                 }
//             });
//         }
//     }
//
//     if (buyNowBtns.length > 0) {
//         for (var i = 0; i < buyNowBtns.length; i++) {
//             buyNowBtns[i].addEventListener('click', function () {
//                 var productId = this.dataset.product;
//                 var action = this.dataset.action;
//
//                 if (user === 'AnonymousUser') {
//                     console.log('User is not authenticated');
//                     Swal.fire({
//                         icon: "error",
//                         title: "Oops...",
//                         text: "Log In First!",
//                         confirmButtonText: "Go to Login",
//                         confirmButtonColor: '#FED154',
//                         allowEscapeKey: true,
//                         customClass: 'swal-background',
//                     }).then((result) => {
//                         if (result.isConfirmed) {
//                             window.location.href = loginUrl;
//                         }
//                     });
//                 } else {
//                     updateUserOrder(productId, action).then(() => {
//                         window.location.href = checkoutUrl;
//                     });
//                 }
//             });
//         }
//     }
//
//     function updateUserOrder(productId, action){
//         console.log('User is authenticated, sending data...')
//         var url = '/shop/update_item/'
//
//         fetch(url, {
//             method: 'POST',
//             headers:{
//                 'Content-Type':'application/json',
//                 'X-CSRFToken':csrftoken,
//             },
//             body:JSON.stringify({'productId':productId, 'action':action})
//         })
//             .then((response) => {
//                 return response.json();
//             })
//             .then((data) => {
//                 console.log('Data:', data)
//                 location.reload()
//             })
//     }
// });

document.addEventListener('DOMContentLoaded', function() {
    if (window.hasCartLoaded) return;
    window.hasCartLoaded = true;

    var updateBtns = document.getElementsByClassName('add-btn');
    var buyNowBtns = document.getElementsByClassName('buy-now-btn');
    var loginUrl = "{% url 'login' %}";
    var checkoutUrl = "http://127.0.0.1:8000/shop/checkout/";

    function getCSRFToken() {
        var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        if (!csrfToken) {
            csrfToken = getCookie('csrftoken');
        }
        return csrfToken;
    }

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    if (updateBtns.length > 0) {
        console.log('updateBtns is not null and has items');
        for (var i = 0; i < updateBtns.length; i++) {
            updateBtns[i].addEventListener('click', function () {
                var productId = this.dataset.product;
                var action = this.dataset.action;
                console.log('productId:', productId, 'Action:', action);
                console.log('USER:', user)

                if(user === 'AnonymousUser'){
                    console.log('User is not Authenticated');
                    Swal.fire({
                        icon: "error",
                        title: "Oops...",
                        text: "Log In First!",
                        confirmButtonText: "Go to Login",
                        confirmButtonColor: '#FED154',
                        allowEscapeKey: true,
                        customClass: 'swal-background',
                    }).then((result) => {
                        if (result.isConfirmed) {
                            window.location.href = loginUrl;
                        }
                    });
                } else {
                    // Proceed with adding to cart
                    console.log('Updating user order...');
                    updateUserOrder(productId, action).then((data) => {
                        console.log('Item added to cart:', data);
                        location.reload();
                    }).catch(error => {
                        console.error('Error adding item to cart:', error);
                    });
                }
            });
        }
    }

    // Buy Now Button
    if (buyNowBtns.length > 0) {
        for (var i = 0; i < buyNowBtns.length; i++) {
            buyNowBtns[i].addEventListener('click', function () {
                var productId = this.dataset.product;
                var action = this.dataset.action;

                if (user === 'AnonymousUser') {
                    console.log('User is not authenticated');
                    Swal.fire({
                        icon: "error",
                        title: "Oops...",
                        text: "Log In First!",
                        confirmButtonText: "Go to Login",
                        confirmButtonColor: '#FED154',
                        allowEscapeKey: true,
                        customClass: 'swal-background',
                    }).then((result) => {
                        if (result.isConfirmed) {
                            window.location.href = loginUrl;
                        }
                    });
                } else {
                    updateUserOrder(productId, action).then((data) => {
                        console.log('Item added to cart, redirecting to checkout...', data);
                        window.location.href = checkoutUrl;
                    }).catch(error => {
                        console.error('Error adding item to cart:', error);
                    });
                }
            });
        }
    }

    function updateUserOrder(productId, action) {
        console.log('User is authenticated, sending data...');
        var url = '/shop/update_item/';
        var csrfToken = getCSRFToken();

        return fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({ 'productId': productId, 'action': action })
        })
        .then((response) => {
            console.log('Response status:', response.status);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then((data) => {
            console.log('Data:', data);
            return data;
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
});


