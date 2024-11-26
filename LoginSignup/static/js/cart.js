document.addEventListener('DOMContentLoaded', function() {
    if (window.hasCartLoaded) return;
    window.hasCartLoaded = true;
    var updateBtns = document.getElementsByClassName('add-btn');
    var loginUrl = "{% url 'login' %}";
    if (updateBtns.length > 0) {
        console.log('updateBtns is not null and has items');
        for (var i = 0; i < updateBtns.length; i++) {
            updateBtns[i].addEventListener('click', function () {
                var productId = this.dataset.product;
                var action = this.dataset.action;
                console.log('productId:', productId, 'Action:', action);
                console.log('USER:', user)
                if(user === 'AnonymousUser'){
                    console.log('User is not Authenticated')
                    Swal.fire({
                        icon: "error",
                        title: "Oops...",
                        text: "Log In First!",
                        confirmButtonText: "Go to Login",
                    }).then((result) => {
                        if (result.isConfirmed) {
                            // Redirect to homepage
                            window.location.href = "/";
                        }
                    });
                } else {
                    updateUserOrder(productId,action)
                }
            });
        }
    } else {
        console.log('No update buttons found (updateBtns is null or empty).')
    }
    function updateUserOrder(productId, action){
        console.log('User is authenticated, sending data...')
        var url = '/shop/update_item/'

        fetch(url, {
            method: 'POST',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'productId':productId, 'action':action})
        })
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                console.log('Data:', data)
                location.reload()
            })
    }
});

