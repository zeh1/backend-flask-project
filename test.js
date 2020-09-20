


x = {
    y: function() {
        console.log(5)
        return {
            z: function() {
                console.log(6)
            }
        }
    }
}

x.y().z()