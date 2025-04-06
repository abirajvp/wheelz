$('#add-category').click(function() {
    var category_type = $('#category-type').val();
    var category_value = $('#category-value').val();
    $.ajax({
        type: 'POST',
        url: '/add-category',
        data: {
            category_type: category_type,
            category_value: category_value,
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        },
        success: function(response) {
            alert('Category added successfully!');
        },
        error: function(xhr, status, error) {
            alert('An error occurred: ' + error);
        },
        finally: function() {
            window.location.reload();
        }
    });
});

// $('#_add-car').click(function() {
//     console.log('clicked');
//     var name = $('#name').val();
//     var vehicle_id = $('#vehicle_id').val();
//     var price_amount = $('#price_amount').val();
//     var price_display = $('#price_display').val();
//     var price_description = $('#price_description').val();
//     var new_used = $('#new_used').val();
//     var make = $('#make').val();
//     var vehicle_mode = $('#vehicle_mode').val();
//     var gear = $('#gear').val();
//     var fuel = $('#fuel').val();
//     var vehicle_mode = $('#vechicle_type').val();
//     var model = $('#model').val();
//     var doors = $('#doors').val();
//     var seats = $('#seats').val();
//     var mileage = $('#mileage').val();
//     var mileage_display = $('#mileage_display').val();
//     var engine = $('#engine').val();
//     var power = $('#power').val();
//     var color = $('#color').val();
//     var registration_date = $('#registration_date').val();
//     var year = $('#year').val();
//     var owner_name = $('#owner_name').val();
//     var owner_phone = $('#owner_phone').val();
//     var owner_address = $('#owner_address').val();
//     var display_home = $('#display_home').val();
//     console.log(display_home);
//     var image = $('#image')[0].files[0];
//     console.log(image);
//     $.ajax({
//         type: 'POST',
//         url: '/add-car',
//         data: {
//             name: name,
//             vehicle_id: vehicle_id,
//             price_amount: price_amount,
//             price_display: price_display,
//             price_description: price_description,
//             new_used: new_used,
//             make: make,
//             vehicle_mode: vehicle_mode,
//             gear: gear,
//             fuel: fuel,
//             vehicle_mode: vehicle_mode,
//             model: model,
//             doors: doors,
//             seats: seats,
//             mileage: mileage,
//             mileage_display: mileage_display,
//             engine: engine,
//             power: power,
//             color: color,
//             registration_date: registration_date,
//             year: year,
//             owner_name: owner_name,
//             owner_phone: owner_phone,
//             owner_address: owner_address,
//             display_home: display_home,
//             image: image,
//             csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
//         },
//         success: function() {
//             alert('Car added successfully!');
//         },
//         error: function(xhr, status, error) {
//             alert('An error occurred: ' + error);
//         }
//     });
// });
