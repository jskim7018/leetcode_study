function validWordAbbreviation(word: string, abbr: string): boolean {
    
    let curr_idx = 0
    for (let i=0;i<abbr.length;i++) {
        if (abbr[i] == word[curr_idx]) {
            curr_idx += 1
        } else if (abbr[i] >= '0' && abbr[i] <= '9') {
            let j = 1
            let number = 0
            while (abbr[i] >= '0' && abbr[i] <= '9') {
                number += Number(abbr[i]) * j
                j *= 10
            }
            curr_idx += number
        } else {
            return false
        }
    }
    if (curr_idx >= word.length) {
        return true
    } else {
        return false
    }
};