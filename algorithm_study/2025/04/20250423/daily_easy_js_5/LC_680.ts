function validPalindrome(s: string): boolean {
    const dp: number[][] = Array.from({length: s.length}, ()=>
        Array(3).fill(-1)
    )


    function solve(i: number, chance:number,
        s:string 
    ): boolean {
        if (i+chance >= Math.ceil(s.length/2)) {
            return true
        }
        if (dp[i][chance==-1?2:chance] != -1) return dp[i][chance==-1?2:chance]==1 ? true:false

        let ret = false

        if (s[i+chance] == s[s.length-i-1]) {
            ret ||= solve(i+1, chance, s);
        } else {
            if (chance != 0) {
                return false
            } else {
                ret ||= solve(i+1, -1, s) || solve(i,1,s)
            }
        }
        dp[i][chance==-1?2:chance] = ret ? 1:0
        return ret
    }
    let ans = solve(0,0,s)
    return ans
};
