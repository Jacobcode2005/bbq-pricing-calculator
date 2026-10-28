// ==========================
// Index Page
// ==========================

// functions for the home page

function index(){
    const target_element = document.getElementById("new_orders")
    if (!target_element) 
        return;
    document.getElementById("new_orders").addEventListener("click", function(){window.location.href= "/new_order"});

    document.getElementById("past_orders").addEventListener("click", function(){window.location.href= "/past_order"});

    document.getElementById("edit_database").addEventListener("click", function(){window.location.href= "/edit_database"});
}
index()
// ==========================
// Display Order
// ==========================
/**
 * Builds and displays an order receipt using data returned by Flask.
 * Shared by the New Order and Past Orders pages.
 */
function display_order(order){
    const modal = document.getElementById("your_order")
    const modal_content = document.querySelector(".modal_content")  
        modal.style.display="flex"
       const order_number_p= document.createElement("p")
       order_number_p.textContent=`Order Number: ${order.order_number}| Number of People ${order.number_of_people}`
       modal_content.appendChild(order_number_p)
       // Create receipt entries for each selected meat and side.
       order.meats.forEach(function(meat){
            const meat_p = document.createElement("p")
                meat_p.textContent =`${meat.meatID.toUpperCase()}- Raw Amount: ${meat.raw_weight}
                 | Price ${meat.meat_total.toLocaleString("en-US", {
                style: "currency",
                 currency: "USD"
})}`
                modal_content.appendChild(meat_p)
            })
        order.sides.forEach(function(side){
            const side_p = document.createElement("p")
            side_p.textContent=`${side.sideID.toUpperCase()}- Number of Half Pans ${side.number_of_half}
             | Price ${side.side_total.toLocaleString("en-US", {
            style: "currency",
            currency: "USD"
})}`
            modal_content.appendChild(side_p)
             })
        const total_p = document.createElement("p")
        total_p.textContent=`Total Meat Cost ${order.meat_total.toLocaleString("en-US", {
    style: "currency",
    currency: "USD"
})}| Total Side Cost ${order.side_total.toLocaleString("en-US", {
    style: "currency",
    currency: "USD"
})} | Final Cost:${order.final_price.toLocaleString("en-US", {
    style: "currency",
    currency: "USD"
})}`
        modal_content.appendChild(total_p)
        
    }

// ==========================
// New Order Page
// ==========================

// functions for creating an order
function new_order(){
   const target_element = document.getElementById("new_return")
   const modal = document.getElementById("your_order")
   
   if(!target_element)
        return;
   
   const meat = []
    const side = []
    const reset_meats= document.getElementById("reset_meats")
    var x= document.getElementById("meats")
    var a = document.getElementById("sides")
   
   
    document.getElementById("new_return").addEventListener("click", function(){window.location.href= "/"});
   
    document.getElementById("meats").addEventListener("change",function(){
        
        var y= x.options[x.selectedIndex].value
        meat.push(y)
         const number_of_meats = meat.length
       // Limit each order to two different meat selections.
         if (number_of_meats == 2)
        x.disabled = true
       x.options[x.selectedIndex].disabled = true
       document.getElementById("selected_meats").textContent = meat});
      // Clear selected items and re-enable the dropdown options.
       document.getElementById("reset_meats").addEventListener("click", function(){
       document.getElementById("selected_meats").textContent = "" 
        x.disabled = false
        meat.length = 0
        for( const option of x.options)
            option.disabled= false
    })
       
       
        document.getElementById("sides").addEventListener("change", function(){
       
        var b = a.options[a.selectedIndex].value
        side.push(b)
        document.getElementById("sides").options[a.selectedIndex].disabled = true

        document.getElementById("selected_sides").textContent= side});
    document.getElementById("reset_sides").addEventListener("click", function(){
        document.getElementById("selected_sides").textContent =""
        a.disabled =  false
        side.length = 0
        for (const option of a.options)
            option.disabled=false
    })
  
   document.getElementById("close").addEventListener("click", function(){
        window.location.reload();

    })
   document.getElementById("submit_order").addEventListener("click", function(){
      const number_of_people_id = document.getElementById("number_of_people")
      const  number_of_people = number_of_people_id.valueAsNumber
      const o ={meat, side,number_of_people} 
     
    fetch("/submit_order", {method: 'POST',
            headers:{'Content-type': 'application/json'},
            body: JSON.stringify(o)
            
        })
    .then(response => response.json())
    .then(order => {    
        display_order(order)
    });
    
});

}
new_order()
// ==========================
// Past Orders Page
// ==========================

// functions for looking up orders
function past_order(){
    const target_element = document.getElementById("past_return")
    if(!target_element)
        return;
    document.getElementById("past_return").addEventListener("click", function(){window.location.href= "/"});
     document.getElementById("close").addEventListener("click", function(){
        window.location.reload();

    })
    document.getElementById("Submit").addEventListener("click", function(){
        const orderdropdown= document.getElementById("order_number")
        const order_number = Number(orderdropdown.value)
        const o = {order_number}
        // Request the saved order details from Flask using the selected order number.
        fetch("/past_order", {method: 'POST',
            headers:{'Content-type': 'application/json'},
            body: JSON.stringify(o)
        })
        .then(response => response.json())
        
        .then(order => {    
        display_order(order)
        })
    })
    document.getElementById("recent_order").addEventListener("click", function(){
        const dropdown = document.getElementById("order_number")
       // Select the newest order and reuse the Submit button's event handler.
        dropdown.selectedIndex= 1
        document.getElementById("Submit").click()
    })
  
}
past_order()
// ==========================
// Edit Database Page
// ==========================
function edit_database(){
    const target_element = document.getElementById("data_return")
    const database_data= document.getElementById("database_data")
    const SideID_or_MeatID= document.getElementById("SideID_or_MeatID")
    if (!target_element)
        return;
    document.getElementById("data_return").addEventListener("click", function(){window.location.href= "/"});
    const choice_dropdown = document.getElementById("meat_or_side");
    choice_dropdown.addEventListener("change", function(){
        SideID_or_MeatID.replaceChildren()
        if(choice_dropdown.value ==="Meat"){
            const meat_Ids=JSON.parse(database_data.dataset.meats)
            meat_Ids.forEach(function(meat){
                const option= document.createElement("option")
                option.value= meat
                option.textContent= meat
                SideID_or_MeatID.appendChild(option)
            })
             SideID_or_MeatID.disabled= false

               }
        else if(choice_dropdown.value === "Side"){
            const side_IDS= JSON.parse(database_data.dataset.sides)
            side_IDS.forEach(function(side){
                 const option= document.createElement("option")
                 option.value= side
                 option.textContent=side
                 SideID_or_MeatID.appendChild(option)
            })
            SideID_or_MeatID.disabled= false
        }
    })
}
edit_database()
// functions for editing meats and sides