console.log('Hello World!')
var updateBtns = document.getElementsByClassName('add-btn')

for(var i=0; i < updateBtns.length; i++) {
    console.log('Hello World')
    updateBtns[i].addEventListener('click', function (){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)

        console.log('USER:', user)
        if(user === 'AnonymousUser'){
            console.log('User is not Authenticated')
        } else {
            console.log('User is authenticated, sending data...')
        }
    })
}