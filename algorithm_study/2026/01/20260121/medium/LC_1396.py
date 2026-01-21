from collections import defaultdict


class UndergroundSystem:

    # TODO: avg를 미리 계산하지 말고 그냥 총 합과 갯수만 저장해서 갱신해 나가는 식으로 해도됨.
    def __init__(self):
        self.avg_time = defaultdict(float)
        self.data_cnt = defaultdict(int)
        self.id_start_station = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id_start_station[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, s_t = self.id_start_station[id]
        key = (start_station, stationName)
        curr_avg = self.avg_time[key]
        new_avg = (curr_avg * self.data_cnt[key] + (t-s_t))/(self.data_cnt[key]+1)
        self.data_cnt[key] += 1
        self.avg_time[key] = new_avg

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avg_time[(startStation, endStation)]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)