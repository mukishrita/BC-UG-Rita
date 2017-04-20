class BinarySearch(list):
    def __init__(self, a, b):
        super().__init__()
        self.length = a
        self.list_step = b
        for i in range(self.length):
            list.append(self, self.list_step)
            self.list_step += b

    def search(self, num_to_find):
        counter = 0
        low_bound = 0
        high_bound = self.length - 1

        if num_to_find in self:
            if num_to_find == self[-1]:
                return {'count': 0, 'index': self.length - 1}
            while high_bound >= low_bound:
                counter += 1
                mid_bound = int((low_bound + high_bound) / 2)
                if self[mid_bound] == num_to_find:
                    return {'count': counter, 'index': mid_bound}
                else:
                    if num_to_find < self[mid_bound]:
                        high_bound = mid_bound - 1
                    else:
                        low_bound = mid_bound + 1
        return {'count': counter, 'index': -1}
