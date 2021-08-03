// https://leetcode.com/problemset/all/?status=AC

var last = (typeof result === 'undefined') ? new Array() : result;
var result = $('.ant-table-tbody').textContent.split(/Medium|Easy|Hard/g)
result = result.map(x => x.trim())

var head = (result[0] > result[1]) ? 1 : 0;
var tail = (result[result.length-1] =='')? result.length-1: result.length;
result = result.slice(head, tail);

result = result.map(x => x.replace(/[0-9. ]*([^0-9]*).*/,'$1')
	.toLowerCase().replace(/\(|\)/gi, '').replace(/ /g,'-') )

result = result.concat(last)
result = result.filter((v, i, a) => a.indexOf(v) === i);
result.sort()
