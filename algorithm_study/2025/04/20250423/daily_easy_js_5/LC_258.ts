function addDigits(num: number): number {

    // functional programming style
    while (num > 9) {
        num = num
          .toString()
          .split('')
          .reduce((sum, digit) => sum + Number(digit), 0);
      }
      return num;
};