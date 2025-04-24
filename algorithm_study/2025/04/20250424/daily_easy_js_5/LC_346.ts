import {Queue} from 'datastructures-js'

class MovingAverage {
    private size: number;
    private queue: Queue<number>;
    private currSum: number;

    constructor(size: number) {
        this.size = size;
        this.queue = new Queue()
        this.currSum = 0
    }

    next(val: number): number {
        this.queue.push(val)
        this.currSum += val
        if (this.queue.size() > this.size) {
            this.currSum -= this.queue.pop()
        }
        return this.currSum / this.queue.size()
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = new MovingAverage(size)
 * var param_1 = obj.next(val)
 */