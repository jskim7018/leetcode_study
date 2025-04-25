function findKthPositive(arr: number[], k: number): number {
    let prev = 0
    
    let missing_cnt = 0
    let ans = 0
    for (let i=0;i<arr.length;i++) {
        let curr = arr[i]
        let missing = Math.max(curr-prev-1,0)

        if (missing >= k) {
            ans = prev + k
            break
        }
        
        if (i===arr.length-1) {
            ans = prev + k + 1
        }
        else {
            missing_cnt += missing
            k -= missing
        }
        prev = curr
    }
    return ans
}; 
