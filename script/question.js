// https://leetcode.com/submissions/#/1

var result = (typeof result === 'undefined') ? new Array() : result;
$('table tr').each( function() { 
    var title= $(this).find("td:eq(1)").text().trim()
    var status= $(this).find("td:eq(2)").text().trim()

    title = title.toLowerCase().replace(/\(|\)/gi, '').replace(/ /g,'-')
    if (status == 'Accepted' && result.indexOf(title)== -1){
        result.push(title);
    }
})
result.sort()
