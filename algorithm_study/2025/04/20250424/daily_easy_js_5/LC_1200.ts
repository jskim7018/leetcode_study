function minimumAbsDifference(arr: number[]): number[][] {
    arr.sort((a,b)=>a-b)
    
    let minim_diff = Number.MAX_VALUE

    for (let i=1;i<arr.length; i++) {
        minim_diff = Math.min(minim_diff, arr[i]-arr[i-1]);
    }
    console.log(arr)
    let ans:[number,number][] = []
    for (let i=1;i<arr.length;i++) {
        if (arr[i]-arr[i-1] == minim_diff) {
            ans.push([arr[i-1],arr[i]])
        }
    }
    return ans
};