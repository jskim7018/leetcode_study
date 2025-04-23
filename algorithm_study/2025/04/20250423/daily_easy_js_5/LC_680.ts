function validPalindrome(s: string): boolean {
    const dp: number[][][] = Array.from({length: s.length}, ()=>
        Array.from({length: s.length}, ()=>
            Array(2).fill(-1)
        )
    )


    function solve(i: number, j: number, chance:number,
        s:string
    ): boolean {
        if (i >= j) {
            return true
        }

        if (dp[i][j][chance] != -1) return dp[i][j][chance]==1?true:false

        let ret = false
        if (s[i] == s[j]) {
            ret ||= solve(i+1, j-1, chance, s);
        } else {
            if (chance > 0) {
                ret ||= solve(i+1, j, chance-1, s) 
                || solve(i,j-1, chance-1,s)
            }
        }
        dp[i][j][chance] = ret ? 1:0
        return ret
    }

    return solve(0, s.length-1, 1, s)
};