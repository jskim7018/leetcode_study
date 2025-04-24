function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    let ret: number[] = []

    for (let i=0; i<arr.length;i++) {
        ret.push(fn(arr[i], i))
    }
    return ret
};