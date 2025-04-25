function firstUniqChar(s: string): number {
    let mp = new Map()
    
    for (const c of s) {
        mp.set(c, (mp.get(c) || 0) + 1)
    }
    for (let i=0;i<s.length;i++) {
        if (mp.get(s[i]) == 1) {
            return i
        }
    }
    return -1
};