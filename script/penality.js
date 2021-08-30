
var penality = (typeof penality === 'undefined') ? {}: penality
$('table tr').each( function() { 
    var title = $(this).find("td:eq(1)").text().trim()
    var status = $(this).find("td:eq(2)").text().trim()
    var lang = $(this).find("td:eq(4)").text().trim()
    
    if (lang != 'python3') return true
    
    if (status == 'Accepted'){
        penality[title] = 0
    } else if (title in penality) {
        penality[title] = penality[title] + 1
    }
})
penality