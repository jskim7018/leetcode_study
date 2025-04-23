function canAttendMeetings(intervals: number[][]): boolean {
    intervals.sort((a,b,) => {
        if (a[0] != b[0]) return a[0] - b[0]
        return a[1]-b[1]
    })
    // One-liner comparator-> intervals.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    for (let i=1; i<intervals.length;i++) {
        if (intervals[i-1][1] > intervals[i][0]) {
            return false
        }
    }
    return true
};