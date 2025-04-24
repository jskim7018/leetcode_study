function makeFancyString(s: string): string {
    let ans: string[] = []
    for (let i=0;i<Math.min(s.length, 2); i++) {
        ans.push(s[i])
    }
    for (let i=2; i<s.length; i++) {
        if (s[i] != ans[ans.length-1] || s[i] != ans[ans.length-2]) {
            ans.push(s[i])
        }
    }
    return ans.join('')
};