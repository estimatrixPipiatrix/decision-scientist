class prefix_sum:
    def __init__(self,vec):
        self.prefix = []
        total = 0
        for n in vec:
            total += n
            self.prefix.append(total)

    def rangeSum(self,left,right):
        preRight = self.prefix[right]
        if (left-1)>=0:
            preLeft = self.prefix[left-1]
        else:
            preLeft = 0.0
        return (preRight-preLeft)
