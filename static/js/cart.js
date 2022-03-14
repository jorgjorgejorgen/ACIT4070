var updateBtns = document.getElementsByClassName('update-cart')

// legg til element i cart
for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var rideId = this.dataset.ride
        var action = this.dataset.action
        console.log('rideId:', rideId, 'Action:', action) // for å se action


// sjekk om bruker er logget inn
        console.log('USER:', user)
        if (user == 'AnonymousUser') {
            console.log('user not authenticated')
        }
        else {
            updateUserOrder(rideId, action)
        }
    })
}

// sende ordre til kurv
function updateUserOrder(rideId, action){
    console.log('')

    var url = '/update-ticket/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'rideId': rideId, 'action':action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)

        if (action == 'add') {
            location.href= 'cart';
        }

    })
}