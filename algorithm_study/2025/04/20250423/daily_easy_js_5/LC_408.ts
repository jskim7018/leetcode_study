function validWordAbbreviation(word: string, abbr: string): boolean {
    let i = 0; 
    let j = 0; 
  
    while (i < abbr.length && j <= word.length) {
      if (abbr[i] >= '0' && abbr[i] <= '9') {
        if (abbr[i] === '0') return false;
  
        let num = 0;
        while (i < abbr.length && abbr[i] >= '0' && abbr[i] <= '9') {
          num = num * 10 + Number(abbr[i]);
          i++;
        }
        j += num;
      } else {
        if (word[j] !== abbr[i]) return false;
        i++;
        j++;
      }
    }
  
    return i === abbr.length && j === word.length;
  }
  