// https://leetcode.com/submissions/#/1

var results = (typeof results === 'undefined') ? new Array() : results;
$('table tr').each( function() { 
    var title = $(this).find("td:eq(1)").text().trim()
    var status = $(this).find("td:eq(2)").text().trim()
    var lang = $(this).find("td:eq(4)").text().trim()

    title = title.toLowerCase().replace(/\(|\)/gi, '').replace(/ /g,'_')
    if (status == 'Accepted' && lang == 'python3' && results.indexOf(title)== -1){
        results.push(title);
    }
})
results.sort()
