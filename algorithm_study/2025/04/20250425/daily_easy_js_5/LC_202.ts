function isHappy(n: number): boolean {
    const st = new Set()
    
    let prev = n
    while (!st.has(prev)) {
        st.add(prev)

        let sum = 0
        while (prev > 0) {
            sum += Math.pow(prev%10, 2)
            prev = Math.floor(prev / 10)
        }
        if (sum == 1) {
            return true
        }
        prev = sum
    }
    return false
};