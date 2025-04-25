function addStrings(num1: string, num2: string): string {
    let idx = 0

    let ans:string[] = []
    let carry = 0
    while (idx < num1.length || idx < num2.length || carry === 1) {
        let digit1 = 0
        let digit2 = 0
        if (idx < num1.length) {
            digit1 = Number(num1[num1.length - idx - 1])
        }
        if (idx < num2.length) {
            digit2 = Number(num2[num2.length - idx - 1])
        }

        let digit3 = digit1 + digit2 + carry
        carry = Math.floor(digit3 / 10)
        ans.push((digit3%10).toString())
        idx += 1
    }
    return ans.reverse().join('')
};