/**
 * @param {number} n
 * @return {number}
 */
var countLargestGroup = function(n) {
    mp = new Map()
    maxim = 0
    for (i=1; i<=n;i++) {
        str_i = String(i)
        sum = 0
        for (j=0; j<str_i.length; j++) {
            sum += Number(str_i[j])
        }
        mp.set(sum, (mp.get(sum) || 0)+1)
        if (mp.get(sum) > maxim) {
            maxim = mp.get(sum)
        }
    }
    ans = 0
    for (let [k,v] of mp) {
        if (v == maxim) {
            ans += 1
        }
    }
    return ans
};
