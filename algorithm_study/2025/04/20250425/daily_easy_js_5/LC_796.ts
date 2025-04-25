function rotateString(s: string, goal: string): boolean {
    if (s.length != goal.length) {
        return false
    }
    for (let i=0;i<s.length;i++) {
        let j = 0
        let possible = true
        while (j < s.length) {
            if (s[(i+j) % s.length] != goal[j]) {
                possible = false
                break
            }
            j += 1
        }
        if (possible) {
            return true
        }
    }
    return false
};